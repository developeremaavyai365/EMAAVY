from pathlib import Path
import re
text = Path(__file__).resolve().parents[1].joinpath("emaavy_white_blue (2).html").read_text(encoding="utf-8")
assert "ELEGANT HERO" in text
assert "hero-glow-layer" not in text.split("<section class=\"hero\"")[1].split("</section>")[0]
hero_start = text.find("ELEGANT HERO")
style_end = text.find("</style>", hero_start)
block = text[hero_start:style_end]
assert "0 0" not in block
print("Hero override OK, no glow in override block")
# check hero html
h = text[text.find('<section class="hero"'):text.find('<section class="hero"')+800]
print("Hero markup snippet:")
print(h[:500])
