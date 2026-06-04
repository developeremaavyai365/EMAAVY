"""Eliminate all decorative blue accent lines from landing page."""
from pathlib import Path
import re

HTML = Path(__file__).resolve().parents[1] / "emaavy_white_blue (2).html"
text = HTML.read_text(encoding="utf-8")

# --- 1. Patch base minified CSS: neutralize any ::before/::after with accent gradients ---
lines = text.splitlines()
if len(lines) > 7:
    base = lines[7]

    def kill_pseudo(m):
        sel = m.group(0).split("{")[0].strip()
        return f"{sel}{{display:none!important;content:none!important;background:none!important;height:0!important;opacity:0!important}}"

    # Top accent bars & horizontal gradient lines
    base = re.sub(
        r"\.[a-z0-9_-]+::(?:before|after)\s*\{[^}]*(?:height:\s*[1-4]px|linear-gradient\s*\(\s*90deg)[^}]*\}",
        kill_pseudo,
        base,
        flags=re.I,
    )
    lines[7] = base
    text = "\n".join(lines)

# --- 2. Disable formatted rules that recreate top accent bars ---
accent_blocks = [
    (
        r"\.h-card::after\s*\{[^}]+\}\s*\.h-card:hover,\s*\.h-card:focus-visible[^}]+\}\s*\.h-card:hover::after,\s*\.h-card:focus-visible::after\s*\{[^}]+\}",
        ".h-card::after{display:none!important;content:none!important}",
    ),
    (
        r"\.workflow-node-card::after\s*\{[^}]+\}\s*\.workflow-node:hover \.workflow-node-card,\s*\.workflow-node:focus-visible \.workflow-node-card\s*\{[^}]+\}\s*\.workflow-node:hover \.workflow-node-card::after,\s*\.workflow-node:focus-visible \.workflow-node-card::after\s*\{[^}]+\}",
        ".workflow-node-card::after{display:none!important;content:none!important}",
    ),
]
for pat, repl in accent_blocks:
    text2, n = re.subn(pat, repl, text, count=1, flags=re.S)
    if n:
        text = text2

# Simpler single-rule replacements
simple = [
    (".h-card::after {\n  content: '' !important;", ".h-card::after {\n  display: none !important;\n  content: none !important;"),
    (".workflow-node-card::after {\n  content: '' !important;", ".workflow-node-card::after {\n  display: none !important;\n  content: none !important;"),
]
for old, new in simple:
    if old in text:
        text = text.replace(old, new, 1)

# --- 3. Remove brand rules that paint kicker lines ---
text = re.sub(
    r"\.hero-kicker-line\s*\{[^}]+\}\s*\.hero-kicker-line:last-child\s*\{[^}]+\}\s*",
    "",
    text,
    count=1,
)
text = re.sub(
    r"\.section-kicker::before\s*\{\s*background:\s*#4A658B[^}]+\}\s*",
    ".section-kicker::before{display:none!important;content:none!important}\n",
    text,
    count=1,
)

# --- 4. HTML: remove kicker line spans and empty hiw-step-icon ---
text = text.replace(
    '<span class="hero-kicker-line" aria-hidden="true"></span>',
    "",
)
text = re.sub(
    r'<span class="hiw-step-icon" aria-hidden="true"></span>\s*',
    "",
    text,
)

# --- 5. Replace or extend NO BLUE block with nuclear rule ---
NUCLEAR = """
/* ═══ ZERO DECORATIVE LINES — entire page ═══ */
.masthead *::before,
.masthead *::after,
.shell *::before,
.shell *::after,
body > *::before,
body > *::after {
  background-image: none !important;
}
.masthead *::before,
.masthead *::after,
.shell section ::before,
.shell section ::after,
.shell .cap-section ::before,
.shell .cap-section ::after,
.shell .int-showcase ::before,
.shell .int-showcase ::after,
.shell .hiw-stage ::before,
.shell .hiw-stage ::after,
.shell .template-shell ::before,
.shell .template-shell ::after,
.shell .workflow-shell ::before,
.shell .workflow-shell ::after,
.shell .platform-shell ::before,
.shell .platform-shell ::after,
.shell .telephony-shell ::before,
.shell .telephony-shell ::after,
.shell .page-section ::before,
.shell .page-section ::after,
.shell .feature-card ::before,
.shell .feature-card ::after,
.shell .h-card ::before,
.shell .h-card ::after,
.shell .bento ::before,
.shell .bento ::after,
.shell .int-card ::before,
.shell .int-card ::after,
.shell .hiw-step ::before,
.shell .hiw-step ::after,
.shell .hiw-steps ::before,
.shell .hiw-steps ::after,
.shell h1::before, .shell h1::after,
.shell h2::before, .shell h2::after,
.shell h3::before, .shell h3::after,
.shell h4::before, .shell h4::after,
.hero-kicker-line,
.hiw-step-icon,
.section-kicker::before,
.scanlines, .grain, .masthead-scan {
  display: none !important;
  content: none !important;
  background: none !important;
  background-image: none !important;
  box-shadow: none !important;
  border: none !important;
  height: 0 !important;
  width: 0 !important;
  max-height: 0 !important;
  opacity: 0 !important;
  visibility: hidden !important;
  pointer-events: none !important;
}

/* Keep only functional UI (not decorative lines) */
.hero-showcase-progress,
.hero-showcase-dots button .hero-showcase-progress,
.nav-hamburger span,
.workflow-connector::after,
.hiw-flow-arrows,
.hiw-flow-arrows path,
.hiw-flow-arrows polygon,
.rail-dots a,
.hero-showcase-eq i {
  display: revert !important;
  content: revert !important;
  visibility: visible !important;
  opacity: revert !important;
  height: revert !important;
  width: revert !important;
  background: revert !important;
  background-image: revert !important;
}
.hero-showcase-eq i {
  display: block !important;
  width: 2px !important;
  height: 4px !important;
  background: #7a94b2 !important;
}
.workflow-connector::after {
  display: block !important;
  content: '▶' !important;
  height: auto !important;
  width: auto !important;
  background: none !important;
}
.nav-hamburger span {
  display: block !important;
  width: 22px !important;
  height: 2px !important;
  background: #334155 !important;
}

"""

marker = "/* ═══ NO BLUE ACCENT LINES"
if "/* ═══ ZERO DECORATIVE LINES" in text:
    print("Nuclear block already present")
else:
    if marker in text:
        # Replace old block through next major section or </style>
        text = re.sub(
            r"/\* ═══ NO BLUE ACCENT LINES[\s\S]*?(?=/\* Final overrides|</style>)",
            NUCLEAR,
            text,
            count=1,
        )
    else:
        text = text.replace("</style>", NUCLEAR + "\n</style>", 1)
    print("Inserted nuclear ZERO DECORATIVE LINES block")

# Remove duplicate Final overrides if redundant
text = re.sub(
    r"/\* Final overrides — no stray lines after brand tokens \*/\s*\.section-kicker::before\s*\{[^}]+\}\s*\.hero-showcase::before,\s*\.hero-showcase-device::before\s*\{[^}]+\}\s*\.hero-kicker-line\s*\{[^}]+\}\s*",
    "",
    text,
    count=1,
)

HTML.write_text(text, encoding="utf-8")
print("Saved", HTML)
