"""HD showcase: new header, sharp images, smooth crossfade."""
from pathlib import Path
import re

HTML = Path(__file__).resolve().parents[1] / "emaavy_white_blue (2).html"

OLD_CHROME = (
    '<div class="hero-showcase-chrome"> <span class="hero-showcase-dot" aria-hidden="true"></span>'
    '<span class="hero-showcase-dot" aria-hidden="true"></span><span class="hero-showcase-dot" aria-hidden="true"></span> '
    '<span class="hero-showcase-live-badge" id="heroShowcaseLive"><span class="hero-showcase-pulse" aria-hidden="true"></span>Live preview</span> '
    '<span class="hero-showcase-url" id="heroShowcaseUrl">app.emaavy.com/dashboard</span> </div>'
)

NEW_CHROME = (
    '<div class="hero-showcase-header"> '
    '<div class="hero-showcase-header-brand"><span class="hero-showcase-gem" aria-hidden="true"></span>'
    '<span class="hero-showcase-header-label">EMAAVY Cloud</span></div> '
    '<span class="hero-showcase-live-badge" id="heroShowcaseLive">'
    '<span class="hero-showcase-eq" aria-hidden="true"><i></i><i></i><i></i><i></i><i></i></span>'
    '<span class="hero-showcase-live-text">Live preview</span></span> '
    '<span class="hero-showcase-url" id="heroShowcaseUrl">app.emaavy.com/dashboard</span> </div>'
)

IMG_ATTRS = {
    "dashboard.png": 'width="1024" height="487" sizes="(min-width:1200px) 620px, 90vw" srcset="assets/hero/dashboard.png 1024w"',
    "campaigns.png": 'width="1024" height="566" sizes="(min-width:1200px) 620px, 90vw" srcset="assets/hero/campaigns.png 1024w"',
    "agents.png": 'width="1024" height="577" sizes="(min-width:1200px) 620px, 90vw" srcset="assets/hero/agents.png 1024w"',
    "integrations.png": 'width="1024" height="573" sizes="(min-width:1200px) 620px, 90vw" srcset="assets/hero/integrations.png 1024w"',
}

def main():
    text = HTML.read_text(encoding="utf-8")
    if OLD_CHROME not in text:
        raise SystemExit("chrome block not found")
    text = text.replace(OLD_CHROME, NEW_CHROME, 1)

    for fname, attrs in IMG_ATTRS.items():
        text = text.replace(f'src="assets/hero/{fname}"', f'src="assets/hero/{fname}" {attrs}', 1)

    HTML.write_text(text, encoding="utf-8")
    print("HTML patched.")


if __name__ == "__main__":
    main()
