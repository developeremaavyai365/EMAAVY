"""Fix telephony nav links, hub copy, broken HTML, routes."""
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
HTML = ROOT / "emaavy_white_blue (2).html"
ROUTES = ROOT / "assets" / "routes.js"
INDEX = ROOT / "pages" / "integrations" / "index.html"

def patch_html():
    s = HTML.read_text(encoding="utf-8")
    # Broken closing tags after integration-tools
    s = s.replace(
        "</section>iv> </div> </div> </section>",
        "</section>",
        1,
    )
    # Hub description
    s = s.replace(
        "Five connected layers — telephony, LLMs, speech, voice, and tools. Click any card for full specs and setup details.",
        "Five connected layers — telephony, LLMs, speech, voice, and tools. Explore telephony and platform capabilities on dedicated pages; other layers scroll here on the home page.",
        1,
    )
    # Masthead telephony dropdown: overview + carrier anchors on telephony page
    old_tel = re.search(
        r'<div class="dropdown-section-title">\s*Telephony</div>\s*<div class="dropdown-link-grid">.*?</div>\s*</div>',
        s,
        re.DOTALL,
    )
    if old_tel:
        new_tel = """<div class="dropdown-section-title"> Telephony</div> <div class="dropdown-link-grid"> <a href="pages/integrations/telephony.html">Explore telephony</a> <a href="pages/integrations/telephony.html#vobiz">Vobiz</a> <a href="pages/integrations/telephony.html#twilio">Twilio</a> <a href="pages/integrations/telephony.html#plivo">Plivo</a> <a href="pages/integrations/telephony.html#vonage">Vonage</a> <a href="pages/integrations/telephony.html#exotel">Exotel</a> <a href="pages/integrations/telephony.html#knowlarity">Knowlarity</a> <a href="pages/integrations/telephony.html#telnyx">Telnyx</a> <a href="pages/integrations/telephony.html#bandwidth">Bandwidth</a> </div> </div>"""
        s = s[: old_tel.start()] + new_tel + s[old_tel.end() :]

    HTML.write_text(s, encoding="utf-8")
    print("patched HTML")


def patch_routes():
    text = ROUTES.read_text(encoding="utf-8")
    telephony_block = """    telephony: [
      { id: 'telephony', label: 'Explore telephony', path: 'pages/integrations/telephony.html' },
      { id: 'vobiz', label: 'Vobiz', path: 'pages/integrations/vobiz.html' },
      { id: 'twilio', label: 'Twilio', path: 'pages/integrations/telephony.html#twilio' },
      { id: 'plivo', label: 'Plivo', path: 'pages/integrations/telephony.html#plivo' },
      { id: 'vonage', label: 'Vonage', path: 'pages/integrations/telephony.html#vonage' },
      { id: 'exotel', label: 'Exotel', path: 'pages/integrations/telephony.html#exotel' },
      { id: 'knowlarity', label: 'Knowlarity', path: 'pages/integrations/telephony.html#knowlarity' },
      { id: 'telnyx', label: 'Telnyx', path: 'pages/integrations/telephony.html#telnyx' },
      { id: 'bandwidth', label: 'Bandwidth', path: 'pages/integrations/telephony.html#bandwidth' },
    ],"""
    text = re.sub(
        r"    telephony: \[.*?\],",
        telephony_block,
        text,
        count=1,
        flags=re.DOTALL,
    )
    ROUTES.write_text(text, encoding="utf-8")
    print("patched routes.js")


def patch_index():
    s = INDEX.read_text(encoding="utf-8")
    card = """          <a href="telephony.html" class="glow-card"><div class="card-icon">📞</div><h3>Telephony</h3><p>EMAAVY voice infrastructure — global carriers, CPaaS, SIP, PSTN, and live call lifecycle.</p><span class="card-tag">Telephony →</span></a>
"""
    if "telephony.html" not in s:
        s = s.replace(
            '<div class="card-grid">\n          <a href="vobiz.html"',
            '<div class="card-grid">\n' + card + '          <a href="vobiz.html"',
            1,
        )
        INDEX.write_text(s, encoding="utf-8")
        print("patched integrations index")


if __name__ == "__main__":
    patch_html()
    patch_routes()
    patch_index()
