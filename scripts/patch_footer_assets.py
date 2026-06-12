#!/usr/bin/env python3
"""Ensure every page with site-footer-root loads footer-premium.css and correct placement."""
from __future__ import annotations

import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
FOOTER_LINK = '<link rel="stylesheet" href="{base}assets/footer-premium.css" />'

PATTERNS = [
    ('href="assets/site.css"', 'href="assets/site.css" />\n  <link rel="stylesheet" href="assets/footer-premium.css"'),
    ('href="../assets/site.css"', 'href="../assets/site.css" />\n  <link rel="stylesheet" href="../assets/footer-premium.css"'),
    ('href="../../assets/site.css"', 'href="../../assets/site.css" />\n  <link rel="stylesheet" href="../../assets/footer-premium.css"'),
]


def patch_html(path: Path) -> bool:
    text = path.read_text(encoding="utf-8")
    if "site-footer-root" not in text:
        return False
    changed = False
    if "footer-premium.css" not in text:
        for needle, repl in PATTERNS:
            if needle in text:
                text = text.replace(
                    f'<link rel="stylesheet" {needle} />',
                    f'<link rel="stylesheet" {repl} />',
                    1,
                )
                changed = True
                break
    # Move footer mount outside .shell on home page
    if path.name == "index.html":
        old = "</section> <div id=\"site-footer-root\"></div> </div>"
        new = "</section> </div> <div id=\"site-footer-root\"></div>"
        if old in text:
            text = text.replace(old, new, 1)
            changed = True
    if changed:
        path.write_text(text, encoding="utf-8")
    return changed


def main():
    count = 0
    for html in ROOT.rglob("*.html"):
        if patch_html(html):
            print(f"patched {html.relative_to(ROOT)}")
            count += 1
    print(f"Done — {count} file(s) updated.")


if __name__ == "__main__":
    main()
