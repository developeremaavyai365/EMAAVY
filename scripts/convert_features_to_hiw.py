#!/usr/bin/env python3
"""Convert Platform Capabilities (#features) to HIW card system; remove abbreviations."""
from pathlib import Path
import re

PATH = Path(__file__).resolve().parents[1] / "emaavy_white_blue (2).html"
HIW_HINT = "Tap for details →"

FEATURE_CARD_RE = re.compile(
    r'<article\b[^>]*class="[^"]*\bfeature-card\b[^"]*"[^>]*>.*?</article>',
    re.DOTALL | re.I,
)


def parse_feature_card(html: str) -> dict:
    detail = ""
    m = re.search(r'data-detail="([^"]*)"', html)
    if m:
        detail = m.group(1)

    title = ""
    m = re.search(r"<h3[^>]*>([^<]*)</h3>", html, re.I)
    if m:
        title = m.group(1).strip()

    desc = ""
    m = re.search(r"<p[^>]*>([^<]*)</p>", html, re.I)
    if m:
        desc = m.group(1).strip()

    tag = ""
    m = re.search(r'<span class="feature-tag"[^>]*>([^<]*)</span>', html, re.I)
    if m:
        tag = m.group(1).strip()

    hint = HIW_HINT
    m = re.search(r'<span class="feature-card-hint"[^>]*>([^<]*)</span>', html, re.I)
    if m:
        hint = m.group(1).strip()

    return {"detail": detail, "title": title, "desc": desc, "tag": tag, "hint": hint}


def build_hiw_step(data: dict, index: int) -> str:
    detail = data["detail"]
    title = data["title"] or "Capability"
    desc = data["desc"] or ""
    tag = data["tag"] or "Platform"
    hint = data["hint"] or HIW_HINT
    return (
        f'<article class="hiw-step reveal click-detail" data-detail="{detail}" tabindex="0">'
        f'<div class="hiw-step-num">{index}</div>'
        '<span class="hiw-step-icon" aria-hidden="true"></span>'
        f"<h4>{title}</h4>"
        f"<p>{desc}</p>"
        f'<span class="hiw-step-tag">{tag}</span>'
        f'<span class="hiw-step-hint">{hint}</span>'
        "</article>"
    )


