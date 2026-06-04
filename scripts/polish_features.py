from pathlib import Path

p = Path(__file__).resolve().parents[1] / "emaavy_white_blue (2).html"
s = p.read_text(encoding="utf-8")
s = s.replace('header class="features-head"', 'header class="features-head reveal"')
s = s.replace(".feature-card p, .hiw-step p", ".hiw-step p")
s = s.replace("feature-card p, .hiw-step p", ".hiw-step p")
p.write_text(s, encoding="utf-8")
print("ok")
