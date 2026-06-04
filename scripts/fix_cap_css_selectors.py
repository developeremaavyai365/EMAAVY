"""Fix broken comma-expanded #features descendant selectors."""
from pathlib import Path
import re

HTML = Path(__file__).resolve().parents[1] / "emaavy_white_blue (2).html"
IDS = ["features", "agents", "case-studies", "bento", "journey", "docs"]
MARKER = "#features, #agents, #case-studies, #bento, #journey, #docs"


def expand_suffix(suffix: str) -> str:
    """suffix starts with :: or space."""
    if suffix.startswith("::"):
        m = re.match(r"(::[\w-]+)(.*)", suffix, re.DOTALL)
        if not m:
            return suffix
        pseudo, rest = m.group(1), m.group(2)
        return ", ".join(f"#{i}{pseudo}" for i in IDS) + rest
    if suffix.startswith(" "):
        brace = suffix.find("{")
        if brace >= 0:
            sel, rest = suffix[:brace], suffix[brace:]
        else:
            sel, rest = suffix, ""
        return ", ".join(f"#{i}{sel}" for i in IDS) + rest
    return suffix


def fix_line(line: str) -> str:
    if MARKER not in line:
        return line
    out = []
    pos = 0
    while True:
        i = line.find(MARKER, pos)
        if i < 0:
            out.append(line[pos:])
            break
        out.append(line[pos:i])
        after = line[i + len(MARKER) :]
        if after.strip().startswith("{"):
            out.append(MARKER + after)
            break
        out.append(expand_suffix(after))
        pos = i + len(MARKER) + len(after)
        if pos >= len(line):
            break
    return "".join(out)


def main():
    text = HTML.read_text(encoding="utf-8")
    start = text.find("/* ═══ ELEGANT FEATURES — refined shell (HIW cards below) ═══ */")
    end = text.find("/* ═══ ELEGANT TEMPLATE — refined shell, cards preserved ═══ */")
    block = text[start:end]
    lines = block.splitlines(keepends=True)
    fixed = "".join(fix_line(ln) for ln in lines)
    text = text[:start] + fixed + text[end:]

    # Fix animation disable line in head
    bad = (
        "#features, #agents, #case-studies, #bento, #journey, #docs::before, "
        ".template-shell::before"
    )
    good = (
        ", ".join(f"#{i}::before" for i in IDS)
        + ", .template-shell::before"
    )
    text = text.replace(bad, good)

    HTML.write_text(text, encoding="utf-8")
    print("fixed selectors")


if __name__ == "__main__":
    main()
