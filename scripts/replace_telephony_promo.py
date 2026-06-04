"""Replace telephony int-showcase with promo on landing page."""
from pathlib import Path
import re

ROOT = Path(__file__).resolve().parents[1]
HTML = ROOT / "emaavy_white_blue (2).html"
text = HTML.read_text(encoding="utf-8")

pat = r'<div class="int-showcase reveal" id="integration-telephony">.*?</div>\s*<div class="int-showcase reveal" id="integration-llm">'

PROMO = '''<div class="int-showcase reveal telephony-promo-wrap" id="integration-telephony">
  <div class="int-shell int-shell--telephony telephony-promo-shell">
    <div class="telephony-promo reveal">
      <div class="telephony-promo-copy">
        <span class="section-kicker">Foundation layer · Telephony</span>
        <h3>EMAAVY powers every call from ring one</h3>
        <p class="telephony-promo-lead">Telephony is the bedrock of AI voice. EMAAVY provisions numbers globally, routes through CPaaS APIs or SIP trunks, and streams carrier-grade audio into your agents — so campaigns connect fast and conversations never drop.</p>
        <ul class="telephony-promo-highlights" aria-label="Telephony highlights">
          <li><strong>Global reach</strong> — 180+ countries, 8+ carrier partners</li>
          <li><strong>Sub-second connect</strong> — intelligent routing and native Vobiz integration</li>
          <li><strong>Live lifecycle</strong> — voice channel → carrier → EMAAVY → agent → CRM</li>
          <li><strong>Enterprise ready</strong> — 99.9% platform uptime and compliance-friendly recording</li>
        </ul>
        <div class="telephony-promo-actions">
          <a href="pages/integrations/telephony.html" class="btn-telephony-explore">Explore telephony</a>
          <a href="book-demo.html" class="btn-telephony-secondary">Book a demo</a>
        </div>
      </div>
      <div class="telephony-promo-panel" aria-hidden="true">
        <div class="telephony-promo-panel-head">Carriers EMAAVY connects today</div>
        <div class="telephony-promo-chips">
          <span>Vobiz</span><span>Twilio</span><span>Plivo</span><span>Vonage</span>
          <span>Exotel</span><span>Knowlarity</span><span>Telnyx</span><span>Bandwidth</span>
        </div>
        <p class="telephony-promo-panel-note">Full specs, live call flow, and per-carrier details on the telephony page.</p>
      </div>
    </div>
    <div class="telephony-promo-stats">
      <div class="int-stat"><span class="int-stat-dot" aria-hidden="true"></span><b>8+</b><span>Carrier partners</span></div>
      <div class="int-stat"><b>180+</b><span>Countries</span></div>
      <div class="int-stat"><b>&lt;1s</b><span>Ring-to-answer</span></div>
      <div class="int-stat"><b>99.9%</b><span>Platform uptime</span></div>
    </div>
  </div>
</div>
<div class="int-showcase reveal" id="integration-llm">'''

text2, n = re.subn(pat, PROMO, text, count=1, flags=re.S)
if not n:
    raise SystemExit("replace failed")
HTML.write_text(text2, encoding="utf-8")
print("ok")
