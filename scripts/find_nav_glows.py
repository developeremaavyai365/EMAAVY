from pathlib import Path
import re
text = Path(__file__).resolve().parents[1] / "emaavy_white_blue (2).html"
text = text.read_text(encoding="utf-8")
patterns = [
    "Enterprise Professional",
    "nav-dropdown-menu-glow",
    "premium-overhaul",
    ".masthead-beam",
    "nav-dropdown-split",
    "masthead.compact",
    "NAVBAR",
]
for p in patterns:
    idx = text.find(p)
    print(f"\n=== {p} @ {idx} ===")
    if idx >= 0:
        snippet = text[max(0, idx-100):idx+800]
        Path(__file__).resolve().parent / f"snippet_{p.replace(' ','_').replace('.','')}.txt"
        out = Path(__file__).resolve().parent / f"snippet_{re.sub(r'[^a-zA-Z0-9]', '_', p)}.txt"
        out.write_text(snippet, encoding="utf-8")
        print(f"  wrote {len(snippet)} chars")

# find all glow box-shadow in style
style_start = text.find("<style>")
style_end = text.rfind("</style>")
style = text[style_start:style_end]
glows = re.findall(r'[^}]{0,200}0 0 \d+px[^}]{0,200}', style)
Path(__file__).resolve().parent / "glow_rules.txt"
Path(__file__).resolve().parent.joinpath("glow_rules.txt").write_text("\n---\n".join(glows[:40]), encoding="utf-8")
print(f"\nFound {len(glows)} glow rules in style")
