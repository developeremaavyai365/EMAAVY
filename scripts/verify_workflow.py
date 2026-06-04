from pathlib import Path
text = Path(__file__).resolve().parents[1].joinpath("emaavy_white_blue (2).html").read_text(encoding="utf-8")
assert "ELEGANT WORKFLOW" in text
wf = text.split('id="workflow"')[1].split("<!-- Proof wall")[0]
assert "workflow-glow" not in wf
assert "workflow-node-glow" not in wf
assert "workflow-pulse" not in wf
assert "Autonomous pipeline" in wf
assert "workflow-node-card" in wf
print("Workflow section OK")
