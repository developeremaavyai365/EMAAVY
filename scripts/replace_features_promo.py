"""Replace Platform Capabilities grid with promo + link to features page."""
from pathlib import Path
import re

HTML = Path(__file__).resolve().parents[1] / "emaavy_white_blue (2).html"
text = HTML.read_text(encoding="utf-8")

NEW_SECTION = '''<!-- FEATURES -->
<section id="features" class="cap-section cap-section--promo">
  <div class="capabilities-promo reveal">
    <div class="capabilities-promo-copy">
      <span class="section-kicker">Platform Capabilities</span>
      <h2>Everything your enterprise needs to run voice AI at scale</h2>
      <p class="capabilities-promo-lead">EMAAVY is the operating system for AI-powered conversations — from the first outbound dial to live transcription, reasoning, and automated follow-through. One platform replaces fragmented dialers, STT vendors, and manual QA.</p>
      <ul class="capabilities-promo-highlights" aria-label="Core capabilities">
        <li><strong>Campaigns</strong> — personalized outbound at population scale</li>
        <li><strong>Intelligence</strong> — sentiment, intent, and risk on every live call</li>
        <li><strong>Automation</strong> — webhooks and CRM actions the moment events fire</li>
        <li><strong>Security</strong> — encryption, compliance, and deployment you control</li>
      </ul>
      <div class="capabilities-promo-actions">
        <a href="pages/features.html" class="btn-capabilities-explore">Explore all capabilities</a>
        <a href="book-demo.html" class="btn-capabilities-secondary">Book a demo</a>
      </div>
    </div>
    <div class="capabilities-promo-panel" aria-hidden="true">
      <div class="capabilities-promo-panel-head">Built for revenue, ops, and engineering</div>
      <div class="capabilities-promo-chips">
        <span>Bulk calling</span>
        <span>API triggers</span>
        <span>Real-time STT</span>
        <span>Voice agents</span>
        <span>Call intelligence</span>
        <span>Enterprise security</span>
      </div>
      <p class="capabilities-promo-panel-note">Six core capabilities — each designed to reduce cognitive load and amplify signal inside every conversation.</p>
    </div>
  </div>
  <div class="platform-stats">
    <div class="platform-stat"><b>6</b><span>Core capabilities</span></div>
    <div class="platform-stat"><b>17+</b><span>Integration partners</span></div>
    <div class="platform-stat"><b>1</b><span>Unified API</span></div>
  </div>
</section>'''

pattern = r"<!-- FEATURES -->.*?</section>\s*<!-- INTEGRATIONS"
text2, n = re.subn(pattern, NEW_SECTION + "\n <!-- INTEGRATIONS", text, count=1, flags=re.S)
if not n:
    raise SystemExit("Could not replace features section")
HTML.write_text(text2, encoding="utf-8")
print("Replaced features section")
