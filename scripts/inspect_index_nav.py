import re
from pathlib import Path

s = Path(__file__).resolve().parents[1] / "index.html"
text = s.read_text(encoding="utf-8")
idx = text.find('<body data-page="home">')
print("body at:", idx)
for marker in ['mobile-nav-drawer', 'mobileNavDrawer', '<section id="top"', '<div id="top"', 'class="hero"', 'rail-dots']:
    pos = text.find(marker, idx)
    print(marker, pos)
if idx >= 0:
    chunk = text[idx:idx+8000]
    drawer_end = text.find('</nav>', text.find('mobile-nav-drawer', idx))
    print("drawer </nav> at", drawer_end)
    after = text[drawer_end:drawer_end+500]
    with open(Path(__file__).parent / "_nav_snip.txt", "w", encoding="utf-8") as f:
        f.write(text[idx:idx+5000])
        f.write("\n---AFTER DRAWER---\n")
        f.write(text[drawer_end:drawer_end+1200])
