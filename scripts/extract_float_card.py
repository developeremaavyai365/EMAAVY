from pathlib import Path
text = Path(__file__).resolve().parents[1].joinpath("emaavy_white_blue (2).html").read_text(encoding="utf-8")
style = text[text.find("<style>"):text.rfind("</style>")]
rules = [c.strip()+ "}" for c in style.split("}") if "float-card" in c or ".btn-fill" in c or ".btn-line" in c or ".btn-magnetic" in c]
Path(__file__).resolve().parent.joinpath("float_card_rules.txt").write_text("\n\n".join(rules), encoding="utf-8")
print(len(rules))
