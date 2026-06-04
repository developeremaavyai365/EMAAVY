import re
import urllib.request

UA = {"User-Agent": "Mozilla/5.0"}
html = urllib.request.urlopen(
    urllib.request.Request("https://exotel.com/", headers=UA), timeout=20
).read().decode("utf-8", "ignore")

for pat in [r'og:image[^>]+', r'favicon[^"\']+', r'exotel[^"\']*\.(?:png|svg|webp)', r'aria-label="Exotel"[^>]*>.*?</a>']:
    hits = re.findall(pat, html, re.I | re.DOTALL)
    print("PAT", pat[:30], len(hits))
    for h in hits[:5]:
        print(h[:300])

# header link area
idx = html.find('aria-label="Exotel"')
if idx >= 0:
    print("\nHEADER SNIP:")
    print(html[idx:idx+800])

urls = [
    "https://raw.githubusercontent.com/raivo-otp/issuer-icons/master/vectors/exotel.com/exotel.svg",
    "https://raw.githubusercontent.com/raivo-otp/issuer-icons/master/vectors/exotel.in/exotel.svg",
    "https://raw.githubusercontent.com/raivo-otp/issuer-icons/master/vectors/bandwidth.com/bandwidth.svg",
    "https://exotel.com/favicon.ico",
    "https://exotel.com/apple-touch-icon.png",
    "https://www.bandwidth.com/favicon.ico",
]
print("\n--- tries ---")
for u in urls:
    try:
        req = urllib.request.Request(u, headers=UA)
        r = urllib.request.urlopen(req, timeout=15)
        d = r.read()
        print("OK", len(d), r.headers.get("content-type"), u)
    except Exception as e:
        print("FAIL", u, e)
