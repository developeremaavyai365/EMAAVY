"""Elevate STT segment — premium cards, spacing, call-flow strip."""
import re
from pathlib import Path

HTML = Path(__file__).resolve().parents[1] / "emaavy_white_blue (2).html"
MARKER = "/* ═══ STT CARDS — speech layer layout ═══ */"

PARTNERS = [
    ("assemblyai", "AssemblyAI", "AssemblyAI", "https://cdn.simpleicons.org/assemblyai/2545D0", "Real-time", "Real-time transcription with strong punctuation for live voice agents.", "Live punctuation · Agent-ready"),
    ("azure-stt", "Azure Speech", "Microsoft", "https://cdn.simpleicons.org/microsoftazure/0078D4", "Enterprise", "Enterprise-grade speech recognition with global language support.", "Enterprise SLA · Global languages"),
    ("deepgram", "Deepgram", "Deepgram", "https://cdn.simpleicons.org/deepgram/13EF93", "Low latency", "High-accuracy, low-latency transcription with keyword boosting.", "Sub-500ms · Keyword boost"),
    ("elevenlabs-stt", "ElevenLabs STT", "ElevenLabs", "assets/logos/elevenlabs.svg", "Unified stack", "Unified voice stack — same API key for STT and TTS.", "One API key · STT + TTS"),
    ("gladia", "Gladia", "Gladia", "", "Multilingual", "Multilingual transcription with code-switching and sub-300ms latency.", "Code-switching · Sub-300ms"),
    ("google-stt", "Google STT", "Google", "https://cdn.simpleicons.org/google/4285F4", "Global", "Broad language coverage with telephony-optimized models.", "Telephony-tuned · Broad coverage"),
    ("openai-stt", "OpenAI Whisper", "OpenAI", "https://cdn.worldvectorlogo.com/logos/openai-2.svg", "Whisper", "Accurate speech recognition across languages and accents.", "Multi-accent · Whisper model"),
    ("sarvam", "Sarvam AI", "Sarvam", "assets/logos/flash-bulbul.svg", "India · 22 langs", "Optimized for Hindi, Tamil, Telugu — 22 Indian languages natively.", "Indian languages · Native accuracy"),
    ("smallest", "Smallest AI", "Smallest", "", "Lightweight", "Lightweight, fast transcription for low-latency conversations.", "Ultra-light · Low latency"),
]

HEAD_OLD = (
    "<h3>Every word captured — in real time</h3> "
    "<p>Nine STT providers, one platform. Pick the best engine per language, accent, or latency requirement — EMAAVY routes automatically.</p>"
)
HEAD_NEW = (
    "<h3>Every word captured — in real time</h3> "
    "<p>Nine speech engines, one platform. Route by language, accent, or latency — EMAAVY picks the best STT provider for every live call.</p>"
)

FLOW_OLD = (
    '<div class="int-cap-strip"> '
    '<div class="int-cap-label">From speech to structured insight</div> '
    '<div class="int-cap-row"> '
    '<span class="int-cap">Audio captured</span> '
    '<span class="int-cap">STT transcribes</span> '
    '<span class="int-cap">Intent parsed</span> '
    '<span class="int-cap">Score assigned</span> '
    '<span class="int-cap">Action triggered</span> '
    "</div> </div> "
)

FLOW_NEW = (
    '<div class="call-flow" aria-label="Speech-to-text pipeline"> '
    '<header class="call-flow-head"> '
    '<span class="call-flow-kicker">Speech pipeline</span> '
    '<p class="call-flow-title">From speech to structured insight</p> '
    "</header> "
    '<ol class="call-flow-track"> '
    '<li class="call-flow-step"><span class="call-flow-index">01</span>'
    '<span class="call-flow-label">Audio captured</span></li> '
    '<li class="call-flow-step" aria-hidden="true"><span class="call-flow-connector"></span></li> '
    '<li class="call-flow-step"><span class="call-flow-index">02</span>'
    '<span class="call-flow-label">STT transcribes</span></li> '
    '<li class="call-flow-step" aria-hidden="true"><span class="call-flow-connector"></span></li> '
    '<li class="call-flow-step"><span class="call-flow-index">03</span>'
    '<span class="call-flow-label">Intent parsed</span></li> '
    '<li class="call-flow-step" aria-hidden="true"><span class="call-flow-connector"></span></li> '
    '<li class="call-flow-step"><span class="call-flow-index">04</span>'
    '<span class="call-flow-label">Score assigned</span></li> '
    '<li class="call-flow-step" aria-hidden="true"><span class="call-flow-connector"></span></li> '
    '<li class="call-flow-step"><span class="call-flow-index">05</span>'
    '<span class="call-flow-label">Action triggered</span></li> '
    "</ol></div> "
)

