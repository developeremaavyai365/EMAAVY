"""Rebuild telephony segment — holistic voice layer, all carrier partners, no FX."""
import re
from pathlib import Path

HTML = Path(__file__).resolve().parents[1] / "emaavy_white_blue (2).html"
ROUTES = Path(__file__).resolve().parents[1] / "assets" / "routes.js"
MARKER = "/* ═══ ELEGANT TELEPHONY — voice infrastructure ═══ */"

TELEPHONY_PARTNERS = [
    {
        "id": "vobiz",
        "name": "Vobiz",
        "badge": "Native partner",
        "desc": "Global DIDs, intelligent routing, and sub-second connect times for AI voice at scale.",
        "logo": "",
        "text_logo": "Vobiz",
        "metric": "99.2% connect rate",
    },
    {
        "id": "twilio",
        "name": "Twilio",
        "desc": "Programmable Voice APIs with global reach and trusted carrier infrastructure.",
        "logo": "https://cdn.worldvectorlogo.com/logos/twilio-2.svg",
        "metric": "Global CPaaS",
    },
    {
        "id": "plivo",
        "name": "Plivo",
        "desc": "Cloud telephony with direct carrier routes and competitive international pricing.",
        "logo": "https://cdn.simpleicons.org/plivo/1282C4",
        "metric": "Direct routes",
    },
    {
        "id": "vonage",
        "name": "Vonage",
        "desc": "Voice API platform for inbound, outbound, and SIP connectivity worldwide.",
        "logo": "https://cdn.simpleicons.org/vonage/000000",
        "metric": "SIP + PSTN",
    },
    {
        "id": "exotel",
        "name": "Exotel",
        "desc": "India-focused cloud telephony with IVR, call tracking, and regulatory compliance.",
        "logo": "",
        "text_logo": "Exotel",
        "metric": "India · APAC",
    },
    {
        "id": "knowlarity",
        "name": "Knowlarity",
        "desc": "Virtual numbers and cloud PBX built for high-volume Indian voice operations.",
        "logo": "",
        "text_logo": "Knowlarity",
        "metric": "Cloud PBX",
    },
    {
        "id": "telnyx",
        "name": "Telnyx",
        "desc": "Private global network with programmable voice and number provisioning APIs.",
        "logo": "https://cdn.simpleicons.org/telnyx/00E3AA",
        "metric": "Private network",
    },
    {
        "id": "bandwidth",
        "name": "Bandwidth",
        "desc": "Direct-to-carrier voice APIs with enterprise-grade reliability and control.",
        "logo": "",
        "text_logo": "Bandwidth",
        "metric": "Enterprise SLA",
    },
]

