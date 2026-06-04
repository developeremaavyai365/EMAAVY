"""Add structured tel-card layouts to telephony partner grid."""
import re
from pathlib import Path

HTML = Path(__file__).resolve().parents[1] / "emaavy_white_blue (2).html"
MARKER = "/* ═══ TELEPHONY CARDS — partner grid layout ═══ */"

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

CSS = """
/* ═══ TELEPHONY CARDS — partner grid layout ═══ */
#integration-telephony .int-cards-grid {
  display: grid !important;
  grid-template-columns: repeat(4, minmax(0, 1fr)) !important;
  gap: 1.35rem 1.15rem !important;
  margin-top: 1rem !important;
  margin-bottom: 0.5rem !important;
  padding: 0.25rem !important;
}
#integration-telephony .tel-card {
  display: flex !important;
  flex-direction: column !important;
  min-height: 176px !important;
  height: 100% !important;
  padding: 0 !important;
  overflow: hidden !important;
  cursor: pointer !important;
  background: #ffffff !important;
  border: 1px solid #e2e8f0 !important;
  border-radius: 10px !important;
  box-shadow: 0 1px 3px rgba(15, 23, 42, 0.04) !important;
  transition: border-color 0.2s ease, box-shadow 0.2s ease !important;
  isolation: isolate !important;
}
#integration-telephony .tel-card:hover,
#integration-telephony .tel-card:focus-visible {
  border-color: #bfdbfe !important;
  box-shadow: 0 6px 20px rgba(37, 99, 235, 0.08) !important;
  outline: none !important;
}
#integration-telephony .tel-card-head {
  display: flex !important;
  align-items: center !important;
  justify-content: space-between !important;
  gap: 0.5rem !important;
  padding: 0.9rem 0.95rem 0.75rem !important;
  border-bottom: 1px solid #f1f5f9 !important;
  background: #fafbfc !important;
}
#integration-telephony .tel-card-tag {
  font-size: 0.55rem !important;
  font-weight: 600 !important;
  letter-spacing: 0.06em !important;
  text-transform: uppercase !important;
  color: #64748b !important;
  background: #ffffff !important;
  border: 1px solid #e2e8f0 !important;
  border-radius: 4px !important;
  padding: 0.2rem 0.45rem !important;
  white-space: nowrap !important;
  flex-shrink: 0 !important;
}
#integration-telephony .tel-card-body {
  flex: 1 !important;
  display: flex !important;
  flex-direction: column !important;
  gap: 0.35rem !important;
  padding: 0.8rem 0.95rem 0.65rem !important;
}
#integration-telephony .tel-card-body h4 {
  font-family: 'Clash Display', sans-serif !important;
  font-size: 0.9rem !important;
  font-weight: 600 !important;
  color: #0f172a !important;
  margin: 0 !important;
  line-height: 1.25 !important;
  transition: color 0.2s ease !important;
}
#integration-telephony .tel-card:hover .tel-card-body h4,
#integration-telephony .tel-card:focus-visible .tel-card-body h4 {
  color: #1e40af !important;
}
#integration-telephony .tel-card-body p {
  font-size: 0.76rem !important;
  line-height: 1.55 !important;
  color: #64748b !important;
  margin: 0 !important;
  flex: 1 !important;
}
#integration-telephony .tel-card-foot {
  margin-top: auto !important;
  padding: 0.6rem 0.95rem 0.8rem !important;
  border-top: 1px solid #f1f5f9 !important;
}
#integration-telephony .tel-card-cta {
  font-size: 0.58rem !important;
  font-weight: 600 !important;
  letter-spacing: 0.07em !important;
  text-transform: uppercase !important;
  color: #94a3b8 !important;
  transition: color 0.2s ease !important;
}
#integration-telephony .tel-card:hover .tel-card-cta,
#integration-telephony .tel-card:focus-visible .tel-card-cta {
  color: #2563eb !important;
}
#integration-telephony .int-card-logo {
  width: 42px !important;
  height: 42px !important;
  margin: 0 !important;
  border-radius: 8px !important;
  background: #ffffff !important;
  border: 1px solid #e2e8f0 !important;
  box-shadow: none !important;
}
#integration-telephony .int-card-logo img {
  max-height: 22px !important;
  max-width: 32px !important;
  object-fit: contain !important;
}
@media (max-width: 1080px) {
  #integration-telephony .int-cards-grid {
    grid-template-columns: repeat(2, minmax(0, 1fr)) !important;
    gap: 1.25rem 1rem !important;
  }
}
@media (max-width: 560px) {
  #integration-telephony .int-cards-grid {
    grid-template-columns: 1fr !important;
    gap: 1rem !important;
    padding: 0 !important;
  }
  #integration-telephony .tel-card {
    min-height: 0 !important;
  }
}
"""


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


def build_grid():
    cards = "".join(card(*p) for p in PARTNERS)
    return f'<div class="int-cards-grid" aria-label="Telephony partners">{cards}</div> '


def main():
    text = HTML.read_text(encoding="utf-8")

    pattern = re.compile(
        r'<div class="int-cards-grid" aria-label="Telephony partners">'
        r".*?</div>\s*(?=<div class=\"call-flow\")",
        re.DOTALL,
    )
    if not pattern.search(text):
        print("ERROR: telephony cards grid not found")
        return

    text = pattern.sub(build_grid(), text, count=1)
    print("Rebuilt telephony card grid")

    if MARKER in text:
        start = text.index(MARKER)
        end = text.index("/* ═══ ELEGANT CALL FLOW", start)
        text = text[:start] + text[end:]
        print("Replaced existing telephony card CSS")

    insert_at = text.index("/* ═══ ELEGANT CALL FLOW")
    text = text[:insert_at] + CSS + text[insert_at:]
    print("Added telephony card CSS")

    HTML.write_text(text, encoding="utf-8")
    print("Done")


if __name__ == "__main__":
    main()
