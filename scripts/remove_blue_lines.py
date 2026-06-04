"""Remove decorative blue accent lines (pseudo-elements) site-wide."""
from pathlib import Path
import re

HTML = Path(__file__).resolve().parents[1] / "emaavy_white_blue (2).html"
text = HTML.read_text(encoding="utf-8")

NO_BLUE_LINES = """
/* ═══ NO BLUE ACCENT LINES — site-wide (wins over base + brand) ═══ */
.hiw-steps::before,
.hiw-step::before,
.hiw-step::after,
.hiw-step-icon,
.feature-card::before,
.feature-card::after,
.int-card::before,
.int-card::after,
.h-card::before,
.h-card::after,
.bento::before,
.bento::after,
.template-card::before,
.template-card::after,
.template-deck::before,
.template-shell::before,
.workflow-shell::before,
.workflow-node-card::before,
.workflow-node-card::after,
.workflow-connector::before,
.platform-shell::before,
.platform-chip-inner::before,
.platform-marquee-zone::before,
.journey-track::before,
.signal-chip::before,
.telephony-shell::before,
.telephony-hero::before,
.int-shell::before,
.page-section::before,
.cinematic-inner::before,
.h-scroll-wrap::before,
.float-card::before,
.glow-card::after,
.nav-dropdown-menu::before,
.dropdown-section::before,
.cap-section::before,
#how-it-works::before,
#how-it-works.hiw-stage::before,
.hiw-flow-card::before,
.hiw-flow-card::after,
.int-head::before,
.int-head::after,
.masthead::before,
.masthead::after,
.masthead-beam::before,
.masthead-inner::before,
.masthead-inner::after,
.logo-mega::before,
.logo-mega::after,
.logo-mega-brand::before,
.logo-mega-maavy::before,
.logo-tag::before,
.logo-tag::after,
.hero::before,
.hero::after,
.hero-eyebrow::before,
.hero-kicker-line,
.section-kicker::before,
.masthead-scan,
.scanlines,
.grain {
  display: none !important;
  content: none !important;
  background: none !important;
  background-image: none !important;
  box-shadow: none !important;
  height: 0 !important;
  width: 0 !important;
  max-height: 0 !important;
  opacity: 0 !important;
  visibility: hidden !important;
  pointer-events: none !important;
  border: none !important;
}

/* Empty icon placeholders — no bordered boxes between badge and title */
.hiw-step-icon,
.cap-section .hiw-step-icon,
#integrations .hiw-step-icon {
  display: none !important;
  width: 0 !important;
  height: 0 !important;
  margin: 0 !important;
  padding: 0 !important;
  border: none !important;
  overflow: hidden !important;
}

/* Hero title outline stroke reads as stray lines */
.hero-title .line-every .outline,
.hero h1 .outline {
  -webkit-text-stroke: 0 !important;
  text-stroke: 0 !important;
  color: #64748b !important;
  -webkit-text-fill-color: #64748b !important;
}

"""

marker = "/* Final overrides — no stray lines after brand tokens */"
if "/* ═══ NO BLUE ACCENT LINES" in text:
    print("NO_BLUE_LINES block already present")
else:
    if marker not in text:
        text = text.replace("</style>", NO_BLUE_LINES + "\n</style>", 1)
    else:
        text = text.replace(marker, NO_BLUE_LINES + marker, 1)
    print("Inserted NO_BLUE_LINES block")

# Patch early rule that forces hiw-step-icon visible
old_icon = (
    ".hiw-step-icon, .signal-chip-icon-wrap, .workflow-node-icon, .telephony-feature-icon "
    "{ display: flex !important;"
)
new_icon = (
    ".signal-chip-icon-wrap, .workflow-node-icon, .telephony-feature-icon "
    "{ display: flex !important;"
)
if old_icon in text:
    text = text.replace(old_icon, new_icon, 1)
    print("Removed hiw-step-icon from early flex rule")

# Neuter base minified accent lines (line 8)
lines = text.splitlines()
if len(lines) > 7:
    base = lines[7]
    subs = [
        (r"\.hiw-steps::before\s*\{[^}]+\}", ".hiw-steps::before{display:none!important;content:none!important}"),
        (r"\.hiw-step::before\s*\{[^}]+\}", ".hiw-step::before{display:none!important;content:none!important}"),
        (r"\.feature-card::after\s*\{[^}]+\}", ".feature-card::after{display:none!important;content:none!important}"),
        (r"\.int-card::before\s*\{[^}]+\}", ".int-card::before{display:none!important;content:none!important}"),
        (r"\.h-card::after\s*\{[^}]+\}", ".h-card::after{display:none!important;content:none!important}"),
        (r"\.bento::after\s*\{[^}]+\}", ".bento::after{display:none!important;content:none!important}"),
        (r"\.template-card::after\s*\{[^}]+\}", ".template-card::after{display:none!important;content:none!important}"),
        (r"\.nav-dropdown-menu::before\s*\{[^}]+\}", ".nav-dropdown-menu::before{display:none!important;content:none!important}"),
    ]
    new_base = base
    for pat, repl in subs:
        new_base, n = re.subn(pat, repl, new_base)
        if n:
            print(f"Patched base: {pat[:30]}... ({n})")
    lines[7] = new_base
    text = "\n".join(lines)

# Strengthen cap-section rules
text = text.replace(
    ".cap-section .hiw-steps::before {\n  display: none !important;\n}",
    ".cap-section .hiw-steps::before,\n.hiw-steps::before {\n  display: none !important;\n  content: none !important;\n  background: none !important;\n  height: 0 !important;\n}",
    1,
)
text = text.replace(
    ".cap-section .hiw-step::before {\n  display: none !important;\n}",
    ".cap-section .hiw-step::before,\n.hiw-step::before {\n  display: none !important;\n  content: none !important;\n  background: none !important;\n  height: 0 !important;\n}",
    1,
)

# Add hiw-steps to glitch kill if missing
if ".hiw-steps::before," not in text.split("GLITCH-FREE")[1][:1200]:
    text = text.replace(
        "#how-it-works .hiw-mesh-lines,",
        "#how-it-works .hiw-mesh-lines,\n.hiw-steps::before,\n.hiw-step::before,\n.hiw-step::after,\n.feature-card::after,\n.int-card::before,\n.h-card::after,\n.bento::after,\n.template-card::after,\n.nav-dropdown-menu::before,",
        1,
    )
    print("Extended GLITCH-FREE list")

HTML.write_text(text, encoding="utf-8")
print("Done.")
