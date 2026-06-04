"""100% remove decorative blue lines — universal pseudo-element kill."""
from pathlib import Path
import re

HTML = Path(__file__).resolve().parents[1] / "emaavy_white_blue (2).html"
text = HTML.read_text(encoding="utf-8")

FINAL_CSS = """
/* ═══ 100% NO DECORATIVE LINES — must be last in stylesheet ═══ */
body[data-page="home"] *::before,
body[data-page="home"] *::after {
  display: none !important;
  content: none !important;
  background: none !important;
  background-image: none !important;
  box-shadow: none !important;
  border: none !important;
  outline: none !important;
  height: 0 !important;
  width: 0 !important;
  max-height: 0 !important;
  min-height: 0 !important;
  opacity: 0 !important;
  visibility: hidden !important;
  pointer-events: none !important;
  animation: none !important;
}

/* Decorative overlay elements (real DOM, not pseudo) */
body[data-page="home"] [class*="scanline"],
body[data-page="home"] [class*="-glow"]:not(.hero-showcase-live-badge),
body[data-page="home"] .scanlines,
body[data-page="home"] .grain,
body[data-page="home"] .ambient,
body[data-page="home"] .masthead-scan,
body[data-page="home"] .hero-kicker-line,
body[data-page="home"] .hiw-step-icon,
body[data-page="home"] .nav-dropdown-menu-glow,
body[data-page="home"] .feature-card-glow,
body[data-page="home"] .hiw-step-glow,
body[data-page="home"] .h-card-glow,
body[data-page="home"] .template-card-glow,
body[data-page="home"] .template-card-scanline,
body[data-page="home"] .workflow-node-scanline,
body[data-page="home"] .workflow-node-glow,
body[data-page="home"] .int-card-glow,
body[data-page="home"] .int-card-scanline,
body[data-page="home"] .telephony-scanline,
body[data-page="home"] .telephony-hero-scanline,
body[data-page="home"] .int-scanline,
body[data-page="home"] .platform-hub-glow,
body[data-page="home"] .platform-hub-ring,
body[data-page="home"] .platform-chip-glow,
body[data-page="home"] .platform-marquee-pill-glow,
body[data-page="home"] .signal-chip-glow {
  display: none !important;
  visibility: hidden !important;
  opacity: 0 !important;
  height: 0 !important;
  width: 0 !important;
  overflow: hidden !important;
  pointer-events: none !important;
}

/* Whitelist: functional UI only */
body[data-page="home"] .nav-hamburger span {
  display: block !important;
  visibility: visible !important;
  opacity: 1 !important;
  width: 22px !important;
  height: 2px !important;
  background: #334155 !important;
  content: none !important;
}
body[data-page="home"] .hero-showcase-progress {
  display: block !important;
  visibility: visible !important;
  opacity: 1 !important;
  height: 4px !important;
  width: auto !important;
  background: linear-gradient(90deg, #4A658B, #5a7d9e) !important;
  content: none !important;
}
body[data-page="home"] .hero-showcase-eq i {
  display: block !important;
  visibility: visible !important;
  opacity: 1 !important;
  width: 2px !important;
  height: 4px !important;
  background: #7a94b2 !important;
  content: none !important;
}
body[data-page="home"] .workflow-connector::after {
  display: block !important;
  visibility: visible !important;
  opacity: 1 !important;
  width: auto !important;
  height: auto !important;
  content: "▶" !important;
  background: none !important;
  color: #94a3b8 !important;
  font-size: 0.45rem !important;
}
body[data-page="home"] .workflow-node-icon::before {
  display: flex !important;
  visibility: visible !important;
  opacity: 1 !important;
  width: auto !important;
  height: auto !important;
  content: attr(data-label) !important;
}
body[data-page="home"] #workflow .workflow-node-icon::before {
  display: flex !important;
  align-items: center !important;
  justify-content: center !important;
  visibility: visible !important;
  opacity: 1 !important;
  width: 100% !important;
  height: 100% !important;
  font-size: 0.75rem !important;
  color: #4A658B !important;
  background: #f8fafc !important;
  content: "" !important;
}
body[data-page="home"] .workflow-node[data-detail="wf-ingest"] .workflow-node-icon::before { content: "IN" !important; }
body[data-page="home"] .workflow-node[data-detail="wf-understand"] .workflow-node-icon::before { content: "UN" !important; }
body[data-page="home"] .workflow-node[data-detail="wf-orchestrate"] .workflow-node-icon::before { content: "OR" !important; }
body[data-page="home"] .workflow-node[data-detail="wf-optimize"] .workflow-node-icon::before { content: "OP" !important; }
body[data-page="home"] .hiw-flow-arrows,
body[data-page="home"] .hiw-flow-arrows path,
body[data-page="home"] .hiw-flow-arrows polygon {
  display: block !important;
  visibility: visible !important;
  opacity: revert !important;
  content: none !important;
}
body[data-page="home"] .call-flow-connector::after,
body[data-page="home"] #integration-stt .call-flow-connector::after {
  display: block !important;
  visibility: visible !important;
  opacity: 1 !important;
  content: "" !important;
}

/* Hero title — no stroke lines through text */
body[data-page="home"] .hero-title .line-every .outline,
body[data-page="home"] .hero h1 .outline {
  -webkit-text-stroke: 0 !important;
  text-stroke: 0 !important;
  color: #64748b !important;
  -webkit-text-fill-color: #64748b !important;
}

"""

