"""Inject elegant signal-band CSS and clean Live Processing markup."""
import re
from pathlib import Path

SIGNAL_MARKER = "/* ═══ ELEGANT SIGNAL — refined, no glow ═══ */"

SIGNAL_OVERRIDE = """
/* ═══ ELEGANT SIGNAL — refined, no glow ═══ */
.signal-band {
  position: relative !important;
  overflow: visible !important;
  margin: 0 auto 4rem !important;
  max-width: 1200px !important;
  padding: 3rem clamp(1.25rem, 4vw, 2.5rem) 2.5rem !important;
  border-radius: 12px !important;
  border: 1px solid #e2e8f0 !important;
  background: #ffffff !important;
  box-shadow: none !important;
  isolation: auto !important;
}
.signal-band::before,
.signal-band-glow,
.signal-band-grid,
.signal-chip-glow {
  display: none !important;
}
.signal-band-head {
  text-align: center !important;
  max-width: 560px !important;
  margin: 0 auto 2rem !important;
}
.signal-live-badge {
  display: inline-flex !important;
  align-items: center !important;
  gap: 0.5rem !important;
  padding: 0.35rem 0.85rem !important;
  margin-bottom: 1rem !important;
  border-radius: 6px !important;
  background: #f8fafc !important;
  border: 1px solid #e2e8f0 !important;
  box-shadow: none !important;
  font-size: 0.68rem !important;
  font-weight: 500 !important;
  letter-spacing: 0.1em !important;
  text-transform: uppercase !important;
  color: #64748b !important;
  animation: none !important;
}
.signal-band .signal-dot {
  width: 6px !important;
  height: 6px !important;
  flex-shrink: 0 !important;
  background: #16a34a !important;
  box-shadow: none !important;
}
.signal-dot::after {
  display: none !important;
}
.signal-band-title {
  font-family: 'Clash Display', sans-serif !important;
  font-size: clamp(1.75rem, 3.5vw, 2.25rem) !important;
  font-weight: 600 !important;
  letter-spacing: -0.02em !important;
  color: #0f172a !important;
  margin-bottom: 0.5rem !important;
  text-shadow: none !important;
}
.signal-band-desc {
  font-size: 0.95rem !important;
  line-height: 1.65 !important;
  color: #64748b !important;
  max-width: 480px !important;
  margin: 0 auto !important;
}
.signal-chips {
  display: grid !important;
  grid-template-columns: repeat(4, 1fr) !important;
  gap: 0.75rem !important;
}
.signal-chip {
  position: relative !important;
  overflow: visible !important;
  display: flex !important;
  flex-direction: column !important;
  align-items: flex-start !important;
  padding: 1.25rem 1.1rem 1.1rem !important;
  border-radius: 8px !important;
  background: #ffffff !important;
  border: 1px solid #e2e8f0 !important;
  box-shadow: none !important;
  cursor: pointer !important;
  transition: border-color 0.2s ease, box-shadow 0.2s ease !important;
  isolation: auto !important;
}
.signal-chip::before {
  display: none !important;
}
.signal-chip:hover,
.signal-chip:focus-visible {
  border-color: #cbd5e1 !important;
  box-shadow: 0 4px 16px rgba(15, 23, 42, 0.06) !important;
  outline: none !important;
  transform: none !important;
}
.signal-chip-icon-wrap {
  position: relative !important;
  z-index: 1 !important;
  width: 40px !important;
  height: 40px !important;
  border-radius: 8px !important;
  display: flex !important;
  align-items: center !important;
  justify-content: center !important;
  margin-bottom: 0.85rem !important;
  background: #f8fafc !important;
  border: 1px solid #e2e8f0 !important;
  box-shadow: none !important;
  transition: border-color 0.2s ease !important;
}
.signal-chip-icon-wrap::before {
  font-family: 'Clash Display', sans-serif !important;
  font-weight: 700 !important;
  font-size: 0.68rem !important;
  color: #1e40af !important;
  letter-spacing: 0.02em !important;
}
.signal-chip[data-detail="snap-speed"] .signal-chip-icon-wrap::before { content: 'RT'; }
.signal-chip[data-detail="snap-lang"] .signal-chip-icon-wrap::before { content: 'LG'; }
.signal-chip[data-detail="snap-intent"] .signal-chip-icon-wrap::before { content: 'IN'; }
.signal-chip[data-detail="snap-api"] .signal-chip-icon-wrap::before { content: 'AP'; }
.signal-chip:hover .signal-chip-icon-wrap,
.signal-chip:focus-visible .signal-chip-icon-wrap {
  box-shadow: none !important;
  border-color: #cbd5e1 !important;
}
.signal-chip-metric {
  margin-bottom: 0.3rem !important;
}
.signal-chip-metric strong {
  font-family: 'Clash Display', sans-serif !important;
  font-size: 1.5rem !important;
  font-weight: 600 !important;
  color: #0f172a !important;
  letter-spacing: -0.02em !important;
  transition: color 0.2s ease !important;
}
.signal-chip:hover .signal-chip-metric strong,
.signal-chip:focus-visible .signal-chip-metric strong {
  color: #1e40af !important;
}
.signal-chip-label {
  font-size: 0.85rem !important;
  line-height: 1.5 !important;
  color: #64748b !important;
  margin: 0 0 0.75rem !important;
}
.signal-chip-tag {
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
.signal-chip:hover .signal-chip-tag,
.signal-chip:focus-visible .signal-chip-tag {
  background: #eff6ff !important;
  border-color: #cbd5e1 !important;
  color: #1e40af !important;
  box-shadow: none !important;
}
@media (max-width: 900px) {
  .signal-chips {
    grid-template-columns: 1fr 1fr !important;
  }
  .signal-band {
    padding: 2.5rem 1.25rem 2rem !important;
  }
}
@media (max-width: 520px) {
  .signal-chips {
    grid-template-columns: 1fr !important;
  }
  .signal-band {
    margin-inline: 0.75rem !important;
    border-radius: 10px !important;
  }
}
"""

DECOR_REMOVALS = [
    '<div class="signal-band-glow signal-band-glow-a" aria-hidden="true"></div> ',
    '<div class="signal-band-glow signal-band-glow-b" aria-hidden="true"></div> ',
    '<div class="signal-band-grid" aria-hidden="true"></div> ',
]
CHIP_GLOW_RE = re.compile(r'<div class="signal-chip-glow" aria-hidden="true"></div>\s*')


def main():
    html_path = Path(__file__).resolve().parents[1] / "emaavy_white_blue (2).html"
    text = html_path.read_text(encoding="utf-8")

    if SIGNAL_MARKER in text:
        start = text.index(SIGNAL_MARKER)
        end = text.index("</style>", start)
        text = text[:start] + SIGNAL_OVERRIDE.strip() + "\n" + text[end:]
        print("Updated existing signal override block")
    else:
        text = text.replace("</style>", SIGNAL_OVERRIDE + "\n</style>", 1)
        print("Injected signal override block")

    for chunk in DECOR_REMOVALS:
        if chunk in text:
            text = text.replace(chunk, "", 1)
            print("Removed:", chunk[:50])

    new_text, n = CHIP_GLOW_RE.subn("", text)
    if n:
        print(f"Removed {n} signal-chip-glow elements")
    text = new_text

    html_path.write_text(text, encoding="utf-8")
    print("Done:", html_path.name)


if __name__ == "__main__":
    main()
