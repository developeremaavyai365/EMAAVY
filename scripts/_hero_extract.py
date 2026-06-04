from pathlib import Path
t = Path(__file__).resolve().parents[1] / "emaavy_white_blue (2).html"
text = t.read_text(encoding="utf-8")
i = text.find('<section class="hero"')
j = text.find("</section>", i) + len("</section>")
print(text[i:j])
