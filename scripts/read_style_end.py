from pathlib import Path
text = Path(__file__).resolve().parents[1].joinpath("emaavy_white_blue (2).html").read_text(encoding="utf-8")
style_end = text.rfind("</style>")
print(text[style_end-4000:style_end])
