from pathlib import Path
import re
t = Path(__file__).resolve().parents[1] / "emaavy_white_blue (2).html"
text = t.read_text(encoding="utf-8")
# hero section in body
m = re.search(r'<section class="hero"[^>]*>.*?</section>', text, re.DOTALL)
print("BODY HERO LEN", len(m.group(0)) if m else 0)
if m:
    print(m.group(0)[:4000])
# base hero css in first style block
for pat in [r'/\* ─── Hero: asymmetric.*?\*/.*?(?=/\* ───)', r'\.hero-copy\{[^}]+\}', r'\.hero \{ min-height: 100vh']:
    x = re.search(pat, text, re.DOTALL)
    if x:
        print("\n--- MATCH", pat[:40], "---\n", x.group(0)[:2000])