DETAIL_ENTRIES = {
    "vobiz": {
        "tag": "Telephony",
        "title": "Vobiz",
        "logo": '<span class="detail-brand-mark">VZ</span>',
        "desc": "Vobiz is EMAAVY's native telephony partner - global number provisioning, intelligent routing, and sub-second connect times for AI-powered voice conversations.",
        "stats": [["99.2%", "Connect rate"], ["<1s", "Ring-to-answer"]],
        "list": [
            "Global DID provisioning & number pools",
            "Intent-aware routing rules",
            "Real-time call status webhooks",
            "Carrier-grade redundancy across regions",
            "Compliance-ready call recording hooks",
        ],
    },
    "twilio": {
        "tag": "Telephony",
        "title": "Twilio Voice",
        "logo": '<img src="https://cdn.worldvectorlogo.com/logos/twilio-2.svg" alt="Twilio" style="height:28px"/>',
        "desc": "Connect EMAAVY to Twilio Programmable Voice — initiate and receive calls, manage numbers, and stream audio over WebSocket for real-time AI agents.",
        "stats": [["Global", "Coverage"], ["REST + WS", "APIs"]],
        "list": [
            "Programmable Voice outbound & inbound",
            "Phone number provisioning worldwide",
            "Media streams for live AI processing",
            "Call status webhooks & recording",
            "Twilio Elastic SIP Trunking support",
        ],
    },
    "plivo": {
        "tag": "Telephony",
        "title": "Plivo",
        "logo": '<img src="https://cdn.simpleicons.org/plivo/1282C4" alt="Plivo" style="height:28px"/>',
        "desc": "Route voice through Plivo's cloud platform — direct carrier relationships, competitive rates, and APIs designed for high-volume AI voice workloads.",
        "stats": [["190+", "Countries"], ["Direct", "Carriers"]],
        "list": [
            "Voice API for outbound & inbound calls",
            "Global number inventory",
            "Real-time call events & recording",
            "SIP trunking for enterprise setups",
            "Competitive per-minute pricing",
        ],
    },
    "vonage": {
        "tag": "Telephony",
        "title": "Vonage Voice API",
        "logo": '<img src="https://cdn.simpleicons.org/vonage/000000" alt="Vonage" style="height:28px"/>',
        "desc": "Integrate Vonage Voice API with EMAAVY for programmable calling, SIP connectivity, and global number management across your AI voice deployments.",
        "stats": [["SIP + PSTN", "Connectivity"], ["Global", "Numbers"]],
        "list": [
            "Outbound & inbound voice sessions",
            "SIP trunking & WebRTC support",
            "Number provisioning & porting",
            "Call recording & event webhooks",
            "Low-latency media handling",
        ],
    },
    "exotel": {
        "tag": "Telephony",
        "title": "Exotel",
        "logo": '<span class="detail-brand-mark">EX</span>',
        "desc": "Exotel powers Indian and APAC voice operations — virtual numbers, IVR, and call tracking integrated with EMAAVY's AI agent layer.",
        "stats": [["India", "Primary market"], ["IVR + API", "Stack"]],
        "list": [
            "Virtual numbers across India",
            "IVR & call flow orchestration",
            "Real-time call analytics",
            "TRAI-compliant operations",
            "API-first integration with EMAAVY",
        ],
    },
    "knowlarity": {
        "tag": "Telephony",
        "title": "Knowlarity",
        "logo": '<span class="detail-brand-mark">KL</span>',
        "desc": "Knowlarity cloud telephony for virtual numbers, call routing, and PBX features — connected to EMAAVY for intelligent AI voice handling.",
        "stats": [["Cloud PBX", "Platform"], ["India", "Scale"]],
        "list": [
            "Virtual business numbers",
            "Cloud PBX & call routing",
            "Click-to-call & API dialer",
            "Call recording & monitoring",
            "High-volume campaign support",
        ],
    },
    "telnyx": {
        "tag": "Telephony",
        "title": "Telnyx",
        "logo": '<img src="https://cdn.simpleicons.org/telnyx/00E3AA" alt="Telnyx" style="height:28px"/>',
        "desc": "Telnyx private network delivers programmable voice with number APIs and media streaming — ideal for latency-sensitive AI voice agents on EMAAVY.",
        "stats": [["Private", "Network"], ["<300ms", "Media latency"]],
        "list": [
            "Programmable voice & messaging",
            "Global number search & provisioning",
            "Real-time media streaming API",
            "SIP connections & elastic trunks",
            "Private IP backbone",
        ],
    },
    "bandwidth": {
        "tag": "Telephony",
        "title": "Bandwidth",
        "logo": '<span class="detail-brand-mark">BW</span>',
        "desc": "Bandwidth provides direct-to-carrier voice APIs with enterprise SLAs — connect EMAAVY to a carrier-grade network you control end to end.",
        "stats": [["Direct", "Carrier"], ["Enterprise", "SLA"]],
        "list": [
            "Voice API with direct carrier access",
            "Number ordering & porting",
            "Emergency calling compliance",
            "Call recording & transcription hooks",
            "Dedicated enterprise support",
        ],
    },
}

