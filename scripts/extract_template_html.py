from pathlib import Path
text = Path(__file__).resolve().parents[1].joinpath("emaavy_white_blue (2).html").read_text(encoding="utf-8")
idx = text.find('class="template-lab"')
if idx < 0:
    idx = text.find('template-lab')
end = text.find('<!--', idx + 100)
for m in ['<!-- WORKFLOW', '<section id="workflow', '<section class="workflow', '<!-- INTEGRATIONS']:
    p = text.find(m, idx + 50)
    if p > idx:
        end = min(end, p) if end > idx else p
Path(__file__).resolve().parent.joinpath("template_html.txt").write_text(text[idx:end], encoding="utf-8")
print(len(text[idx:end]))
