#!/usr/bin/env python3
"""Reorder landing hub sections and renumber zone indices."""
from pathlib import Path
import re

ROOT = Path(__file__).resolve().parents[1]
HTML = ROOT / "emaavy_white_blue (2).html"

ORDER = [
    "integrations",
    "agents",
    "campaigns",
    "features",
    "case-studies",
    "journey",
    "faq",
]

# hub index 02..08, alternating from integrations (alt)
ZONE_META = {
    "integrations": {"num": "02", "zone": "2", "alt": True},
    "agents": {"num": "03", "zone": "3", "alt": False},
    "campaigns": {"num": "04", "zone": "4", "alt": False},
    "features": {"num": "05", "zone": "5", "alt": True},
    "case-studies": {"num": "06", "zone": "6", "alt": True},
    "journey": {"num": "07", "zone": "7", "alt": True},
    "faq": {"num": "08", "zone": "8", "alt": False},
}


def extract_block(html: str, section_id: str) -> str:
    pat = rf'(<!--[^>]*-->\s*)?<section id="{re.escape(section_id)}"[^>]*>.*?</section>'
    m = re.search(pat, html, re.DOTALL | re.IGNORECASE)
    if not m:
        raise SystemExit(f"Section not found: {section_id}")
    return m.group(0)


def patch_block(block: str, section_id: str) -> str:
    meta = ZONE_META[section_id]
    block = re.sub(
        r'<span class="hub-zone-index">\d+</span>',
        f'<span class="hub-zone-index">{meta["num"]}</span>',
        block,
        count=1,
    )
    alt = " hub-zone--alt" if meta["alt"] else ""
    # hub-zone--N
    block = re.sub(
        rf'(<section id="{section_id}" class="[^"]*?)hub-zone--\d+',
        rf"\1hub-zone--{meta['zone']}",
        block,
        count=1,
    )
    if meta["alt"]:
        if "hub-zone--alt" not in block.split(">", 1)[0]:
            block = re.sub(
                rf'(<section id="{section_id}" class=")([^"]*)"',
                rf'\1\2 hub-zone--alt"',
                block,
                count=1,
            )
    else:
        block = re.sub(r"(\s)hub-zone--alt(?=\s|")", "", block)
    return block


def main():
    text = HTML.read_text(encoding="utf-8")
    start = text.find("<!-- CONVERSATIONAL FLOWS -->")
    end = text.find("<!-- BOOK A DEMO -->")
    if start < 0 or end < 0:
        raise SystemExit("Markers not found")

    prefix = text[:start]
    suffix = text[end:]

    blocks = {sid: patch_block(extract_block(text, sid), sid) for sid in ORDER}

    connector = '<div class="hub-connector reveal" aria-hidden="true"><span class="hub-connector-dot"></span></div>\n'
    assembled = ""
    for i, sid in enumerate(ORDER):
        if i > 0:
            assembled += connector
        assembled += blocks[sid] + "\n"

    HTML.write_text(prefix + assembled + suffix, encoding="utf-8")
    print("Reordered sections:", ", ".join(ORDER))


if __name__ == "__main__":
    main()
