from pathlib import Path
import re
text = Path(__file__).resolve().parents[1].joinpath("emaavy_white_blue (2).html").read_text(encoding="utf-8")
wf = text.split('id="workflow"')[1].split("<!-- Proof wall")[0]
for m in re.finditer(r'Step 0\d|workflow-node-num|>0[1-4]<', wf):
    start = max(0, m.start()-30)
    print(repr(wf[start:m.end()+20]))
