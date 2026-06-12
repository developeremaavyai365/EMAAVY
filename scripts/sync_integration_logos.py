#!/usr/bin/env python3
"""Download and install official integration logos to assets/logos/integrations/."""
from __future__ import annotations

import shutil
import urllib.request
from pathlib import Path

from integration_logos import LOGO_DIR, LOGO_SOURCES

ROOT = Path(__file__).resolve().parents[1]
LEGACY = ROOT / "assets" / "logos"

CUSTOM_SVG: dict[str, str] = {
    "sarvam.svg": """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 120 32" role="img" aria-label="Sarvam AI">
  <rect width="120" height="32" fill="none"/>
  <circle cx="16" cy="16" r="11" fill="#E85D24"/>
  <path d="M12 16 L15 19 L21 12" stroke="#fff" stroke-width="2.2" fill="none" stroke-linecap="round" stroke-linejoin="round"/>
  <text x="34" y="21" font-family="system-ui,Arial,sans-serif" font-size="14" font-weight="700" fill="#0f172a">Sarvam AI</text>
</svg>""",
    "qwen.svg": """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 120 32" role="img" aria-label="Qwen">
  <rect width="120" height="32" fill="none"/>
  <rect x="4" y="6" width="20" height="20" rx="5" fill="#615EFF"/>
  <text x="10" y="20" font-family="system-ui,Arial,sans-serif" font-size="11" font-weight="800" fill="#fff">QW</text>
  <text x="32" y="21" font-family="system-ui,Arial,sans-serif" font-size="15" font-weight="700" fill="#615EFF">Qwen</text>
</svg>""",
    "grok.svg": """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 120 32" role="img" aria-label="Grok">
  <rect width="120" height="32" fill="none"/>
  <circle cx="16" cy="16" r="11" fill="#0f172a"/>
  <path d="M10 16c0-3.3 2.7-6 6-6 2.2 0 4.1 1.2 5.1 3" stroke="#fff" stroke-width="2" fill="none" stroke-linecap="round"/>
  <text x="34" y="21" font-family="system-ui,Arial,sans-serif" font-size="15" font-weight="700" fill="#0f172a">Grok</text>
</svg>""",
    "gladia.svg": """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 120 32" role="img" aria-label="Gladia">
  <rect width="120" height="32" fill="none"/>
  <rect x="4" y="6" width="20" height="20" rx="5" fill="#6366F1"/>
  <path d="M10 20 V12 h8" stroke="#fff" stroke-width="2" fill="none" stroke-linecap="round"/>
  <text x="32" y="21" font-family="system-ui,Arial,sans-serif" font-size="15" font-weight="700" fill="#6366F1">Gladia</text>
</svg>""",
    "smallest.svg": """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 140 32" role="img" aria-label="Smallest AI">
  <rect width="140" height="32" fill="none"/>
  <circle cx="16" cy="16" r="11" fill="#0d9488"/>
  <circle cx="16" cy="16" r="5" fill="#fff"/>
  <text x="32" y="21" font-family="system-ui,Arial,sans-serif" font-size="14" font-weight="700" fill="#0d9488">Smallest AI</text>
</svg>""",
    "webhooks.svg": """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 32 32" role="img" aria-label="Webhooks">
  <rect width="32" height="32" fill="none"/>
  <path d="M8 20c0-2.2 1.8-4 4-4h2a3 3 0 1 0 0-6H12" stroke="#4a658b" stroke-width="2.2" fill="none" stroke-linecap="round"/>
  <circle cx="22" cy="10" r="3" fill="#4a658b"/>
  <circle cx="22" cy="22" r="3" fill="#18345d"/>
</svg>""",
    "exotel.svg": """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 120 32" role="img" aria-label="Exotel">
  <rect width="120" height="32" fill="none"/>
  <rect x="4" y="6" width="20" height="20" rx="4" fill="#E85D24"/>
  <text x="8" y="20" font-family="system-ui,Arial,sans-serif" font-size="10" font-weight="800" fill="#fff">exo</text>
  <text x="32" y="21" font-family="system-ui,Arial,sans-serif" font-size="15" font-weight="700" fill="#E85D24">Exotel</text>
</svg>""",
    "knowlarity.svg": """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 140 32" role="img" aria-label="Knowlarity">
  <rect width="140" height="32" fill="none"/>
  <rect x="4" y="6" width="20" height="20" rx="4" fill="#E31937"/>
  <text x="7" y="20" font-family="system-ui,Arial,sans-serif" font-size="9" font-weight="800" fill="#fff">KNO</text>
  <text x="32" y="21" font-family="system-ui,Arial,sans-serif" font-size="13" font-weight="700" fill="#E31937">Knowlarity</text>
</svg>""",
    "assemblyai.svg": """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 140 32" role="img" aria-label="AssemblyAI">
  <rect width="140" height="32" fill="none"/>
  <rect x="4" y="6" width="20" height="20" rx="5" fill="#2545D0"/>
  <path d="M10 20 V12 h5l3 6 3-6 h5v8" stroke="#fff" stroke-width="1.8" fill="none" stroke-linecap="round" stroke-linejoin="round"/>
  <text x="32" y="21" font-family="system-ui,Arial,sans-serif" font-size="13" font-weight="700" fill="#2545D0">AssemblyAI</text>
</svg>""",
    "bandwidth.svg": """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 130 32" role="img" aria-label="Bandwidth">
  <rect width="130" height="32" fill="none"/>
  <rect x="4" y="6" width="20" height="20" rx="4" fill="#0047BB"/>
  <text x="9" y="20" font-family="system-ui,Arial,sans-serif" font-size="11" font-weight="800" fill="#fff">BW</text>
  <text x="32" y="21" font-family="system-ui,Arial,sans-serif" font-size="14" font-weight="700" fill="#0047BB">Bandwidth</text>
</svg>""",
}

