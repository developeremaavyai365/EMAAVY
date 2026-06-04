from pathlib import Path
text = Path(__file__).resolve().parents[1].joinpath("emaavy_white_blue (2).html").read_text(encoding="utf-8")
marker = text.find("ELEGANT NAVBAR")
style_end = text.find("</style>", marker)
print("Override starts:", marker)
print("Style ends:", style_end)
print("Override length:", style_end - marker)
# show context around last masthead-go:hover
idx = text.rfind("masthead-go:hover")
print("\nContext at last masthead-go:hover:")
print(text[idx-80:idx+120])
