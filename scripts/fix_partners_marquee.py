"""Remove leftover marquee and fix partner logos."""
import re
from pathlib import Path

HTML = Path(__file__).resolve().parents[1] / "emaavy_white_blue (2).html"
text = HTML.read_text(encoding="utf-8")

start = text.find(' <div class="platform-marquee-zone" aria-label="Connected platform partners">')
if start >= 0:
    end = text.find(' </div> </section>', start)
    if end > start:
        text = text[:start] + text[end:]
        print("Removed platform-marquee-zone")

# Fix logos that 404 — use text marks
text = text.replace(
    '<img src="https://cdn.simpleicons.org/sarvam/6366F1" alt="Sarvam" loading="lazy" />',
    '<span class="partner-logo-text logo-sarvam">Sarvam</span>',
)
text = text.replace(
    '<img src="https://cdn.simpleicons.org/xdotai/000000" alt="Grok" loading="lazy" />',
    '<span class="partner-logo-text logo-grok">Grok</span>',
)

# Add sarvam/grok logo text styles if missing
if ".partner-logo-text.logo-sarvam" not in text:
    insert = """
.partner-logo-text.logo-sarvam {
  font-family: system-ui, sans-serif !important;
  font-weight: 700 !important;
  font-size: 1rem !important;
  color: #4338ca !important;
}
.partner-logo-text.logo-grok {
  font-family: system-ui, sans-serif !important;
  font-weight: 700 !important;
  font-size: 1rem !important;
  color: #0f172a !important;
  letter-spacing: -0.03em !important;
}
"""
    marker = "/* ═══ ELEGANT PARTNERS — Powered by the best ═══ */"
    pos = text.find(".partner-logo-text.logo-webhooks")
    if pos > 0:
        text = text[:pos] + insert + text[pos:]

HTML.write_text(text, encoding="utf-8")
print("Done")
