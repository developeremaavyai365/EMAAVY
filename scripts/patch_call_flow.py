"""Refine telephony call-flow strip to elegant timeline design."""
from pathlib import Path

HTML = Path(__file__).resolve().parents[1] / "emaavy_white_blue (2).html"
MARKER = "/* ═══ ELEGANT CALL FLOW — telephony lifecycle ═══ */"

OLD = (
    '<div class="int-cap-strip"> '
    '<div class="int-cap-label">What happens on every live call</div> '
    '<div class="int-cap-row"> '
    '<span class="int-cap">Voice channel opens</span> '
    '<span class="int-cap">Carrier routes signal</span> '
    '<span class="int-cap">EMAAVY captures audio</span> '
    '<span class="int-cap">AI agent responds</span> '
    '<span class="int-cap">CRM synced live</span> '
    "</div></div></div></div> "
)

NEW = (
    '<div class="call-flow" aria-label="Live call lifecycle"> '
    '<header class="call-flow-head"> '
    '<span class="call-flow-kicker">Live call flow</span> '
    "<p class=\"call-flow-title\">What happens on every call</p> "
    "</header> "
    '<ol class="call-flow-track"> '
    '<li class="call-flow-step"><span class="call-flow-index">01</span>'
    "<span class=\"call-flow-label\">Voice channel opens</span></li> "
    '<li class="call-flow-step" aria-hidden="true"><span class="call-flow-connector"></span></li> '
    '<li class="call-flow-step"><span class="call-flow-index">02</span>'
    "<span class=\"call-flow-label\">Carrier routes the call</span></li> "
    '<li class="call-flow-step" aria-hidden="true"><span class="call-flow-connector"></span></li> '
    '<li class="call-flow-step"><span class="call-flow-index">03</span>'
    "<span class=\"call-flow-label\">EMAAVY streams audio</span></li> "
    '<li class="call-flow-step" aria-hidden="true"><span class="call-flow-connector"></span></li> '
    '<li class="call-flow-step"><span class="call-flow-index">04</span>'
    "<span class=\"call-flow-label\">AI agent responds</span></li> "
    '<li class="call-flow-step" aria-hidden="true"><span class="call-flow-connector"></span></li> '
    '<li class="call-flow-step"><span class="call-flow-index">05</span>'
    "<span class=\"call-flow-label\">CRM updated in real time</span></li> "
    "</ol></div></div></div> "
)

CSS = """
/* ═══ ELEGANT CALL FLOW — telephony lifecycle ═══ */
#integration-telephony .call-flow {
  margin-top: 2rem !important;
  padding: 1.75rem clamp(1rem, 3vw, 1.5rem) 1.5rem !important;
  border-radius: 10px !important;
  border: 1px solid #e2e8f0 !important;
  background: #fafbfc !important;
  box-shadow: none !important;
}
#integration-telephony .call-flow-head {
  text-align: center !important;
  margin-bottom: 1.35rem !important;
}
#integration-telephony .call-flow-kicker {
  display: inline-flex !important;
  font-size: 0.62rem !important;
  font-weight: 500 !important;
  letter-spacing: 0.1em !important;
  text-transform: uppercase !important;
  color: #64748b !important;
  margin-bottom: 0.4rem !important;
}
#integration-telephony .call-flow-title {
  font-family: 'Clash Display', sans-serif !important;
  font-size: clamp(0.95rem, 2vw, 1.05rem) !important;
  font-weight: 600 !important;
  letter-spacing: -0.01em !important;
  color: #0f172a !important;
  margin: 0 !important;
  line-height: 1.3 !important;
}
#integration-telephony .call-flow-track {
  display: flex !important;
  align-items: center !important;
  justify-content: center !important;
  flex-wrap: wrap !important;
  gap: 0 !important;
  list-style: none !important;
  padding: 0 !important;
  margin: 0 auto !important;
  max-width: 920px !important;
}
#integration-telephony .call-flow-step {
  display: flex !important;
  flex-direction: column !important;
  align-items: center !important;
  text-align: center !important;
  gap: 0.45rem !important;
  flex: 0 0 auto !important;
  min-width: 96px !important;
  max-width: 130px !important;
  padding: 0 0.15rem !important;
}
#integration-telephony .call-flow-step[aria-hidden="true"] {
  min-width: 0 !important;
  max-width: none !important;
  flex: 0 1 28px !important;
  padding: 0 !important;
  align-self: center !important;
  margin-top: -1.1rem !important;
}
#integration-telephony .call-flow-index {
  display: inline-flex !important;
  align-items: center !important;
  justify-content: center !important;
  width: 2rem !important;
  height: 2rem !important;
  border-radius: 50% !important;
  font-family: 'Clash Display', sans-serif !important;
  font-size: 0.68rem !important;
  font-weight: 600 !important;
  letter-spacing: 0.04em !important;
  color: #1e40af !important;
  background: #ffffff !important;
  border: 1px solid #dbeafe !important;
  box-shadow: none !important;
}
#integration-telephony .call-flow-label {
  font-size: 0.72rem !important;
  font-weight: 500 !important;
  line-height: 1.45 !important;
  color: #475569 !important;
  letter-spacing: 0.01em !important;
}
#integration-telephony .call-flow-connector {
  display: block !important;
  width: 100% !important;
  min-width: 18px !important;
  height: 1px !important;
  background: linear-gradient(90deg, #cbd5e1 0%, #e2e8f0 100%) !important;
  position: relative !important;
}
#integration-telephony .call-flow-connector::after {
  content: '' !important;
  position: absolute !important;
  right: -1px !important;
  top: 50% !important;
  transform: translateY(-50%) !important;
  width: 0 !important;
  height: 0 !important;
  border-top: 3px solid transparent !important;
  border-bottom: 3px solid transparent !important;
  border-left: 4px solid #cbd5e1 !important;
}
@media (max-width: 720px) {
  #integration-telephony .call-flow-track {
    flex-direction: column !important;
    align-items: stretch !important;
    gap: 0 !important;
    max-width: 280px !important;
  }
  #integration-telephony .call-flow-step {
    max-width: none !important;
    width: 100% !important;
    flex-direction: row !important;
    text-align: left !important;
    gap: 0.75rem !important;
    padding: 0.55rem 0 !important;
  }
  #integration-telephony .call-flow-step[aria-hidden="true"] {
    flex: 0 0 auto !important;
    width: 2rem !important;
    margin: 0 0 0 0.15rem !important;
    align-self: stretch !important;
    justify-content: center !important;
  }
  #integration-telephony .call-flow-connector {
    width: 1px !important;
    min-width: 1px !important;
    height: 14px !important;
    background: #e2e8f0 !important;
    margin-left: 0.95rem !important;
  }
  #integration-telephony .call-flow-connector::after {
    display: none !important;
  }
}
"""


def main():
    text = HTML.read_text(encoding="utf-8")
    if OLD not in text:
        print("ERROR: telephony cap-strip block not found")
        return
    text = text.replace(OLD, NEW, 1)
    print("Replaced call-flow HTML")

    if MARKER not in text:
        text = text.replace("</style>", CSS + "</style>", 1)
        print("Added call-flow CSS")
    else:
        print("CSS marker already present")

    HTML.write_text(text, encoding="utf-8")
    print("Done")


if __name__ == "__main__":
    main()
