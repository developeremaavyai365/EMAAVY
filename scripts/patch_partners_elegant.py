"""Rebuild Powered by the best section with all partners, logos, authentic names."""
import re
from pathlib import Path

HTML = Path(__file__).resolve().parents[1] / "emaavy_white_blue (2).html"

PARTNERS = [
    {"name": "OpenAI", "cat": "LLM", "logo": "https://cdn.worldvectorlogo.com/logos/openai-2.svg", "class": "name-openai"},
    {"name": "Claude", "cat": "LLM", "logo": "https://cdn.simpleicons.org/anthropic/191919", "class": "name-claude"},
    {"name": "Gemini", "cat": "LLM", "logo": "https://cdn.simpleicons.org/googlegemini/8E75B2", "class": "name-gemini"},
    {"name": "Qwen", "cat": "LLM", "logo": "https://cdn.simpleicons.org/alibabacloud/FF6A00", "class": "name-qwen"},
    {"name": "Grok", "cat": "LLM", "logo": "https://cdn.simpleicons.org/xdotai/000000", "class": "name-grok"},
    {"name": "Deepgram", "cat": "Speech", "logo": "https://cdn.simpleicons.org/deepgram/13EF93", "class": "name-deepgram"},
    {"name": "Sarvam", "cat": "Speech", "logo": "https://cdn.simpleicons.org/sarvam/6366F1", "class": "name-sarvam"},
    {"name": "ElevenLabs", "cat": "Voice", "logo": "https://cdn.simpleicons.org/elevenlabs/000000", "class": "name-elevenlabs"},
    {"name": "Bulbul", "cat": "Voice", "logo": "", "class": "name-bulbul", "text_logo": "Bulbul"},
    {"name": "Vobiz", "cat": "Telephony", "logo": "", "class": "name-vobiz", "text_logo": "Vobiz"},
    {"name": "Salesforce", "cat": "CRM", "logo": "https://cdn.worldvectorlogo.com/logos/salesforce-2.svg", "class": "name-salesforce"},
    {"name": "HubSpot", "cat": "CRM", "logo": "https://cdn.simpleicons.org/hubspot/FF7A59", "class": "name-hubspot"},
    {"name": "WhatsApp", "cat": "Messaging", "logo": "https://cdn.simpleicons.org/whatsapp/25D366", "class": "name-whatsapp"},
    {"name": "Slack", "cat": "Messaging", "logo": "https://cdn.simpleicons.org/slack/4A154B", "class": "name-slack"},
    {"name": "Cal.com", "cat": "Scheduling", "logo": "https://cdn.simpleicons.org/caldotcom/292929", "class": "name-calcom"},
    {"name": "Google Calendar", "cat": "Scheduling", "logo": "https://cdn.simpleicons.org/googlecalendar/4285F4", "class": "name-gcal"},
    {"name": "Webhooks", "cat": "Automation", "logo": "", "class": "name-webhooks", "text_logo": "{ }"},
]

