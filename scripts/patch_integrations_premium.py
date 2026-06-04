#!/usr/bin/env python3
"""Align integrations with How It Works premium treatment."""
from pathlib import Path
import re

PATH = Path(__file__).resolve().parents[1] / "emaavy_white_blue (2).html"

PREMIUM_CSS = r"""
/* ═══ INTEGRATIONS PREMIUM — HIW parity (reveal, navy, smooth hovers) ═══ */
#integrations .int-stat-dot {
  background: #4A658B !important;
}
#integrations .int-showcase.reveal {
  transform: translateY(28px) !important;
}
#integrations .int-showcase.reveal.in {
  transform: translateY(0) !important;
}
#integrations .int-cards-grid {
  position: relative !important;
}
#integrations .int-card.reveal,
#integrations .tel-card.reveal,
#integrations .llm-card.reveal,
#integrations .stt-card.reveal {
  opacity: 0 !important;
  transform: translateY(24px) !important;
  transition:
    opacity 0.65s cubic-bezier(0.16, 1, 0.3, 1),
    transform 0.65s cubic-bezier(0.16, 1, 0.3, 1),
    border-color 0.2s ease,
    box-shadow 0.2s ease !important;
}
#integrations .int-card.reveal.in,
#integrations .tel-card.reveal.in,
#integrations .llm-card.reveal.in,
#integrations .stt-card.reveal.in {
  opacity: 1 !important;
  transform: translateY(0) !important;
}
#integrations .int-cards-grid .int-card.reveal:nth-child(1),
#integrations .int-cards-grid .tel-card.reveal:nth-child(1),
#integrations .int-cards-grid .llm-card.reveal:nth-child(1),
#integrations .int-cards-grid .stt-card.reveal:nth-child(1) { transition-delay: 0.04s !important; }
#integrations .int-cards-grid .int-card.reveal:nth-child(2),
#integrations .int-cards-grid .tel-card.reveal:nth-child(2),
#integrations .int-cards-grid .llm-card.reveal:nth-child(2),
#integrations .int-cards-grid .stt-card.reveal:nth-child(2) { transition-delay: 0.09s !important; }
#integrations .int-cards-grid .int-card.reveal:nth-child(3),
#integrations .int-cards-grid .tel-card.reveal:nth-child(3),
#integrations .int-cards-grid .llm-card.reveal:nth-child(3),
#integrations .int-cards-grid .stt-card.reveal:nth-child(3) { transition-delay: 0.14s !important; }
#integrations .int-cards-grid .int-card.reveal:nth-child(4),
#integrations .int-cards-grid .tel-card.reveal:nth-child(4),
#integrations .int-cards-grid .llm-card.reveal:nth-child(4),
#integrations .int-cards-grid .stt-card.reveal:nth-child(4) { transition-delay: 0.19s !important; }
#integrations .int-cards-grid .int-card.reveal:nth-child(5),
#integrations .int-cards-grid .tel-card.reveal:nth-child(5),
#integrations .int-cards-grid .llm-card.reveal:nth-child(5),
#integrations .int-cards-grid .stt-card.reveal:nth-child(5) { transition-delay: 0.24s !important; }
#integrations .int-cards-grid .int-card.reveal:nth-child(6),
#integrations .int-cards-grid .tel-card.reveal:nth-child(6),
#integrations .int-cards-grid .llm-card.reveal:nth-child(6),
#integrations .int-cards-grid .stt-card.reveal:nth-child(6) { transition-delay: 0.29s !important; }
#integrations .int-cards-grid .int-card.reveal:nth-child(7),
#integrations .int-cards-grid .tel-card.reveal:nth-child(7),
#integrations .int-cards-grid .llm-card.reveal:nth-child(7),
#integrations .int-cards-grid .stt-card.reveal:nth-child(7) { transition-delay: 0.34s !important; }
#integrations .int-cards-grid .int-card.reveal:nth-child(8),
#integrations .int-cards-grid .tel-card.reveal:nth-child(8),
#integrations .int-cards-grid .llm-card.reveal:nth-child(8),
#integrations .int-cards-grid .stt-card.reveal:nth-child(8) { transition-delay: 0.39s !important; }
#integrations .call-flow.reveal {
  opacity: 0 !important;
  transform: translateY(20px) !important;
  transition: opacity 0.6s cubic-bezier(0.16, 1, 0.3, 1), transform 0.6s cubic-bezier(0.16, 1, 0.3, 1) !important;
}
#integrations .call-flow.reveal.in {
  opacity: 1 !important;
  transform: translateY(0) !important;
}
#integration-llm .int-shell--llm {
  background: #ffffff !important;
  border-color: #e2e8f0 !important;
}
#integration-llm .int-stat b,
#integration-llm .llm-card-tag,
#integration-llm .llm-card:hover .llm-card-body h4,
#integration-llm .llm-card:focus-visible .llm-card-body h4,
#integration-llm .llm-card-value,
#integration-llm .llm-card:hover .llm-card-cta,
#integration-llm .llm-card:focus-visible .llm-card-cta,
#integration-llm .int-card-logo .brand-mark {
  color: #4A658B !important;
}
#integration-llm .llm-card-tag {
  background: #f0f4f8 !important;
  border-color: #e2e8f0 !important;
}
#integration-llm .llm-card {
  box-shadow: none !important;
  transition: border-color 0.2s ease, box-shadow 0.2s ease, opacity 0.65s cubic-bezier(0.16, 1, 0.3, 1), transform 0.65s cubic-bezier(0.16, 1, 0.3, 1) !important;
}
#integration-llm .llm-card:hover,
#integration-llm .llm-card:focus-visible {
  border-color: #cbd5e1 !important;
  box-shadow: 0 4px 16px rgba(15, 23, 42, 0.06) !important;
  transform: translateY(0) !important;
  outline: none !important;
}
#integration-stt .stt-card {
  box-shadow: none !important;
  transition: border-color 0.2s ease, box-shadow 0.2s ease, opacity 0.65s cubic-bezier(0.16, 1, 0.3, 1), transform 0.65s cubic-bezier(0.16, 1, 0.3, 1) !important;
}
#integration-stt .stt-card:hover,
#integration-stt .stt-card:focus-visible {
  border-color: #cbd5e1 !important;
  box-shadow: 0 4px 16px rgba(15, 23, 42, 0.06) !important;
  transform: translateY(0) !important;
  outline: none !important;
}
#integration-telephony .tel-card {
  transition: border-color 0.2s ease, box-shadow 0.2s ease, opacity 0.65s cubic-bezier(0.16, 1, 0.3, 1), transform 0.65s cubic-bezier(0.16, 1, 0.3, 1) !important;
}
#integration-telephony .tel-card:hover,
#integration-telephony .tel-card:focus-visible {
  border-color: #cbd5e1 !important;
  box-shadow: 0 4px 16px rgba(15, 23, 42, 0.06) !important;
  transform: translateY(0) !important;
}
#integrations .int-card:hover,
#integrations .int-card:focus-visible {
  transform: translateY(0) !important;
}
#integration-telephony .call-flow-index,
#integration-llm .call-flow-index,
#integration-stt .call-flow-index {
  border-radius: 8px !important;
  width: 2.25rem !important;
  height: 2.25rem !important;
  color: #ffffff !important;
  background: #4A658B !important;
  border: none !important;
  transition: background 0.2s ease !important;
}
#integration-telephony .call-flow-track:hover .call-flow-index,
#integration-llm .call-flow-track:hover .call-flow-index,
#integration-stt .call-flow-track:hover .call-flow-index {
  background: #18345D !important;
}
#integrations .tel-card-tag,
#integrations .stt-card-tag,
#integrations .llm-card-tag {
  transition: background 0.2s ease, border-color 0.2s ease, color 0.2s ease !important;
}
#integrations .tel-card:hover .tel-card-tag,
#integrations .tel-card:focus-visible .tel-card-tag,
#integrations .stt-card:hover .stt-card-tag,
#integrations .stt-card:focus-visible .stt-card-tag,
#integrations .llm-card:hover .llm-card-tag,
#integrations .llm-card:focus-visible .llm-card-tag {
  background: #f0f4f8 !important;
  border-color: #cbd5e1 !important;
  color: #4A658B !important;
}
#integrations .int-card-hint,
#integrations .tel-card-cta,
#integrations .llm-card-cta,
#integrations .stt-card-cta {
  transition: color 0.2s ease !important;
}
@media (prefers-reduced-motion: reduce) {
  #integrations .int-card.reveal,
  #integrations .tel-card.reveal,
  #integrations .llm-card.reveal,
  #integrations .stt-card.reveal,
  #integrations .call-flow.reveal,
  #integrations .int-showcase.reveal {
    opacity: 1 !important;
    transform: none !important;
    transition: none !important;
  }
}

"""

