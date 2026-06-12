import re
from pathlib import Path
t = Path("index.html").read_text(encoding="utf-8")
m = re.search(r'<div class="hero-visual[^>]*>.*?</div>\s*</div>\s*</section>', t, re.DOTALL)
if m:
    s = m.group(0)
    Path("scripts/_hero_visual_snip.txt").write_text(s[:8000], encoding="utf-8")
    print("len", len(s))
else:
    m2 = re.search(r'hero-visual.*', t)
    print("not found full block")
