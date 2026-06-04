from pathlib import Path
import re
text = Path(__file__).resolve().parents[1] / "emaavy_white_blue (2).html"
t = text.read_text(encoding="utf-8")
m = re.search(r'/\* ─── Hero: asymmetric split ─── \*/(.*?)/\* ─── Signal snapshots', t, re.DOTALL)
if m:
    Path(__file__).parent.joinpath("_base_hero_css.txt").write_text(m.group(1), encoding="utf-8")
    print("wrote", len(m.group(1)))
else:
    print("not found")
