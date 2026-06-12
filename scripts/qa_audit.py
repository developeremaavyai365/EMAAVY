#!/usr/bin/env python3
"""Pre-production QA audit for EMAAVY static site."""
from __future__ import annotations

import json
import re
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
PRODUCTION_ROOT = {
    "index.html", "login.html", "book-demo.html", "404.html",
}
LEGACY_HTML = {
    "index1.html", "index.html.html", "creative.html.html",
    "emaavy white blue(2).html", "emaavy landing page claude.html",
}
SKIP_HTML = LEGACY_HTML | {
    "scripts/_hero_current.html",
    "inbound-agent.html", "outbound-agent.html", "sales-agent.html", "support-agent.html",
}

issues: list[dict] = []


def add(severity: str, category: str, message: str, path: str = "") -> None:
    issues.append({"severity": severity, "category": category, "message": message, "path": path})


def html_files() -> list[Path]:
    out = []
    for p in ROOT.rglob("*.html"):
        if p.name in SKIP_HTML or "node_modules" in p.parts:
            continue
        if "scripts" in p.parts:
            continue
        out.append(p)
    return out


def resolve_href(source: Path, href: str) -> Path | None:
    href = href.split("#")[0].split("?")[0].strip()
    if not href or href.startswith(("http://", "https://", "mailto:", "tel:", "javascript:")):
        return None
    if href.startswith("/"):
        return ROOT / href.lstrip("/")
    return (source.parent / href).resolve()


def audit_assets() -> None:
    for html in html_files():
        text = html.read_text(encoding="utf-8", errors="ignore")
        if "assets/assets/" in text:
            add("CRITICAL", "assets", "Double assets/ path in CSS/JS reference", str(html.relative_to(ROOT)))

        for m in re.finditer(r'(?:href|src)="([^"]+)"', text):
            href = m.group(1)
            if href.endswith((".css", ".js", ".svg", ".png", ".jpg", ".webp", ".mp4", ".woff2")):
                target = resolve_href(html, href)
                if target and not target.exists():
                    add("CRITICAL", "assets", f"Missing asset: {href}", str(html.relative_to(ROOT)))

        if "viewport" not in text.lower() and html.name not in {"inbound-agent.html", "outbound-agent.html", "sales-agent.html", "support-agent.html"}:
            if str(html).replace("\\", "/").startswith(str(ROOT / "pages")) or html.name in PRODUCTION_ROOT:
                add("HIGH", "seo", "Missing viewport meta tag", str(html.relative_to(ROOT)))

        if "<title>" not in text.lower():
            add("HIGH", "seo", "Missing <title>", str(html.relative_to(ROOT)))

        if 'href="#"' in text and html.name in {"login.html", "book-demo.html"} or (
            html.name in PRODUCTION_ROOT and 'href="#"' in text
        ):
            add("HIGH", "links", "Dead href=\"#\" link", str(html.relative_to(ROOT)))


def audit_routes() -> None:
    routes_file = ROOT / "assets" / "routes.js"
    if not routes_file.exists():
        add("CRITICAL", "routes", "routes.js missing")
        return
    text = routes_file.read_text(encoding="utf-8")
    for m in re.finditer(r"path:\s*'([^']+\.html[^']*)'", text):
        path = m.group(1).split("#")[0]
        if path.startswith("index.html"):
            continue
        target = ROOT / path.replace("/", "\\") if sys.platform == "win32" else ROOT / path
        if not target.exists():
            add("CRITICAL", "routes", f"Route points to missing file: {path}", "assets/routes.js")

    if not (ROOT / "404.html").exists():
        add("CRITICAL", "routes", "404.html missing")


def audit_security() -> None:
    patterns = [
        (r"sk-[a-zA-Z0-9]{20,}", "Possible OpenAI API key"),
        (r"AKIA[0-9A-Z]{16}", "Possible AWS access key"),
        (r"api[_-]?key\s*[:=]\s*['\"][^'\"]+['\"]", "Hardcoded API key"),
    ]
    for path in list(ROOT.rglob("*.js")) + list(ROOT.rglob("*.html")):
        if path.name in SKIP_HTML:
            continue
        text = path.read_text(encoding="utf-8", errors="ignore")
        for pat, label in patterns:
            if re.search(pat, text, re.I):
                add("CRITICAL", "security", label, str(path.relative_to(ROOT)))


def audit_js_syntax() -> tuple[int, int]:
    js_dir = ROOT / "assets"
    ok = fail = 0
    for js in sorted(js_dir.glob("*.js")):
        try:
            subprocess.run(
                ["node", "--check", str(js)],
                capture_output=True,
                check=True,
                timeout=10,
            )
            ok += 1
        except (subprocess.CalledProcessError, FileNotFoundError) as e:
            fail += 1
            msg = "JS syntax error"
            if isinstance(e, subprocess.CalledProcessError) and e.stderr:
                msg = e.stderr.decode("utf-8", errors="ignore")[:200]
            add("CRITICAL", "js", msg, str(js.relative_to(ROOT)))
    return ok, fail


def audit_build() -> None:
    if not (ROOT / "package.json").exists():
        add("LOW", "build", "No package.json — static site, npm build N/A (expected)")


def score() -> dict:
    counts = {"CRITICAL": 0, "HIGH": 0, "MEDIUM": 0, "LOW": 0}
    for i in issues:
        counts[i["severity"]] = counts.get(i["severity"], 0) + 1

    critical = counts["CRITICAL"]
    high = counts["HIGH"]
    if critical == 0 and high == 0:
        readiness = "DEPLOYMENT READY"
        score_val = 95
    elif critical == 0 and high <= 3:
        readiness = "READY WITH WARNINGS"
        score_val = 85
    elif critical == 0:
        readiness = "NEEDS REVIEW"
        score_val = 70
    else:
        readiness = "NOT READY"
        score_val = max(0, 50 - critical * 10 - high * 2)

    return {
        "readiness": readiness,
        "score": score_val,
        "counts": counts,
        "issues": issues,
    }


def main() -> None:
    audit_routes()
    audit_assets()
    audit_security()
    js_ok, js_fail = audit_js_syntax()
    audit_build()

    result = score()
    result["js_syntax"] = {"passed": js_ok, "failed": js_fail}
    result["pages_audited"] = len(html_files())
    result["legacy_excluded"] = sorted(LEGACY_HTML)

    out = ROOT / "PRE_PRODUCTION_AUDIT_REPORT.json"
    out.write_text(json.dumps(result, indent=2), encoding="utf-8")

    print(f"Pages audited: {result['pages_audited']}")
    print(f"JS syntax: {js_ok} passed, {js_fail} failed")
    print(f"Issues: CRITICAL={result['counts']['CRITICAL']} HIGH={result['counts']['HIGH']} "
          f"MEDIUM={result['counts'].get('MEDIUM', 0)} LOW={result['counts'].get('LOW', 0)}")
    print(f"Readiness: {result['readiness']} (score {result['score']}/100)")
    print(f"Report: {out.relative_to(ROOT)}")

    if result["counts"]["CRITICAL"] > 0:
        sys.exit(1)


if __name__ == "__main__":
    main()