MARKER = "/* ═══ INTEGRATIONS PREMIUM — HIW parity"
BRAND_MARKER = "/* ═══ EMAAVY BRAND PALETTE — white + secondary navy ═══ */"


def add_reveal_to_cards(html: str) -> str:
    """Add reveal class to integration partner cards and call-flow blocks."""
    start = html.find("<!-- INTEGRATIONS HUB -->")
    if start < 0:
        return html
    end = len(html)
    for needle in ["<section id=\"pricing\"", "<!-- PRICING", "<footer class=", "</main>"]:
        i = html.find(needle, start + 50)
        if i > start:
            end = min(end, i)
    chunk = html[start:end]
    m = re.search(r'id="integrations"[^>]*>.*?</section>', chunk, re.DOTALL)
    if not m:
        return html
    sec = m.group(0)
    sec = re.sub(r'<article class="int-card (?!reveal)', '<article class="int-card reveal', sec)
    sec = sec.replace("int-card reveal reveal", "int-card reveal")
    sec = sec.replace('<div class="call-flow" ', '<div class="call-flow reveal" ')
    return html[:start] + sec + html[start + len(m.group(0)) :]


def patch_llm_legacy_css(html: str) -> str:
    """Normalize LLM block purple accents to navy in existing rules."""
    block_start = html.find("/* ═══ LLM CARDS — reasoning layer layout ═══ */")
    block_end = html.find("/* ═══ STT CARDS — speech layer layout ═══ */")
    if block_start < 0 or block_end < 0:
        return html
    block = html[block_start:block_end]
    repl = {
        "#4338ca": "#4A658B",
        "#6366f1": "#4A658B",
        "#eef2ff": "#f0f4f8",
        "#e0e7ff": "#e2e8f0",
        "#c7d2fe": "#cbd5e1",
        "#fafaff": "#ffffff",
        "rgba(99, 102, 241, 0.12)": "rgba(15, 23, 42, 0.06)",
        "transform 0.2s ease, ": "",
        "transform: translateY(-2px) !important;\n  ": "",
    }
    for old, new in repl.items():
        block = block.replace(old, new)
    return html[:block_start] + block + html[block_end:]


