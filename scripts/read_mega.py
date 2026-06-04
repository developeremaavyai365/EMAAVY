from pathlib import Path
s = (Path(__file__).resolve().parents[1] / "emaavy_white_blue (2).html").read_text(encoding="utf-8")
i = s.find('id="integrationsMenu"')
print(s[i : i + 2500])
