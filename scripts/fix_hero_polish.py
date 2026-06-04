"""Fix hero encoding + showcase polish."""
from pathlib import Path
import re

HTML = Path(__file__).resolve().parents[1] / "emaavy_white_blue (2).html"

def main():
    text = HTML.read_text(encoding="utf-8")

    text = re.sub(
        r"every call.\s*<strong>one enterprise",
        "every call—<strong>one enterprise",
        text,
        count=1,
    )
    text = text.replace(
        "create campaign  outbound and inbound",
        "create campaign — outbound and inbound",
    )
    text = text.replace(
        "create campaign \ufffd outbound and inbound",
        "create campaign — outbound and inbound",
    )

    text = text.replace(
        'id="heroVisual" aria-label="EMAAVY platform preview"',
        'id="heroVisual" tabindex="0" aria-label="EMAAVY platform preview"',
        1,
    )
    if 'id="heroShowcaseUrl"' not in text:
        text = text.replace(
            '<span class="hero-showcase-url">app.emaavy.com</span>',
            '<span class="hero-showcase-url" id="heroShowcaseUrl">app.emaavy.com/dashboard</span>',
            1,
        )

    slide_paths = [
        ('class="hero-slide is-active" data-caption="Dashboard"',
         'class="hero-slide is-active" data-caption="Dashboard" data-path="/dashboard"'),
        ('<figure class="hero-slide" data-caption="Campaigns"',
         '<figure class="hero-slide" data-caption="Campaigns" data-path="/campaigns"'),
        ('<figure class="hero-slide" data-caption="AI Agents"',
         '<figure class="hero-slide" data-caption="AI Agents" data-path="/agents"'),
        ('<figure class="hero-slide" data-caption="Integrations"',
         '<figure class="hero-slide" data-caption="Integrations" data-path="/integrations"'),
    ]
    for old, new in slide_paths:
        if old in text:
            text = text.replace(old, new, 1)

    text = text.replace(
        "aspect-ratio: 16 / 9 !important;",
        "aspect-ratio: 16 / 10 !important;\n  min-height: clamp(220px, 42vw, 340px) !important;",
        1,
    )

    HTML.write_text(text, encoding="utf-8")
    print("Hero polish applied.")

if __name__ == "__main__":
    main()
