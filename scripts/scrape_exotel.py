import re
import urllib.request

UA = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36"}
html = urllib.request.urlopen(
    urllib.request.Request("https://exotel.com/", headers=UA), timeout=20
).read().decode("utf-8", "ignore")

# header logo patterns
for m in re.finditer(r'.{0,80}(?:logo|Logo|navbar|header).{0,120}', html):
    s = m.group(0)
    if "svg" in s or "png" in s or "webp" in s:
        print(s[:200])

print("\n--- all svg/png in first 50k ---")
for u in sorted(set(re.findall(r'/(?:assets|static|images|media)[^"\']+\.(?:svg|png|webp)', html))):
    if "logo" in u.lower() or "exotel" in u.lower() or "brand" in u.lower():
        print(u)
