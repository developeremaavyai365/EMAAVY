#!/usr/bin/env python3
"""Inject responsive-system.css into all HTML pages (load last among global styles)."""
from __future__ import annotations

import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
LINK = '<link rel="stylesheet" href="{href}" />'

ANCHORS = [
    'href="assets/hero-viewport-fit.css"',
    'href="assets/footer-premium.css"',
    'href="assets/emaavy-theme.css"',
    'href="assets/auth-page.css"',
    'href="assets/book-demo-page.css"',
    'href="assets/contact-page.css"',
    'href="assets/pricing-page.css"',
    'href="assets/docs-page.css"',
    'href="../assets/emaavy-theme.css"',
    'href="../../assets/emaavy-theme.css"',
    'href="../assets/footer-premium.css"',
    'href="../../assets/footer-premium.css"',
]


def responsive_href(anchor: str) -> str:
    if '../' in anchor:
        prefix = anchor.split('assets/')[0].replace('href="', '')
        return f'{prefix}assets/responsive-system.css'
    return 'assets/responsive-system.css'


REDIRECT_STUBS = {
    "inbound-agent.html", "outbound-agent.html", "sales-agent.html", "support-agent.html",
}


def patch_html(path: Path) -> bool:
    if path.name in REDIRECT_STUBS:
        return False
    text = path.read_text(encoding="utf-8")
    if "responsive-system.css" in text:
        return False
    if "<html" not in text.lower():
        return False

    for anchor in ANCHORS:
        if anchor in text:
            insert = LINK.format(href=responsive_href(anchor))
            pattern = re.compile(
                r'(<link rel="stylesheet" ' + re.escape(anchor) + r'[^/]*/>)',
                re.IGNORECASE,
            )
            match = pattern.search(text)
            if match:
                text = text[: match.end()] + "\n  " + insert + text[match.end() :]
                path.write_text(text, encoding="utf-8")
                return True

    if "</head>" in text:
        text = text.replace(
            "</head>",
            f'  {LINK.format(href="assets/responsive-system.css")}\n</head>',
            1,
        )
        path.write_text(text, encoding="utf-8")
        return True
    return False


def fix_double_assets(path: Path) -> bool:
    text = path.read_text(encoding="utf-8")
    fixed = text.replace('assets/assets/responsive-system.css', 'assets/responsive-system.css')
    fixed = fixed.replace('../assets/assets/responsive-system.css', '../assets/responsive-system.css')
    fixed = fixed.replace('../../assets/assets/responsive-system.css', '../../assets/responsive-system.css')
    if fixed != text:
        path.write_text(fixed, encoding="utf-8")
        return True
    return False


def main() -> None:
    patched = fixed = 0
    for html in sorted(ROOT.rglob("*.html")):
        if fix_double_assets(html):
            print(f"fixed double path {html.relative_to(ROOT)}")
            fixed += 1
        if patch_html(html):
            print(f"patched {html.relative_to(ROOT)}")
            patched += 1
    print(f"Done — {patched} patched, {fixed} double-path fixes.")


if __name__ == "__main__":
    main()
