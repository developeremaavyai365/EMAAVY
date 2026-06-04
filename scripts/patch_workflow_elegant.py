"""Elegant autonomous pipeline section — clean shell; premium step cards."""
import re
from pathlib import Path

WORKFLOW_MARKER = "/* ═══ ELEGANT WORKFLOW — refined shell, premium pipeline ═══ */"

WORKFLOW_OVERRIDE = """
/* ═══ ELEGANT WORKFLOW — refined shell, premium pipeline ═══ */
.workflow-section {
  padding: 0 0 4rem !important;
  scroll-margin-top: 100px !important;
}
.workflow-shell {
  position: relative !important;
  width: min(1200px, calc(100% - 2rem)) !important;
  margin: 0 auto !important;
  padding: 3rem clamp(1.25rem, 4vw, 2.5rem) 2.5rem !important;
  border-radius: 12px !important;
  border: 1px solid #e2e8f0 !important;
  background: #ffffff !important;
  box-shadow: none !important;
  isolation: auto !important;
  overflow: visible !important;
}
.workflow-shell::before,
.workflow-glow,
.workflow-node-glow,
.workflow-node-scanline,
.workflow-pulse {
  display: none !important;
}
.workflow-head {
  position: relative !important;
  z-index: 2 !important;
  text-align: center !important;
  max-width: 680px !important;
  margin: 0 auto 2rem !important;
}
.workflow-head .section-kicker {
  display: inline-flex !important;
  align-items: center !important;
  font-size: 0.68rem !important;
  font-weight: 500 !important;
  letter-spacing: 0.1em !important;
  text-transform: uppercase !important;
  color: #64748b !important;
  background: #f8fafc !important;
  border: 1px solid #e2e8f0 !important;
  border-radius: 6px !important;
  padding: 0.35rem 0.85rem !important;
  margin-bottom: 0.85rem !important;
  box-shadow: none !important;
}
.workflow-head .section-kicker::before {
  display: none !important;
}
.workflow-head h3 {
  font-family: 'Clash Display', sans-serif !important;
  font-size: clamp(1.75rem, 3.5vw, 2.25rem) !important;
  font-weight: 600 !important;
  letter-spacing: -0.02em !important;
  line-height: 1.12 !important;
  color: #0f172a !important;
  text-shadow: none !important;
}
.workflow-head p {
  color: #64748b !important;
  margin-top: 0.5rem !important;
  font-size: 0.95rem !important;
  line-height: 1.65 !important;
}
.workflow-flow {
  position: relative !important;
  z-index: 2 !important;
}
.workflow-track {
  position: absolute !important;
  left: 6% !important;
  right: 6% !important;
  top: calc(100% - 3.4rem) !important;
  height: 1px !important;
  background: #e2e8f0 !important;
  border-radius: 0 !important;
  box-shadow: none !important;
  pointer-events: none !important;
}
.workflow-track::after {
  display: none !important;
}
.workflow-pipeline {
  display: grid !important;
  grid-template-columns: 1fr auto 1fr auto 1fr auto 1fr !important;
  align-items: end !important;
  gap: 0 !important;
  min-height: 320px !important;
  padding-bottom: 2.5rem !important;
}
.workflow-connector {
  position: relative !important;
  width: clamp(28px, 4vw, 56px) !important;
  height: 2px !important;
  align-self: flex-end !important;
  margin-bottom: 3.15rem !important;
  flex-shrink: 0 !important;
}
.workflow-connector::before {
  content: '' !important;
  position: absolute !important;
  inset: 0 !important;
  background: #cbd5e1 !important;
  border-radius: 999px !important;
  box-shadow: none !important;
}
.workflow-connector::after {
  content: '▶' !important;
  position: absolute !important;
  right: -4px !important;
  top: 50% !important;
  transform: translateY(-50%) !important;
  font-size: 0.45rem !important;
  color: #94a3b8 !important;
  text-shadow: none !important;
}
/* Premium step cards — template studio style */
.workflow-node {
  position: relative !important;
  display: flex !important;
  flex-direction: column !important;
  align-items: center !important;
  cursor: pointer !important;
  isolation: isolate !important;
  min-width: 0 !important;
}
.workflow-node-card {
  position: relative !important;
  width: 100% !important;
  border: 2px solid rgba(37, 99, 235, 0.2) !important;
  border-radius: 22px !important;
  background: #0f172a !important;
  padding: 1.15rem 1rem 1rem !important;
  box-shadow: 0 16px 44px rgba(37, 99, 235, 0.12) !important;
  transition: border-color 0.35s ease, box-shadow 0.35s ease !important;
  overflow: hidden !important;
  backdrop-filter: none !important;
}
.workflow-node-card::after {
  content: '' !important;
  position: absolute !important;
  top: 0 !important;
  left: 0 !important;
  right: 0 !important;
  height: 3px !important;
  background: linear-gradient(90deg, #2563eb, #60a5fa, #818cf8) !important;
  opacity: 0.6 !important;
  transition: opacity 0.35s ease !important;
  pointer-events: none !important;
  z-index: 3 !important;
}
.workflow-node:hover .workflow-node-card,
.workflow-node:focus-visible .workflow-node-card {
  border-color: rgba(37, 99, 235, 0.4) !important;
  box-shadow: 0 20px 48px rgba(15, 23, 42, 0.22) !important;
  outline: none !important;
}
.workflow-node:hover .workflow-node-card::after,
.workflow-node:focus-visible .workflow-node-card::after {
  opacity: 1 !important;
}
#workflow .workflow-node-icon {
  position: relative !important;
  z-index: 2 !important;
  width: 40px !important;
  height: 40px !important;
  border-radius: 8px !important;
  display: flex !important;
  align-items: center !important;
  justify-content: center !important;
  font-size: 0 !important;
  background: #1e40af !important;
  border: none !important;
  box-shadow: none !important;
  margin-bottom: 0.75rem !important;
}
#workflow .workflow-node-icon::before {
  font-family: 'Clash Display', sans-serif !important;
  font-weight: 700 !important;
  font-size: 0.68rem !important;
  color: #ffffff !important;
  letter-spacing: 0.02em !important;
}
.workflow-node[data-detail="wf-ingest"] .workflow-node-icon::before { content: 'IN'; }
.workflow-node[data-detail="wf-understand"] .workflow-node-icon::before { content: 'UN'; }
.workflow-node[data-detail="wf-orchestrate"] .workflow-node-icon::before { content: 'OR'; }
.workflow-node[data-detail="wf-optimize"] .workflow-node-icon::before { content: 'OP'; }
.workflow-node-tag {
  position: relative !important;
  z-index: 2 !important;
  display: inline-block !important;
  font-size: 0.58rem !important;
  font-weight: 700 !important;
  letter-spacing: 0.1em !important;
  text-transform: uppercase !important;
  color: #fff !important;
  background: rgba(37, 99, 235, 0.82) !important;
  border: 1px solid rgba(255, 255, 255, 0.28) !important;
  border-radius: 999px !important;
  padding: 0.25rem 0.55rem !important;
  margin-bottom: 0.5rem !important;
  box-shadow: none !important;
}
.workflow-node h4 {
  position: relative !important;
  z-index: 2 !important;
  font-family: 'Clash Display', sans-serif !important;
  font-size: clamp(0.95rem, 1.05vw, 1.08rem) !important;
  font-weight: 600 !important;
  color: #ffffff !important;
  margin-bottom: 0.35rem !important;
  transition: color 0.35s ease !important;
}
.workflow-node:hover h4,
.workflow-node:focus-visible h4 {
  color: #dbeafe !important;
}
.workflow-node p {
  position: relative !important;
  z-index: 2 !important;
  color: rgba(255, 255, 255, 0.82) !important;
  font-size: clamp(0.72rem, 0.8vw, 0.82rem) !important;
  line-height: 1.55 !important;
  margin: 0 !important;
}
.workflow-node-hint {
  position: relative !important;
  z-index: 2 !important;
  display: block !important;
  margin-top: 0.65rem !important;
  font-size: 0.58rem !important;
  font-weight: 600 !important;
  letter-spacing: 0.08em !important;
  text-transform: uppercase !important;
  color: rgba(255, 255, 255, 0.45) !important;
  opacity: 1 !important;
  transition: color 0.35s ease !important;
}
.workflow-node:hover .workflow-node-hint,
.workflow-node:focus-visible .workflow-node-hint {
  color: #93c5fd !important;
}
.workflow-node-anchor {
  position: relative !important;
  display: flex !important;
  flex-direction: column !important;
  align-items: center !important;
  margin-top: 1rem !important;
  z-index: 2 !important;
}
.workflow-node-stem {
  width: 2px !important;
  height: 28px !important;
  background: #cbd5e1 !important;
  box-shadow: none !important;
  border-radius: 999px !important;
}
.workflow-node-dot {
  width: 14px !important;
  height: 14px !important;
  border-radius: 50% !important;
  background: #1e40af !important;
  border: 2px solid #fff !important;
  box-shadow: none !important;
  animation: none !important;
  transition: background 0.2s ease !important;
}
.workflow-node:hover .workflow-node-dot,
.workflow-node:focus-visible .workflow-node-dot {
  box-shadow: none !important;
  border-color: #fff !important;
  background: #1e3a8a !important;
}
.workflow-node-num {
  margin-top: 0.45rem !important;
  font-family: 'Clash Display', sans-serif !important;
  font-size: 0.68rem !important;
  font-weight: 600 !important;
  letter-spacing: 0.1em !important;
  color: #64748b !important;
  text-shadow: none !important;
}
@media (max-width: 1024px) {
  .workflow-pipeline {
    grid-template-columns: 1fr !important;
    gap: 0 !important;
    min-height: 0 !important;
    padding-bottom: 0 !important;
  }
  .workflow-track {
    display: none !important;
  }
  .workflow-connector {
    width: 2px !important;
    height: 36px !important;
    margin: 0 auto !important;
    align-self: center !important;
  }
  .workflow-connector::before {
    background: #cbd5e1 !important;
  }
  .workflow-connector::after {
    content: '▼' !important;
    right: auto !important;
    left: 50% !important;
    top: auto !important;
    bottom: -6px !important;
    transform: translateX(-50%) !important;
    color: #94a3b8 !important;
  }
  .workflow-node:nth-child(n) {
    margin-bottom: 0 !important;
  }
  .workflow-node-anchor {
    margin-top: 0.75rem !important;
  }
  .workflow-node-stem {
    height: 20px !important;
  }
}
@media (max-width: 680px) {
  .workflow-shell {
    padding: 2.5rem 1rem 2rem !important;
    border-radius: 10px !important;
  }
}
"""

