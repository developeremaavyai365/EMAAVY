import urllib.request
from pathlib import Path

UA = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36"}
OUT = Path(__file__).resolve().parents[1] / "assets" / "logos"
OUT.mkdir(parents=True, exist_ok=True)

downloads = {
    "exotel.png": "https://www.google.com/s2/favicons?domain=exotel.com&sz=128",
    "bandwidth.png": "https://www.google.com/s2/favicons?domain=bandwidth.com&sz=128",
    "knowlarity.png": "https://www.knowlarity.com/header/knowlarityLogo-small.png",
    "flash-bulbul.svg": "https://assets.sarvam.ai/assets/brand/logos/sarvam-wordmark-black.svg",
    "elevenlabs.svg": "https://cdn.simpleicons.org/elevenlabs/000000",
    "vobiz.svg": "https://www.vobiz.ai/whitelogo.svg",
}

for name, url in downloads.items():
    req = urllib.request.Request(url, headers=UA)
    with urllib.request.urlopen(req, timeout=20) as r:
        data = r.read()
    (OUT / name).write_bytes(data)
    print(f"saved {name} ({len(data)} bytes)")

# remove misnamed knowlarity.svg if present
bad = OUT / "knowlarity.svg"
if bad.exists():
    bad.unlink()
    print("removed knowlarity.svg")
