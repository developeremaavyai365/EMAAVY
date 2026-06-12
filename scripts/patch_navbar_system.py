"""Wire navbar design tokens + typography enforcement across all HTML pages."""
from __future__ import annotations

import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

TOKENS = "navbar-tokens.css"
TYPO = "navbar-typography.css"
BRAND = "brand-logo.css"

# Legacy inline masthead typography blocks to strip from index.html
INDEX_NAV_TYPO_PATTERNS = [
    r"\.masthead-nav a,\s*\.nav-dropdown-trigger,\s*\.nav-integrations-link,\s*\.nav-dropdown-caret\s*\{[^}]+\}",
    r"\.masthead-nav a:hover,\s*\.nav-dropdown-trigger:hover,\s*\.nav-integrations-link:hover,\s*\.nav-dropdown-caret:hover\s*\{[^}]+\}",
    r"\.masthead-nav a\.active\s*\{[^}]+\}",
    r"\.masthead-nav a\.active:hover\s*\{[^}]+\}",
    r"\.masthead-nav a,\s*\.masthead-nav \.nav-dropdown-trigger,\s*\.masthead-nav \.nav-integrations-link,\s*\.masthead-nav \.nav-dropdown-caret\s*\{[^}]+\}",
    r"\.masthead-nav a:hover,\s*\.masthead-nav \.nav-dropdown-trigger:hover,\s*\.masthead-nav \.nav-integrations-link:hover,\s*\.masthead-nav \.nav-dropdown-caret:hover,\s*\.masthead-nav a\.active:hover\s*\{[^}]+\}",
    r"\.masthead-nav a\.active\s*\{[^}]+\}",
    r"\.masthead-nav a\.active,\s*\.nav-integrations-link\.active,\s*\.masthead-nav a\.active:hover\s*\{[^}]+\}",
    r"\.masthead-login\s*\{[^}]+\}",
    r"\.masthead-login:hover\s*\{[^}]+\}",
    r"\.masthead-go\s*\{[^}]+\}",
    r"\.masthead-go:hover\s*\{[^}]+\}",
    r"\.masthead-login,\s*\.masthead-go\s*\{[^}]+\}",
]


def asset_base(rel: Path) -> str:
    depth = len(rel.parent.parts)
    if depth == 0:
        return "assets/"
    return "../" * depth + "assets/"


def insert_tokens(text: str, base: str) -> tuple[str, bool]:
    link = f'<link rel="stylesheet" href="{base}{TOKENS}" />\n'
    if TOKENS in text:
        return text, False
    needle = f'<link rel="stylesheet" href="{base}nav.css" />'
    if needle not in text:
        return text, False
    return text.replace(needle, link + needle, 1), True


def insert_brand_logo(text: str, base: str) -> tuple[str, bool]:
    link = f'<link rel="stylesheet" href="{base}{BRAND}" />\n'
    if BRAND in text:
        return text, False
    needle = f'<link rel="stylesheet" href="{base}masthead-flex.css" />'
    if needle not in text:
        return text, False
    return text.replace(needle, needle + "\n" + link, 1), True


def insert_typography(text: str, base: str) -> tuple[str, bool]:
    link = f'<link rel="stylesheet" href="{base}{TYPO}" />\n'
    if TYPO in text:
        return text, False
    needle = f'<link rel="stylesheet" href="{base}masthead-flex.css" />'
    if needle not in text:
        return text, False
    return text.replace(needle, needle + "\n" + link, 1), True


def clean_index_inline(text: str) -> tuple[str, int]:
    removed = 0
    for pat in INDEX_NAV_TYPO_PATTERNS:
        text, n = re.subn(pat, "/* navbar typography: assets/navbar-typography.css */", text, flags=re.DOTALL)
        removed += n
    return text, removed


