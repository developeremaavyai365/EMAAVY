#!/usr/bin/env python3
"""Remove breadcrumb nav blocks from all EMAAVY subpage HTML files."""
from __future__ import annotations

import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
BREADCRUMB_RE = re.compile(
    r"\s*<nav\s+class=\"breadcrumb\"[^>]*>.*?</nav>\s*",
    re.DOTALL | re.IGNORECASE,
)

TARGETS = [
    ROOT / "pages",
    ROOT / "book-demo.html",
    ROOT / "login.html",
]


def strip_breadcrumbs(text: str) -> tuple[str, int]:
    new_text, n = BREADCRUMB_RE.subn("\n", text)
    return new_text, n


def main():
    total_files = 0
    total_removed = 0
    for target in TARGETS:
        paths = [target] if target.is_file() else target.rglob("*.html")
        for path in paths:
            text = path.read_text(encoding="utf-8")
            if "breadcrumb" not in text:
                continue
            new_text, n = strip_breadcrumbs(text)
            if n:
                path.write_text(new_text, encoding="utf-8")
                print(f"  {path.relative_to(ROOT)} — removed {n}")
                total_files += 1
                total_removed += n
    print(f"Done — {total_removed} breadcrumb block(s) removed from {total_files} file(s).")


if __name__ == "__main__":
    main()
