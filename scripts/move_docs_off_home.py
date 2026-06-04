"""Remove documentation from home landing; full docs on pages/documentation.html."""
from pathlib import Path
import re

ROOT = Path(__file__).resolve().parents[1]
HTML = ROOT / "emaavy_white_blue (2).html"
DOCS_PAGE = ROOT / "pages" / "documentation.html"

DOCS_PAGE_HTML = """<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0" />
  <title>Documentation — EMAAVY</title>
  <meta name="description" content="EMAAVY docs — quickstart guides, API reference, and agent builder documentation." />
  <meta name="robots" content="index, follow" />
  <meta property="og:title" content="Documentation — EMAAVY" />
  <meta property="og:description" content="EMAAVY docs — quickstart guides, API reference, and agent builder documentation." />
  <meta property="og:type" content="website" />
  <link rel="preconnect" href="https://fonts.googleapis.com" />
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin />
  <link href="https://api.fontshare.com/v2/css?f[]=clash-display@400,500,600,700&f[]=general-sans@300,400,500,600&display=swap" rel="stylesheet" />
  <link rel="stylesheet" href="../assets/nav.css" />
  <link rel="stylesheet" href="../assets/site.css" />
  <link rel="stylesheet" href="../assets/docs-page.css" />
  <style>
    .reveal {{ opacity: 0; transform: translateY(24px); transition: opacity 0.7s ease, transform 0.7s ease; }}
    .reveal.in {{ opacity: 1; transform: none; }}
  </style>
</head>
<body data-base="../" data-route="documentation">
  <div id="site-nav-root"></div>
  <main class="page-main docs-page-main">
{docs_inner}
  </main>
  <div id="site-footer-root"></div>
  <script src="../assets/routes.js"></script>
  <script src="../assets/components.js"></script>
  <script src="../assets/nav.js"></script>
  <script src="../assets/docs-page.js"></script>
</body>
</html>
"""


def main():
    text = HTML.read_text(encoding="utf-8")
    m = re.search(
        r"<!-- DOCS -->.*?</section>\s*<!-- BOOK A DEMO -->",
        text,
        re.DOTALL,
    )
    if not m:
        raise SystemExit("docs section not found")

    docs_inner = re.sub(r"<!-- DOCS -->\s*", "", m.group(0))
    docs_inner = re.sub(r"\s*<!-- BOOK A DEMO -->$", "", docs_inner).strip()

    text = text[: m.start()] + "<!-- BOOK A DEMO -->" + text[m.end() - len("<!-- BOOK A DEMO -->") :]

    replacements = [
        (
            'href="#docs" data-nav-section="docs"',
            'href="pages/documentation.html" data-nav-id="documentation"',
        ),
        ('href="#docs" data-index="', 'href="pages/documentation.html" data-index="'),
        ('href="#docs" data-label="', 'href="pages/documentation.html" data-label="'),
        (
            '<a href="#docs" style="color:#475569;">Documentation</a>',
            '<a href="pages/documentation.html" style="color:#475569;">Documentation</a>',
        ),
    ]
    for old, new in replacements:
        text = text.replace(old, new)

    text = re.sub(r"'docs',\s*", "", text)

    HTML.write_text(text, encoding="utf-8")
    DOCS_PAGE.write_text(DOCS_PAGE_HTML.format(docs_inner=docs_inner), encoding="utf-8")
    print("OK: docs removed from home; pages/documentation.html updated")


if __name__ == "__main__":
    main()
