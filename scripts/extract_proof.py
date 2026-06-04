from pathlib import Path
text = Path(__file__).resolve().parents[1].joinpath("emaavy_white_blue (2).html").read_text(encoding="utf-8")
idx = text.find('id="proof"')
if idx < 0:
    idx = text.find('Powered by the best')
end = text.find('<!--', idx + 50)
for m in ['<!-- PRICING', '<section id="pricing', '<!-- INTEGRATIONS', '<section id="integrations', '<!-- CTA', '<section class="int-']:
    p = text.find(m, idx + 50)
    if p > idx:
        end = min(end, p) if end > idx else p
Path(__file__).resolve().parent.joinpath("proof_html.txt").write_text(text[idx:end], encoding="utf-8")
style = text[text.find("<style>"):text.rfind("</style>")]
rules = [c.strip()+ "}" for c in style.split("}") if "platform-" in c or "proof-wall" in c]
Path(__file__).resolve().parent.joinpath("platform_rules.txt").write_text("\n\n".join(rules), encoding="utf-8")
print("html len", len(text[idx:end]), "rules", len(rules))
