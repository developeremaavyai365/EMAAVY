"""Elevate LLM integration segment — premium cards, spacing, reasoning flow."""
import re
from pathlib import Path

HTML = Path(__file__).resolve().parents[1] / "emaavy_white_blue (2).html"
MARKER = "/* ═══ LLM CARDS — reasoning layer layout ═══ */"

MODELS = [
    {
        "id": "gpt",
        "provider": "OpenAI",
        "title": "GPT-5.5 / GPT-5.4",
        "tag": "Flagship",
        "logo": '<img src="https://cdn.worldvectorlogo.com/logos/openai-2.svg" alt="OpenAI" loading="lazy" />',
        "desc": "Flagship reasoning for complex sales flows and multi-step objection handling.",
        "value": "Deep reasoning · 128K context",
    },
    {
        "id": "claude",
        "provider": "Anthropic",
        "title": "Claude Opus · Sonnet · Haiku",
        "tag": "Enterprise",
        "logo": '<img src="https://cdn.simpleicons.org/anthropic/191919" alt="Anthropic" loading="lazy" />',
        "desc": "Best-in-class comprehension for nuanced conversations and compliance-sensitive calls.",
        "value": "Nuanced dialogue · Safety-first",
    },
    {
        "id": "gemini",
        "provider": "Google",
        "title": "Gemini Flash Preview",
        "tag": "Real-time",
        "logo": '<img src="https://cdn.simpleicons.org/google/4285F4" alt="Google" loading="lazy" />',
        "desc": "Ultra-fast inference for real-time intent detection during live calls.",
        "value": "Sub-second latency · Live intent",
    },
    {
        "id": "qwen",
        "provider": "Alibaba Cloud",
        "title": "Qwen 3.6",
        "tag": "Multilingual",
        "logo": '<span class="brand-mark">QW</span>',
        "desc": "Cost-efficient multilingual model optimized for Hinglish and regional dialects.",
        "value": "Hinglish-native · Cost-efficient",
    },
    {
        "id": "grok",
        "provider": "xAI",
        "title": "Grok Beta",
        "tag": "Experimental",
        "logo": '<span class="brand-mark">GX</span>',
        "desc": "Experimental reasoning layer for creative scripts and dynamic rebuttals.",
        "value": "Creative scripts · Dynamic rebuttals",
    },
]

HEAD_OLD = (
    "<h3>Pick the perfect brain for every conversation</h3> "
    "<p>Route each call to the best model for reasoning, extraction, or dialogue — switch per agent, per intent, or mid-call without missing a beat.</p>"
)
HEAD_NEW = (
    "<h3>The reasoning engine behind every conversation</h3> "
    "<p>Choose the model that fits each moment — flagship reasoning, real-time inference, or multilingual dialogue. "
    "Route per agent, per intent, or mid-call without losing context.</p>"
)

FLOW_OLD = (
    '<div class="int-cap-strip"> '
    '<div class="int-cap-label">How EMAAVY uses your LLM stack</div> '
    '<div class="int-cap-row"> '
    '<span class="int-cap">Transcript in</span> '
    '<span class="int-cap">Model selected</span> '
    '<span class="int-cap">Intent detected</span> '
    '<span class="int-cap">Data extracted</span> '
    '<span class="int-cap">Agent responds</span> '
    "</div> </div> "
)

FLOW_NEW = (
    '<div class="call-flow" aria-label="LLM orchestration lifecycle"> '
    '<header class="call-flow-head"> '
    '<span class="call-flow-kicker">Model orchestration</span> '
    '<p class="call-flow-title">How EMAAVY uses your LLM stack</p> '
    "</header> "
    '<ol class="call-flow-track"> '
    '<li class="call-flow-step"><span class="call-flow-index">01</span>'
    "<span class=\"call-flow-label\">Transcript in</span></li> "
    '<li class="call-flow-step" aria-hidden="true"><span class="call-flow-connector"></span></li> '
    '<li class="call-flow-step"><span class="call-flow-index">02</span>'
    "<span class=\"call-flow-label\">Model selected</span></li> "
    '<li class="call-flow-step" aria-hidden="true"><span class="call-flow-connector"></span></li> '
    '<li class="call-flow-step"><span class="call-flow-index">03</span>'
    "<span class=\"call-flow-label\">Intent detected</span></li> "
    '<li class="call-flow-step" aria-hidden="true"><span class="call-flow-connector"></span></li> '
    '<li class="call-flow-step"><span class="call-flow-index">04</span>'
    "<span class=\"call-flow-label\">Data extracted</span></li> "
    '<li class="call-flow-step" aria-hidden="true"><span class="call-flow-connector"></span></li> '
    '<li class="call-flow-step"><span class="call-flow-index">05</span>'
    "<span class=\"call-flow-label\">Agent responds</span></li> "
    "</ol></div> "
)

