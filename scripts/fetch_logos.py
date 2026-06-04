import urllib.request
from pathlib import Path

UA = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36"}
OUT = Path(__file__).resolve().parents[1] / "assets" / "logos"
OUT.mkdir(parents=True, exist_ok=True)

SOURCES = {
    "plivo.svg": "https://www.plivo.com/images/plivo-logo.svg",
    "telnyx.svg": "https://telnyx.com/images/competitors/telnyx-lockup.svg",
}

for name, url in SOURCES.items():
    req = urllib.request.Request(url, headers=UA)
    with urllib.request.urlopen(req, timeout=20) as r:
        data = r.read()
    (OUT / name).write_bytes(data)
    print(f"saved {name} ({len(data)} bytes)")
