"""Extract documentation-section CSS from home HTML into assets/docs-page.css"""
from pathlib import Path
import re

ROOT = Path(__file__).resolve().parents[1]
HTML = ROOT / "emaavy_white_blue (2).html"
OUT = ROOT / "assets" / "docs-page.css"

PREFIXES = (
    ".cap-section",
    "#docs",
    ".features-head",
    ".section-kicker",
    ".hiw-steps",
    ".hiw-step",
    ".hiw-step-num",
    ".hiw-step-tag",
    ".hiw-step-hint",
    ".platform-stats",
    ".platform-stat",
    ".docs-page",
    ".bento-label",
)


def main():
    text = HTML.read_text(encoding="utf-8")
    m = re.search(r"<style>(.*?)</style>", text, re.DOTALL)
    if not m:
        raise SystemExit("no style tag")
    css = m.group(1)
    rules = []
    for chunk in css.split("}"):
        chunk = chunk.strip()
        if not chunk or "{" not in chunk:
            continue
        sel = chunk.split("{")[0]
        if any(p in sel for p in PREFIXES):
            rules.append(chunk + "}")

    header = """/* Documentation page — extracted from home stylesheet */
:root {
  --void: #ffffff;
  --ink: #f8fafc;
  --panel: #f1f5f9;
  --ice: #1e3a5f;
  --bolt: #1e40af;
  --deep: #0f172a;
  --violet: #334155;
  --dim: #64748b;
  --border: #e2e8f0;
  --glass: rgba(255, 255, 255, 0.92);
}

.docs-page-main {
  padding-top: calc(var(--masthead-h, 88px) + 2rem);
  padding-bottom: 4rem;
  background: #fff;
}
.docs-page-main .cap-section {
  max-width: 1200px;
  margin: 0 auto;
  padding: 0 1.5rem 3rem;
}
"""
    OUT.write_text(header + "\n".join(rules), encoding="utf-8")
    print("wrote", OUT, "rules", len(rules))


if __name__ == "__main__":
    main()