CSS = """
/* ═══ LLM CARDS — reasoning layer layout ═══ */
#integration-llm .int-shell--llm {
  background: linear-gradient(180deg, #ffffff 0%, #fafaff 100%) !important;
  border-color: #e0e7ff !important;
}
#integration-llm .int-head h3 {
  font-size: clamp(1.4rem, 3.2vw, 1.95rem) !important;
}
#integration-llm .int-stat b {
  color: #4338ca !important;
}
#integration-llm .int-cards-grid {
  display: grid !important;
  grid-template-columns: repeat(3, minmax(0, 1fr)) !important;
  gap: 1.35rem 1.1rem !important;
  margin-top: 1.15rem !important;
  margin-bottom: 0.5rem !important;
  padding: 0.25rem !important;
}
#integration-llm .llm-card {
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
#integration-llm .llm-card:hover,
#integration-llm .llm-card:focus-visible {
  border-color: #c7d2fe !important;
  box-shadow: 0 8px 24px rgba(99, 102, 241, 0.12) !important;
  transform: translateY(-2px) !important;
  outline: none !important;
}
#integration-llm .llm-card-head {
  display: flex !important;
  align-items: center !important;
  justify-content: space-between !important;
  gap: 0.45rem !important;
  padding: 0.95rem 1rem 0.8rem !important;
  border-bottom: 1px solid #f1f5f9 !important;
  background: #f8fafc !important;
}
#integration-llm .llm-card-tag {
  font-size: 0.54rem !important;
  font-weight: 600 !important;
  letter-spacing: 0.07em !important;
  text-transform: uppercase !important;
  color: #4338ca !important;
  background: #eef2ff !important;
  border: 1px solid #e0e7ff !important;
  border-radius: 4px !important;
  padding: 0.22rem 0.48rem !important;
  white-space: nowrap !important;
  flex-shrink: 0 !important;
}
#integration-llm .llm-card-body {
  flex: 1 !important;
  display: flex !important;
  flex-direction: column !important;
  gap: 0.4rem !important;
  padding: 0.85rem 1rem 0.7rem !important;
}
#integration-llm .llm-card-provider {
  font-size: 0.62rem !important;
  font-weight: 600 !important;
  letter-spacing: 0.06em !important;
  text-transform: uppercase !important;
  color: #94a3b8 !important;
  margin: 0 !important;
}
#integration-llm .llm-card-body h4 {
  font-family: 'Clash Display', sans-serif !important;
  font-size: 0.92rem !important;
  font-weight: 600 !important;
  color: #0f172a !important;
  margin: 0 !important;
  line-height: 1.3 !important;
  transition: color 0.2s ease !important;
}
#integration-llm .llm-card:hover .llm-card-body h4,
#integration-llm .llm-card:focus-visible .llm-card-body h4 {
  color: #4338ca !important;
}
#integration-llm .llm-card-desc {
  font-size: 0.76rem !important;
  line-height: 1.58 !important;
  color: #64748b !important;
  margin: 0 !important;
  flex: 1 !important;
}
#integration-llm .llm-card-value {
  font-size: 0.68rem !important;
  font-weight: 500 !important;
  color: #6366f1 !important;
  margin: 0.15rem 0 0 !important;
  padding-top: 0.55rem !important;
  border-top: 1px solid #f1f5f9 !important;
  letter-spacing: 0.01em !important;
}
#integration-llm .llm-card-foot {
  margin-top: auto !important;
  padding: 0.65rem 1rem 0.85rem !important;
  border-top: 1px solid #f1f5f9 !important;
  background: #fafbfc !important;
}
#integration-llm .llm-card-cta {
  font-size: 0.58rem !important;
  font-weight: 600 !important;
  letter-spacing: 0.07em !important;
  text-transform: uppercase !important;
  color: #94a3b8 !important;
  transition: color 0.2s ease !important;
}
#integration-llm .llm-card:hover .llm-card-cta,
#integration-llm .llm-card:focus-visible .llm-card-cta {
  color: #6366f1 !important;
}
#integration-llm .int-card-logo {
  width: 44px !important;
  height: 44px !important;
  margin: 0 !important;
  border-radius: 8px !important;
  background: #ffffff !important;
  border: 1px solid #e2e8f0 !important;
  box-shadow: none !important;
}
#integration-llm .int-card-logo img {
  max-height: 24px !important;
  max-width: 34px !important;
  object-fit: contain !important;
}
#integration-llm .int-card-logo .brand-mark {
  font-family: 'Clash Display', sans-serif !important;
  font-size: 0.72rem !important;
  font-weight: 700 !important;
  color: #4338ca !important;
}
@media (max-width: 1180px) {
  #integration-llm .int-cards-grid {
    grid-template-columns: repeat(3, minmax(0, 1fr)) !important;
    gap: 1.25rem 1rem !important;
  }
}
@media (max-width: 820px) {
  #integration-llm .int-cards-grid {
    grid-template-columns: repeat(2, minmax(0, 1fr)) !important;
  }
}
@media (max-width: 560px) {
  #integration-llm .int-cards-grid {
    grid-template-columns: 1fr !important;
    gap: 1rem !important;
    padding: 0 !important;
  }
  #integration-llm .llm-card {
    min-height: 0 !important;
  }
  #integration-llm .llm-card:hover,
  #integration-llm .llm-card:focus-visible {
    transform: none !important;
  }
}
"""


