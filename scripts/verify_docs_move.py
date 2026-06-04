from pathlib import Path

t = Path(__file__).resolve().parents[1] / "emaavy_white_blue (2).html"
text = t.read_text(encoding="utf-8")
assert "<!-- DOCS -->" not in text
assert 'href="#docs"' not in text
assert text.count("pages/documentation.html") >= 3
assert "'docs'," not in text.split("navSections")[1].split(";")[0]
print("OK")
