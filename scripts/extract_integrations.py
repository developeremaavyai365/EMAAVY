from pathlib import Path
text = Path(__file__).resolve().parents[1].joinpath("emaavy_white_blue (2).html").read_text(encoding="utf-8")
idx = text.find('id="integrations"')
if idx < 0:
    idx = text.find('int-showcase')
end = len(text)
for m in ['<!-- PRICING', 'id="pricing"', '<!-- AGENTS', 'id="agents"', '<!-- WORKFLOW', 'proof-wall', 'id="proof"']:
    p = text.find(m, idx + 50 if idx >= 0 else 0)
    if idx >= 0 and p > idx:
        end = min(end, p)
if idx >= 0:
    Path(__file__).resolve().parent.joinpath("integrations_html.txt").write_text(text[idx:idx+8000], encoding="utf-8")
style = text[text.find("<style>"):text.rfind("</style>")]
rules = [c.strip()+ "}" for c in style.split("}") if c.strip().startswith(".int-") or "#integrations" in c or ".int-" in c[:80]]
# broader
rules = [c.strip()+ "}" for c in style.split("}") if ".int-" in c or "#integrations" in c]
Path(__file__).resolve().parent.joinpath("integrations_rules.txt").write_text("\n\n".join(rules[:80]), encoding="utf-8")
print("idx", idx, "rules", len(rules))