TELEPHONY_CSS = """
/* ═══ ELEGANT TELEPHONY — voice infrastructure ═══ */
#integration-telephony .telephony-shell {
  position: relative !important;
  width: min(1200px, calc(100% - 2rem)) !important;
  margin: 0 auto 2rem !important;
  padding: 2.75rem clamp(1.25rem, 4vw, 2.25rem) 2rem !important;
  border-radius: 12px !important;
  border: 1px solid #e2e8f0 !important;
  background: #ffffff !important;
  box-shadow: none !important;
  overflow: visible !important;
}
#integration-telephony .telephony-head {
  text-align: center !important;
  max-width: 720px !important;
  margin: 0 auto 2rem !important;
}
#integration-telephony .telephony-head .section-kicker {
  display: inline-flex !important;
  font-size: 0.65rem !important;
  font-weight: 500 !important;
  letter-spacing: 0.08em !important;
  text-transform: uppercase !important;
  color: #64748b !important;
  background: #f8fafc !important;
  border: 1px solid #e2e8f0 !important;
  border-radius: 6px !important;
  padding: 0.35rem 0.75rem !important;
  box-shadow: none !important;
}
#integration-telephony .telephony-head h3 {
  font-family: 'Clash Display', sans-serif !important;
  font-size: clamp(1.45rem, 3.2vw, 2rem) !important;
  font-weight: 600 !important;
  letter-spacing: -0.02em !important;
  color: #0f172a !important;
  margin-top: 0.75rem !important;
  line-height: 1.15 !important;
}
#integration-telephony .telephony-head p {
  color: #64748b !important;
  font-size: 0.94rem !important;
  line-height: 1.7 !important;
  margin-top: 0.65rem !important;
}
#integration-telephony .telephony-stat-row {
  display: flex !important;
  flex-wrap: wrap !important;
  justify-content: center !important;
  gap: 0.5rem !important;
  margin-bottom: 2rem !important;
}
#integration-telephony .telephony-stat {
  padding: 0.55rem 1rem !important;
  border-radius: 6px !important;
  background: #f8fafc !important;
  border: 1px solid #e2e8f0 !important;
  font-size: 0.78rem !important;
  color: #64748b !important;
  box-shadow: none !important;
  backdrop-filter: none !important;
}
#integration-telephony .telephony-stat b {
  font-family: 'Clash Display', sans-serif !important;
  font-size: 0.95rem !important;
  font-weight: 600 !important;
  color: #1e40af !important;
  margin-right: 0.35rem !important;
}
#integration-telephony .telephony-layout {
  display: grid !important;
  grid-template-columns: 1fr 1fr !important;
  gap: 1rem !important;
  margin-bottom: 2rem !important;
}
#integration-telephony .telephony-flow-panel,
#integration-telephony .telephony-capabilities-panel {
  border: 1px solid #e2e8f0 !important;
  border-radius: 10px !important;
  background: #f8fafc !important;
  padding: 1.35rem 1.25rem !important;
}
#integration-telephony .telephony-section-title {
  font-family: 'Clash Display', sans-serif !important;
  font-size: 0.82rem !important;
  font-weight: 600 !important;
  letter-spacing: 0.04em !important;
  text-transform: uppercase !important;
  color: #475569 !important;
  margin: 0 0 1rem !important;
}
#integration-telephony .telephony-flow-steps {
  list-style: none !important;
  margin: 0 !important;
  padding: 0 !important;
  display: flex !important;
  flex-direction: column !important;
  gap: 0.75rem !important;
}
#integration-telephony .telephony-flow-steps li {
  display: flex !important;
  align-items: flex-start !important;
  gap: 0.85rem !important;
  padding: 0.75rem 0.85rem !important;
  border-radius: 8px !important;
  background: #ffffff !important;
  border: 1px solid #e2e8f0 !important;
}
#integration-telephony .telephony-flow-num {
  flex-shrink: 0 !important;
  font-family: 'Clash Display', sans-serif !important;
  font-size: 0.72rem !important;
  font-weight: 600 !important;
  color: #1e40af !important;
  background: #eff6ff !important;
  border: 1px solid #bfdbfe !important;
  border-radius: 6px !important;
  padding: 0.25rem 0.45rem !important;
  line-height: 1 !important;
}
#integration-telephony .telephony-flow-steps b {
  display: block !important;
  font-size: 0.88rem !important;
  font-weight: 600 !important;
  color: #0f172a !important;
  margin-bottom: 0.15rem !important;
}
#integration-telephony .telephony-flow-steps span {
  font-size: 0.78rem !important;
  color: #64748b !important;
  line-height: 1.5 !important;
}
#integration-telephony .telephony-cap-grid {
  list-style: none !important;
  margin: 0 !important;
  padding: 0 !important;
  display: grid !important;
  grid-template-columns: 1fr 1fr !important;
  gap: 0.65rem !important;
}
#integration-telephony .telephony-cap-grid li {
  padding: 0.85rem !important;
  border-radius: 8px !important;
  background: #ffffff !important;
  border: 1px solid #e2e8f0 !important;
}
#integration-telephony .telephony-cap-grid b {
  display: block !important;
  font-size: 0.84rem !important;
  font-weight: 600 !important;
  color: #0f172a !important;
  margin-bottom: 0.2rem !important;
}
#integration-telephony .telephony-cap-grid span {
  font-size: 0.74rem !important;
  color: #64748b !important;
  line-height: 1.45 !important;
}
#integration-telephony .telephony-partners-block {
  margin-bottom: 1.75rem !important;
}
#integration-telephony .telephony-partners-head {
  text-align: center !important;
  max-width: 560px !important;
  margin: 0 auto 1.25rem !important;
}
#integration-telephony .telephony-partners-head h4 {
  font-family: 'Clash Display', sans-serif !important;
  font-size: 1.05rem !important;
  font-weight: 600 !important;
  color: #0f172a !important;
  margin: 0 0 0.4rem !important;
}
#integration-telephony .telephony-partners-head p {
  font-size: 0.85rem !important;
  color: #64748b !important;
  line-height: 1.6 !important;
  margin: 0 !important;
}
#integration-telephony .telephony-partners-grid {
  display: grid !important;
  grid-template-columns: repeat(auto-fill, minmax(220px, 1fr)) !important;
  gap: 0.75rem !important;
}
#integration-telephony .telephony-partner-card {
  position: relative !important;
  padding: 1.15rem !important;
  border-radius: 10px !important;
  border: 1px solid #e2e8f0 !important;
  background: #ffffff !important;
  box-shadow: none !important;
  cursor: pointer !important;
  display: flex !important;
  flex-direction: column !important;
  gap: 0.4rem !important;
  transition: border-color 0.2s ease, box-shadow 0.2s ease !important;
}
#integration-telephony .telephony-partner-card:hover,
#integration-telephony .telephony-partner-card:focus-visible {
  border-color: #cbd5e1 !important;
  box-shadow: 0 4px 16px rgba(15, 23, 42, 0.06) !important;
  outline: none !important;
}
#integration-telephony .telephony-partner-card.is-native {
  border-color: #bfdbfe !important;
  background: linear-gradient(180deg, #f8fbff 0%, #ffffff 100%) !important;
}
#integration-telephony .telephony-partner-top {
  display: flex !important;
  align-items: flex-start !important;
  justify-content: space-between !important;
  gap: 0.5rem !important;
}
#integration-telephony .telephony-partner-logo {
  width: 44px !important;
  height: 44px !important;
  border-radius: 8px !important;
  background: #f8fafc !important;
  border: 1px solid #e2e8f0 !important;
  display: flex !important;
  align-items: center !important;
  justify-content: center !important;
  flex-shrink: 0 !important;
  box-shadow: none !important;
}
#integration-telephony .telephony-partner-logo img {
  max-height: 22px !important;
  width: auto !important;
  object-fit: contain !important;
}
#integration-telephony .telephony-partner-logo .brand-mark {
  font-family: 'Clash Display', sans-serif !important;
  font-size: 0.62rem !important;
  font-weight: 700 !important;
  color: #1e40af !important;
  letter-spacing: -0.02em !important;
}
#integration-telephony .telephony-partner-badge {
  font-size: 0.55rem !important;
  font-weight: 600 !important;
  letter-spacing: 0.06em !important;
  text-transform: uppercase !important;
  color: #1e40af !important;
  background: #eff6ff !important;
  border: 1px solid #bfdbfe !important;
  border-radius: 4px !important;
  padding: 0.18rem 0.45rem !important;
  white-space: nowrap !important;
}
#integration-telephony .telephony-partner-card h4 {
  font-family: 'Clash Display', sans-serif !important;
  font-size: 0.92rem !important;
  font-weight: 600 !important;
  color: #0f172a !important;
  margin: 0 !important;
}
#integration-telephony .telephony-partner-card p {
  font-size: 0.78rem !important;
  color: #64748b !important;
  line-height: 1.55 !important;
  margin: 0 !important;
  flex: 1 !important;
}
#integration-telephony .telephony-partner-metric {
  font-size: 0.68rem !important;
  font-weight: 500 !important;
  color: #94a3b8 !important;
  margin-top: 0.25rem !important;
}
#integration-telephony .telephony-partner-hint {
  font-size: 0.58rem !important;
  font-weight: 500 !important;
  letter-spacing: 0.04em !important;
  text-transform: uppercase !important;
  color: #94a3b8 !important;
  margin-top: 0.35rem !important;
}
#integration-telephony .telephony-partner-card:hover .telephony-partner-hint {
  color: #64748b !important;
}
#integration-telephony .telephony-cap-strip {
  margin-top: 0 !important;
  padding-top: 1.35rem !important;
  border-top: 1px solid #e2e8f0 !important;
}
#integration-telephony .telephony-cap-label {
  text-align: center !important;
  font-size: 0.6rem !important;
  font-weight: 600 !important;
  letter-spacing: 0.08em !important;
  text-transform: uppercase !important;
  color: #94a3b8 !important;
  margin-bottom: 0.65rem !important;
}
#integration-telephony .telephony-cap-row {
  display: flex !important;
  flex-wrap: wrap !important;
  justify-content: center !important;
  gap: 0.4rem !important;
}
#integration-telephony .telephony-cap {
  padding: 0.35rem 0.65rem !important;
  border-radius: 6px !important;
  font-size: 0.7rem !important;
  font-weight: 500 !important;
  color: #475569 !important;
  background: #f8fafc !important;
  border: 1px solid #e2e8f0 !important;
  box-shadow: none !important;
}
#integration-telephony .telephony-stage,
#integration-telephony .telephony-visual,
#integration-telephony .telephony-vobiz-zone,
#integration-telephony .telephony-hero,
#integration-telephony .telephony-features,
#integration-telephony .int-fx {
  display: none !important;
}
@media (max-width: 900px) {
  #integration-telephony .telephony-layout {
    grid-template-columns: 1fr !important;
  }
}
@media (max-width: 640px) {
  #integration-telephony .telephony-shell {
    width: calc(100% - 1.5rem) !important;
    padding: 2rem 1rem 1.5rem !important;
  }
  #integration-telephony .telephony-cap-grid {
    grid-template-columns: 1fr !important;
  }
  #integration-telephony .telephony-partners-grid {
    grid-template-columns: 1fr !important;
  }
}
"""