SHELL_DECOR = [
    '<div class="workflow-glow workflow-glow-a" aria-hidden="true"></div> ',
    '<div class="workflow-glow workflow-glow-b" aria-hidden="true"></div> ',
]
NODE_FX_RE = re.compile(
    r'<div class="workflow-node-glow" aria-hidden="true"></div>\s*'
    r'<div class="workflow-node-scanline" aria-hidden="true"></div>\s*'
)
PULSE_RE = re.compile(r'<span class="workflow-pulse"></span>')


def main():
    html_path = Path(__file__).resolve().parents[1] / "emaavy_white_blue (2).html"
    text = html_path.read_text(encoding="utf-8")

    if WORKFLOW_MARKER in text:
        start = text.index(WORKFLOW_MARKER)
        end = text.index("</style>", start)
        text = text[:start] + WORKFLOW_OVERRIDE.strip() + "\n" + text[end:]
        print("Updated existing workflow override block")
    else:
        text = text.replace("</style>", WORKFLOW_OVERRIDE + "\n</style>", 1)
        print("Injected workflow override block")

    for chunk in SHELL_DECOR:
        if chunk in text:
            text = text.replace(chunk, "", 1)
            print("Removed shell decor")

    new_text, n = NODE_FX_RE.subn("", text)
    if n:
        print(f"Removed glow FX from {n} workflow nodes")
    text = new_text

    new_text, n2 = PULSE_RE.subn("", text)
    if n2:
        print(f"Removed {n2} workflow-pulse elements")
    text = new_text

    html_path.write_text(text, encoding="utf-8")
    print("Done:", html_path.name)


if __name__ == "__main__":
    main()
