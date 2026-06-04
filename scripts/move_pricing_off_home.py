"""Remove pricing from home landing; full pricing on pages/pricing.html; nav links to page."""
from pathlib import Path
import re

ROOT = Path(__file__).resolve().parents[1]
HTML = ROOT / "emaavy_white_blue (2).html"
PRICING_PAGE = ROOT / "pages" / "pricing.html"
SITE_CSS = ROOT / "assets" / "site.css"

PRICING_PAGE_HTML = """<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0" />
  <title>Pricing — EMAAVY</title>
  <meta name="description" content="EMAAVY pricing — Starter, Pro, Business, and Enterprise plans for call intelligence at any scale." />
  <meta name="robots" content="index, follow" />
  <link rel="preconnect" href="https://fonts.googleapis.com" />
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin />
  <link href="https://api.fontshare.com/v2/css?f[]=clash-display@400,500,600,700&f[]=general-sans@300,400,500,600&display=swap" rel="stylesheet" />
  <link rel="stylesheet" href="../assets/nav.css" />
  <link rel="stylesheet" href="../assets/site.css" />
  <link rel="stylesheet" href="../assets/pricing-page.css" />
</head>
<body data-base="../" data-route="pricing">
  <div id="site-nav-root"></div>
  <main class="page-main pricing-page-main">
{pricing_inner}
  </main>
  <div id="site-footer-root"></div>
  <script src="../assets/routes.js"></script>
  <script src="../assets/components.js"></script>
  <script src="../assets/nav.js"></script>
  <script src="../assets/pricing-page.js"></script>
</body>
</html>
"""


def main():
    text = HTML.read_text(encoding="utf-8")
    m = re.search(r"<!-- Pricing -->.*?</section>\s*<!-- FAQ -->", text, re.DOTALL)
    if not m:
        raise SystemExit("pricing section not found")
    pricing_block = m.group(0)
    pricing_inner = re.sub(r"<!-- Pricing -->\s*", "", pricing_block)
    pricing_inner = re.sub(r"\s*<!-- FAQ -->$", "", pricing_inner)

    text = text[: m.start()] + "<!-- FAQ -->" + text[m.end() - len("<!-- FAQ -->") :]

    # Nav: pricing -> pages/pricing.html (no scroll spy on home)
    text = text.replace(
        'href="#pricing" data-nav-section="pricing"',
        'href="pages/pricing.html" data-nav-id="pricing"',
    )
    text = text.replace('href="#pricing" data-index="', 'href="pages/pricing.html" data-index="')
    text = text.replace('href="#pricing" data-label="', 'href="pages/pricing.html" data-label="')
    text = text.replace('<a href="#pricing" style="color:#475569;">Pricing</a>', '<a href="pages/pricing.html" style="color:#475569;">Pricing</a>')

    # Rail / scroll sections — drop pricing
    text = re.sub(
        r"const sections = \[([^\]]*?)'pricing',\s*",
        r"const sections = [\1",
        text,
    )
    text = re.sub(
        r"const navSections = \[([^\]]*?)'pricing',\s*",
        r"const navSections = [\1",
        text,
    )

    HTML.write_text(text, encoding="utf-8")

    inner = pricing_inner.strip()
    if not inner.startswith("<section"):
        inner = f'<section class="pricing-page-wrap">{inner}</section>'
    PRICING_PAGE.write_text(PRICING_PAGE_HTML.format(pricing_inner=inner), encoding="utf-8")

    print("OK: pricing removed from home; pages/pricing.html updated")


if __name__ == "__main__":
    main()
