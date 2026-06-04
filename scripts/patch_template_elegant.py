"""Elegant video template section — clean shell; preserve template cards."""
import re
from pathlib import Path

TEMPLATE_MARKER = "/* ═══ ELEGANT TEMPLATE — refined shell, cards preserved ═══ */"

TEMPLATE_OVERRIDE = """
/* ═══ ELEGANT TEMPLATE — refined shell, cards preserved ═══ */
.template-lab {
  padding: 4rem 0 5rem !important;
  scroll-margin-top: 100px !important;
}
.template-shell {
  position: relative !important;
  width: min(1200px, calc(100% - 2rem)) !important;
  margin: 0 auto !important;
  padding: 3rem clamp(1.25rem, 4vw, 2.5rem) 2.5rem !important;
  border-radius: 12px !important;
  border: 1px solid #e2e8f0 !important;
  background: #ffffff !important;
  box-shadow: none !important;
  isolation: auto !important;
  overflow: visible !important;
}
.template-shell::before,
.template-glow,
.template-orbit-ring,
.template-spark,
.template-card-glow,
.template-card-scanline,
.template-card-ring {
  display: none !important;
}
.template-head {
  position: relative !important;
  z-index: 2 !important;
  text-align: center !important;
  max-width: 760px !important;
  margin: 0 auto 2rem !important;
}
.template-head .section-kicker {
  display: inline-flex !important;
  align-items: center !important;
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
.template-head .section-kicker::before {
  display: none !important;
}
.template-head h2 {
  font-family: 'Clash Display', sans-serif !important;
  font-size: clamp(1.75rem, 3.5vw, 2.25rem) !important;
  font-weight: 600 !important;
  letter-spacing: -0.02em !important;
  line-height: 1.12 !important;
  color: #0f172a !important;
  margin-bottom: 0.5rem !important;
  text-shadow: none !important;
}
.template-head p {
  color: #64748b !important;
  max-width: 580px !important;
  margin: 0 auto !important;
  line-height: 1.65 !important;
  font-size: 0.95rem !important;
}
.template-filters {
  display: flex !important;
  gap: 0.5rem !important;
  flex-wrap: wrap !important;
  justify-content: center !important;
  margin-top: 1.25rem !important;
}
.template-filter {
  border: 1px solid #e2e8f0 !important;
  background: #fff !important;
  color: #475569 !important;
  font-size: 0.72rem !important;
  letter-spacing: 0.06em !important;
  text-transform: uppercase !important;
  padding: 0.45rem 0.85rem !important;
  border-radius: 6px !important;
  cursor: pointer !important;
  font-family: inherit !important;
  font-weight: 600 !important;
  transition: background 0.2s, color 0.2s, border-color 0.2s !important;
  box-shadow: none !important;
}
.template-filter.active,
.template-filter:hover {
  background: #1e40af !important;
  color: #fff !important;
  border-color: #1e40af !important;
  box-shadow: none !important;
}
.template-stat-row {
  display: grid !important;
  grid-template-columns: repeat(3, 1fr) !important;
  gap: 0.65rem !important;
  max-width: 640px !important;
  margin: 1.25rem auto 0 !important;
}
.template-stat {
  border: 1px solid #e2e8f0 !important;
  border-radius: 8px !important;
  background: #f8fafc !important;
  padding: 0.85rem 0.75rem !important;
  text-align: center !important;
  backdrop-filter: none !important;
  box-shadow: none !important;
}
.template-stat b {
  font-family: 'Clash Display', sans-serif !important;
  display: block !important;
  font-size: 1.1rem !important;
  font-weight: 600 !important;
  color: #1e40af !important;
  margin-bottom: 0.15rem !important;
}
.template-stat span {
  font-size: 0.72rem !important;
  color: #64748b !important;
}
.template-deck {
  position: relative !important;
  z-index: 2 !important;
  margin-top: 2rem !important;
}
.template-deck::before {
  display: none !important;
}
/* Cards — preserve layout & video styling; remove glow halos only */
.template-card:hover,
.template-card:focus-visible {
  border-color: rgba(37, 99, 235, 0.4) !important;
  box-shadow: 0 20px 48px rgba(15, 23, 42, 0.22) !important;
  outline: none !important;
}
.template-card-num {
  text-shadow: 0 2px 10px rgba(15, 23, 42, 0.75) !important;
}
.template-badge {
  box-shadow: none !important;
}
.template-preview {
  animation: none !important;
  box-shadow: 0 4px 12px rgba(15, 23, 42, 0.15) !important;
}
.template-progress i {
  box-shadow: none !important;
}
@media (max-width: 680px) {
  .template-shell {
    padding: 2.5rem 1rem 2rem !important;
    border-radius: 10px !important;
  }
  .template-stat-row {
    grid-template-columns: 1fr !important;
  }
}
"""

SHELL_DECOR = [
    '<div class="template-glow template-glow-a" aria-hidden="true"></div> ',
    '<div class="template-glow template-glow-b" aria-hidden="true"></div> ',
    '<div class="template-glow template-glow-c" aria-hidden="true"></div> ',
    '<div class="template-orbit-ring" aria-hidden="true"></div> ',
    '<span class="template-spark template-spark-a" aria-hidden="true"></span> ',
    '<span class="template-spark template-spark-b" aria-hidden="true"></span> ',
    '<span class="template-spark template-spark-c" aria-hidden="true"></span> ',
]
CARD_FX_RE = re.compile(
    r'<div class="template-card-glow" aria-hidden="true"></div>\s*'
    r'<div class="template-card-scanline" aria-hidden="true"></div>\s*'
    r'<span class="template-card-ring" aria-hidden="true"></span>\s*'
)


def main():
    html_path = Path(__file__).resolve().parents[1] / "emaavy_white_blue (2).html"
    text = html_path.read_text(encoding="utf-8")

    if TEMPLATE_MARKER in text:
        start = text.index(TEMPLATE_MARKER)
        end = text.index("</style>", start)
        text = text[:start] + TEMPLATE_OVERRIDE.strip() + "\n" + text[end:]
        print("Updated existing template override block")
    else:
        text = text.replace("</style>", TEMPLATE_OVERRIDE + "\n</style>", 1)
        print("Injected template override block")

    for chunk in SHELL_DECOR:
        if chunk in text:
            text = text.replace(chunk, "", 1)
            print("Removed shell decor")

    new_text, n = CARD_FX_RE.subn("", text)
    if n:
        print(f"Removed glow FX from {n} template cards")
    text = new_text

    html_path.write_text(text, encoding="utf-8")
    print("Done:", html_path.name)


if __name__ == "__main__":
    main()
