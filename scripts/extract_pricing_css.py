"""Extract pricing-related CSS rules from home HTML into assets/pricing-page.css"""
from pathlib import Path
import re

ROOT = Path(__file__).resolve().parents[1]
HTML = ROOT / "emaavy_white_blue (2).html"
OUT = ROOT / "assets" / "pricing-page.css"

PREFIXES = (
    ".pricing",
    ".price-card",
    ".pricing-head",
    ".pricing-stage",
    ".pricing-compare",
    ".compare-row",
    ".billing-toggle",
    ".toggle-switch",
    ".save-pill",
    ".pack-",
    ".feat-check",
    ".pricing-page",
)


def main():
    text = HTML.read_text(encoding="utf-8")
    m = re.search(r"<style>(.*?)</style>", text, re.DOTALL)
    if not m:
        raise SystemExit("no style tag")
    css = m.group(1)
    # crude rule split on } then rejoin blocks matching prefixes
    rules = []
    for chunk in css.split("}"):
        chunk = chunk.strip()
        if not chunk:
            continue
        sel = chunk.split("{")[0] if "{" in chunk else ""
        if any(p in sel for p in PREFIXES):
            rules.append(chunk + "}")

    header = "/* Pricing page — extracted from home stylesheet */\n"
    body = """
.pricing-page-main {
  padding-top: calc(var(--masthead-h, 88px) + 2rem);
  padding-bottom: 4rem;
  background: #fff;
}
.pricing-page-main .pricing {
  max-width: 1200px;
  margin: 0 auto;
  padding: 0 1.5rem 3rem;
}
"""
    OUT.write_text(header + body + "\n".join(rules), encoding="utf-8")
    print("wrote", OUT, "rules", len(rules))


if __name__ == "__main__":
    main()