PARTNERS_CSS = """
/* ═══ ELEGANT PARTNERS — Powered by the best ═══ */
.proof-wall {
  padding: 0 0 4rem !important;
}
.proof-wall .platform-shell {
  position: relative !important;
  width: min(1200px, calc(100% - 2rem)) !important;
  margin: 0 auto !important;
  padding: 3rem clamp(1.25rem, 4vw, 2.5rem) 2.5rem !important;
  border-radius: 12px !important;
  border: 1px solid #e2e8f0 !important;
  background: #ffffff !important;
  box-shadow: none !important;
  overflow: visible !important;
  isolation: auto !important;
}
.proof-wall .platform-shell::before,
.proof-wall .platform-glow,
.proof-wall .platform-constellation,
.proof-wall .platform-marquee-zone,
.proof-wall .platform-orbit-layout,
.proof-wall .platform-hub-glow,
.proof-wall .platform-hub-ring,
.proof-wall .platform-chip-glow,
.proof-wall .platform-marquee-pill-glow {
  display: none !important;
}
.proof-wall .platform-marquee-head {
  position: relative !important;
  z-index: 1 !important;
  text-align: center !important;
  max-width: 680px !important;
  margin: 0 auto 2.25rem !important;
}
.proof-wall .platform-marquee-head .section-kicker {
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
.proof-wall .platform-marquee-head .section-kicker::before {
  display: none !important;
}
.proof-wall .platform-marquee-head h3 {
  font-family: 'Clash Display', sans-serif !important;
  font-size: clamp(1.75rem, 3.5vw, 2.25rem) !important;
  font-weight: 600 !important;
  letter-spacing: -0.02em !important;
  color: #0f172a !important;
  margin-bottom: 0.5rem !important;
  text-shadow: none !important;
  line-height: 1.12 !important;
}
.proof-wall .platform-marquee-head p {
  color: #64748b !important;
  font-size: 0.95rem !important;
  line-height: 1.65 !important;
  max-width: 520px !important;
  margin: 0 auto !important;
}
.partner-grid {
  display: grid !important;
  grid-template-columns: repeat(auto-fill, minmax(140px, 1fr)) !important;
  gap: 0.75rem !important;
  margin-bottom: 2rem !important;
}
.partner-tile {
  display: flex !important;
  flex-direction: column !important;
  align-items: center !important;
  justify-content: center !important;
  gap: 0.65rem !important;
  padding: 1.15rem 0.75rem 1rem !important;
  border: 1px solid #e2e8f0 !important;
  border-radius: 10px !important;
  background: #ffffff !important;
  min-height: 118px !important;
  transition: border-color 0.2s ease, box-shadow 0.2s ease, background 0.2s ease !important;
}
.partner-tile:hover {
  border-color: #cbd5e1 !important;
  background: #f8fafc !important;
  box-shadow: 0 4px 16px rgba(15, 23, 42, 0.06) !important;
}
.partner-logo {
  display: flex !important;
  align-items: center !important;
  justify-content: center !important;
  width: 100% !important;
  height: 36px !important;
}
.partner-logo img {
  max-height: 28px !important;
  max-width: 88px !important;
  width: auto !important;
  height: auto !important;
  object-fit: contain !important;
}
.partner-logo-text {
  font-family: 'Clash Display', sans-serif !important;
  font-weight: 700 !important;
  font-size: 1.05rem !important;
  color: #0f172a !important;
  letter-spacing: -0.02em !important;
}
.partner-logo-text.logo-bulbul {
  font-family: 'General Sans', system-ui, sans-serif !important;
  font-weight: 600 !important;
  font-size: 0.95rem !important;
  color: #1e40af !important;
}
.partner-logo-text.logo-vobiz {
  font-family: 'Clash Display', sans-serif !important;
  font-weight: 700 !important;
  font-size: 1.1rem !important;
  color: #1e40af !important;
  letter-spacing: 0.04em !important;
}
.partner-logo-text.logo-webhooks {
  font-family: 'JetBrains Mono', ui-monospace, monospace !important;
  font-weight: 500 !important;
  font-size: 0.85rem !important;
  color: #64748b !important;
  background: #f1f5f9 !important;
  border: 1px solid #e2e8f0 !important;
  border-radius: 6px !important;
  padding: 0.35rem 0.55rem !important;
}
.partner-name {
  font-size: 0.82rem !important;
  font-weight: 600 !important;
  color: #0f172a !important;
  text-align: center !important;
  line-height: 1.2 !important;
  letter-spacing: -0.01em !important;
}
.partner-name.name-openai {
  font-family: system-ui, -apple-system, 'Segoe UI', sans-serif !important;
  font-weight: 600 !important;
  letter-spacing: -0.03em !important;
}
.partner-name.name-claude {
  font-family: system-ui, -apple-system, 'Segoe UI', sans-serif !important;
  font-weight: 600 !important;
}
.partner-name.name-gemini {
  font-family: 'Google Sans', system-ui, sans-serif !important;
  font-weight: 500 !important;
  background: linear-gradient(90deg, #4285F4, #9B72CB, #D96570) !important;
  -webkit-background-clip: text !important;
  background-clip: text !important;
  -webkit-text-fill-color: transparent !important;
  color: transparent !important;
}
.partner-name.name-qwen {
  font-family: system-ui, sans-serif !important;
  font-weight: 700 !important;
}
.partner-name.name-grok {
  font-family: system-ui, sans-serif !important;
  font-weight: 700 !important;
  letter-spacing: -0.02em !important;
}
.partner-name.name-deepgram {
  font-family: system-ui, sans-serif !important;
  font-weight: 600 !important;
}
.partner-name.name-sarvam {
  font-family: system-ui, sans-serif !important;
  font-weight: 600 !important;
}
.partner-name.name-elevenlabs {
  font-family: system-ui, sans-serif !important;
  font-weight: 600 !important;
  letter-spacing: -0.02em !important;
}
.partner-name.name-bulbul {
  font-family: 'General Sans', system-ui, sans-serif !important;
  font-weight: 600 !important;
}
.partner-name.name-vobiz {
  font-family: 'Clash Display', sans-serif !important;
  font-weight: 700 !important;
  letter-spacing: 0.02em !important;
}
.partner-name.name-salesforce {
  font-family: system-ui, sans-serif !important;
  font-weight: 700 !important;
  color: #0176D3 !important;
}
.partner-name.name-hubspot {
  font-family: system-ui, sans-serif !important;
  font-weight: 700 !important;
  color: #FF7A59 !important;
}
.partner-name.name-whatsapp {
  font-family: system-ui, sans-serif !important;
  font-weight: 600 !important;
}
.partner-name.name-slack {
  font-family: system-ui, sans-serif !important;
  font-weight: 700 !important;
  color: #4A154B !important;
}
.partner-name.name-calcom {
  font-family: system-ui, sans-serif !important;
  font-weight: 600 !important;
  letter-spacing: -0.02em !important;
}
.partner-name.name-gcal {
  font-family: 'Google Sans', system-ui, sans-serif !important;
  font-weight: 500 !important;
  font-size: 0.76rem !important;
}
.partner-name.name-webhooks {
  font-family: system-ui, sans-serif !important;
  font-weight: 600 !important;
  color: #475569 !important;
}
.partner-cat {
  font-size: 0.58rem !important;
  font-weight: 500 !important;
  letter-spacing: 0.08em !important;
  text-transform: uppercase !important;
  color: #94a3b8 !important;
}
.proof-wall .platform-stats {
  display: grid !important;
  grid-template-columns: repeat(3, 1fr) !important;
  gap: 0.65rem !important;
  max-width: 640px !important;
  margin: 0 auto !important;
}
.proof-wall .platform-stat {
  border: 1px solid #e2e8f0 !important;
  border-radius: 8px !important;
  background: #f8fafc !important;
  padding: 0.85rem 0.75rem !important;
  text-align: center !important;
  box-shadow: none !important;
  backdrop-filter: none !important;
}
.proof-wall .platform-stat b {
  font-family: 'Clash Display', sans-serif !important;
  font-size: 1.1rem !important;
  font-weight: 600 !important;
  color: #1e40af !important;
}
.proof-wall .platform-stat span {
  font-size: 0.72rem !important;
  color: #64748b !important;
}
@media (max-width: 640px) {
  .partner-grid {
    grid-template-columns: repeat(2, 1fr) !important;
  }
  .proof-wall .platform-shell {
    padding: 2.5rem 1rem 2rem !important;
    border-radius: 10px !important;
  }
  .proof-wall .platform-stats {
    grid-template-columns: 1fr !important;
  }
}
"""

