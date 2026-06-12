"""Remove legacy inline navbar logo CSS from index.html and enforce brand-logo layer."""
from __future__ import annotations

import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
INDEX = ROOT / "index.html"

INLINE_LOGO_PATTERNS = [
    r"\.logo-mega\.logo-mega--wordmark\s*\{[^}]+\}",
    r"\.logo-mega-brand\s*\{[^}]+\}",
    r"\.logo-mega-mark\s*\{[^}]+\}",
    r"\.logo-mega-maavy\s*\{[^}]+\}",
    r"\.masthead\.compact\s+\.logo-mega\.logo-mega--wordmark\s*\{[^}]+\}",
    r"\.masthead\.compact\s+\.logo-mega-mark\s*\{[^}]+\}",
    r"\.masthead\.compact\s+\.logo-mega-maavy\s*\{[^}]+\}",
    r"\.logo-mega--wordmark\s+\.logo-tag\s*\{[^}]+\}",
    r"\.masthead\.compact\s+\.logo-mega--wordmark\s+\.logo-tag\s*\{[^}]+\}",
]

LATE_BRAND_LINK = '  <link rel="stylesheet" href="assets/brand-logo.css" />\n'


def main() -> None:
    text = INDEX.read_text(encoding="utf-8")
    orig = text
    removed = 0
    for pat in INLINE_LOGO_PATTERNS:
        text, n = re.subn(pat, "", text, flags=re.DOTALL)
        removed += n

    # Remove prior placeholder comments / broken selectors
    text = re.sub(r"\s*/\* logo: assets/brand-logo\.css \*/\s*", "\n", text)
    text = re.sub(r"\.masthead\.compact\s*/\* logo:[^*]+\*/\s*", "", text)

    # Ensure brand-logo.css loads last in head (after inline + section-heading)
    if "</head>" in text:
        head, tail = text.split("</head>", 1)
        head = re.sub(
            r'\s*<link rel="stylesheet" href="assets/brand-logo\.css" />\s*',
            "\n",
            head,
        )
        head = head.rstrip() + "\n" + LATE_BRAND_LINK
        text = head + "</head>" + tail

    if text != orig:
        INDEX.write_text(text, encoding="utf-8")
    print(f"Removed {removed} inline logo blocks; brand-logo.css ordered last in head.")


if __name__ == "__main__":
    main()
