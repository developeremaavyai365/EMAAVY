"""Unify landing navbar: site-nav-root mount + remove duplicate inline nav CSS."""
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
INDEX = ROOT / "index.html"

NAV_CSS_START = "/* ═══ ELEGANT NAVBAR — refined, no glow ═══ */"
NAV_CSS_END = "/* ═══ ELEGANT HERO — brand + dynamic showcase ═══ */"

NAV_REPLACE_START = '<header class="masthead" id="masthead">'
NAV_REPLACE_END = '<aside class="rail">'


def patch_index(text: str) -> tuple[str, list[str]]:
    logs: list[str] = []

    if NAV_CSS_START in text and NAV_CSS_END in text:
        before, rest = text.split(NAV_CSS_START, 1)
        _, after = rest.split(NAV_CSS_END, 1)
        text = before + NAV_CSS_END + after
        logs.append("Removed inline ELEGANT NAVBAR CSS block")
    else:
        logs.append("WARN: inline navbar CSS block not found")

    body_idx = text.find('<body data-page="home">')
    if body_idx < 0:
        logs.append("WARN: home body tag not found")
        return text, logs

    start = text.find(NAV_REPLACE_START, body_idx)
    end = text.find(NAV_REPLACE_END, body_idx)
    if start < 0 or end < 0:
        logs.append(f"WARN: masthead block markers missing (start={start}, end={end})")
        return text, logs

    replacement = '<div id="site-nav-root"></div> '
    text = text[:start] + replacement + text[end:]
    logs.append("Replaced static masthead with site-nav-root")

    return text, logs


def ensure_script_stack(text: str) -> tuple[str, list[str]]:
    logs: list[str] = []
    if "assets/routes.js" not in text:
        logs.append("WARN: routes.js missing on index")
    if "assets/components.js" not in text:
        logs.append("WARN: components.js missing on index")
    if "assets/nav.js" not in text:
        logs.append("WARN: nav.js missing on index")
    return text, logs


def main() -> None:
    text = INDEX.read_text(encoding="utf-8")
    text, logs = patch_index(text)
    text, logs2 = ensure_script_stack(text)
    logs.extend(logs2)
    INDEX.write_text(text, encoding="utf-8")
    for line in logs:
        print(line)


if __name__ == "__main__":
    main()
