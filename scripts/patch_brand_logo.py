"""Standardize Emaavy logo to assets/brand/emaavy-logo.svg across all pages."""
from __future__ import annotations

import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
BRAND_CSS = "brand-logo.css"
LOGO_REL = "brand/emaavy-logo.svg"
LEGACY_PATHS = (
    "emaavy-mark.png",
    "emaavy-logo.png",
    "emaavy-wordmark.png",
    "emaavy-wordmark-source.png",
)

HERO_IMG = (
    '<img src="{base}{logo}" alt="Emaavy" class="emaavy-logo emaavy-logo--hero" '
    'width="648" height="116" decoding="async" fetchpriority="high" />'
)

AUTH_LOGO = (
    '<img src="{base}{logo}" alt="Emaavy" class="emaavy-logo emaavy-logo--auth" '
    'width="648" height="116" decoding="async" />'
)


def asset_base(rel: Path) -> str:
    depth = len(rel.parent.parts)
    if depth == 0:
        return "assets/"
    return "../" * depth + "assets/"


def insert_brand_css(text: str, base: str) -> tuple[str, bool]:
    link = f'<link rel="stylesheet" href="{base}{BRAND_CSS}" />\n'
    if BRAND_CSS in text:
        # Re-order: strip and append last in <head>
        if "</head>" in text:
            head, tail = text.split("</head>", 1)
            head = re.sub(
                rf'\s*<link rel="stylesheet" href="{re.escape(base)}{BRAND_CSS}" />\s*',
                "\n",
                head,
            )
            head = head.rstrip() + "\n" + link
            return head + "</head>" + tail, True
        return text, False
    if "</head>" in text:
        head, tail = text.split("</head>", 1)
        head = head.rstrip() + "\n" + link
        return head + "</head>" + tail, True
    needle = f'<link rel="stylesheet" href="{base}masthead-flex.css" />'
    if needle in text:
        return text.replace(needle, needle + "\n" + link, 1), True
    return text, False


def insert_favicon(text: str, base: str) -> tuple[str, bool]:
    if 'rel="icon"' in text or "rel='icon'" in text:
        return text, False
    icon = f'  <link rel="icon" href="{base}{LOGO_REL}" type="image/svg+xml" />\n'
    m = re.search(r"<head[^>]*>", text, re.I)
    if not m:
        return text, False
    return text[: m.end()] + "\n" + icon + text[m.end() :], True


def insert_og_image(text: str, base: str) -> tuple[str, bool]:
    if "og:image" in text:
        return text, False
    tag = f'  <meta property="og:image" content="{base}brand/emaavy-logo.png" />\n'
    m = re.search(r"<head[^>]*>", text, re.I)
    if not m:
        return text, False
    return text[: m.end()] + "\n" + tag + text[m.end() :], True


def replace_legacy_logo_paths(text: str, base: str) -> tuple[str, int]:
    n = 0
    logo = f"{base}{LOGO_REL}"
    for legacy in LEGACY_PATHS:
        for pat in (f"{base}{legacy}", f"assets/{legacy}"):
            if pat in text:
                c = text.count(pat)
                text = text.replace(pat, logo)
                n += c
    return text, n


def replace_hero_letters(text: str, base: str) -> tuple[str, int]:
    img = HERO_IMG.format(base=base, logo=LOGO_REL)
    pat = r'<span class="hero-brand-letters"[^>]*>.*?</span>'
    text, n = re.subn(pat, img, text, flags=re.DOTALL)
    return text, n


def remove_auth_showcase_logo(text: str, base: str) -> tuple[str, int]:
    """Login / book-demo side panels: no wordmark (navbar only)."""
    pat = (
        r'\s*<a href="[^"]*" class="(?:auth|demo)-showcase-logo"[^>]*>\s*'
        r'<img[^>]*emaavy[^>]*>\s*</a>'
    )
    text, n = re.subn(pat, "", text, flags=re.DOTALL | re.IGNORECASE)
    return text, n


def replace_nav_logo_img(text: str, base: str) -> tuple[str, int]:
    logo = f"{base}{LOGO_REL}"
    pat = (
        r'<img src="[^"]*emaavy-mark\.png"[^>]*class="logo-mega-mark"[^>]*/>'
    )
    repl = (
        f'<img src="{logo}" alt="Emaavy" class="emaavy-logo emaavy-logo--nav logo-mega-mark" '
        f'width="648" height="116" decoding="async" fetchpriority="high" />'
    )
    text, n = re.subn(pat, repl, text, flags=re.IGNORECASE)
    text = text.replace('logo-mega--mark', 'logo-mega--wordmark')
    return text, n


def patch_file(path: Path) -> list[str]:
    logs: list[str] = []
    text = path.read_text(encoding="utf-8")
    base = asset_base(path.relative_to(ROOT))
    orig = text

    text, b1 = insert_brand_css(text, base)
    text, b2 = insert_favicon(text, base)
    text, b3 = insert_og_image(text, base)
    text, n1 = replace_legacy_logo_paths(text, base)
    text, n2 = replace_hero_letters(text, base)
    text, n3 = remove_auth_showcase_logo(text, base)
    text, n4 = replace_nav_logo_img(text, base)

    if text != orig:
        path.write_text(text, encoding="utf-8")
        rel = path.relative_to(ROOT)
        if b1:
            logs.append(f"{rel}: +brand-logo.css")
        if b2:
            logs.append(f"{rel}: +favicon")
        if b3:
            logs.append(f"{rel}: +og:image")
        if n1:
            logs.append(f"{rel}: {n1} legacy logo path(s)")
        if n2:
            logs.append(f"{rel}: hero wordmark img")
        if n3:
            logs.append(f"{rel}: removed auth/demo showcase logo")
        if n4:
            logs.append(f"{rel}: nav logo img")
    return logs


def main() -> None:
    logs: list[str] = []
    for path in sorted(ROOT.rglob("*.html")):
        if "node_modules" in path.parts:
            continue
        logs.extend(patch_file(path))
    print("\n".join(logs) if logs else "No changes.")
    print(f"Done — {len(logs)} update(s).")


if __name__ == "__main__":
    main()
