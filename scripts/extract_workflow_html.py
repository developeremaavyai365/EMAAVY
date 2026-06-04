from pathlib import Path
text = Path(__file__).resolve().parents[1].joinpath("emaavy_white_blue (2).html").read_text(encoding="utf-8")
idx = text.find('id="workflow"')
end = text.find('<!-- Proof wall', idx)
Path(__file__).resolve().parent.joinpath("workflow_html.txt").write_text(text[idx:end], encoding="utf-8")
print(len(text[idx:end]))