COPY_MAP = {
    "vobiz.svg": LEGACY / "vobiz.svg",
    "flash-bulbul.svg": LEGACY / "flash-bulbul.svg",
    "plivo.svg": LEGACY / "plivo.svg",
    "telnyx.svg": LEGACY / "telnyx.svg",
}

JSDELIVR_ICONS = {
    "azure.svg": "microsoftazure",
    "slack.svg": "slack",
}


def fetch(url: str, dest: Path) -> bool:
    try:
        req = urllib.request.Request(url, headers={"User-Agent": "EMAAVY-logo-sync/1.0"})
        with urllib.request.urlopen(req, timeout=30) as resp:
            dest.write_bytes(resp.read())
        return True
    except Exception as exc:
        print(f"  FAIL {dest.name}: {exc}")
        return False


def main():
    LOGO_DIR.mkdir(parents=True, exist_ok=True)
    ok = 0

    for filename, content in CUSTOM_SVG.items():
        (LOGO_DIR / filename).write_text(content.strip(), encoding="utf-8")
        print(f"  wrote custom {filename}")
        ok += 1

    for filename, src in COPY_MAP.items():
        if src.exists():
            shutil.copy2(src, LOGO_DIR / filename)
            print(f"  copied {filename}")
            ok += 1

    for filename, url in LOGO_SOURCES.items():
        dest = LOGO_DIR / filename
        if fetch(url, dest):
            print(f"  fetched {filename}")
            ok += 1

    for filename, icon in JSDELIVR_ICONS.items():
        url = f"https://cdn.jsdelivr.net/npm/simple-icons@v11/icons/{icon}.svg"
        dest = LOGO_DIR / filename
        if fetch(url, dest):
            print(f"  fetched {filename} (jsDelivr)")
            ok += 1

    # Normalize any extensionless files from prior runs
    for path in LOGO_DIR.iterdir():
        if path.is_file() and path.suffix == "":
            target = path.with_suffix(".svg")
            if not target.exists():
                path.rename(target)
                print(f"  renamed {path.name} -> {target.name}")

    print(f"Done — {ok} logo assets in {LOGO_DIR.relative_to(ROOT)}")


if __name__ == "__main__":
    main()
