import re
import urllib.request

UA = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36"}

for site in ["https://exotel.com/", "https://bandwidth.com/"]:
    req = urllib.request.Request(site, headers=UA)
    html = urllib.request.urlopen(req, timeout=20).read().decode("utf-8", "ignore")
    print("===", site, "===")
    for pat in [
        r'src="([^"]+)"',
        r"href='([^']+)'",
    ]:
        hits = [h for h in set(re.findall(pat, html)) if re.search(r"logo|brand|header", h, re.I)]
        for h in sorted(hits)[:40]:
            print(h)

urls = [
    "https://cdn.worldvectorlogo.com/logos/exotel.svg",
    "https://cdn.worldvectorlogo.com/logos/exotel-1.svg",
    "https://cdn.worldvectorlogo.com/logos/bandwidth-1.svg",
    "https://www.bandwidth.com/wp-content/uploads/2020/07/bandwidth-logo.svg",
    "https://www.bandwidth.com/wp-content/themes/bandwidth/dist/images/logo.svg",
    "https://exotel.com/assets/images/exotel-logo-white.svg",
    "https://exotel.com/static/media/exotel-logo.abc.svg",
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
