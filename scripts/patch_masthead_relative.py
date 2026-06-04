"""Set landing masthead to position:relative (not sticky/fixed)."""
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
path = ROOT / "emaavy_white_blue (2).html"
s = path.read_text(encoding="utf-8")

old = (
    ".masthead { position: sticky; top: 0; left: 0; right: 0; z-index: 900; "
    "height: auto; min-height: var(--masthead-h-compact, 72px); pointer-events: auto; "
    "transition: transform 0.45s cubic-bezier(0.16, 1, 0.3, 1), box-shadow 0.4s ease; "
    "will-change: transform; }"
)
new = (
    ".masthead { position: relative; top: auto; left: auto; right: auto; z-index: 100; "
    "height: auto; min-height: var(--masthead-h-compact, 72px); pointer-events: auto; "
    "transition: box-shadow 0.35s ease; }"
)

if old in s:
    s = s.replace(old, new, 1)
    print("Updated masthead to relative")
elif "position: relative; top: auto" in s:
    print("Already relative")
else:
    print("WARN: masthead block not found — check inline CSS")

path.write_text(s, encoding="utf-8")
print("Done")