def logo_html(p):
    if p.get("logo"):
        return f'<img src="{p["logo"]}" alt="{p["name"]}" loading="lazy" />'
    text = p.get("text_logo", p["name"][:2])
    return f'<span class="brand-mark">{text}</span>'


def build_partner_card(p):
    native = ' is-native' if p.get("badge") else ""
    badge = (
        f'<span class="telephony-partner-badge">{p["badge"]}</span>'
        if p.get("badge")
        else ""
    )
    return (
        f'<article class="telephony-partner-card click-detail{native}" '
        f'data-detail="{p["id"]}" tabindex="0" role="button">'
        f'<div class="telephony-partner-top">'
        f'<div class="telephony-partner-logo">{logo_html(p)}</div>'
        f"{badge}"
        f"</div>"
        f'<h4>{p["name"]}</h4>'
        f'<p>{p["desc"]}</p>'
        f'<span class="telephony-partner-metric">{p["metric"]}</span>'
        f'<span class="telephony-partner-hint">View specs →</span>'
        f"</article>"
    )


def build_telephony_html():
    cards = "".join(build_partner_card(p) for p in TELEPHONY_PARTNERS)
    return (
        '<div class="telephony-showcase reveal" id="integration-telephony"> '
        '<div class="telephony-shell"> '
        '<header class="telephony-head"> '
        '<span class="section-kicker">Foundation layer · Telephony</span> '
        "<h3>Enterprise voice infrastructure for AI agents</h3> "
        "<p>Telephony is the foundation of every AI voice conversation. EMAAVY connects to your carrier "
        "of choice — CPaaS APIs, SIP trunks, or PSTN — so you provision numbers, route calls globally, "
        "and capture audio from the first ring with carrier-grade reliability.</p> "
        "</header> "
        '<div class="telephony-stat-row"> '
        '<div class="telephony-stat"><b>8+</b>Carrier partners</div> '
        '<div class="telephony-stat"><b>180+</b>Countries</div> '
        '<div class="telephony-stat"><b>&lt;1s</b>Ring-to-answer</div> '
        '<div class="telephony-stat"><b>99.9%</b>Platform uptime</div> '
        "</div> "
        '<div class="telephony-layout"> '
        '<section class="telephony-flow-panel" aria-label="How voice connects"> '
        '<h4 class="telephony-section-title">How voice connects</h4> '
        '<ol class="telephony-flow-steps"> '
        "<li><span class=\"telephony-flow-num\">01</span><div><b>Caller connects</b>"
        "<span>Phone, SIP trunk, or API-initiated voice session</span></div></li> "
        "<li><span class=\"telephony-flow-num\">02</span><div><b>Carrier routes the call</b>"
        "<span>Your CPaaS or SIP provider handles signaling &amp; media</span></div></li> "
        "<li><span class=\"telephony-flow-num\">03</span><div><b>EMAAVY processes in real time</b>"
        "<span>Transcribe, understand intent, and respond through your agent</span></div></li> "
        "</ol></section> "
        '<section class="telephony-capabilities-panel" aria-label="Platform capabilities"> '
        '<h4 class="telephony-section-title">Platform capabilities</h4> '
        '<ul class="telephony-cap-grid"> '
        "<li><b>Global DIDs</b><span>Provision numbers and pools across regions</span></li> "
        "<li><b>Smart routing</b><span>Intent-aware paths with carrier redundancy</span></li> "
        "<li><b>Live webhooks</b><span>Call status events from first ring to hangup</span></li> "
        "<li><b>Compliance ready</b><span>Recording hooks and audit trails built in</span></li> "
        "</ul></section></div> "
        '<section class="telephony-partners-block"> '
        '<div class="telephony-partners-head"> '
        "<h4>Supported telephony partners</h4> "
        "<p>Bring your own carrier or use our native integrations. Click any partner for specs and setup details.</p> "
        "</div> "
        f'<div class="telephony-partners-grid" aria-label="Telephony partners">{cards}</div> '
        "</section> "
        '<div class="telephony-cap-strip"> '
        '<div class="telephony-cap-label">What happens on every live call</div> '
        '<div class="telephony-cap-row"> '
        '<span class="telephony-cap">Voice channel opens</span> '
        '<span class="telephony-cap">Carrier routes signal</span> '
        '<span class="telephony-cap">EMAAVY captures audio</span> '
        '<span class="telephony-cap">AI agent responds</span> '
        '<span class="telephony-cap">CRM synced live</span> '
        "</div></div></div></div> "
    )


