from pathlib import Path
text = Path(__file__).resolve().parents[1].joinpath("emaavy_white_blue (2).html").read_text(encoding="utf-8")
assert "ELEGANT TEMPLATE" in text
tpl = text.split('id="templates"')[1].split("</section>")[0]
assert "template-glow" not in tpl
assert "template-spark" not in tpl
assert "template-orbit-ring" not in tpl
assert "template-card-glow" not in tpl
assert "template-thumb" in tpl
assert "template-card-frame" in tpl
assert "video muted" in tpl
print("Template section OK — cards preserved")
