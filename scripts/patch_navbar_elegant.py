"""Inject elegant navbar CSS override into main HTML."""
from pathlib import Path

NAV_OVERRIDE = """
/* ═══ ELEGANT NAVBAR — refined, no glow ═══ */
.masthead-beam {
  background: rgba(255, 255, 255, 0.97) !important;
  border-bottom: 1px solid #e2e8f0 !important;
  backdrop-filter: blur(12px) !important;
  box-shadow: none !important;
}
.masthead.compact .masthead-beam {
  box-shadow: 0 1px 3px rgba(15, 23, 42, 0.06) !important;
  border-bottom-color: #e2e8f0 !important;
}
.masthead-nav {
  background: transparent !important;
  border: none !important;
  box-shadow: none !important;
  gap: 0.15rem !important;
  padding: 0 !important;
}
.masthead-nav:has(a:hover),
.masthead-nav:has(.nav-dropdown:hover),
.masthead-nav:has(.nav-dropdown-caret:hover),
.masthead-nav:has(.nav-dropdown-trigger:hover) {
  border-color: transparent !important;
  box-shadow: none !important;
}
.masthead-nav a,
.masthead-nav .nav-dropdown-trigger,
.masthead-nav .nav-integrations-link,
.masthead-nav .nav-dropdown-caret {
  font-weight: 500 !important;
  color: #475569 !important;
  letter-spacing: 0.02em !important;
  padding: 0.45rem 0.75rem !important;
  border-radius: 6px !important;
  background: transparent !important;
  box-shadow: none !important;
  transform: none !important;
}
.masthead-nav a:hover,
.masthead-nav .nav-dropdown-trigger:hover,
.masthead-nav .nav-integrations-link:hover,
.masthead-nav .nav-dropdown-caret:hover,
.masthead-nav a.active:hover {
  color: #0f172a !important;
  background: #f1f5f9 !important;
  box-shadow: none !important;
}
.masthead-nav a.active {
  color: #1e40af !important;
  background: #eff6ff !important;
  box-shadow: none !important;
}
.nav-dropdown.open .nav-dropdown-split,
.nav-dropdown:hover .nav-dropdown-split {
  background: transparent !important;
  box-shadow: none !important;
}
.nav-dropdown-split:hover .nav-integrations-link,
.nav-dropdown.open .nav-dropdown-split .nav-integrations-link,
.nav-dropdown-split:hover .nav-dropdown-caret,
.nav-dropdown.open .nav-dropdown-split .nav-dropdown-caret {
  color: #0f172a !important;
  background: #f1f5f9 !important;
  box-shadow: none !important;
}
.nav-dropdown.open .nav-integrations-link,
.nav-dropdown:hover .nav-integrations-link,
.nav-integrations-link.active {
  color: #1e40af !important;
  background: #eff6ff !important;
  box-shadow: none !important;
}
.masthead-login {
  color: #475569 !important;
  font-weight: 500 !important;
  padding: 0.45rem 0.85rem !important;
  border-radius: 6px !important;
  border: 1px solid transparent !important;
  background: transparent !important;
}
.masthead-login:hover {
  color: #0f172a !important;
  background: #f8fafc !important;
  border-color: #e2e8f0 !important;
  box-shadow: none !important;
}
.masthead-go {
  background: #1e40af !important;
  color: #fff !important;
  border-radius: 6px !important;
  font-weight: 600 !important;
  box-shadow: none !important;
  animation: none !important;
}
.masthead-go:hover {
  background: #1e3a8a !important;
  box-shadow: none !important;
}
.nav-dropdown-menu {
  background: #ffffff !important;
  border: 1px solid #e2e8f0 !important;
  border-radius: 10px !important;
  box-shadow: 0 8px 24px rgba(15, 23, 42, 0.08) !important;
}
.nav-dropdown.open .nav-dropdown-menu.is-visible,
.nav-dropdown-menu.is-visible {
  border-color: #e2e8f0 !important;
  box-shadow: 0 12px 32px rgba(15, 23, 42, 0.1) !important;
}
.nav-dropdown-menu-kicker {
  background: #f8fafc !important;
  border: 1px solid #e2e8f0 !important;
  color: #64748b !important;
  box-shadow: none !important;
}
.dropdown-section {
  border: 1px solid #e2e8f0 !important;
  box-shadow: none !important;
}
.dropdown-section:hover {
  box-shadow: none !important;
  border-color: #cbd5e1 !important;
}
.nav-dropdown-menu .dropdown-section a:hover {
  color: #1e40af !important;
  background: #eff6ff !important;
  box-shadow: none !important;
}
.site-header {
  background: rgba(255, 255, 255, 0.97) !important;
  border-bottom: 1px solid #e2e8f0 !important;
  box-shadow: none !important;
}
.site-header.scrolled {
  box-shadow: 0 1px 3px rgba(15, 23, 42, 0.06) !important;
}
.site-nav {
  background: transparent !important;
  border: none !important;
  box-shadow: none !important;
  padding: 0 !important;
  gap: 0.15rem !important;
}
.site-nav:has(a:hover),
.site-nav:has(.nav-dropdown:hover),
.site-nav:has(.nav-dropdown-trigger:hover),
.site-nav:has(.nav-dropdown-caret:hover) {
  box-shadow: none !important;
  border-color: transparent !important;
}
.site-nav a,
.site-nav .nav-dropdown-trigger,
.site-nav .nav-integrations-link,
.site-nav .nav-dropdown-caret {
  font-weight: 500 !important;
  color: #475569 !important;
  box-shadow: none !important;
}
.site-nav a:hover,
.site-nav .nav-dropdown-trigger:hover,
.site-nav .nav-integrations-link:hover,
.site-nav .nav-dropdown-caret:hover,
.site-nav a.active:hover,
.site-nav .nav-dropdown-trigger.active:hover {
  color: #0f172a !important;
  background: #f1f5f9 !important;
  box-shadow: none !important;
}
.site-nav a.active,
.site-nav .nav-dropdown-trigger.active {
  color: #1e40af !important;
  background: #eff6ff !important;
  box-shadow: none !important;
}
.btn-nav-login {
  border: 1px solid #e2e8f0 !important;
  border-radius: 6px !important;
  font-weight: 500 !important;
  color: #475569 !important;
  box-shadow: none !important;
}
.btn-nav-login:hover {
  border-color: #cbd5e1 !important;
  color: #0f172a !important;
  background: #f8fafc !important;
  box-shadow: none !important;
}
.btn-nav-demo {
  background: #1e40af !important;
  border-radius: 6px !important;
  box-shadow: none !important;
  animation: none !important;
}
.btn-nav-demo:hover {
  background: #1e3a8a !important;
  box-shadow: none !important;
}
"""

MARKER = "/* ═══ ELEGANT NAVBAR — refined, no glow ═══ */"

def main():
    html_path = Path(__file__).resolve().parents[1] / "emaavy_white_blue (2).html"
    text = html_path.read_text(encoding="utf-8")

    if MARKER in text:
        start = text.index(MARKER)
        end = text.index("</style>", start)
        text = text[:start] + NAV_OVERRIDE.strip() + "\n" + text[end:]
        print("Updated existing navbar override block")
    else:
        text = text.replace("</style>", NAV_OVERRIDE + "\n</style>", 1)
        print("Injected navbar override block")

    html_path.write_text(text, encoding="utf-8")
    print("Done:", html_path.name)

if __name__ == "__main__":
    main()
