import re
from pathlib import Path
t = Path("index.html").read_text(encoding="utf-8")
i = t.find("hero-command-center")
s = t[i:i+12000]
parts = [
    "hcc-stage", "hcc-ambient", "hcc-grid", "hcc-connections",
    "hcc-core", "hcc-core-body", "hcc-core-mark", "hcc-core-label", "hcc-core-sub",
    "hcc-core-ring", "hcc-core-aura", "hcc-nodes", "hcc-status",
    "data-hcc-status-label", "data-hcc-metric", "hcc-path-flow",
]
for p in parts:
    print(f"{p}: {p in s}")
print("nodes:", s.count("class=\"hcc-node"))