# Replace old ZERO DECORATIVE / NO BLUE blocks
markers = (
    "/* ═══ ZERO DECORATIVE LINES",
    "/* ═══ 100% NO DECORATIVE LINES",
    "/* ═══ NO BLUE ACCENT LINES",
)
if "/* ═══ 100% NO DECORATIVE LINES" in text:
    start = text.index("/* ═══ 100% NO DECORATIVE LINES")
    end = text.index("</style>", start)
    text = text[:start] + FINAL_CSS.strip() + "\n\n" + text[end:]
else:
    for m in markers:
        if m in text:
            start = text.index(m)
            end = text.index("</style>", start)
            text = text[:start] + FINAL_CSS.strip() + "\n\n" + text[end:]
            break
    else:
        text = text.replace("</style>", FINAL_CSS + "\n</style>", 1)

# Strip duplicate hero outline block if present after FINAL_CSS
text = re.sub(
    r"/\* No outline stroke through hero words \*/\s*\.hero-title \.line-every \.outline[\s\S]*?-webkit-text-fill-color: #64748b !important;\s*\}\s*",
    "",
    text,
    count=1,
)

# Neutralize formatted rules that still paint top accent bars (between line 100 and </style>)
style_match = re.search(r"(<style>)(.*?)(</style>)", text, re.S)
if style_match:
    css = style_match.group(2)
    lines = css.split("\n")
    out = []
    for line in lines:
        if re.search(r"::(?:before|after).*\{", line) and "display:\s*none" not in line.replace(" ", ""):
            if any(
                x in line
                for x in (
                    "linear-gradient(90deg",
                    "height: 3px",
                    "height: 2px",
                    "height: 1px",
                    "height: 4px",
                    "#4A658B",
                    "2563eb",
                    "37, 99, 235",
                )
            ) and "workflow-connector::after" not in line and "workflow-node-icon::before" not in line:
                # skip — universal rule handles
                pass
        out.append(line)
    # Force-disable known accent blocks in formatted CSS
    patches = [
        (
            ".h-card::after{display:none!important;content:none!important}",
            ".h-card::after { display: none !important; content: none !important; background: none !important; height: 0 !important; opacity: 0 !important; }",
        ),
        (
            ".workflow-node-card::after {\n  display: none !important;\n  content: none !important;",
            ".workflow-node-card::after { display: none !important; content: none !important; background: none !important; height: 0 !important; opacity: 0 !important;",
        ),
    ]
    css_new = "\n".join(out)
    for a, b in patches:
        if a in css_new:
            css_new = css_new.replace(a, b, 1)
    text = text[: style_match.start(2)] + css_new + text[style_match.end(2) :]

HTML.write_text(text, encoding="utf-8")
print("Applied universal line kill to", HTML.name)
