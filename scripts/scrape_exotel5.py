import re
import urllib.request

UA = {"User-Agent": "Mozilla/5.0"}
html = urllib.request.urlopen(
    urllib.request.Request("https://exotel.com/", headers=UA), timeout=20
).read().decode("utf-8", "ignore")

for kw in ["site-logo", "SiteLogo", "brand-logo", "exotel-logo", "LogoExotel", "logo-exotel"]:
    if kw.lower() in html.lower():
        idx = html.lower().find(kw.lower())
        print(kw, html[idx - 100 : idx + 400])
        print("---")

# link to home
for m in re.finditer(r'href="/"[^>]*>[\s\S]{0,500}?</a>', html):
    s = m.group(0)
    if "svg" in s or "img" in s or len(s) < 400:
        print("HOME LINK:", s[:600])
        print("---")
