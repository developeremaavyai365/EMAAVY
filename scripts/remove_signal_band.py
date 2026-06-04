"""Remove Live Processing / signal snapshots segment and clean CSS."""
from pathlib import Path
import re

HTML = Path(__file__).resolve().parents[1] / "emaavy_white_blue (2).html"

SIGNAL_CSS_START = "/* ═══ ELEGANT SIGNAL — refined, no glow ═══ */"
SIGNAL_CSS_END = "/* ═══ HOW IT WORKS — staggered flow + integration panel (EMAAVY) ═══ */"

def main():
    text = HTML.read_text(encoding="utf-8")

    # Remove HTML section
    m = re.search(
        r"<!-- Signal snapshots -->.*?</section>\s*<!-- HOW IT WORKS -->",
        text,
        re.DOTALL,
    )
    if not m:
        m = re.search(
            r'<section[^>]*id="snapshots"[^>]*>.*?</section>\s*<!-- HOW IT WORKS -->',
            text,
            re.DOTALL,
        )
    if not m:
        raise SystemExit("snapshots section not found")
    text = text[: m.start()] + "<!-- HOW IT WORKS -->" + text[m.end() :]
    print("removed snapshots HTML")

    # Remove signal CSS block
    s = text.find(SIGNAL_CSS_START)
    e = text.find(SIGNAL_CSS_END)
    if s >= 0 and e > s:
        text = text[:s] + text[e:]
        print("removed signal CSS block")
    else:
        print("warn: signal CSS markers not found", s, e)

    # Remove signal rules from global disable (line 5 area)
    text = text.replace(".signal-band::before, ", "")
    text = text.replace(".signal-band-title { text-shadow: none !important; }\n", "")
    text = text.replace(".signal-live-badge { animation: none !important; box-shadow: none !important; }\n", "")

    # cap_section.css inline block - remove signal chip hide
    text = text.replace(
        "#signal-snapshots .signal-chip-icon-wrap,\n.signal-band .signal-chip-icon-wrap {\n  display: none !important;\n}\n\n",
        "",
    )

    # Brand overrides
    text = text.replace(
        ".signal-live-badge .signal-dot,\n.hero-showcase-pulse {\n",
        ".hero-showcase-pulse {\n",
    )
    text = text.replace(
        ".platform-stat b,\n.signal-chip-metric strong {\n",
        ".platform-stat b {\n",
    )

    # Global white bg lists
    text = re.sub(r",?\s*\.signal-band", "", text)

    # Hero scroll cue -> features
    text = text.replace('href="#snapshots"', 'href="#features"')
    text = text.replace('href="#snapshots"', 'href="#features"')

    # Rail / nav links to snapshots
    text = text.replace('href="#snapshots"', 'href="#features"')
    text = text.replace('data-label="Powers"', 'data-label="Features"')
    text = re.sub(r'data-nav-section="snapshots"[^>]*>', "", text)

    HTML.write_text(text, encoding="utf-8")
    print("done")


if __name__ == "__main__":
    main()
