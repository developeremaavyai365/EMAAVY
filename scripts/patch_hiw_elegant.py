"""Inject elegant How It Works (EMAAVY Method) CSS and clean markup."""
import re
from pathlib import Path

HIW_MARKER = "/* ═══ ELEGANT HIW — refined, no glow ═══ */"

HIW_OVERRIDE = """
/* ═══ ELEGANT HIW — refined, no glow ═══ */
#how-it-works {
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
#how-it-works::before,
.hiw-glow,
.hiw-step-glow {
  display: none !important;
}
.hiw-head {
  position: relative !important;
  z-index: 1 !important;
  text-align: center !important;
  margin-bottom: 2.5rem !important;
}
#how-it-works .section-kicker,
.hiw-head .section-kicker {
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
#how-it-works .section-kicker::before,
.hiw-head .section-kicker::before {
  display: none !important;
}
.hiw-head h2 {
  font-family: 'Clash Display', sans-serif !important;
  font-size: clamp(1.75rem, 3.5vw, 2.25rem) !important;
  font-weight: 600 !important;
  letter-spacing: -0.02em !important;
  color: #0f172a !important;
  margin-bottom: 0.5rem !important;
  text-shadow: none !important;
}
.hiw-head p {
  color: #64748b !important;
  max-width: 520px !important;
  margin: 0 auto !important;
  line-height: 1.65 !important;
  font-size: 0.95rem !important;
}
.hiw-steps {
  position: relative !important;
  z-index: 1 !important;
  display: grid !important;
  grid-template-columns: repeat(4, 1fr) !important;
  gap: 0.75rem !important;
}
.hiw-steps::before {
  content: '' !important;
  position: absolute !important;
  top: 2rem !important;
  left: 8% !important;
  right: 8% !important;
  height: 1px !important;
  background: #e2e8f0 !important;
  box-shadow: none !important;
  pointer-events: none !important;
  z-index: 0 !important;
}
.hiw-step {
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
  transition: border-color 0.2s ease, box-shadow 0.2s ease !important;
}
.hiw-step::before {
  display: none !important;
}
.hiw-step:hover,
.hiw-step:focus-visible {
  border-color: #cbd5e1 !important;
  box-shadow: 0 4px 16px rgba(15, 23, 42, 0.06) !important;
  outline: none !important;
  transform: none !important;
}
.hiw-step-num {
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
  background: #1e40af !important;
  border: none !important;
  box-shadow: none !important;
  transition: background 0.2s ease !important;
}
.hiw-step:hover .hiw-step-num,
.hiw-step:focus-visible .hiw-step-num {
  background: #1e3a8a !important;
  box-shadow: none !important;
}
#how-it-works .hiw-step-icon {
  display: none !important;
}
.hiw-step h4 {
  position: relative !important;
  z-index: 1 !important;
  font-family: 'Clash Display', sans-serif !important;
  font-size: 1rem !important;
  font-weight: 600 !important;
  color: #0f172a !important;
  margin-bottom: 0.45rem !important;
  transition: color 0.2s ease !important;
}
.hiw-step:hover h4,
.hiw-step:focus-visible h4 {
  color: #1e40af !important;
}
.hiw-step p {
  position: relative !important;
  z-index: 1 !important;
  font-size: 0.85rem !important;
  color: #64748b !important;
  line-height: 1.6 !important;
  margin: 0 0 0.85rem !important;
}
.hiw-step-tag {
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
.hiw-step:hover .hiw-step-tag,
.hiw-step:focus-visible .hiw-step-tag {
  background: #eff6ff !important;
  border-color: #cbd5e1 !important;
  color: #1e40af !important;
  box-shadow: none !important;
}
.hiw-step-hint {
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
.hiw-step:hover .hiw-step-hint,
.hiw-step:focus-visible .hiw-step-hint {
  color: #64748b !important;
}
@media (max-width: 900px) {
  .hiw-steps {
    grid-template-columns: 1fr 1fr !important;
  }
  .hiw-steps::before {
    display: none !important;
  }
  #how-it-works {
    margin-inline: 1rem !important;
    padding: 2.5rem 1.25rem 2rem !important;
  }
}
@media (max-width: 520px) {
  .hiw-steps {
    grid-template-columns: 1fr !important;
  }
  #how-it-works {
    border-radius: 10px !important;
  }
}
"""

DECOR_REMOVALS = [
    '<div class="hiw-glow hiw-glow-a" aria-hidden="true"></div> ',
    '<div class="hiw-glow hiw-glow-b" aria-hidden="true"></div> ',
]
STEP_GLOW_RE = re.compile(r'<div class="hiw-step-glow" aria-hidden="true"></div>\s*')


def main():
    html_path = Path(__file__).resolve().parents[1] / "emaavy_white_blue (2).html"
    text = html_path.read_text(encoding="utf-8")

    if HIW_MARKER in text:
        start = text.index(HIW_MARKER)
        end = text.index("</style>", start)
        text = text[:start] + HIW_OVERRIDE.strip() + "\n" + text[end:]
        print("Updated existing HIW override block")
    else:
        text = text.replace("</style>", HIW_OVERRIDE + "\n</style>", 1)
        print("Injected HIW override block")

    for chunk in DECOR_REMOVALS:
        if chunk in text:
            text = text.replace(chunk, "", 1)
            print("Removed:", chunk[:45])

    new_text, n = STEP_GLOW_RE.subn("", text)
    if n:
        print(f"Removed {n} hiw-step-glow elements")
    text = new_text

    html_path.write_text(text, encoding="utf-8")
    print("Done:", html_path.name)


if __name__ == "__main__":
    main()
