"""Remove 01-04 step numbers from autonomous pipeline section."""
import re
from pathlib import Path

html_path = Path(__file__).resolve().parents[1] / "emaavy_white_blue (2).html"
text = html_path.read_text(encoding="utf-8")

# Remove Step 01-04 tags and anchor numbers from markup
text, n1 = re.subn(
    r'<span class="workflow-node-tag">Step 0[1-4]</span>\s*',
    "",
    text,
)
text, n2 = re.subn(
    r'<span class="workflow-node-num">0[1-4]</span>\s*',
    "",
    text,
)

# Ensure CSS hides any remaining instances
hide_rule = """
.workflow-node-num,
.workflow-node-tag {
  display: none !important;
}
"""
marker = "/* ═══ ELEGANT WORKFLOW — refined shell, premium pipeline ═══ */"
if hide_rule.strip() not in text and marker in text:
    insert_at = text.find(".workflow-node-anchor {", text.find(marker))
    if insert_at > 0:
        text = text[:insert_at] + hide_rule + text[insert_at:]

html_path.write_text(text, encoding="utf-8")
print(f"Removed {n1} step tags, {n2} anchor numbers")
