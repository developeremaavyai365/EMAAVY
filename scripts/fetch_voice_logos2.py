import urllib.request
from pathlib import Path

UA = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36"}
OUT = Path(__file__).resolve().parents[1] / "assets" / "logos"


def try_url(url):
    req = urllib.request.Request(url, headers=UA)
    with urllib.request.urlopen(req, timeout=20) as r:
        data = r.read()
        ctype = r.headers.get("content-type", "")
        return data, ctype


urls = [
    ("vobiz.svg", "https://www.vobiz.ai/whitelogo.svg"),
    ("exotel.svg", "https://exotel.com/assets/images/exotel-logo.svg"),
    ("exotel.svg", "https://exotel.com/assets/images/logo.svg"),
    ("exotel.svg", "https://my.exotel.com/assets/images/exotel-logo.svg"),
    ("knowlarity.svg", "https://www.knowlarity.com/header/knowlarityLogo-small.png"),
    ("knowlarity.svg", "https://www.knowlarity.com/footer/knowlarity_Logo.png"),
    ("bandwidth.svg", "https://cdn.worldvectorlogo.com/logos/bandwidth.svg"),
    ("bandwidth.svg", "https://cdn.worldvectorlogo.com/logos/bandwidth-com.svg"),
    ("elevenlabs.svg", "https://elevenlabs.io/icon.svg"),
    ("elevenlabs.svg", "https://cdn.simpleicons.org/elevenlabs/000000"),
    ("flash-bulbul.svg", "https://assets.sarvam.ai/assets/brand/logos/sarvam-wordmark-black.svg"),
    ("flash-bulbul.svg", "https://assets.sarvam.ai/assets/brand/logos/sarvam-logo-white.svg"),
]

for fname, url in urls:
    try:
        data, ctype = try_url(url)
        if "html" in ctype and len(data) > 50000:
            print("SKIP html", url, len(data))
            continue
        if len(data) < 80:
            print("SKIP tiny", url, len(data))
            continue
        path = OUT / fname
        path.write_bytes(data)
        print("OK", fname, url, len(data), ctype)
    except Exception as e:
        print("FAIL", url, e)
