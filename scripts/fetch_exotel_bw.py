import urllib.request
from pathlib import Path

UA = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36"}
OUT = Path(__file__).resolve().parents[1] / "assets" / "logos"

pairs = {
    "exotel.png": "https://exotel.com/assets/images/exotel-logo.png",
    "bandwidth.png": "https://icon.horse/icon/bandwidth.com",
}

for name, url in pairs.items():
    req = urllib.request.Request(url, headers=UA)
    with urllib.request.urlopen(req, timeout=20) as r:
        (OUT / name).write_bytes(r.read())
    print("saved", name)