FEATURES_CSS = r"""
/* ═══ FEATURES — HIW card system (Platform Capabilities) ═══ */
#features .features-grid,
#features .hiw-steps {
  position: relative !important;
  z-index: 1 !important;
  display: grid !important;
  grid-template-columns: repeat(3, 1fr) !important;
  gap: 0.75rem !important;
}
#features .hiw-steps::before {
  display: none !important;
}
#features .hiw-step {
  position: relative !important;
  z-index: 1 !important;
  display: flex !important;
  flex-direction: column !important;
  align-items: center !important;
  text-align: center !important;
  padding: 1.35rem 1.1rem 1.15rem !important;
  border-radius: 8px !important;
  background: #ffffff !important;
  border: 1px solid #e2e8f0 !important;
  box-shadow: none !important;
  cursor: pointer !important;
  overflow: visible !important;
  isolation: auto !important;
  transition: border-color 0.2s ease, box-shadow 0.2s ease, opacity 0.65s cubic-bezier(0.16, 1, 0.3, 1), transform 0.65s cubic-bezier(0.16, 1, 0.3, 1) !important;
}
#features .hiw-step::before {
  display: none !important;
}
#features .hiw-step:hover,
#features .hiw-step:focus-visible {
  border-color: #cbd5e1 !important;
  box-shadow: 0 4px 16px rgba(15, 23, 42, 0.06) !important;
  outline: none !important;
  transform: none !important;
}
#features .hiw-step-num {
  position: relative !important;
  z-index: 1 !important;
  width: 40px !important;
  height: 40px !important;
  border-radius: 8px !important;
  display: flex !important;
  align-items: center !important;
  justify-content: center !important;
  margin: 0 auto 0.85rem !important;
  font-family: 'Clash Display', sans-serif !important;
  font-weight: 600 !important;
  font-size: 1rem !important;
  color: #ffffff !important;
  background: #4A658B !important;
  border: none !important;
  box-shadow: none !important;
  transition: background 0.2s ease !important;
}
#features .hiw-step:hover .hiw-step-num,
#features .hiw-step:focus-visible .hiw-step-num {
  background: #18345D !important;
}
#features .hiw-step-icon {
  display: none !important;
}
#features .hiw-step h4 {
  position: relative !important;
  z-index: 1 !important;
  font-family: 'Clash Display', sans-serif !important;
  font-size: 1rem !important;
  font-weight: 600 !important;
  color: #0f172a !important;
  margin-bottom: 0.45rem !important;
  transition: color 0.2s ease !important;
}
#features .hiw-step:hover h4,
#features .hiw-step:focus-visible h4 {
  color: #4A658B !important;
}
#features .hiw-step p {
  position: relative !important;
  z-index: 1 !important;
  font-size: 0.85rem !important;
  color: #64748b !important;
  line-height: 1.6 !important;
  margin: 0 0 0.85rem !important;
}
#features .hiw-step-tag {
  position: relative !important;
  z-index: 1 !important;
  margin-top: auto !important;
  font-size: 0.6rem !important;
  font-weight: 600 !important;
  letter-spacing: 0.08em !important;
  text-transform: uppercase !important;
  color: #64748b !important;
  background: #f8fafc !important;
  border: 1px solid #e2e8f0 !important;
  border-radius: 4px !important;
  padding: 0.25rem 0.55rem !important;
  box-shadow: none !important;
  transition: background 0.2s ease, border-color 0.2s ease, color 0.2s ease !important;
}
#features .hiw-step:hover .hiw-step-tag,
#features .hiw-step:focus-visible .hiw-step-tag {
  background: #f0f4f8 !important;
  border-color: #cbd5e1 !important;
  color: #4A658B !important;
}
#features .hiw-step-hint {
  position: relative !important;
  z-index: 1 !important;
  margin-top: 0.55rem !important;
  font-size: 0.6rem !important;
  font-weight: 500 !important;
  letter-spacing: 0.06em !important;
  text-transform: uppercase !important;
  color: #94a3b8 !important;
  opacity: 1 !important;
  transition: color 0.2s ease !important;
}
#features .hiw-step:hover .hiw-step-hint,
#features .hiw-step:focus-visible .hiw-step-hint {
  color: #64748b !important;
}
#features .hiw-step.reveal {
  opacity: 0 !important;
  transform: translateY(24px) !important;
}
#features .hiw-step.reveal.in {
  opacity: 1 !important;
  transform: translateY(0) !important;
}
#features .hiw-steps .hiw-step.reveal:nth-child(1) { transition-delay: 0.04s !important; }
#features .hiw-steps .hiw-step.reveal:nth-child(2) { transition-delay: 0.09s !important; }
#features .hiw-steps .hiw-step.reveal:nth-child(3) { transition-delay: 0.14s !important; }
#features .hiw-steps .hiw-step.reveal:nth-child(4) { transition-delay: 0.19s !important; }
#features .hiw-steps .hiw-step.reveal:nth-child(5) { transition-delay: 0.24s !important; }
#features .hiw-steps .hiw-step.reveal:nth-child(6) { transition-delay: 0.29s !important; }
@media (max-width: 900px) {
  #features .features-grid,
  #features .hiw-steps {
    grid-template-columns: 1fr 1fr !important;
  }
}
@media (max-width: 560px) {
  #features .features-grid,
  #features .hiw-steps {
    grid-template-columns: 1fr !important;
  }
}
@media (prefers-reduced-motion: reduce) {
  #features .hiw-step.reveal {
    opacity: 1 !important;
    transform: none !important;
    transition: border-color 0.2s ease, box-shadow 0.2s ease !important;
  }
}

"""

CSS_MARKER = "/* ═══ FEATURES — HIW card system (Platform Capabilities) ═══ */"


def convert_features_html(html: str) -> str:
    m = re.search(r'<section id="features"[^>]*>.*?</section>', html, re.DOTALL)
    if not m:
        raise SystemExit("features section not found")
    sec = m.group(0)
    idx = 1

    def repl(match):
        nonlocal idx
        out = build_hiw_step(parse_feature_card(match.group(0)), idx)
        idx += 1
        return out

    sec = FEATURE_CARD_RE.sub(repl, sec)
    sec = sec.replace('class="features-grid"', 'class="hiw-steps"')
    return html[: m.start()] + sec + html[m.end() :]


def remove_abbrev_css(html: str) -> str:
    """Remove icon abbreviation content rules (RT, LG, BC, AP, etc.)."""
    patterns = [
        r"\.signal-chip\[data-detail[^\]]+\] \.signal-chip-icon-wrap::before \{ content: '[^']*'; \}\n?",
        r"\.feature-card\[data-detail[^\]]+\] \.feature-icon::before \{ content: '[^']*'; \}\n?",
        r"#features \.feature-icon::before \{[^}]+\}\n?",
    ]
    for pat in patterns:
        html = re.sub(pat, "", html)
    # Hide signal chip abbrev boxes — use metric text only
    if "#signal-snapshots .signal-chip-icon-wrap" not in html:
        html = html.replace(
            "/* ═══ FEATURES — HIW card system",
            """#signal-snapshots .signal-chip-icon-wrap,
.signal-band .signal-chip-icon-wrap {
  display: none !important;
}

/* ═══ FEATURES — HIW card system""",
            1,
        )
    return html


