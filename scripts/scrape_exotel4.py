import re
import urllib.request

UA = {"User-Agent": "Mozilla/5.0"}
html = urllib.request.urlopen(
    urllib.request.Request("https://exotel.com/", headers=UA), timeout=20
).read().decode("utf-8", "ignore")

header_end = html.find("</header>")
header = html[: header_end + 9] if header_end > 0 else html[:15000]
print("HEADER LENGTH", len(header))
for m in re.finditer(r"<img[^>]+>", header):
    print(m.group(0))
for m in re.finditer(r"Exotel", header):
    start = max(0, m.start() - 200)
    print("\nCTX:", header[start : m.start() + 200])
