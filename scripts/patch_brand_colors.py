"""Apply EMAAVY white + navy brand colors across landing page."""
from pathlib import Path

HTML = Path(__file__).resolve().parents[1] / "emaavy_white_blue (2).html"

ROOT_NEW = (
    ":root { --void: #ffffff; --ink: #ffffff; --panel: #f8fafc; --ice: #18345D; "
    "--bolt: #4A658B; --deep: #18345D; --violet: #4A658B; --white: #18345D; "
    "--dim: #64748b; --glass: rgba(255, 255, 255, 0.92); --rail: 88px; "
    "--masthead-h: 148px; --masthead-h-compact: 72px; --border: #e2e8f0; "
    "--border-strong: #cbd5e1; --surface: #ffffff; --surface-muted: #f8fafc; "
    "--accent: #4A658B; --accent-hover: #18345D; --brand-light: #4A658B; "
    "--brand-dark: #18345D; --brand-grad: linear-gradient(135deg, #4A658B 0%, #18345D 100%); }"
)

REPLACEMENTS = [
    ("#2563eb", "#4A658B"),
    ("#1e40af", "#4A658B"),
    ("#1e3a8a", "#18345D"),
    ("#1d4ed8", "#18345D"),
    ("#3b82f6", "#4A658B"),
    ("#60a5fa", "#5a7d9e"),
    ("#93c5fd", "#7a94b2"),
    ("#bfdbfe", "#c5d4e4"),
    ("#dbeafe", "#e4ebf3"),
    ("#eff6ff", "#f0f4f8"),
    ("#22c55e", "#4A658B"),
    ("#4ade80", "#6b87ab"),
    ("#10b981", "#4A658B"),
    ("#f87171", "#4A658B"),
    ("#fbbf24", "#6b87ab"),
    ("#0ea5e9", "#4A658B"),
    ("#38bdf8", "#5a7d9e"),
    ("#06b6d4", "#4A658B"),
    ("#8b5cf6", "#4A658B"),
    ("#a855f7", "#4A658B"),
]

BRAND_CSS = r"""
/* ═══ EMAAVY BRAND PALETTE — white + secondary navy ═══ */
html { background: #ffffff !important; }
body {
  background: #ffffff !important;
  color: #18345D !important;
}
section,
.page-section,
.signal-band,
.int-shell,
.hiw-step,
.feature-card,
.h-card,
.template-shell,
.workflow-shell,
.platform-shell,
.price-card,
.contact-card,
.book-demo-shell,
.detail-drawer,
.nav-dropdown-menu,
.masthead-beam,
.hero-showcase-device,
.hero-showcase-footer {
  background-color: #ffffff !important;
}
.signal-band,
.int-shell,
.hiw-step,
.feature-card,
.h-card,
.template-shell,
.workflow-shell,
.platform-shell,
.price-card,
.contact-card,
.page-section,
.nav-dropdown-menu,
.hero-showcase-device {
  border-color: #e2e8f0 !important;
}
.btn-fill,
.masthead-go,
.hero-actions .btn-fill,
.pricing-cta.is-primary,
.pack-cta.btn-fill,
.template-cta .btn-fill {
  background: linear-gradient(135deg, #4A658B 0%, #18345D 100%) !important;
  color: #ffffff !important;
  border-color: transparent !important;
}
.btn-fill:hover,
.masthead-go:hover,
.hero-actions .btn-fill:hover,
.pricing-cta.is-primary:hover {
  background: #18345D !important;
  color: #ffffff !important;
}
.masthead-nav a.active,
.nav-integrations-link.active,
.masthead-nav a.active:hover {
  color: #18345D !important;
  background: #f0f4f8 !important;
}
.section-kicker {
  color: #4A658B !important;
}
.section-kicker::before {
  background: #4A658B !important;
}
.signal-live-badge .signal-dot,
.hero-showcase-pulse {
  background: #4A658B !important;
  box-shadow: 0 0 0 0 rgba(74, 101, 139, 0.45) !important;
}
.hero-kicker-line {
  background: linear-gradient(90deg, transparent, #7a94b2 55%, #4A658B) !important;
}
.hero-kicker-line:last-child {
  background: linear-gradient(90deg, #4A658B, #7a94b2 45%, transparent) !important;
}
.hero-pitch strong,
.masthead-login:hover,
.footer-links a:hover {
  color: #4A658B !important;
}
.hero-showcase::before {
  background: radial-gradient(ellipse 75% 65% at 50% 40%, rgba(74, 101, 139, 0.16) 0%, rgba(24, 52, 93, 0.06) 45%, transparent 70%) !important;
}
.hero-showcase-device {
  box-shadow:
    0 1px 2px rgba(24, 52, 93, 0.05),
    0 24px 56px -14px rgba(24, 52, 93, 0.22),
    0 0 0 1px rgba(255, 255, 255, 0.85) inset !important;
}
.hero-showcase-dot:nth-child(1) { background: #4A658B !important; }
.hero-showcase-dot:nth-child(2) { background: #6b87ab !important; }
.hero-showcase-dot:nth-child(3) { background: #18345D !important; }
.price-card.featured {
  border-color: #4A658B !important;
}
.pack-badge.hot {
  background: linear-gradient(135deg, #4A658B, #18345D) !important;
  color: #fff !important;
}
.platform-stat b,
.signal-chip-metric strong {
  color: #4A658B !important;
}
a { color: #4A658B; }
a:hover { color: #18345D; }

"""

def main():
    text = HTML.read_text(encoding="utf-8")
    import re

    text, n = re.subn(
        r":root\s*\{[^}]+\}",
        ROOT_NEW,
        text,
        count=1,
    )
    if n != 1:
        raise SystemExit(f":root replace failed ({n})")

    for old, new in REPLACEMENTS:
        text = text.replace(old, new)

    if "EMAAVY BRAND PALETTE" not in text:
        text = text.replace("</style>", BRAND_CSS + "\n</style>", 1)

    HTML.write_text(text, encoding="utf-8")
    print("Brand colors applied.")


if __name__ == "__main__":
    main()
