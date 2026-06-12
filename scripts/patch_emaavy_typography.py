#!/usr/bin/env python3
"""Ensure emaavy-type-tokens.css + section-heading.css on every HTML page."""
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SKIP = {"node_modules", ".git"}
TOKENS = "emaavy-type-tokens.css"
HEADING = "section-heading.css"


def asset_base(html_path: Path) -> str:
    depth = len(html_path.relative_to(ROOT).parts) - 1
    return "assets/" if depth <= 0 else "../" * depth + "assets/"


def patch_file(path: Path) -> list[str]:
    logs: list[str] = []
    text = path.read_text(encoding="utf-8")
    if "</head>" not in text:
        return logs
    base = asset_base(path)
    changed = False

    token_link = f'  <link rel="stylesheet" href="{base}{TOKENS}" />\n'
    if TOKENS not in text:
        for needle in (
            f'<link rel="stylesheet" href="{base}site.css" />',
            f'<link rel="stylesheet" href="{base}nav.css" />',
        ):
            if needle in text:
                text = text.replace(needle, token_link + needle, 1)
                logs.append(f"+{TOKENS}")
                changed = True
                break

    heading_link = f'  <link rel="stylesheet" href="{base}{HEADING}" />\n'
    if HEADING not in text:
        text = text.replace("</head>", heading_link + "</head>", 1)
        logs.append(f"+{HEADING}")
        changed = True

    if changed:
        path.write_text(text, encoding="utf-8")
        logs.insert(0, str(path.relative_to(ROOT)))
    return logs


def patch_templates() -> None:
    replacements = [
        (
            '<link rel="stylesheet" href="../../assets/site.css" />',
            '<link rel="stylesheet" href="../../assets/emaavy-type-tokens.css" />\n'
            '  <link rel="stylesheet" href="../../assets/site.css" />',
        ),
        (
            '<link rel="stylesheet" href="../assets/site.css" />',
            '<link rel="stylesheet" href="../assets/emaavy-type-tokens.css" />\n'
            '  <link rel="stylesheet" href="../assets/site.css" />',
        ),
    ]
    for name in (
        "integration_pages_common.py",
        "case_studies_pages_common.py",
        "generate_pages.py",
        "build_call_lifecycle_pages.py",
    ):
        p = ROOT / "scripts" / name
        if not p.exists():
            continue
        text = p.read_text(encoding="utf-8")
        orig = text
        for old, new in replacements:
            if old in text and TOKENS not in text.split(old)[0][-200:]:
                text = text.replace(old, new, 1)
        if text != orig:
            p.write_text(text, encoding="utf-8")
            print(f"template: {name}")


def main() -> None:
    n = 0
    for path in sorted(ROOT.rglob("*.html")):
        if any(s in path.parts for s in SKIP):
            continue
        logs = patch_file(path)
        if logs:
            n += 1
            print(" ".join(logs))
    patch_templates()
    print(f"OK: {n} html files updated")


if __name__ == "__main__":
    main()
