from pathlib import Path
text = Path(__file__).resolve().parents[1].joinpath("emaavy_white_blue (2).html").read_text(encoding="utf-8")
# find template-related sections
for marker in ['template', 'gallery', 'h-scroll', 'Video', 'video']:
    idx = text.find(marker)
    print(marker, idx)
# extract template section html
for start_marker in ['id="gallery"', 'template-lab', 'id="templates"', 'Video Template', 'video-template']:
    idx = text.find(start_marker)
    if idx >= 0:
        snippet = text[max(0, idx-50):idx+3000]
        Path(__file__).resolve().parent.joinpath(f"seg_{start_marker.replace('=','_').replace('"','')}.txt").write_text(snippet, encoding="utf-8")
        print("wrote", start_marker)

style = text[text.find("<style>"):text.rfind("</style>")]
rules = [c.strip()+ "}" for c in style.split("}") if "template" in c.lower() or "h-scroll" in c or "h-card" in c or "cinematic" in c]
Path(__file__).resolve().parent.joinpath("template_rules.txt").write_text("\n\n".join(rules), encoding="utf-8")
print(len(rules), "rules")
