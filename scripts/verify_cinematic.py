from pathlib import Path
text = Path(__file__).resolve().parents[1].joinpath("emaavy_white_blue (2).html").read_text(encoding="utf-8")
assert "ELEGANT CINEMATIC" in text
gal = text.split('id="gallery"')[1].split("<!-- Video templates -->")[0]
assert "cinematic-glow" not in gal
assert "h-card-glow" not in gal
assert "h-card-media" in gal
assert "Cinematic product moments" in gal
print("Cinematic section OK")
