from pathlib import Path
text = Path(__file__).resolve().parents[1].joinpath("emaavy_white_blue (2).html").read_text(encoding="utf-8")
for marker in ['autonomous', 'Autonomous', 'pipeline', 'workflow-shell', 'id="workflow"']:
    idx = text.find(marker)
    print(marker, idx)
# extract section
for start in ['Autonomous', 'autonomous', 'id="workflow"', 'workflow-shell']:
    idx = text.find(start)
    if idx > 0:
        snippet = text[max(0, idx-80):idx+4000]
        safe = start.replace('"','').replace('=','_')
        Path(__file__).resolve().parent.joinpath(f"pipe_{safe}.txt").write_text(snippet, encoding="utf-8")
style = text[text.find("<style>"):text.rfind("</style>")]
rules = [c.strip()+ "}" for c in style.split("}") if "workflow" in c.lower() or "pipeline" in c.lower()]
Path(__file__).resolve().parent.joinpath("workflow_rules.txt").write_text("\n\n".join(rules), encoding="utf-8")
print(len(rules), "rules")
