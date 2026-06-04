"""Elegant integrations hub — clean shells, professional cards, no glow."""
import re
from pathlib import Path

HTML = Path(__file__).resolve().parents[1] / "emaavy_white_blue (2).html"
MARKER = "/* ═══ ELEGANT INTEGRATIONS — refined hub ═══ */"

INTEGRATIONS_CSS = """
/* ═══ ELEGANT INTEGRATIONS — refined hub ═══ */
#integrations {
  scroll-margin-top: 100px !important;
  padding: 0 0 4rem !important;
}
#integrations .int-hub-head {
  text-align: center !important;
  max-width: 680px !important;
  margin: 0 auto 2.5rem !important;
  padding: 0 1rem !important;
}
#integrations .int-hub-head .section-kicker {
  display: inline-flex !important;
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
#integrations .int-hub-head .section-kicker::before {
  display: none !important;
}
#integrations .int-hub-head h2 {
  font-family: 'Clash Display', sans-serif !important;
  font-size: clamp(1.75rem, 3.5vw, 2.25rem) !important;
  font-weight: 600 !important;
  letter-spacing: -0.02em !important;
  color: #0f172a !important;
  text-shadow: none !important;
}
#integrations .int-hub-head p {
  color: #64748b !important;
  font-size: 0.95rem !important;
  line-height: 1.65 !important;
  max-width: 560px !important;
  margin: 0.5rem auto 0 !important;
}
#integrations .telephony-showcase,
#integrations .int-showcase {
  margin-bottom: 2rem !important;
  scroll-margin-top: 100px !important;
}
#integrations .telephony-shell,
#integrations .int-shell {
  position: relative !important;
  width: min(1200px, calc(100% - 2rem)) !important;
  margin: 0 auto 2rem !important;
  padding: 2.5rem clamp(1.25rem, 4vw, 2rem) 2rem !important;
  border-radius: 12px !important;
  border: 1px solid #e2e8f0 !important;
  background: #ffffff !important;
  box-shadow: none !important;
  overflow: visible !important;
  isolation: auto !important;
}
#integrations .telephony-shell::before,
#integrations .int-shell::before,
#integrations .telephony-glow,
#integrations .telephony-scanline,
#integrations .telephony-visual-glow,
#integrations .telephony-vobiz-orb,
#integrations .telephony-hero-glow,
#integrations .telephony-hero-ring,
#integrations .telephony-hero-spark,
#integrations .telephony-hero-scanline,
#integrations .telephony-feature-glow,
#integrations .telephony-node-glow,
#integrations .int-glow,
#integrations .int-scanline,
#integrations .int-visual-panel-glow,
#integrations .int-card-glow,
#integrations .int-card-scanline,
#integrations .int-card-spark {
  display: none !important;
}
#integrations .telephony-head,
#integrations .int-head {
  text-align: center !important;
  max-width: 720px !important;
  margin: 0 auto 1.75rem !important;
}
#integrations .telephony-head .section-kicker,
#integrations .int-head .section-kicker {
  display: inline-flex !important;
  font-size: 0.65rem !important;
  font-weight: 500 !important;
  letter-spacing: 0.08em !important;
  text-transform: uppercase !important;
  color: #64748b !important;
  background: #f8fafc !important;
  border: 1px solid #e2e8f0 !important;
  border-radius: 6px !important;
  padding: 0.35rem 0.75rem !important;
  box-shadow: none !important;
}
#integrations .telephony-head h3,
#integrations .int-head h3 {
  font-family: 'Clash Display', sans-serif !important;
  font-size: clamp(1.35rem, 3vw, 1.85rem) !important;
  font-weight: 600 !important;
  letter-spacing: -0.02em !important;
  color: #0f172a !important;
  margin-top: 0.75rem !important;
  line-height: 1.15 !important;
}
#integrations .telephony-head p,
#integrations .int-head p {
  color: #64748b !important;
  font-size: 0.92rem !important;
  line-height: 1.65 !important;
  margin-top: 0.5rem !important;
}
#integrations .telephony-stat-row,
#integrations .int-stat-row {
  display: flex !important;
  flex-wrap: wrap !important;
  justify-content: center !important;
  gap: 0.5rem !important;
  margin-bottom: 1.5rem !important;
}
#integrations .telephony-stat,
#integrations .int-stat {
  padding: 0.5rem 0.9rem !important;
  border-radius: 6px !important;
  background: #f8fafc !important;
  border: 1px solid #e2e8f0 !important;
  box-shadow: none !important;
  backdrop-filter: none !important;
  font-size: 0.75rem !important;
  color: #64748b !important;
  gap: 0.4rem !important;
}
#integrations .telephony-stat b,
#integrations .int-stat b {
  font-family: 'Clash Display', sans-serif !important;
  font-size: 0.95rem !important;
  font-weight: 600 !important;
  color: #1e40af !important;
}
#integrations .telephony-stat-dot,
#integrations .int-stat-dot {
  width: 6px !important;
  height: 6px !important;
  background: #16a34a !important;
  box-shadow: none !important;
  animation: none !important;
}
#integrations .telephony-visual,
#integrations .int-visual-panel,
#integrations .int-fx,
#integrations .telephony-signal-pulse,
#integrations .telephony-signal-track,
#integrations .telephony-stage {
  display: none !important;
}
#integrations .telephony-vobiz-zone {
  display: grid !important;
  grid-template-columns: 1fr 1fr !important;
  gap: 1rem !important;
  align-items: start !important;
}
#integrations .telephony-hero {
  position: relative !important;
  padding: 1.35rem 1.2rem !important;
  border-radius: 10px !important;
  border: 1px solid #e2e8f0 !important;
  background: #ffffff !important;
  box-shadow: none !important;
  overflow: visible !important;
}
#integrations .telephony-hero:hover,
#integrations .telephony-hero:focus-visible {
  border-color: #cbd5e1 !important;
  box-shadow: 0 4px 16px rgba(15, 23, 42, 0.06) !important;
  outline: none !important;
}
#integrations .telephony-hero-logo {
  width: 48px !important;
  height: 48px !important;
  border-radius: 8px !important;
  background: #f8fafc !important;
  border: 1px solid #e2e8f0 !important;
  box-shadow: none !important;
  font-size: 0 !important;
}
#integrations .telephony-hero-logo::before,
#integrations .telephony-hero-logo::after {
  display: none !important;
}
#integrations .telephony-hero-logo .brand-mark {
  font-family: 'Clash Display', sans-serif !important;
  font-size: 0.75rem !important;
  font-weight: 700 !important;
  color: #1e40af !important;
}
#integrations .telephony-hero-badge {
  font-size: 0.58rem !important;
  font-weight: 600 !important;
  letter-spacing: 0.08em !important;
  text-transform: uppercase !important;
  color: #64748b !important;
  background: #f8fafc !important;
  border: 1px solid #e2e8f0 !important;
  border-radius: 4px !important;
  padding: 0.2rem 0.5rem !important;
}
#integrations .telephony-hero h4 {
  font-family: 'Clash Display', sans-serif !important;
  font-size: 1.05rem !important;
  font-weight: 600 !important;
  color: #0f172a !important;
}
#integrations .telephony-hero p {
  color: #64748b !important;
  font-size: 0.85rem !important;
  line-height: 1.6 !important;
}
#integrations .telephony-hero-metrics {
  display: grid !important;
  grid-template-columns: 1fr 1fr !important;
  gap: 0.5rem !important;
}
#integrations .telephony-hero-metric {
  padding: 0.65rem !important;
  border-radius: 8px !important;
  background: #f8fafc !important;
  border: 1px solid #e2e8f0 !important;
  text-align: center !important;
}
#integrations .telephony-hero-metric b {
  color: #1e40af !important;
  font-size: 1.1rem !important;
}
#integrations .telephony-hero-hint {
  font-size: 0.6rem !important;
  font-weight: 500 !important;
  color: #94a3b8 !important;
  opacity: 1 !important;
}
#integrations .telephony-features {
  display: grid !important;
  grid-template-columns: 1fr 1fr !important;
  gap: 0.65rem !important;
}
#integrations .telephony-feature {
  padding: 0.85rem !important;
  border-radius: 8px !important;
  border: 1px solid #e2e8f0 !important;
  background: #ffffff !important;
  box-shadow: none !important;
  overflow: visible !important;
}
#integrations .telephony-feature:hover {
  border-color: #cbd5e1 !important;
  box-shadow: none !important;
}
#integrations .telephony-feature-icon {
  display: none !important;
}
#integrations .telephony-feature b {
  font-size: 0.82rem !important;
  color: #0f172a !important;
}
#integrations .telephony-feature span {
  font-size: 0.72rem !important;
  color: #64748b !important;
}
#integrations .telephony-cap-strip,
#integrations .int-cap-strip {
  margin-top: 1.5rem !important;
  padding-top: 1.25rem !important;
  border-top: 1px solid #e2e8f0 !important;
}
#integrations .telephony-cap-label,
#integrations .int-cap-label {
  font-size: 0.6rem !important;
  font-weight: 600 !important;
  letter-spacing: 0.08em !important;
  color: #94a3b8 !important;
  margin-bottom: 0.65rem !important;
}
#integrations .telephony-cap-row,
#integrations .int-cap-row {
  gap: 0.4rem !important;
}
#integrations .telephony-cap,
#integrations .int-cap {
  padding: 0.35rem 0.65rem !important;
  border-radius: 6px !important;
  font-size: 0.7rem !important;
  font-weight: 500 !important;
  color: #475569 !important;
  background: #f8fafc !important;
  border: 1px solid #e2e8f0 !important;
  box-shadow: none !important;
}
#integrations .telephony-cap:hover,
#integrations .int-cap:hover {
  border-color: #cbd5e1 !important;
  color: #0f172a !important;
  box-shadow: none !important;
}
#integrations .int-cards-grid {
  display: grid !important;
  grid-template-columns: repeat(auto-fill, minmax(200px, 1fr)) !important;
  gap: 0.75rem !important;
}
#integrations .int-shell--tts .int-cards-grid {
  grid-template-columns: repeat(auto-fill, minmax(200px, 1fr)) !important;
  max-width: none !important;
}
#integrations .int-card {
  padding: 1.15rem !important;
  border-radius: 10px !important;
  border: 1px solid #e2e8f0 !important;
  background: #ffffff !important;
  box-shadow: none !important;
  overflow: visible !important;
  transition: border-color 0.2s ease, box-shadow 0.2s ease !important;
}
#integrations .int-card::before {
  display: none !important;
}
#integrations .int-card:hover,
#integrations .int-card:focus-visible {
  border-color: #cbd5e1 !important;
  box-shadow: 0 4px 16px rgba(15, 23, 42, 0.06) !important;
  outline: none !important;
}
#integrations .int-card-logo {
  width: 44px !important;
  height: 44px !important;
  border-radius: 8px !important;
  background: #f8fafc !important;
  border: 1px solid #e2e8f0 !important;
  box-shadow: none !important;
}
#integrations .int-card-logo img {
  max-height: 24px !important;
}
#integrations .int-card-logo .brand-mark {
  font-size: 0.68rem !important;
  font-weight: 700 !important;
  color: #1e40af !important;
}
#integrations .int-card h4 {
  font-size: 0.92rem !important;
  font-weight: 600 !important;
  color: #0f172a !important;
}
#integrations .int-card:hover h4,
#integrations .int-card:focus-visible h4 {
  color: #1e40af !important;
}
#integrations .int-card p {
  font-size: 0.8rem !important;
  color: #64748b !important;
  line-height: 1.55 !important;
}
#integrations .int-card-hint {
  font-size: 0.58rem !important;
  font-weight: 500 !important;
  color: #94a3b8 !important;
  opacity: 1 !important;
}
#integrations .int-card:hover .int-card-hint,
#integrations .int-card:focus-visible .int-card-hint {
  color: #64748b !important;
}
#integrations .int-card-metric {
  font-size: 0.72rem !important;
  color: #64748b !important;
  background: #f8fafc !important;
  border: 1px solid #e2e8f0 !important;
  border-radius: 6px !important;
  padding: 0.35rem 0.55rem !important;
}
@media (max-width: 900px) {
  #integrations .telephony-vobiz-zone {
    grid-template-columns: 1fr !important;
  }
  #integrations .telephony-features {
    grid-template-columns: 1fr !important;
  }
}
@media (max-width: 640px) {
  #integrations .telephony-shell,
  #integrations .int-shell {
    width: calc(100% - 1.5rem) !important;
    padding: 2rem 1rem 1.5rem !important;
    border-radius: 10px !important;
  }
  #integrations .int-cards-grid {
    grid-template-columns: 1fr !important;
  }
}
"""