MARKER = "/* ═══ ELEGANT PARTNERS — Powered by the best ═══ */"


def logo_html(p):
    if p.get("logo"):
        return f'<img src="{p["logo"]}" alt="{p["name"]}" loading="lazy" />'
    text = p.get("text_logo", p["name"][:2])
    cls = p["class"].replace("name-", "logo-")
    return f'<span class="partner-logo-text {cls}">{text}</span>'


def build_grid():
    tiles = []
    for p in PARTNERS:
        tiles.append(
            f'<article class="partner-tile">'
            f'<div class="partner-logo">{logo_html(p)}</div>'
            f'<span class="partner-name {p["class"]}">{p["name"]}</span>'
            f'<span class="partner-cat">{p["cat"]}</span>'
            f'</article>'
        )
    return f'<div class="partner-grid" aria-label="Integration partners">{"".join(tiles)}</div>'


def main():
    text = HTML.read_text(encoding="utf-8")

    # Remove shell glow markup
    for chunk in [
        '<div class="platform-glow platform-glow-a" aria-hidden="true"></div> ',
        '<div class="platform-glow platform-glow-b" aria-hidden="true"></div> ',
    ]:
        text = text.replace(chunk, "")

    # Replace constellation + marquee with partner grid
    pattern = re.compile(
        r'<div class="platform-constellation">.*?</div>\s*<div class="platform-stats">',
        re.DOTALL,
    )
    replacement = build_grid() + '\n <div class="platform-stats">'
    if not pattern.search(text):
        print("ERROR: platform-constellation block not found")
        return
    text = pattern.sub(replacement, text, count=1)

    # Update stat count
    text = text.replace(
        '<div class="platform-stat"><b>8+</b><span>AI platforms</span></div>',
        '<div class="platform-stat"><b>17+</b><span>Integration partners</span></div>',
        1,
    )

    # Inject CSS
    if MARKER in text:
        start = text.index(MARKER)
        end = text.index("</style>", start)
        text = text[:start] + PARTNERS_CSS.strip() + "\n" + text[end:]
    else:
        text = text.replace("</style>", PARTNERS_CSS + "\n</style>", 1)

    HTML.write_text(text, encoding="utf-8")
    print(f"Updated proof section with {len(PARTNERS)} partners")


if __name__ == "__main__":
    main()
