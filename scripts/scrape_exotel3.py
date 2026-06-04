import re
import urllib.request

UA = {"User-Agent": "Mozilla/5.0"}
html = urllib.request.urlopen(
    urllib.request.Request("https://exotel.com/", headers=UA), timeout=20
).read().decode("utf-8", "ignore")

# first svg blocks
for i, m in enumerate(re.finditer(r"<svg[\s\S]{0,2500}?</svg>", html)):
    s = m.group(0)
    if i < 8 or "exotel" in s.lower() or "Exotel" in s:
        print(f"--- SVG {i} len={len(s)} ---")
        print(s[:1200])
        print()
