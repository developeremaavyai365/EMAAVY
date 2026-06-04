from pathlib import Path
t = Path(__file__).resolve().parents[1] / "emaavy_white_blue (2).html"
text = t.read_text(encoding="utf-8")
i = text.find(".masthead-nav {")
Path(__file__).resolve().parents[1] / "scripts" / "nav_snippet.txt"
out = Path(__file__).resolve().parent / "nav_snippet.txt"
out.write_text(text[i:i+3500], encoding="utf-8")
print("written", len(out.read_text()))