# HTML decor removals (exact strings)
SINGLE_REMOVALS = [
    '<div class="telephony-glow telephony-glow-a" aria-hidden="true"></div> ',
    '<div class="telephony-glow telephony-glow-b" aria-hidden="true"></div> ',
    '<div class="telephony-glow telephony-glow-c" aria-hidden="true"></div> ',
    '<div class="telephony-scanline" aria-hidden="true"></div> ',
    '<div class="telephony-visual-glow" aria-hidden="true"></div> ',
    '<div class="telephony-vobiz-orb telephony-vobiz-orb-a" aria-hidden="true"></div> ',
    '<div class="telephony-vobiz-orb telephony-vobiz-orb-b" aria-hidden="true"></div> ',
    '<div class="telephony-vobiz-orb telephony-vobiz-orb-c" aria-hidden="true"></div> ',
    '<div class="telephony-hero-ring" aria-hidden="true"></div> ',
    '<div class="telephony-hero-scanline" aria-hidden="true"></div> ',
    '<span class="telephony-hero-spark telephony-hero-spark-a" aria-hidden="true"></span> ',
    '<span class="telephony-hero-spark telephony-hero-spark-b" aria-hidden="true"></span> ',
    '<span class="telephony-hero-spark telephony-hero-spark-c" aria-hidden="true"></span> ',
    '<div class="telephony-hero-glow telephony-hero-glow-a" aria-hidden="true"></div> ',
    '<div class="telephony-hero-glow telephony-hero-glow-b" aria-hidden="true"></div> ',
    '<div class="telephony-hero-glow telephony-hero-glow-c" aria-hidden="true"></div> ',
    '<div class="int-glow int-glow-a" aria-hidden="true"></div> ',
    '<div class="int-glow int-glow-b" aria-hidden="true"></div> ',
    '<div class="int-glow int-glow-c" aria-hidden="true"></div> ',
    '<div class="int-scanline" aria-hidden="true"></div> ',
    '<div class="int-visual-panel-glow" aria-hidden="true"></div> ',
]

