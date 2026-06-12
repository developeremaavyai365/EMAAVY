import re
from pathlib import Path

def hero_copy(name):
    t = Path(name).read_text(encoding="utf-8")
    m = re.search(r'<div class="hero-copy">(.*?)</div>\s*<div class="hero-visual', t, re.DOTALL)
    return m.group(1) if m else ""

a = hero_copy("index.html")
b = hero_copy("index1.html")
# normalize logo vs letters for comparison
a2 = re.sub(r'<img[^>]+>', "[[LOGO]]", a)
b2 = re.sub(r'<span class="hero-brand-letters"[^>]*>.*?</span>', "[[LOGO]]", b, flags=re.DOTALL)
if a2 == b2:
    print("Hero copy HTML matches (logo slot only difference)")
else:
    for i, (x, y) in enumerate(zip(a2.splitlines(), b2.splitlines())):
        if x != y:
            print("diff line", i)
            print(" index:", x[:200])
            print(" ref:  ", y[:200])
