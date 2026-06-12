"""Restore hero section typography in index.html from index1.html baseline (keep logo img)."""
from __future__ import annotations

import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
INDEX = ROOT / "index.html"
REF = ROOT / "index1.html"
TYPO = ROOT / "assets" / "emaavy-typography.css"


def extract_hero_css(text: str) -> str:
    m = re.search(
        r"/\* ═══ ELEGANT HERO — brand \+ dynamic showcase ═══ \*/.*?(?=\n</style>)",
        text,
        re.DOTALL,
    )
    return m.group(0) if m else ""


def main() -> None:
    index = INDEX.read_text(encoding="utf-8")
    ref = REF.read_text(encoding="utf-8")
    hero_ref = extract_hero_css(ref)
    if not hero_ref:
        raise SystemExit("Reference hero CSS not found in index1.html")

    # Replace hero CSS block in index.html, preserving logo img in HTML (not in CSS block)
    index_new, n = re.subn(
        r"/\* ═══ ELEGANT HERO — brand \+ dynamic showcase ═══ \*/.*?(?=\n</style>)",
        hero_ref,
        index,
        count=1,
        flags=re.DOTALL,
    )
    if not n:
        raise SystemExit("Hero CSS block not found in index.html")
    INDEX.write_text(index_new, encoding="utf-8")
    print("Restored ELEGANT HERO CSS block from index1.html")

    # Remove global typography overrides that flatten hero headline
    typo = TYPO.read_text(encoding="utf-8")
    hero_override = re.search(
        r"/\* Landing hero headline — solid logo blue.*?\n\}\n\n",
        typo,
        re.DOTALL,
    )
    if hero_override:
        replacement = (
            "/* Landing hero headline — owned by index.html inline hero styles (not global type) */\n\n"
        )
        typo_new = typo.replace(hero_override.group(0), replacement, 1)
        TYPO.write_text(typo_new, encoding="utf-8")
        print("Removed hero-title override from emaavy-typography.css")

    # Ensure brand-logo.css does not affect hero headline (only logo img)
    brand_logo = ROOT / "assets" / "brand-logo.css"
    bl = brand_logo.read_text(encoding="utf-8")
    if "/* Hero headline isolated" not in bl:
        bl = bl.replace(
            "/* ─── Home hero ─── */",
            "/* Hero headline isolated from logo — typography lives in index.html */\n\n/* ─── Home hero logo only ─── */",
        )
        brand_logo.write_text(bl, encoding="utf-8")
        print("Annotated brand-logo.css hero section")


if __name__ == "__main__":
    main()
