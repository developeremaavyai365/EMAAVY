"""Fix duplicate FAQ comment and remove orphaned pricing JS from home."""
from pathlib import Path
import re

ROOT = Path(__file__).resolve().parents[1]
HTML = ROOT / "emaavy_white_blue (2).html"


def main():
    text = HTML.read_text(encoding="utf-8")
    text = text.replace("<!-- FAQ --><!-- FAQ -->", "<!-- FAQ -->")

    # Remove billing + price-card blocks when toggle is absent (guard for safety)
    billing_block = re.compile(
        r"/\* Billing toggle \*/ const billingToggle = document\.getElementById\('billingToggle'\);.*?updatePrices\(\); \}\); ",
        re.DOTALL,
    )
    text2, n1 = billing_block.subn("", text)

    price_reveal = re.compile(
        r"document\.querySelectorAll\('\.price-card\.reveal'\)\.forEach\(\(card\) => \{ new IntersectionObserver\(\(\[e\]\) => \{ if \(e\.isIntersecting\) card\.classList\.add\('in'\); \}, \{ threshold: 0\.2 \}\)\.observe\(card\); \}\); ",
    )
    text2, n2 = price_reveal.subn("", text2)

    price_tilt = re.compile(
        r"/\* Price card 3D tilt \*/ document\.querySelectorAll\('\.price-card'\)\.forEach\(\(card\) => \{.*?if \(featuredCard\) \{.*?\} ",
        re.DOTALL,
    )
    text2, n3 = price_tilt.subn("", text2)

    # sections / navSections: drop pricing if still present
    text2 = re.sub(r"'pricing',\s*", "", text2)

    # Rail Plans dot -> dedicated page (full navigation)
    text2 = text2.replace(
        '<a href="#pricing" data-label="Plans"></a>',
        '<a href="pages/pricing.html" data-label="Plans"></a>',
    )

    HTML.write_text(text2, encoding="utf-8")
    print("FAQ dup fixed; billing removed:", n1, "reveal:", n2, "tilt:", n3)


if __name__ == "__main__":
    main()
