#!/usr/bin/env python3
"""Insert section-heading.css as the last stylesheet on every HTML page."""
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
MARKER = "section-heading.css"
SKIP = {"node_modules", ".git"}


def asset_base(html_path: Path) -> str:
    rel = html_path.relative_to(ROOT)
    depth = len(rel.parts) - 1
    if depth <= 0:
        return "assets/"
    return "../" * depth + "assets/"


def patch_file(path: Path) -> bool:
    text = path.read_text(encoding="utf-8")
    if MARKER in text:
        return False
    if "</head>" not in text:
        return False
    link = f'  <link rel="stylesheet" href="{asset_base(path)}{MARKER}" />\n'
    text = text.replace("</head>", link + "</head>", 1)
    path.write_text(text, encoding="utf-8")
    return True


def main():
    count = 0
    for path in ROOT.rglob("*.html"):
        if any(s in path.parts for s in SKIP):
            continue
        if patch_file(path):
            count += 1
            print(f"patched {path.relative_to(ROOT)}")
    print(f"OK: {count} files patched")


if __name__ == "__main__":
    main()
