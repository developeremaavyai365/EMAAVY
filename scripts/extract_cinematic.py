from pathlib import Path
text = Path(__file__).resolve().parents[1].joinpath("emaavy_white_blue (2).html").read_text(encoding="utf-8")
idx = text.find('id="gallery"')
if idx < 0:
    idx = text.find('h-scroll-section')
end = len(text)
for m in ['<!-- WORKFLOW', 'template-lab', 'id="templates"', '<section id="workflow', '<!-- Template']:
    p = text.find(m, idx + 50)
    if p > idx:
        end = min(end, p)
Path(__file__).resolve().parent.joinpath("cinematic_html.txt").write_text(text[idx:end], encoding="utf-8")
style = text[text.find("<style>"):text.rfind("</style>")]
rules = [c.strip()+ "}" for c in style.split("}") if "h-scroll" in c or "h-card" in c or "cinematic" in c]
Path(__file__).resolve().parent.joinpath("cinematic_rules.txt").write_text("\n\n".join(rules), encoding="utf-8")
print("html", len(text[idx:end]), "rules", len(rules))
