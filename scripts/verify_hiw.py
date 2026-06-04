from pathlib import Path
text = Path(__file__).resolve().parents[1].joinpath("emaavy_white_blue (2).html").read_text(encoding="utf-8")
assert "ELEGANT HIW" in text
hiw = text.split('id="how-it-works"')[1].split("<!-- FEATURES -->")[0]
assert "hiw-glow" not in hiw
assert "hiw-step-glow" not in hiw
print("HIW section OK")
print(hiw[:900])