REGEX_REMOVALS = [
    (r'<div class="telephony-feature-glow" aria-hidden="true"></div>\s*', ""),
    (r'<div class="telephony-node-glow" aria-hidden="true"></div>\s*', ""),
    (r'<div class="int-card-glow" aria-hidden="true"></div>', ""),
    (r'<div class="int-card-scanline" aria-hidden="true"></div>', ""),
    (r'<span class="int-card-spark int-card-spark-a" aria-hidden="true"></span>', ""),
    (r'<span class="int-card-spark int-card-spark-b" aria-hidden="true"></span>', ""),
    (r'<span class="telephony-signal-pulse"></span>', ""),
]


def main():
    text = HTML.read_text(encoding="utf-8")

    if MARKER in text:
        start = text.index(MARKER)
        end = text.index("</style>", start)
        text = text[:start] + INTEGRATIONS_CSS.strip() + "\n" + text[end:]
        print("Updated integrations CSS block")
    else:
        text = text.replace("</style>", INTEGRATIONS_CSS + "\n</style>", 1)
        print("Injected integrations CSS block")

    for chunk in SINGLE_REMOVALS:
        count = text.count(chunk)
        if count:
            text = text.replace(chunk, "")
            print(f"Removed {count}x {chunk[:40]}...")

    for pattern, repl in REGEX_REMOVALS:
        text, n = re.subn(pattern, repl, text)
        if n:
            print(f"Regex removed {n} from {pattern[:30]}")

    # Remove inline style on int-hub p
    text = text.replace(
        '<p style="color:#475569;max-width:560px;margin:0.75rem auto 0;line-height:1.7;">',
        '<p class="int-hub-desc">',
        1,
    )

    HTML.write_text(text, encoding="utf-8")
    print("Done")


if __name__ == "__main__":
    main()
