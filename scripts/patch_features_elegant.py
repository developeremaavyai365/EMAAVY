"""Inject elegant Platform Capabilities (Features) CSS and clean markup."""
import re
from pathlib import Path

FEAT_MARKER = "/* ═══ ELEGANT FEATURES — refined, no glow ═══ */"

FEAT_OVERRIDE = """
/* ═══ ELEGANT FEATURES — refined, no glow ═══ */
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
.features-grid {
  position: relative !important;
  z-index: 1 !important;
  display: grid !important;
  grid-template-columns: repeat(3, 1fr) !important;
  gap: 0.75rem !important;
}
.feature-card {
  position: relative !important;
  display: flex !important;
  flex-direction: column !important;
  align-items: flex-start !important;
  padding: 1.35rem 1.2rem 1.15rem !important;
  border-radius: 8px !important;
  background: #ffffff !important;
  border: 1px solid #e2e8f0 !important;
  box-shadow: none !important;
  cursor: pointer !important;
  overflow: visible !important;
  isolation: auto !important;
  transition: border-color 0.2s ease, box-shadow 0.2s ease !important;
}
.feature-card::after {
  display: none !important;
}
.feature-card:hover,
.feature-card:focus-visible {
  border-color: #cbd5e1 !important;
  box-shadow: 0 4px 16px rgba(15, 23, 42, 0.06) !important;
  outline: none !important;
  transform: none !important;
}
#features .feature-icon {
  position: relative !important;
  z-index: 1 !important;
  width: 40px !important;
  height: 40px !important;
  border-radius: 8px !important;
  display: flex !important;
  align-items: center !important;
  justify-content: center !important;
  margin-bottom: 0.85rem !important;
  font-size: 0 !important;
  background: #f8fafc !important;
  border: 1px solid #e2e8f0 !important;
  box-shadow: none !important;
  transition: border-color 0.2s ease !important;
}
#features .feature-icon::before {
  font-family: 'Clash Display', sans-serif !important;
  font-weight: 700 !important;
  font-size: 0.68rem !important;
  color: #1e40af !important;
  letter-spacing: 0.02em !important;
}
.feature-card[data-detail="feat-bulk"] .feature-icon::before { content: 'BC'; }
.feature-card[data-detail="feat-api"] .feature-icon::before { content: 'AP'; }
.feature-card[data-detail="feat-stt"] .feature-icon::before { content: 'ST'; }
.feature-card[data-detail="feat-agents"] .feature-icon::before { content: 'AG'; }
.feature-card[data-detail="feat-intel"] .feature-icon::before { content: 'CI'; }
.feature-card[data-detail="feat-security"] .feature-icon::before { content: 'SC'; }
.feature-card:hover .feature-icon,
.feature-card:focus-visible .feature-icon {
  box-shadow: none !important;
  border-color: #cbd5e1 !important;
}
.feature-card h3 {
  position: relative !important;
  z-index: 1 !important;
  font-family: 'Clash Display', sans-serif !important;
  font-size: 1rem !important;
  font-weight: 600 !important;
  color: #0f172a !important;
  margin-bottom: 0.45rem !important;
  transition: color 0.2s ease !important;
}
.feature-card:hover h3,
.feature-card:focus-visible h3 {
  color: #1e40af !important;
}
.feature-card p {
  position: relative !important;
  z-index: 1 !important;
  flex: 1 !important;
  margin: 0 !important;
  font-size: 0.85rem !important;
  color: #64748b !important;
  line-height: 1.6 !important;
}
.feature-tag {
  position: relative !important;
  z-index: 1 !important;
  display: inline-block !important;
  margin-top: 0.85rem !important;
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
.feature-card:hover .feature-tag,
.feature-card:focus-visible .feature-tag {
  background: #eff6ff !important;
  border-color: #cbd5e1 !important;
  color: #1e40af !important;
  box-shadow: none !important;
}
.feature-card-hint {
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
.feature-card:hover .feature-card-hint,
.feature-card:focus-visible .feature-card-hint {
  color: #64748b !important;
}
@media (max-width: 900px) {
  .features-grid {
    grid-template-columns: 1fr 1fr !important;
  }
  #features {
    width: calc(100% - 2rem) !important;
    padding: 2.5rem 1.25rem 2rem !important;
  }
}
@media (max-width: 560px) {
  .features-grid {
    grid-template-columns: 1fr !important;
  }
  #features {
    border-radius: 10px !important;
  }
}
"""

DECOR_REMOVALS = [
    '<div class="features-glow features-glow-a" aria-hidden="true"></div> ',
    '<div class="features-glow features-glow-b" aria-hidden="true"></div> ',
    '<div class="features-grid-bg" aria-hidden="true"></div> ',
]
CARD_GLOW_RE = re.compile(r'<div class="feature-card-glow" aria-hidden="true"></div>\s*')


def main():
    html_path = Path(__file__).resolve().parents[1] / "emaavy_white_blue (2).html"
    text = html_path.read_text(encoding="utf-8")

    if FEAT_MARKER in text:
        start = text.index(FEAT_MARKER)
        end = text.index("</style>", start)
        text = text[:start] + FEAT_OVERRIDE.strip() + "\n" + text[end:]
        print("Updated existing features override block")
    else:
        text = text.replace("</style>", FEAT_OVERRIDE + "\n</style>", 1)
        print("Injected features override block")

    for chunk in DECOR_REMOVALS:
        if chunk in text:
            text = text.replace(chunk, "", 1)
            print("Removed:", chunk[:48])

    new_text, n = CARD_GLOW_RE.subn("", text)
    if n:
        print(f"Removed {n} feature-card-glow elements")
    text = new_text

    html_path.write_text(text, encoding="utf-8")
    print("Done:", html_path.name)


if __name__ == "__main__":
    main()
