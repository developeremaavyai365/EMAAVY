"""Align telephony segment with int-showcase pattern (same as LLM/STT layers)."""
import re
from pathlib import Path

HTML = Path(__file__).resolve().parents[1] / "emaavy_white_blue (2).html"
TELEPHONY_MARKER = "/* ═══ ELEGANT TELEPHONY — voice infrastructure ═══ */"

PARTNERS = [
    ("vobiz", "Vobiz", "Vobiz", "assets/logos/vobiz.svg", "Native carrier", "Global DIDs, intelligent routing, and sub-second connect times for AI voice."),
    ("twilio", "Twilio", "", "https://cdn.worldvectorlogo.com/logos/twilio-2.svg", "Global CPaaS", "Programmable Voice APIs with global reach and trusted carrier infrastructure."),
    ("plivo", "Plivo", "", "assets/logos/plivo.svg", "Global CPaaS", "Cloud telephony with direct carrier routes and competitive international pricing."),
    ("vonage", "Vonage", "", "https://cdn.simpleicons.org/vonage/000000", "Global CPaaS", "Voice API platform for inbound, outbound, and SIP connectivity worldwide."),
    ("exotel", "Exotel", "Exotel", "assets/logos/exotel.png", "India · APAC", "India-focused cloud telephony with IVR, call tracking, and compliance."),
    ("knowlarity", "Knowlarity", "Knowlarity", "assets/logos/knowlarity.png", "India · APAC", "Virtual numbers and cloud PBX for high-volume Indian voice operations."),
    ("telnyx", "Telnyx", "", "assets/logos/telnyx.svg", "Private network", "Private global network with programmable voice and number provisioning."),
    ("bandwidth", "Bandwidth", "Bandwidth", "assets/logos/bandwidth.png", "Direct carrier", "Direct-to-carrier voice APIs with enterprise-grade reliability and control."),
]


def logo_html(name, text, img):
    if img:
        return f'<div class="int-card-logo"><img src="{img}" alt="{name}" loading="lazy" /></div>'
    return f'<div class="int-card-logo"><span class="brand-mark">{text}</span></div>'


def card(pid, title, text_logo, img, tag, desc):
    return (
        f'<article class="int-card tel-card click-detail" data-detail="{pid}" tabindex="0">'
        f'<div class="tel-card-head">{logo_html(title, text_logo, img)}'
        f'<span class="tel-card-tag">{tag}</span></div>'
        f'<div class="tel-card-body"><h4>{title}</h4><p>{desc}</p></div>'
        f'<footer class="tel-card-foot"><span class="tel-card-cta">View integration</span></footer>'
        f"</article>"
    )


def build_segment():
    cards = "".join(card(*p) for p in PARTNERS)
    return (
        '<div class="int-showcase reveal" id="integration-telephony"> '
        '<div class="int-shell int-shell--telephony"> '
        '<header class="int-head"> '
        '<span class="section-kicker">Foundation layer · Telephony</span> '
        "<h3>Enterprise voice infrastructure for AI agents</h3> "
        "<p>Telephony is the foundation of every AI voice conversation. Connect via CPaaS APIs, SIP trunks, or PSTN — "
        "provision numbers globally and capture audio from the first ring with carrier-grade reliability.</p> "
        "</header> "
        '<div class="int-stat-row"> '
        '<div class="int-stat"><span class="int-stat-dot" aria-hidden="true"></span><b>8+</b> Carrier partners</div> '
        '<div class="int-stat"><b>180+</b> Countries</div> '
        '<div class="int-stat"><b>&lt;1s</b> Ring-to-answer</div> '
        '<div class="int-stat"><b>99.9%</b> Platform uptime</div> '
        "</div> "
        f'<div class="int-cards-grid" aria-label="Telephony partners">{cards}</div> '
        '<div class="call-flow" aria-label="Live call lifecycle"> '
        '<header class="call-flow-head"> '
        '<span class="call-flow-kicker">Live call flow</span> '
        '<p class="call-flow-title">What happens on every call</p> '
        "</header> "
        '<ol class="call-flow-track"> '
        '<li class="call-flow-step"><span class="call-flow-index">01</span>'
        '<span class="call-flow-label">Voice channel opens</span></li> '
        '<li class="call-flow-step" aria-hidden="true"><span class="call-flow-connector"></span></li> '
        '<li class="call-flow-step"><span class="call-flow-index">02</span>'
        '<span class="call-flow-label">Carrier routes the call</span></li> '
        '<li class="call-flow-step" aria-hidden="true"><span class="call-flow-connector"></span></li> '
        '<li class="call-flow-step"><span class="call-flow-index">03</span>'
        '<span class="call-flow-label">EMAAVY streams audio</span></li> '
        '<li class="call-flow-step" aria-hidden="true"><span class="call-flow-connector"></span></li> '
        '<li class="call-flow-step"><span class="call-flow-index">04</span>'
        '<span class="call-flow-label">AI agent responds</span></li> '
        '<li class="call-flow-step" aria-hidden="true"><span class="call-flow-connector"></span></li> '
        '<li class="call-flow-step"><span class="call-flow-index">05</span>'
        '<span class="call-flow-label">CRM updated in real time</span></li> '
        "</ol></div></div></div> "
    )


def main():
    text = HTML.read_text(encoding="utf-8")

    pattern = re.compile(
        r'<div class="telephony-showcase reveal" id="integration-telephony">'
        r".*?(?=<div class=\"int-showcase reveal\" id=\"integration-llm\">)",
        re.DOTALL,
    )
    if not pattern.search(text):
        pattern = re.compile(
            r'<div class="int-showcase reveal" id="integration-telephony">'
            r".*?(?=<div class=\"int-showcase reveal\" id=\"integration-llm\">)",
            re.DOTALL,
        )
    if not pattern.search(text):
        print("ERROR: telephony block not found")
        return

    text = pattern.sub(build_segment(), text, count=1)
    print("Restructured telephony to int-showcase layout")

    if TELEPHONY_MARKER in text:
        start = text.index(TELEPHONY_MARKER)
        end = text.index("</style>", start)
        text = text[:start] + text[end:]
        print("Removed redundant ELEGANT TELEPHONY CSS block")

    # int-shell--telephony accent (matches hub blue)
    accent = """
.int-shell--telephony { --int-accent: #2563eb; --int-accent-dark: #1d4ed8; --int-accent-soft: rgba(37, 99, 235, 0.14); --int-accent-border: rgba(37, 99, 235, 0.24); --int-glow-a: transparent; --int-glow-b: transparent; }
"""
    if ".int-shell--telephony {" not in text:
        for marker in (".int-shell--llm {", ".int-shell--stt {", ".int-shell--tools {"):
            if marker in text:
                text = text.replace(marker, accent + " " + marker, 1)
                print("Added int-shell--telephony CSS vars")
                break

    HTML.write_text(text, encoding="utf-8")
    print("Done")


if __name__ == "__main__":
    main()