CSS = """
/* ═══ STT CARDS — speech layer layout ═══ */
#integration-stt .int-shell--stt {
  background: linear-gradient(180deg, #ffffff 0%, #fafeff 100%) !important;
  border-color: #cffafe !important;
}
#integration-stt .int-head h3 {
  font-size: clamp(1.4rem, 3.2vw, 1.95rem) !important;
}
#integration-stt .int-stat b {
  color: #0e7490 !important;
}
#integration-stt .int-cards-grid {
  display: grid !important;
  grid-template-columns: repeat(3, minmax(0, 1fr)) !important;
  gap: 1.35rem 1.1rem !important;
  margin-top: 1.15rem !important;
  margin-bottom: 0.5rem !important;
  padding: 0.25rem !important;
}
#integration-stt .stt-card {
  display: flex !important;
  flex-direction: column !important;
  min-height: 210px !important;
  height: 100% !important;
  padding: 0 !important;
  overflow: hidden !important;
  cursor: pointer !important;
  background: #ffffff !important;
  border: 1px solid #e2e8f0 !important;
  border-radius: 10px !important;
  box-shadow: 0 1px 3px rgba(15, 23, 42, 0.04) !important;
  transition: border-color 0.2s ease, box-shadow 0.2s ease, transform 0.2s ease !important;
  isolation: isolate !important;
}
#integration-stt .stt-card:hover,
#integration-stt .stt-card:focus-visible {
  border-color: #a5f3fc !important;
  box-shadow: 0 8px 24px rgba(8, 145, 178, 0.12) !important;
  transform: translateY(-2px) !important;
  outline: none !important;
}
#integration-stt .stt-card-head {
  display: flex !important;
  align-items: center !important;
  justify-content: space-between !important;
  gap: 0.45rem !important;
  padding: 0.95rem 1rem 0.8rem !important;
  border-bottom: 1px solid #f1f5f9 !important;
  background: #f8fafc !important;
}
#integration-stt .stt-card-tag {
  font-size: 0.54rem !important;
  font-weight: 600 !important;
  letter-spacing: 0.07em !important;
  text-transform: uppercase !important;
  color: #0e7490 !important;
  background: #ecfeff !important;
  border: 1px solid #cffafe !important;
  border-radius: 4px !important;
  padding: 0.22rem 0.48rem !important;
  white-space: nowrap !important;
  flex-shrink: 0 !important;
}
#integration-stt .stt-card-body {
  flex: 1 !important;
  display: flex !important;
  flex-direction: column !important;
  gap: 0.4rem !important;
  padding: 0.85rem 1rem 0.7rem !important;
}
#integration-stt .stt-card-provider {
  font-size: 0.62rem !important;
  font-weight: 600 !important;
  letter-spacing: 0.06em !important;
  text-transform: uppercase !important;
  color: #94a3b8 !important;
  margin: 0 !important;
}
#integration-stt .stt-card-body h4 {
  font-family: 'Clash Display', sans-serif !important;
  font-size: 0.92rem !important;
  font-weight: 600 !important;
  color: #0f172a !important;
  margin: 0 !important;
  line-height: 1.3 !important;
  transition: color 0.2s ease !important;
}
#integration-stt .stt-card:hover .stt-card-body h4,
#integration-stt .stt-card:focus-visible .stt-card-body h4 {
  color: #0e7490 !important;
}
#integration-stt .stt-card-desc {
  font-size: 0.76rem !important;
  line-height: 1.58 !important;
  color: #64748b !important;
  margin: 0 !important;
  flex: 1 !important;
}
#integration-stt .stt-card-value {
  font-size: 0.68rem !important;
  font-weight: 500 !important;
  color: #0891b2 !important;
  margin: 0.15rem 0 0 !important;
  padding-top: 0.55rem !important;
  border-top: 1px solid #f1f5f9 !important;
  letter-spacing: 0.01em !important;
}
#integration-stt .stt-card-foot {
  margin-top: auto !important;
  padding: 0.65rem 1rem 0.85rem !important;
  border-top: 1px solid #f1f5f9 !important;
  background: #fafbfc !important;
}
#integration-stt .stt-card-cta {
  font-size: 0.58rem !important;
  font-weight: 600 !important;
  letter-spacing: 0.07em !important;
  text-transform: uppercase !important;
  color: #94a3b8 !important;
  transition: color 0.2s ease !important;
}
#integration-stt .stt-card:hover .stt-card-cta,
#integration-stt .stt-card:focus-visible .stt-card-cta {
  color: #0891b2 !important;
}
#integration-stt .int-card-logo {
  width: 44px !important;
  height: 44px !important;
  margin: 0 !important;
  border-radius: 8px !important;
  background: #ffffff !important;
  border: 1px solid #e2e8f0 !important;
  box-shadow: none !important;
}
#integration-stt .int-card-logo img {
  max-height: 24px !important;
  max-width: 34px !important;
  object-fit: contain !important;
}
#integration-stt .int-card-logo .brand-mark {
  font-family: 'Clash Display', sans-serif !important;
  font-size: 0.72rem !important;
  font-weight: 700 !important;
  color: #0e7490 !important;
}
@media (max-width: 1024px) {
  #integration-stt .int-cards-grid {
    grid-template-columns: repeat(2, minmax(0, 1fr)) !important;
    gap: 1.25rem 1rem !important;
  }
}
@media (max-width: 560px) {
  #integration-stt .int-cards-grid {
    grid-template-columns: 1fr !important;
    gap: 1rem !important;
    padding: 0 !important;
  }
  #integration-stt .stt-card {
    min-height: 0 !important;
  }
  #integration-stt .stt-card:hover,
  #integration-stt .stt-card:focus-visible {
    transform: none !important;
  }
}
"""


