"""Switch landing masthead from fixed to sticky + link masthead-flex.css."""
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
path = ROOT / "emaavy_white_blue (2).html"
s = path.read_text(encoding="utf-8")

old1 = (
    ".masthead { position: fixed; top: 0; left: 0; right: 0; z-index: 500; "
    "height: var(--masthead-h); pointer-events: none; "
    "transition: height 0.55s cubic-bezier(0.16, 1, 0.3, 1); }"
)
new1 = (
    ".masthead { position: sticky; top: 0; left: 0; right: 0; z-index: 900; "
    "height: auto; min-height: var(--masthead-h-compact, 72px); pointer-events: auto; "
    "transition: transform 0.45s cubic-bezier(0.16, 1, 0.3, 1), box-shadow 0.4s ease; "
    "will-change: transform; }"
)
if old1 in s:
    s = s.replace(old1, new1, 1)
    print("Replaced masthead rule 1")
else:
    print("WARN: masthead rule 1 not found")

old2 = (
    ".masthead { position: fixed; top: 0; left: 0; right: 0; width: 100%; "
    "height: auto; min-height: var(--masthead-h-compact); transform: none !important; "
    "overflow: visible; z-index: 900; }"
)
if old2 in s:
    s = s.replace(old2, "/* masthead: sticky + masthead-flex.css */", 1)
    print("Replaced masthead rule 2")
else:
    print("WARN: masthead rule 2 not found")

link = '<link rel="stylesheet" href="assets/masthead-flex.css" />'
if "masthead-flex.css" not in s:
    anchor = '<link rel="stylesheet" href="assets/flows-showcase.css" />'
    if anchor in s:
        s = s.replace(anchor, anchor + "\n  " + link, 1)
        print("Added masthead-flex.css link")
    else:
        print("WARN: could not insert stylesheet link")

path.write_text(s, encoding="utf-8")
print("Done")