def patch_file(path: Path) -> list[str]:
    logs: list[str] = []
    text = path.read_text(encoding="utf-8")
    if "site-nav-root" not in text and path.name != "index.html":
        return logs

    base = asset_base(path.relative_to(ROOT))
    orig = text

    text, t1 = insert_tokens(text, base)
    text, tb = insert_brand_logo(text, base)
    text, t2 = insert_typography(text, base)

    if path.resolve() == (ROOT / "index.html").resolve():
        text, n = clean_index_inline(text)
        if n:
            logs.append(f"index: stripped {n} inline nav typography blocks")
        if "</head>" in text:
            head, tail = text.split("</head>", 1)
            late = f'  <link rel="stylesheet" href="assets/{TYPO}" />\n'
            if late.strip() not in head:
                head = head.rstrip() + "\n" + late
            brand_late = f'  <link rel="stylesheet" href="assets/{BRAND}" />\n'
            head = re.sub(r'\s*<link rel="stylesheet" href="assets/brand-logo\.css" />\s*', "\n", head)
            if brand_late.strip() not in head:
                head = head.rstrip() + "\n" + brand_late
            text = head + "</head>" + tail
            logs.append("index: ordered late navbar + brand logo CSS in head")

    if text != orig:
        path.write_text(text, encoding="utf-8")
        rel = path.relative_to(ROOT)
        if t1:
            logs.append(f"{rel}: +{TOKENS}")
        if tb:
            logs.append(f"{rel}: +{BRAND}")
        if t2:
            logs.append(f"{rel}: +{TYPO}")
    return logs


def patch_common_py() -> None:
    for name in (
        "integration_pages_common.py",
        "agents_pages_common.py",
        "case_studies_pages_common.py",
        "generate_pages.py",
        "build_call_lifecycle_pages.py",
    ):
        path = ROOT / "scripts" / name
        if not path.exists():
            continue
        text = path.read_text(encoding="utf-8")
        orig = text
        text = text.replace(
            '<link rel="stylesheet" href="../../assets/nav.css" />',
            '<link rel="stylesheet" href="../../assets/navbar-tokens.css" />\n'
            '  <link rel="stylesheet" href="../../assets/nav.css" />',
        )
        text = text.replace(
            '<link rel="stylesheet" href="../assets/nav.css" />',
            '<link rel="stylesheet" href="../assets/navbar-tokens.css" />\n'
            '  <link rel="stylesheet" href="../assets/nav.css" />',
        )
        text = text.replace(
            '<link rel="stylesheet" href="{base}assets/nav.css" />',
            '<link rel="stylesheet" href="{base}assets/navbar-tokens.css" />\n'
            '  <link rel="stylesheet" href="{base}assets/nav.css" />',
        )
        if "navbar-typography.css" not in text:
            text = text.replace(
                '<link rel="stylesheet" href="../../assets/masthead-flex.css" />',
                '<link rel="stylesheet" href="../../assets/masthead-flex.css" />\n'
                '  <link rel="stylesheet" href="../../assets/navbar-typography.css" />',
            )
            text = text.replace(
                '<link rel="stylesheet" href="../assets/masthead-flex.css" />',
                '<link rel="stylesheet" href="../assets/masthead-flex.css" />\n'
                '  <link rel="stylesheet" href="../assets/navbar-typography.css" />',
            )
            text = text.replace(
                '<link rel="stylesheet" href="{base}assets/masthead-flex.css" />',
                '<link rel="stylesheet" href="{base}assets/masthead-flex.css" />\n'
                '  <link rel="stylesheet" href="{base}assets/navbar-typography.css" />',
            )
        if text != orig:
            path.write_text(text, encoding="utf-8")
            print(f"patched {name}")


def main() -> None:
    logs: list[str] = []
    for html in sorted(ROOT.rglob("*.html")):
        if "scripts" in html.parts:
            continue
        logs.extend(patch_file(html))
    patch_common_py()
    for line in logs:
        print(line)
    print(f"Done — {len(logs)} log lines")


if __name__ == "__main__":
    main()