def logo_html(name, text, img):
    if img:
        return f'<div class="int-card-logo"><img src="{img}" alt="{name}" loading="lazy" /></div>'
    mark = text[:2].upper() if text else name[:2].upper()
    return f'<div class="int-card-logo"><span class="brand-mark">{mark}</span></div>'


def card(pid, title, provider, img, tag, desc, value):
    return (
        f'<article class="int-card stt-card click-detail" data-detail="{pid}" tabindex="0">'
        f'<div class="stt-card-head">{logo_html(title, provider, img)}'
        f'<span class="stt-card-tag">{tag}</span></div>'
        f'<div class="stt-card-body">'
        f'<p class="stt-card-provider">{provider}</p>'
        f"<h4>{title}</h4>"
        f'<p class="stt-card-desc">{desc}</p>'
        f'<p class="stt-card-value">{value}</p>'
        f"</div>"
        f'<footer class="stt-card-foot"><span class="stt-card-cta">View integration</span></footer>'
        f"</article>"
    )


def build_grid():
    cards = "".join(card(*p) for p in PARTNERS)
    return f'<div class="int-cards-grid" aria-label="STT partners">{cards}</div> '


def extend_call_flow_scopes(text):
    """Add #integration-stt to shared call-flow CSS selectors."""
    pairs = [
        ("#integration-telephony .call-flow,\n#integration-llm .call-flow", "#integration-telephony .call-flow,\n#integration-llm .call-flow,\n#integration-stt .call-flow"),
        ("#integration-telephony .call-flow-head,\n#integration-llm .call-flow-head", "#integration-telephony .call-flow-head,\n#integration-llm .call-flow-head,\n#integration-stt .call-flow-head"),
        ("#integration-telephony .call-flow-kicker,\n#integration-llm .call-flow-kicker", "#integration-telephony .call-flow-kicker,\n#integration-llm .call-flow-kicker,\n#integration-stt .call-flow-kicker"),
        ("#integration-telephony .call-flow-title,\n#integration-llm .call-flow-title", "#integration-telephony .call-flow-title,\n#integration-llm .call-flow-title,\n#integration-stt .call-flow-title"),
        ("#integration-telephony .call-flow-track,\n#integration-llm .call-flow-track", "#integration-telephony .call-flow-track,\n#integration-llm .call-flow-track,\n#integration-stt .call-flow-track"),
        ("#integration-telephony .call-flow-step,\n#integration-llm .call-flow-step", "#integration-telephony .call-flow-step,\n#integration-llm .call-flow-step,\n#integration-stt .call-flow-step"),
        ("#integration-telephony .call-flow-step[aria-hidden=\"true\"],\n#integration-llm .call-flow-step[aria-hidden=\"true\"]", "#integration-telephony .call-flow-step[aria-hidden=\"true\"],\n#integration-llm .call-flow-step[aria-hidden=\"true\"],\n#integration-stt .call-flow-step[aria-hidden=\"true\"]"),
        ("#integration-telephony .call-flow-index,\n#integration-llm .call-flow-index", "#integration-telephony .call-flow-index,\n#integration-llm .call-flow-index,\n#integration-stt .call-flow-index"),
        ("#integration-telephony .call-flow-label,\n#integration-llm .call-flow-label", "#integration-telephony .call-flow-label,\n#integration-llm .call-flow-label,\n#integration-stt .call-flow-label"),
        ("#integration-telephony .call-flow-connector,\n#integration-llm .call-flow-connector", "#integration-telephony .call-flow-connector,\n#integration-llm .call-flow-connector,\n#integration-stt .call-flow-connector"),
        ("#integration-telephony .call-flow-connector::after,\n#integration-llm .call-flow-connector::after", "#integration-telephony .call-flow-connector::after,\n#integration-llm .call-flow-connector::after,\n#integration-stt .call-flow-connector::after"),
    ]
    for old, new in pairs:
        if old in text and "#integration-stt" not in text[text.find(old) : text.find(old) + len(old) + 40]:
            text = text.replace(old, new, 1)

    media_pairs = [
        ("  #integration-telephony .call-flow-track,\n  #integration-llm .call-flow-track", "  #integration-telephony .call-flow-track,\n  #integration-llm .call-flow-track,\n  #integration-stt .call-flow-track"),
        ("  #integration-telephony .call-flow-step,\n  #integration-llm .call-flow-step", "  #integration-telephony .call-flow-step,\n  #integration-llm .call-flow-step,\n  #integration-stt .call-flow-step"),
        ("  #integration-telephony .call-flow-step[aria-hidden=\"true\"],\n  #integration-llm .call-flow-step[aria-hidden=\"true\"]", "  #integration-telephony .call-flow-step[aria-hidden=\"true\"],\n  #integration-llm .call-flow-step[aria-hidden=\"true\"],\n  #integration-stt .call-flow-step[aria-hidden=\"true\"]"),
        ("  #integration-telephony .call-flow-connector,\n  #integration-llm .call-flow-connector", "  #integration-telephony .call-flow-connector,\n  #integration-llm .call-flow-connector,\n  #integration-stt .call-flow-connector"),
        ("  #integration-telephony .call-flow-connector::after,\n  #integration-llm .call-flow-connector::after", "  #integration-telephony .call-flow-connector::after,\n  #integration-llm .call-flow-connector::after,\n  #integration-stt .call-flow-connector::after"),
    ]
    for old, new in media_pairs:
        if old in text and ",\n  #integration-stt" not in text[text.find(old) : text.find(old) + len(old) + 30]:
            text = text.replace(old, new, 1)
    return text


