#!/usr/bin/env python3
"""Fix hero command center HTML: SVG links, status bar, logo."""
from pathlib import Path

INDEX = Path(__file__).resolve().parents[1] / "index.html"

SVG_BLOCK = '''<svg class="hcc-connections" viewBox="0 0 600 600" aria-hidden="true"><defs><linearGradient id="hcc-path-gradient" x1="0%" y1="0%" x2="100%" y2="100%"><stop offset="0%" stop-color="#18345d" stop-opacity="0.35"/><stop offset="50%" stop-color="#4a658b" stop-opacity="0.65"/><stop offset="100%" stop-color="#5a7d9e" stop-opacity="0.4"/></linearGradient></defs><path class="hcc-path-soft" data-hcc-link="agents" d="M300 300 Q335 255 492 300"/><path class="hcc-path" data-hcc-link="agents" d="M300 300 Q335 255 492 300"/><path class="hcc-path-flow" data-hcc-link="agents" d="M300 300 Q335 255 492 300"/><path class="hcc-path-soft" data-hcc-link="telephony" d="M300 300 Q360 240 444 156"/><path class="hcc-path" data-hcc-link="telephony" d="M300 300 Q360 240 444 156"/><path class="hcc-path-flow hcc-path-flow--b" data-hcc-link="telephony" d="M300 300 Q360 240 444 156"/><path class="hcc-path-soft" data-hcc-link="whatsapp" d="M300 300 Q300 215 300 108"/><path class="hcc-path" data-hcc-link="whatsapp" d="M300 300 Q300 215 300 108"/><path class="hcc-path-flow hcc-path-flow--c" data-hcc-link="whatsapp" d="M300 300 Q300 215 300 108"/><path class="hcc-path-soft" data-hcc-link="crm" d="M300 300 Q240 240 164 164"/><path class="hcc-path" data-hcc-link="crm" d="M300 300 Q240 240 164 164"/><path class="hcc-path-flow hcc-path-flow--d" data-hcc-link="crm" d="M300 300 Q240 240 164 164"/><path class="hcc-path-soft" data-hcc-link="campaigns" d="M300 300 Q265 255 108 300"/><path class="hcc-path" data-hcc-link="campaigns" d="M300 300 Q265 255 108 300"/><path class="hcc-path-flow hcc-path-flow--e" data-hcc-link="campaigns" d="M300 300 Q265 255 108 300"/><path class="hcc-path-soft" data-hcc-link="workflows" d="M300 300 Q240 360 164 436"/><path class="hcc-path" data-hcc-link="workflows" d="M300 300 Q240 360 164 436"/><path class="hcc-path-flow hcc-path-flow--f" data-hcc-link="workflows" d="M300 300 Q240 360 164 436"/><path class="hcc-path-soft" data-hcc-link="integrations" d="M300 300 Q300 385 300 468"/><path class="hcc-path" data-hcc-link="integrations" d="M300 300 Q300 385 300 468"/><path class="hcc-path-flow hcc-path-flow--g" data-hcc-link="integrations" d="M300 300 Q300 385 300 468"/><path class="hcc-path-soft" data-hcc-link="analytics" d="M300 300 Q360 360 444 436"/><path class="hcc-path" data-hcc-link="analytics" d="M300 300 Q360 360 444 436"/><path class="hcc-path-flow hcc-path-flow--h" data-hcc-link="analytics" d="M300 300 Q360 360 444 436"/></svg>'''

def main():
    text = INDEX.read_text(encoding="utf-8")

    start = text.find('<svg class="hcc-connections"')
    end = text.find('</svg>', start) + len('</svg>')
    if start < 0:
        raise SystemExit("SVG block not found")
    text = text[:start] + SVG_BLOCK + text[end:]

    text = text.replace(
        '<img class="hcc-core-mark" src="assets/brand/emaavy-logo.svg" alt="" width="42" height="8" decoding="async"/>',
        '<img class="hcc-core-mark" src="assets/brand/emaavy-logo.svg" alt="" width="120" height="22" decoding="async"/>',
    )
    text = text.replace("<footer class=\"hcc-status\">", '<div class="hcc-status">')
    text = text.replace("</footer></div></div>", "</div></div></div>")

    INDEX.write_text(text, encoding="utf-8")
    print("Fixed hero showcase HTML.")


if __name__ == "__main__":
    main()
