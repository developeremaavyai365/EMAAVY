from pathlib import Path
text = Path(__file__).resolve().parents[1].joinpath("emaavy_white_blue (2).html").read_text(encoding="utf-8")
# signal-band html
idx = text.find('id="snapshots"')
if idx >= 0:
    Path(__file__).resolve().parent.joinpath("signal_html.txt").write_text(text[idx:idx+5000], encoding="utf-8")
style = text[text.find("<style>"):text.rfind("</style>")]
rules = [c.strip()+ "}" for c in style.split("}") if "signal-" in c]
Path(__file__).resolve().parent.joinpath("signal_rules.txt").write_text("\n\n".join(rules), encoding="utf-8")
print(len(rules), "signal rules")
