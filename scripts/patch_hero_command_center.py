#!/usr/bin/env python3
"""Replace hero video showcase with Enterprise AI Command Center."""
from pathlib import Path
import re

ROOT = Path(__file__).resolve().parents[1]
INDEX = ROOT / "index.html"

NEW_SHOWCASE = '''<div class="hero-showcase hero-command-center" id="heroVisual" tabindex="0" aria-label="EMAAVY Enterprise AI Command Center — orchestrating agents, communications, workflows, and business operations" aria-live="polite"><div class="hcc-stage"><div class="hcc-ambient" aria-hidden="true"></div><div class="hcc-grid" aria-hidden="true"></div><svg class="hcc-connections" viewBox="0 0 600 600" aria-hidden="true"><defs><linearGradient id="hcc-path-gradient" x1="0%" y1="0%" x2="100%" y2="100%"><stop offset="0%" stop-color="#18345d" stop-opacity="0.35"/><stop offset="50%" stop-color="#4a658b" stop-opacity="0.65"/><stop offset="100%" stop-color="#5a7d9e" stop-opacity="0.4"/></linearGradient></defs><path class="hcc-path-soft" d="M300 300 Q335 255 470 300"/><path class="hcc-path" d="M300 300 Q335 255 470 300"/><path class="hcc-path-flow" d="M300 300 Q335 255 470 300"/><path class="hcc-path-soft" d="M300 300 Q360 240 416 186"/><path class="hcc-path" d="M300 300 Q360 240 416 186"/><path class="hcc-path-flow hcc-path-flow--b" d="M300 300 Q360 240 416 186"/><path class="hcc-path-soft" d="M300 300 Q300 215 300 130"/><path class="hcc-path" d="M300 300 Q300 215 300 130"/><path class="hcc-path-flow hcc-path-flow--c" d="M300 300 Q300 215 300 130"/><path class="hcc-path-soft" d="M300 300 Q240 240 184 186"/><path class="hcc-path" d="M300 300 Q240 240 184 186"/><path class="hcc-path-flow hcc-path-flow--d" d="M300 300 Q240 240 184 186"/><path class="hcc-path-soft" d="M300 300 Q265 255 130 300"/><path class="hcc-path" d="M300 300 Q265 255 130 300"/><path class="hcc-path-flow hcc-path-flow--e" d="M300 300 Q265 255 130 300"/><path class="hcc-path-soft" d="M300 300 Q240 360 184 414"/><path class="hcc-path" d="M300 300 Q240 360 184 414"/><path class="hcc-path-flow hcc-path-flow--f" d="M300 300 Q240 360 184 414"/><path class="hcc-path-soft" d="M300 300 Q300 385 300 470"/><path class="hcc-path" d="M300 300 Q300 385 300 470"/><path class="hcc-path-flow hcc-path-flow--g" d="M300 300 Q300 385 300 470"/><path class="hcc-path-soft" d="M300 300 Q360 360 416 414"/><path class="hcc-path" d="M300 300 Q360 360 416 414"/><path class="hcc-path-flow hcc-path-flow--h" d="M300 300 Q360 360 416 414"/></svg><div class="hcc-core" aria-hidden="true"><div class="hcc-core-aura"></div><div class="hcc-core-ring"></div><div class="hcc-core-body"><img class="hcc-core-mark" src="assets/brand/emaavy-logo.svg" alt="" width="42" height="8" decoding="async"/><span class="hcc-core-label">Emaavy Core</span><span class="hcc-core-sub">AI OS</span></div></div><div class="hcc-nodes"><article class="hcc-node hcc-node--agents is-active" data-system="agents"><div class="hcc-node-card"><span class="hcc-node-pulse" aria-hidden="true"></span><div class="hcc-node-head"><span class="hcc-node-icon" aria-hidden="true"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round"><circle cx="12" cy="8" r="3.5"/><path d="M5 20c0-3.5 3.1-6 7-6s7 2.5 7 6"/><path d="M17 8.5l1.5 1.5M19 11h2"/></svg></span><span class="hcc-node-title">AI Agents</span></div><p class="hcc-node-desc">Handling conversations</p></div></article><article class="hcc-node hcc-node--telephony" data-system="telephony"><div class="hcc-node-card"><span class="hcc-node-pulse" aria-hidden="true"></span><div class="hcc-node-head"><span class="hcc-node-icon" aria-hidden="true"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round"><path d="M6.5 4.8c.6 3.2 2.4 6.1 5 8.7s5.5 4.4 8.7 5l2.2-2.2c.3-.3.8-.4 1.2-.2 1.3.5 2.7.8 4.1.8.7 0 1.2.6 1.2 1.2V21c0 .7-.6 1.2-1.2 1.2C10.1 22.2 1.8 13.9 1.8 3.2 1.8 2.5 2.4 2 3 2h3.5c.7 0 1.2.6 1.2 1.2 0 1.4.3 2.8.8 4.1.1.4 0 .9-.3 1.2L6.5 4.8z"/></svg></span><span class="hcc-node-title">Telephony</span></div><p class="hcc-node-desc">Inbound &amp; outbound calls</p></div></article><article class="hcc-node hcc-node--whatsapp" data-system="whatsapp"><div class="hcc-node-card"><span class="hcc-node-pulse" aria-hidden="true"></span><div class="hcc-node-head"><span class="hcc-node-icon" aria-hidden="true"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round"><path d="M12 3c-4.4 0-8 3.4-8 7.6 0 2.2 1.1 4.2 2.9 5.6L6 21l4.6-1.5c1 .3 2 .4 3 .4 4.4 0 8-3.4 8-7.6S16.4 3 12 3z"/><path d="M9.5 10.5c.3 1.8 2.2 3.4 4 3.7"/></svg></span><span class="hcc-node-title">WhatsApp</span></div><p class="hcc-node-desc">Customer engagement</p></div></article><article class="hcc-node hcc-node--crm" data-system="crm"><div class="hcc-node-card"><span class="hcc-node-pulse" aria-hidden="true"></span><div class="hcc-node-head"><span class="hcc-node-icon" aria-hidden="true"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round"><rect x="4" y="5" width="16" height="14" rx="2"/><path d="M8 9h8M8 13h5"/><path d="M4 9h16"/></svg></span><span class="hcc-node-title">CRM</span></div><p class="hcc-node-desc">Lead &amp; customer sync</p></div></article><article class="hcc-node hcc-node--campaigns" data-system="campaigns"><div class="hcc-node-card"><span class="hcc-node-pulse" aria-hidden="true"></span><div class="hcc-node-head"><span class="hcc-node-icon" aria-hidden="true"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round"><path d="M4 12v5a2 2 0 002 2h12a2 2 0 002-2v-5"/><path d="M12 3v14"/><path d="M8 7l4-4 4 4"/></svg></span><span class="hcc-node-title">Campaigns</span></div><p class="hcc-node-desc">Automated outreach</p></div></article><article class="hcc-node hcc-node--workflows" data-system="workflows"><div class="hcc-node-card"><span class="hcc-node-pulse" aria-hidden="true"></span><div class="hcc-node-head"><span class="hcc-node-icon" aria-hidden="true"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round"><circle cx="6" cy="6" r="2.5"/><circle cx="18" cy="6" r="2.5"/><circle cx="12" cy="18" r="2.5"/><path d="M8.2 7.4l3.3 8.2M15.8 7.4l-3.3 8.2"/></svg></span><span class="hcc-node-title">Workflows</span></div><p class="hcc-node-desc">Process automation</p></div></article><article class="hcc-node hcc-node--integrations" data-system="integrations"><div class="hcc-node-card"><span class="hcc-node-pulse" aria-hidden="true"></span><div class="hcc-node-head"><span class="hcc-node-icon" aria-hidden="true"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round"><path d="M8 12h8"/><path d="M12 8v8"/><circle cx="5" cy="12" r="2"/><circle cx="19" cy="12" r="2"/><circle cx="12" cy="5" r="2"/><circle cx="12" cy="19" r="2"/></svg></span><span class="hcc-node-title">Integrations</span></div><p class="hcc-node-desc">Connected ecosystem</p></div></article><article class="hcc-node hcc-node--analytics" data-system="analytics"><div class="hcc-node-card"><span class="hcc-node-pulse" aria-hidden="true"></span><div class="hcc-node-head"><span class="hcc-node-icon" aria-hidden="true"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round"><path d="M4 19V5"/><path d="M4 19h16"/><rect x="7" y="11" width="3" height="5" rx="0.5"/><rect x="12" y="8" width="3" height="8" rx="0.5"/><rect x="17" y="6" width="3" height="10" rx="0.5"/></svg></span><span class="hcc-node-title">Analytics</span></div><p class="hcc-node-desc">Performance visibility</p></div></article></div><footer class="hcc-status"><span class="hcc-status-live"><span class="hcc-status-dot" aria-hidden="true"></span><span data-hcc-status-label>Agent orchestration</span></span><span class="hcc-status-metric" data-hcc-metric><strong>1</strong> / 8 systems live</span></footer></div></div>'''

OLD_PATTERN = re.compile(
    r'<div class="hero-showcase" id="heroVisual"[^>]*>.*?</div>\s*</div>\s*</div>\s*</section>',
    re.DOTALL,
)

def main():
    text = INDEX.read_text(encoding="utf-8")

    m = OLD_PATTERN.search(text)
    if not m:
        raise SystemExit("Could not find hero showcase block")

    replacement = NEW_SHOWCASE + " </div> </section>"
    text = text[: m.start()] + replacement + text[m.end() :]

    text = text.replace(
        '<link rel="stylesheet" href="assets/hero-video.css" />\n',
        '',
    )
    if 'assets/hero-command-center.css' not in text:
        text = text.replace(
            '<link rel="stylesheet" href="assets/brand-logo.css" />',
            '<link rel="stylesheet" href="assets/brand-logo.css" />\n'
            '  <link rel="stylesheet" href="assets/hero-command-center.css" />',
        )
    text = text.replace(
        '<script src="assets/hero-video.js" defer></script>',
        '<script src="assets/hero-command-center.js" defer></script>',
    )

    INDEX.write_text(text, encoding="utf-8")
    print("Patched index.html — hero command center installed.")


if __name__ == "__main__":
    main()