def main():
    text = HTML.read_text(encoding="utf-8")
    start = text.find('id="integration-stt"')
    end = text.find('id="integration-tts"', start)
    if start < 0 or end < 0:
        print("ERROR: STT section not found")
        return

    segment = text[start:end]
    grid_pat = re.compile(
        r'<div class="int-cards-grid"[^>]*>.*?</div>\s*(?=<div class="int-cap-strip">|<div class="call-flow")',
        re.DOTALL,
    )
    if not grid_pat.search(segment):
        print("ERROR: STT cards grid not found")
        return

    segment = grid_pat.sub(build_grid().rstrip() + " ", segment, count=1)
    if HEAD_OLD in segment:
        segment = segment.replace(HEAD_OLD, HEAD_NEW, 1)
        print("Updated STT headline")
    if FLOW_OLD in segment:
        segment = segment.replace(FLOW_OLD, FLOW_NEW, 1)
        print("Replaced STT cap strip with call-flow")
    else:
        print("WARN: STT flow block not found")

    text = text[:start] + segment + text[end:]
    print("Rebuilt STT card grid")

    if MARKER in text:
        s = text.index(MARKER)
        e = text.index("/* ═══ TELEPHONY CARDS", s)
        text = text[:s] + text[e:]
        print("Replaced existing STT CSS")

    insert_at = text.index("/* ═══ TELEPHONY CARDS")
    text = text[:insert_at] + CSS + text[insert_at:]
    print("Added STT CSS")

    text = extend_call_flow_scopes(text)
    print("Extended call-flow CSS to STT")

    HTML.write_text(text, encoding="utf-8")
    print("Done")


if __name__ == "__main__":
    main()
