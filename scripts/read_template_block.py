from pathlib import Path
text = Path(__file__).resolve().parents[1].joinpath("emaavy_white_blue (2).html").read_text(encoding="utf-8")
start = text.find("ELEGANT TEMPLATE")
end = text.find("</style>", start)
print(text[start:end][-800:])
