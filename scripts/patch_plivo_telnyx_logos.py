"""Update Plivo and Telnyx to use local SVG logos."""
from pathlib import Path

HTML = Path(__file__).resolve().parents[1] / "emaavy_white_blue (2).html"

REPLACEMENTS = [
    (
        'https://cdn.simpleicons.org/plivo/1282C4',
        "assets/logos/plivo.svg",
    ),
    (
        'https://cdn.simpleicons.org/telnyx/00E3AA',
        "assets/logos/telnyx.svg",
    ),
]

text = HTML.read_text(encoding="utf-8")
count = 0
for old, new in REPLACEMENTS:
    n = text.count(old)
    if n:
        text = text.replace(old, new)
        count += n
        print(f"Replaced {n}x: {old} -> {new}")
    else:
        print(f"Not found: {old}")

if count:
    HTML.write_text(text, encoding="utf-8")
    print("Done")
else:
    print("No changes made")
