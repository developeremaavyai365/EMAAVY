"""Fetch official logos for voice/telephony partners missing images."""
import re
import urllib.request
from pathlib import Path

UA = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36"}
OUT = Path(__file__).resolve().parents[1] / "assets" / "logos"
OUT.mkdir(parents=True, exist_ok=True)

# slug -> list of candidate URLs (first success wins)
CANDIDATES = {
    "vobiz.svg": [
        "https://www.vobiz.ai/images/logo.svg",
        "https://vobiz.ai/logo.svg",
    ],
    "exotel.svg": [
        "https://exotel.com/wp-content/themes/exotel/assets/images/logo.svg",
        "https://exotel.com/wp-content/uploads/2020/05/exotel-logo.svg",
    ],
    "knowlarity.svg": [
        "https://www.knowlarity.com/hubfs/knowlarity-logo.svg",
        "https://www.knowlarity.com/hs-fs/hubfs/knowlarity-logo.png",
    ],
    "bandwidth.svg": [
        "https://www.bandwidth.com/wp-content/themes/bandwidth/assets/images/logo.svg",
        "https://www.bandwidth.com/wp-content/uploads/2021/03/bandwidth-logo.svg",
    ],
    "elevenlabs.svg": [
        "https://elevenlabs.io/favicon.svg",
        "https://elevenlabs.io/assets/elevenlabs-logo.svg",
    ],
    "flash-bulbul.svg": [
        "https://www.sarvam.ai/favicon.svg",
    ],
}


def fetch(url):
    req = urllib.request.Request(url, headers=UA)
    with urllib.request.urlopen(req, timeout=20) as r:
        return r.read(), r.headers.get("content-type", "")


def scrape_logos(site):
    html = fetch(site)[0].decode("utf-8", "ignore")
    return sorted(set(re.findall(r'(?:src|href)="([^"]*(?:logo|brand|svg|icon)[^"]*)"', html, re.I)))


for site in [
    "https://www.vobiz.ai/",
    "https://exotel.com/",
    "https://www.knowlarity.com/",
    "https://www.bandwidth.com/",
    "https://elevenlabs.io/",
    "https://www.sarvam.ai/",
]:
    try:
        logos = scrape_logos(site)
        print(f"\n=== {site} ===")
        for l in logos[:25]:
            print(l)
    except Exception as e:
        print(f"FAIL scrape {site}: {e}")

print("\n--- DOWNLOAD ---")
for fname, urls in CANDIDATES.items():
    saved = False
    for url in urls:
        try:
            data, ctype = fetch(url)
            if len(data) < 100:
                continue
            (OUT / fname).write_bytes(data)
            print(f"OK {fname} <- {url} ({len(data)} bytes, {ctype})")
            saved = True
            break
        except Exception as e:
            print(f"try {url}: {e}")
    if not saved:
        print(f"MISSING {fname}")