def inject_css(html: str) -> str:
    if CSS_MARKER in html:
        i = html.find(CSS_MARKER)
        j = html.find("/* ═══ ELEGANT TEMPLATE", i)
        if j < 0:
            j = html.find("/* ═══ INTEGRATIONS", i)
        html = html[:i] + FEATURES_CSS + "\n" + html[j:]
    else:
        html = html.replace(
            "/* ═══ ELEGANT TEMPLATE — refined shell, cards preserved ═══ */",
            FEATURES_CSS + "\n/* ═══ ELEGANT TEMPLATE — refined shell, cards preserved ═══ */",
        )
    return html


def simplify_features_block(html: str) -> str:
    """Point legacy feature-card rules at hiw-step; drop abbrev icon rules."""
    html = re.sub(
        r"\.feature-card\[data-detail[^\]]+\] \.feature-icon::before \{ content: '[^']*'; \}\n",
        "",
        html,
    )
    # Replace features-grid/feature-card block with minimal legacy aliases
    old_start = "/* ═══ ELEGANT FEATURES — refined, no glow ═══ */"
    old_end = "/* ═══ ELEGANT TEMPLATE — refined shell, cards preserved ═══ */"
    if old_start not in html:
        return html
    i = html.find(old_start)
    j = html.find(old_end, i)
    shell = r"""/* ═══ ELEGANT FEATURES — refined shell (HIW cards below) ═══ */
#features {
  position: relative !important;
  overflow: visible !important;
  width: min(1200px, calc(100% - 2rem)) !important;
  margin: 0 auto 4rem !important;
  padding: 3rem clamp(1.25rem, 4vw, 2.5rem) 2.5rem !important;
  border-radius: 12px !important;
  border: 1px solid #e2e8f0 !important;
  background: #ffffff !important;
  box-shadow: none !important;
  isolation: auto !important;
  scroll-margin-top: 100px !important;
}
#features::before,
.features-glow,
.features-grid-bg,
.feature-card-glow {
  display: none !important;
}
.features-head {
  position: relative !important;
  z-index: 1 !important;
  text-align: center !important;
  margin-bottom: 2.5rem !important;
}
#features .section-kicker,
.features-head .section-kicker {
  display: inline-flex !important;
  align-items: center !important;
  gap: 0.5rem !important;
  font-size: 0.68rem !important;
  font-weight: 500 !important;
  letter-spacing: 0.1em !important;
  text-transform: uppercase !important;
  color: #64748b !important;
  background: #f8fafc !important;
  border: 1px solid #e2e8f0 !important;
  border-radius: 6px !important;
  padding: 0.35rem 0.85rem !important;
  margin-bottom: 0.85rem !important;
  box-shadow: none !important;
}
#features .section-kicker::before,
.features-head .section-kicker::before {
  display: none !important;
}
.features-head h2 {
  font-family: 'Clash Display', sans-serif !important;
  font-size: clamp(1.75rem, 3.5vw, 2.25rem) !important;
  font-weight: 600 !important;
  letter-spacing: -0.02em !important;
  color: #0f172a !important;
  margin-bottom: 0.5rem !important;
  text-shadow: none !important;
}
.features-head p {
  color: #64748b !important;
  max-width: 540px !important;
  margin: 0 auto !important;
  line-height: 1.65 !important;
  font-size: 0.95rem !important;
}
@media (max-width: 900px) {
  #features {
    width: calc(100% - 2rem) !important;
    padding: 2.5rem 1.25rem 2rem !important;
  }
}
@media (max-width: 560px) {
  #features {
    border-radius: 10px !important;
  }
}

"""
    return html[:i] + shell + html[j:]


def main():
    html = PATH.read_text(encoding="utf-8")
    html = convert_features_html(html)
    html = simplify_features_block(html)
    html = inject_css(html)
    html = remove_abbrev_css(html)
    # signal chip abbreviations in signal band section
    html = re.sub(
        r"\.signal-chip\[data-detail=\"snap-speed\"\] \.signal-chip-icon-wrap::before \{ content: 'RT'; \}\n?",
        "",
        html,
    )
    html = re.sub(
        r"\.signal-chip\[data-detail=\"snap-lang\"\] \.signal-chip-icon-wrap::before \{ content: 'LG'; \}\n?",
        "",
        html,
    )
    html = re.sub(
        r"\.signal-chip\[data-detail=\"snap-intent\"\] \.signal-chip-icon-wrap::before \{ content: 'IN'; \}\n?",
        "",
        html,
    )
    html = re.sub(
        r"\.signal-chip\[data-detail=\"snap-api\"\] \.signal-chip-icon-wrap::before \{ content: 'AP'; \}\n?",
        "",
        html,
    )
    # generic cleanup any remaining ::before content 2-letter
    html = re.sub(
        r"\.signal-chip-icon-wrap::before \{ content: '[A-Z]{2}'; \}\n?",
        "",
        html,
    )
    PATH.write_text(html, encoding="utf-8")
    n = html.count('id="features"')
    c = len(re.findall(r'<article class="hiw-step reveal click-detail" data-detail="feat-', html))
    print(f"features sections: {n}, hiw feat cards: {c}")


if __name__ == "__main__":
    main()