def patch_stt_hover_css(html: str) -> str:
    block_start = html.find("/* ═══ STT CARDS — speech layer layout ═══ */")
    block_end = html.find("/* ═══ TELEPHONY CARDS — partner grid layout ═══ */")
    if block_start < 0 or block_end < 0:
        return html
    block = html[block_start:block_end]
    block = block.replace("rgba(37, 99, 235, 0.08)", "rgba(15, 23, 42, 0.06)")
    block = block.replace("#c5d4e4", "#cbd5e1")
    block = block.replace("transform 0.2s ease, ", "")
    block = re.sub(
        r"#integration-stt \.stt-card:hover,\s*\n#integration-stt \.stt-card:focus-visible \{[^}]+\}",
        """#integration-stt .stt-card:hover,
#integration-stt .stt-card:focus-visible {
  border-color: #cbd5e1 !important;
  box-shadow: 0 4px 16px rgba(15, 23, 42, 0.06) !important;
  outline: none !important;
}""",
        block,
        count=1,
    )
    block = re.sub(
        r"  #integration-stt \.stt-card:hover,\s*\n  #integration-stt \.stt-card:focus-visible \{\s*\n    transform: none !important;\s*\n  \}",
        "",
        block,
    )
    return html[:block_start] + block + html[block_end:]


def patch_tel_hover_css(html: str) -> str:
    block_start = html.find("/* ═══ TELEPHONY CARDS — partner grid layout ═══ */")
    block_end = html.find("/* ═══ ELEGANT CALL FLOW — lifecycle strips")
    if block_start < 0 or block_end < 0:
        return html
    block = html[block_start:block_end]
    block = block.replace("rgba(37, 99, 235, 0.08)", "rgba(15, 23, 42, 0.06)")
    block = block.replace("#c5d4e4", "#cbd5e1")
    return html[:block_start] + block + html[block_end:]


def main():
    html = PATH.read_text(encoding="utf-8")
    html = add_reveal_to_cards(html)
    html = patch_llm_legacy_css(html)
    html = patch_stt_hover_css(html)
    html = patch_tel_hover_css(html)
    if MARKER not in html:
        html = html.replace(BRAND_MARKER, PREMIUM_CSS + "\n" + BRAND_MARKER)
    else:
        # replace existing premium block
        i = html.find(MARKER)
        j = html.find(BRAND_MARKER, i)
        html = html[:i] + PREMIUM_CSS + "\n" + html[j:]
    PATH.write_text(html, encoding="utf-8")
    print("Patched:", PATH)


if __name__ == "__main__":
    main()
