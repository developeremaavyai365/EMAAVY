"""Post signal removal: fix extra divs, spacing, stale CSS refs."""
from pathlib import Path
import re

HTML = Path(__file__).resolve().parents[1] / "emaavy_white_blue (2).html"

def main():
    text = HTML.read_text(encoding="utf-8")

    # Extra closing div before </section> on cap-sections (legacy wrapper)
    text = re.sub(
        r"(</div> </div> </section> <!-- INTEGRATIONS)",
        r"</div> </section> <!-- INTEGRATIONS",
        text,
        count=1,
    )
    # Same pattern before other section comments if any
    for comment in ["INTEGRATIONS", "AGENTS", "CASE", "BENTO", "JOURNEY", "DOCS", "PRICING"]:
        text = re.sub(
            rf"</div> </div> </section> <!-- {comment}",
            rf"</div> </section> <!-- {comment}",
            text,
        )

    # Global animation disable — drop signal-band
    text = text.replace(".signal-band::before, ", "")
    text = text.replace(".signal-band-title { text-shadow: none !important; }\n", "")
    text = text.replace(".signal-live-badge { animation: none !important; box-shadow: none !important; }\n", "")

    # Hero → first content spacing (was signal band between)
    if "#top.hero" not in text and ".hero {" in text:
        pass
    hero_hiw = """@media (min-width: 1200px) {
  .hero-inner { grid-template-columns: minmax(0, 1.1fr) minmax(0, 0.9fr) !important; }
  .hero-showcase { max-width: 620px !important; }
}

/* Hero → sections rhythm */
.hero {
  margin-bottom: 0 !important;
}
#how-it-works.hiw-stage {
  margin-top: 0 !important;
}

"""
    anchor = "/* ═══ HOW IT WORKS — staggered flow + integration panel (EMAAVY) ═══ */"
    if "/* Hero → sections rhythm */" not in text:
        text = text.replace(anchor, hero_hiw + anchor)

    # Shell vertical rhythm
    if ".shell {" in text and ".shell > section" not in text:
        shell_gap = """
.shell > section,
.shell > .cap-section {
  scroll-margin-top: 100px !important;
}
"""
        text = text.replace(".shell {", ".shell {\n  display: block !important;\n", 1)
        if ".shell > section" not in text:
            idx = text.find(".shell {")
            if idx >= 0:
                end = text.find("}", idx) + 1
                text = text[:end] + shell_gap + text[end:]

    # platform-stats inside cap-section — navy theme match
    if "#features .platform-stats" not in text and ".cap-section .platform-stats" not in text:
        stats_css = """
.cap-section .platform-stats {
  position: relative !important;
  z-index: 1 !important;
  display: grid !important;
  grid-template-columns: repeat(3, 1fr) !important;
  gap: 1rem !important;
  max-width: 640px !important;
  margin: 2rem auto 0 !important;
  padding: 0 !important;
}
.cap-section .platform-stat {
  text-align: center !important;
  padding: 1rem 0.75rem !important;
  border-radius: 8px !important;
  border: 1px solid #e2e8f0 !important;
  background: #f8fafc !important;
  box-shadow: none !important;
  backdrop-filter: none !important;
  transition: border-color 0.2s ease, box-shadow 0.2s ease !important;
}
.cap-section .platform-stat:hover {
  border-color: #cbd5e1 !important;
  box-shadow: 0 4px 16px rgba(15, 23, 42, 0.06) !important;
}
.cap-section .platform-stat b {
  display: block !important;
  font-family: 'Clash Display', sans-serif !important;
  font-size: 1.35rem !important;
  font-weight: 600 !important;
  color: #4A658B !important;
  margin-bottom: 0.25rem !important;
}
.cap-section .platform-stat span {
  font-size: 0.75rem !important;
  color: #64748b !important;
}
@media (max-width: 560px) {
  .cap-section .platform-stats {
    grid-template-columns: 1fr !important;
    max-width: 100% !important;
  }
}

"""
        insert_at = text.find("@media (prefers-reduced-motion: reduce) {\n  .cap-section .hiw-step.reveal {")
        if insert_at > 0:
            end = text.find("}\n\n\n/* ═══ ELEGANT TEMPLATE", insert_at)
            if end > 0:
                text = text[: end + 2] + stats_css + text[end + 2 :]

    HTML.write_text(text, encoding="utf-8")
    print("layout cleanup done")


if __name__ == "__main__":
    main()