def card(m):
    return (
        f'<article class="int-card llm-card click-detail" data-detail="{m["id"]}" tabindex="0">'
        f'<div class="llm-card-head"><div class="int-card-logo">{m["logo"]}</div>'
        f'<span class="llm-card-tag">{m["tag"]}</span></div>'
        f'<div class="llm-card-body">'
        f'<p class="llm-card-provider">{m["provider"]}</p>'
        f'<h4>{m["title"]}</h4>'
        f'<p class="llm-card-desc">{m["desc"]}</p>'
        f'<p class="llm-card-value">{m["value"]}</p>'
        f"</div>"
        f'<footer class="llm-card-foot"><span class="llm-card-cta">Explore model</span></footer>'
        f"</article>"
    )


def build_grid():
    cards = "".join(card(m) for m in MODELS)
    return f'<div class="int-cards-grid" aria-label="LLM partners">{cards}</div> '


def main():
    text = HTML.read_text(encoding="utf-8")

    grid_pat = re.compile(
        r'<div class="int-cards-grid"[^>]*>.*?</div>\s*(?=<div class="int-cap-strip">|<div class="call-flow")',
        re.DOTALL,
    )
    start = text.find('id="integration-llm"')
    end = text.find('id="integration-stt"', start)
    if start < 0 or end < 0:
        print("ERROR: LLM section bounds not found")
        return
    segment = text[start:end]
    if not grid_pat.search(segment):
        print("ERROR: LLM cards grid not found")
        return
    segment = grid_pat.sub(build_grid().rstrip(), segment, count=1)
    text = text[:start] + segment + text[end:]
    print("Rebuilt LLM card grid")

    if HEAD_OLD in text:
        text = text.replace(HEAD_OLD, HEAD_NEW, 1)
        print("Updated LLM headline copy")

    if FLOW_OLD in text:
        text = text.replace(FLOW_OLD, FLOW_NEW, 1)
        print("Replaced LLM cap strip with llm-flow")
    else:
        print("WARN: LLM flow block not found")

    if MARKER in text:
        start = text.index(MARKER)
        end = text.index("/* ═══ TELEPHONY CARDS", start)
        text = text[:start] + text[end:]
        print("Replaced existing LLM CSS")

    insert_at = text.index("/* ═══ TELEPHONY CARDS")
    text = text[:insert_at] + CSS + text[insert_at:]
    print("Added LLM CSS")

    HTML.write_text(text, encoding="utf-8")
    print("Done")


if __name__ == "__main__":
    main()
