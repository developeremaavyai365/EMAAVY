import re
import urllib.request

UA = {"User-Agent": "Mozilla/5.0"}
html = urllib.request.urlopen(
    urllib.request.Request("https://exotel.com/", headers=UA), timeout=20
).read().decode("utf-8", "ignore")

paths = sorted(set(re.findall(r"/assets/images/[^\"'\s>]+\.(?:png|svg|webp)", html)))
for p in paths:
    if "logo" not in p.lower() and "megamenu" not in p and "Ebook" not in p:
        print(p)

# try exotel-deem
for u in [
    "https://exotel.com/assets/images/exotel-deem.png",
    "https://www.google.com/s2/favicons?domain=exotel.com&sz=128",
    "https://www.google.com/s2/favicons?domain=bandwidth.com&sz=128",
]:
    try:
        req = urllib.request.Request(u, headers=UA)
        r = urllib.request.urlopen(req, timeout=15)
        d = r.read()
        print("OK", len(d), u)
    except Exception as e:
        print("FAIL", u, e)