def js_detail_entry(key, d):
    stats = ", ".join(f"['{a}','{b}']" for a, b in d["stats"])
    items = ", ".join(f"'{x}'" for x in d["list"])
    desc = d["desc"].replace("'", "\\'")
    return (
        f"{key}: {{ tag: '{d['tag']}', title: '{d['title']}', "
        f"logo: '{d['logo']}', desc: '{desc}', "
        f"stats: [{stats}], list: [{items}] }}"
    )


def patch_detail_data(text):
    """Replace vobiz entry and insert other telephony partner entries."""
    vobiz_new = js_detail_entry("vobiz", DETAIL_ENTRIES["vobiz"])
    pattern = re.compile(r"vobiz:\s*\{.*?\},\s*gpt:", re.DOTALL)
    m = pattern.search(text)
    if not m:
        print("WARN: could not find vobiz detailData block (expected vobiz: {...}, gpt:)")
        return text
    old = m.group(0)
    others = ", ".join(
        js_detail_entry(p["id"], DETAIL_ENTRIES[p["id"]])
        for p in TELEPHONY_PARTNERS
        if p["id"] != "vobiz"
    )
    new = vobiz_new + ", " + others + ", gpt:"
    return text.replace(old, new, 1)


def patch_routes():
    if not ROUTES.exists():
        return
    text = ROUTES.read_text(encoding="utf-8")
    items = ",\n      ".join(
        f"{{ id: '{p['id']}', label: '{p['name']}', path: 'pages/integrations/{p['id']}.html' }}"
        if p["id"] == "vobiz"
        else f"{{ id: '{p['id']}', label: '{p['name']}', path: 'pages/integrations/index.html' }}"
        for p in TELEPHONY_PARTNERS
    )
    text = re.sub(
        r"telephony:\s*\[[^\]]*\]",
        f"telephony: [\n      {items},\n    ]",
        text,
        count=1,
    )
    text = text.replace("title: '📞 Telephony'", "title: 'Telephony'")
    ROUTES.write_text(text, encoding="utf-8")
    print("Updated routes.js telephony list")


def main():
    text = HTML.read_text(encoding="utf-8")

    pattern = re.compile(
        r'<div class="telephony-showcase reveal" id="integration-telephony">'
        r".*?(?=<div class=\"int-showcase reveal\" id=\"integration-llm\">)",
        re.DOTALL,
    )
    if not pattern.search(text):
        print("ERROR: telephony block not found")
        return
    text = pattern.sub(build_telephony_html(), text, count=1)
    print("Rebuilt telephony HTML")

    text = patch_detail_data(text)

    # Remove telephony live timer JS
    text = re.sub(
        r"/\* Telephony live call timer \*/\s*\(function \(\) \{.*?\}\)\(\);\s*",
        "",
        text,
        flags=re.DOTALL,
    )

    if MARKER in text:
        start = text.index(MARKER)
        end = text.index("</style>", start)
        text = text[:start] + TELEPHONY_CSS.strip() + "\n" + text[end:]
        print("Updated telephony CSS block")
    else:
        text = text.replace("</style>", TELEPHONY_CSS + "\n</style>", 1)
        print("Injected telephony CSS block")

    HTML.write_text(text, encoding="utf-8")
    patch_routes()
    print("Done")


if __name__ == "__main__":
    main()
