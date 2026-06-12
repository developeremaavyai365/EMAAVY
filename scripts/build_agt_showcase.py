#!/usr/bin/env python3
"""Replace agents section with premium template showcase in index.html."""
from __future__ import annotations

import math
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
INDEX = ROOT / "index.html"

import sys
sys.path.insert(0, str(Path(__file__).resolve().parent))
from agent_templates import TEMPLATES  # noqa: E402



def orbit_position(index: int, total: int, radius: float = 38.0) -> tuple[float, float]:
    angle = math.radians(-90 + index * (360 / total))
    x = 50 + radius * math.cos(angle)
    y = 50 + radius * math.sin(angle)
    return round(x, 2), round(y, 2)


def svg_point(x_pct: float, y_pct: float) -> tuple[int, int]:
    return int(x_pct * 6), int(y_pct * 6)


def build_paths() -> str:
    lines = []
    flow_mods = ["", " int-sc-path-flow--b", " int-sc-path-flow--c", " int-sc-path-flow--d",
                 " int-sc-path-flow--e", " int-sc-path-flow--f", " int-sc-path-flow--g",
                 " int-sc-path-flow--h", " int-sc-path-flow--i", " int-sc-path-flow--j",
                 " int-sc-path-flow--k", " int-sc-path-flow--l", " int-sc-path-flow--m"]
    for i, t in enumerate(TEMPLATES):
        x, y = orbit_position(i, len(TEMPLATES))
        sx, sy = svg_point(x, y)
        cx, cy = 300, 300
        qx = (cx + sx) // 2
        qy = (cy + sy) // 2
        d = f"M{cx} {cy} Q{qx} {qy} {sx} {sy}"
        fid = t["id"]
        mod = flow_mods[i] if i < len(flow_mods) else ""
        lines.append(f'                <path class="agt-sc-path-soft" data-agt-link="{fid}" d="{d}"/>')
        lines.append(f'                <path class="agt-sc-path" data-agt-link="{fid}" d="{d}"/>')
        lines.append(f'                <path class="agt-sc-path-flow{mod}" data-agt-link="{fid}" d="{d}"/>')
    return "\n".join(lines)


def build_nodes() -> str:
    cards = []
    for i, t in enumerate(TEMPLATES):
        x, y = orbit_position(i, len(TEMPLATES))
        active = " is-active" if i == 0 else ""
        cards.append(f'''                <article class="agt-sc-node agt-sc-node--{t["id"]}{active}" data-step="{t["id"]}" style="--agt-x: {x}%; --agt-y: {y}%;">
                  <div class="agt-sc-node-card">
                    <span class="agt-sc-node-icon" aria-hidden="true">{t["icon"]}</span>
                    <span class="agt-sc-node-title">{t["title"].split("(")[0].strip()[:18]}</span>
                  </div>
                </article>''')
    return "\n".join(cards)


def build_layer_cards() -> str:
    variants = ["a", "b", "c", "d", "e", "a", "b", "c", "d", "e", "a", "b", "c", "d"]
    items = []
    for i, t in enumerate(TEMPLATES):
        v = variants[i % len(variants)]
        num = f"{i + 1:02d}"
        items.append(f'''          <li class="agt-layer-card agt-layer-card--{v} reveal" data-detail="agt-{t["id"]}" tabindex="0">
            <span class="agt-layer-card-icon" aria-hidden="true">{t["icon"]}</span>
            <div class="agt-layer-card-body">
              <span class="agt-layer-card-kicker">Template {num} · {t["duration"]}</span>
              <h3>{t["title"]}</h3>
              <p>{t["short"]}</p>
            </div>
            <span class="agt-layer-card-mode">{t["mode"]}</span>
          </li>''')
    return "\n".join(items)


def build_slides() -> str:
    slides = []
    for i, t in enumerate(TEMPLATES):
        num = f"{i + 1:02d}"
        points = "".join(f"\n                  <li>{p}</li>" for p in t["points"])
        outcomes = "".join(f'\n                  <span class="agt-sc-slide-outcome">{o}</span>' for o in t["outcomes"])
        usecases = "".join(f"\n                    <li>{u}</li>" for u in t["usecases"])
        flow = "".join(
            f'\n                    <span class="agt-vis-flow-step{" is-live" if j == 0 else ""}">{s}</span>'
            for j, s in enumerate(t["flow"])
        )
        slides.append(f'''              <article class="agt-sc-slide" data-slide="{t["id"]}" role="tabpanel" aria-hidden="true">
                <span class="agt-sc-slide-kicker">{num} — {t["category"]} · {t["mode"]}</span>
                <h3 class="agt-sc-slide-headline">{t["title"]}</h3>
                <p class="agt-sc-slide-desc">{t["desc"]}</p>
                <p class="agt-sc-slide-detail">{t["detail"]}</p>
                <div class="agt-sc-slide-visual">
                  <div class="agt-vis-template">
                    <span class="agt-vis-template-icon" aria-hidden="true">{t["icon"]}</span>
                    <div class="agt-vis-flow">{flow}
                    </div>
                    <span class="agt-vis-template-duration">{t["duration"]} template</span>
                  </div>
                </div>
                <ul class="agt-sc-slide-points">{points}
                </ul>
                <div class="agt-sc-slide-outcomes">{outcomes}
                </div>
                <div class="agt-sc-slide-usecases">
                  <span class="agt-sc-slide-usecases-label">Ideal for</span>
                  <ul class="agt-sc-slide-usecase-list">{usecases}
                  </ul>
                </div>
              </article>''')
    return "\n".join(slides)


def build_split_html() -> str:
    return f'''    <div class="agt-split reveal">
      <div class="agt-templates-col" aria-label="Agent templates">
        <p class="agt-templates-head">Start from a template</p>
        <p class="agt-templates-sub">Pick a template to pre-fill your agent. Customize everything after launch.</p>
        <ol class="agt-layer-steps">
{build_layer_cards()}
        </ol>
      </div>
      <div class="agt-showcase-col">
        <div class="agt-showcase" id="agtShowcase" tabindex="0" aria-label="EMAAVY agent template fleet — live preview" aria-live="polite">
          <div class="agt-sc-stage">
            <div class="agt-sc-fleet">
              <div class="agt-sc-ambient" aria-hidden="true"></div>
              <div class="agt-sc-grid" aria-hidden="true"></div>
              <svg class="agt-sc-paths" viewBox="0 0 600 600" aria-hidden="true">
                <defs>
                  <linearGradient id="agt-sc-path-gradient" x1="0%" y1="0%" x2="100%" y2="100%">
                    <stop offset="0%" stop-color="#18345d" stop-opacity="0.35"/>
                    <stop offset="50%" stop-color="#4a658b" stop-opacity="0.65"/>
                    <stop offset="100%" stop-color="#5a7d9e" stop-opacity="0.4"/>
                  </linearGradient>
                </defs>
{build_paths()}
              </svg>
              <div class="agt-sc-core" aria-hidden="true">
                <div class="agt-sc-core-body">
                  <span class="agt-sc-core-label">Emaavy</span>
                  <span class="agt-sc-core-sub">Agents</span>
                </div>
              </div>
              <div class="agt-sc-nodes">
{build_nodes()}
              </div>
              <div class="agt-sc-status">
                <span class="agt-sc-status-live"><span class="agt-sc-status-dot" aria-hidden="true"></span><span data-agt-status-label>Template fleet</span></span>
                <span class="agt-sc-status-metric" data-agt-metric><strong>1</strong> / {len(TEMPLATES)} templates</span>
              </div>
            </div>
            <div class="agt-sc-presentation" aria-label="Agent template detail" aria-hidden="true">
              <div class="agt-sc-toolbar">
                <button type="button" class="agt-sc-back" aria-label="Return to fleet view">← Fleet</button>
                <span class="agt-sc-progress" data-agt-pres-progress><strong>1</strong> / {len(TEMPLATES)}</span>
                <div class="agt-sc-nav-group">
                  <button type="button" class="agt-sc-nav agt-sc-nav--prev" aria-label="Previous template">←</button>
                  <button type="button" class="agt-sc-nav agt-sc-nav--next" aria-label="Next template">→</button>
                </div>
              </div>
              <div class="agt-sc-slides-viewport">
{build_slides()}
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>'''


BLOCK_RE = re.compile(
    r"    <div class=\"agents-showcase reveal\".*?(?=    <div class=\"hub-clear-why\")",
    re.DOTALL,
)

GRID_RE = re.compile(
    r"    <div class=\"hub-clear-grid\" role=\"list\" aria-label=\"Enterprise agent use cases\">.*?</div>\n",
    re.DOTALL,
)

SLIDES_VIEWPORT_RE = re.compile(
    r"(<div class=\"agt-sc-slides-viewport\">)\s*(?:<article class=\"agt-sc-slide\".*?</article>\s*)+(</div>)",
    re.DOTALL,
)

INLINE_STYLE = '''
  /* Agents premium template showcase */
  body[data-page="home"] #agents .agt-showcase {
    padding: 4px !important;
    border-radius: 24px !important;
    background: linear-gradient(145deg, #4a658b 0%, #18345d 42%, #5a7d9e 100%) !important;
    box-shadow:
      0 0 0 1px rgba(74, 101, 139, 0.45),
      0 22px 52px -14px rgba(24, 52, 93, 0.32),
      0 0 40px -10px rgba(74, 101, 139, 0.28) !important;
  }
  body[data-page="home"] #agents .agt-sc-stage:not(.is-presenting) .agt-sc-fleet {
    display: block !important;
    visibility: visible !important;
    opacity: 1 !important;
  }
  body[data-page="home"] #agents .agt-sc-stage.is-presenting .agt-sc-fleet,
  body[data-page="home"] #agents .agt-sc-stage.is-presenting .agt-sc-ambient,
  body[data-page="home"] #agents .agt-sc-stage.is-presenting .agt-sc-grid,
  body[data-page="home"] #agents .agt-sc-stage.is-presenting .agt-sc-paths,
  body[data-page="home"] #agents .agt-sc-stage.is-presenting .agt-sc-nodes,
  body[data-page="home"] #agents .agt-sc-stage.is-presenting .agt-sc-core {
    display: none !important;
    visibility: hidden !important;
    opacity: 0 !important;
    pointer-events: none !important;
  }
  body[data-page="home"] #agents .agt-sc-presentation {
    display: none !important;
    visibility: hidden !important;
    opacity: 0 !important;
    pointer-events: none !important;
  }
  body[data-page="home"] #agents .agt-sc-stage.is-presenting .agt-sc-presentation {
    display: flex !important;
    flex-direction: column !important;
    visibility: visible !important;
    opacity: 1 !important;
    pointer-events: auto !important;
    z-index: 20 !important;
    background: linear-gradient(165deg, #f8fafc 0%, #f1f5f9 48%, #eef2f7 100%) !important;
  }
  body[data-page="home"] #agents .agt-sc-stage.is-presenting .agt-sc-slide.is-active {
    display: flex !important;
    flex-direction: column !important;
  }
  body[data-page="home"] #agents .agt-sc-stage.is-presenting .agt-sc-slide:not(.is-active) {
    display: none !important;
  }
  body[data-page="home"] #agents .agt-sc-slide-usecase-list li::before,
  body[data-page="home"] #agents .agt-sc-slide-points li::before {
    display: block !important;
    visibility: visible !important;
    opacity: 1 !important;
    content: "" !important;
  }
  body[data-page="home"] #agents .agt-sc-stage.is-presenting {
    min-height: 520px !important;
  }
'''


def write_agt_js() -> None:
    ids = [t["id"] for t in TEMPLATES]
    labels = {t["id"]: t["title"].split("(")[0].strip()[:28] for t in TEMPLATES}
    detail_map = {f"agt-{t['id']}": t["id"] for t in TEMPLATES}
    js = f"""(function () {{
  'use strict';

  var STEP_ORDER = {ids!r};

  var labels = {labels!r};

  var detailMap = {detail_map!r};

  function init() {{
    var root = document.getElementById('agtShowcase');
    if (!root) return;

    var stage = root.querySelector('.agt-sc-stage');
    var presentation = root.querySelector('.agt-sc-presentation');
    var nodes = Array.prototype.slice.call(root.querySelectorAll('.agt-sc-node'));
    var slideEls = Array.prototype.slice.call(root.querySelectorAll('.agt-sc-slide'));
    var layerCards = Array.prototype.slice.call(document.querySelectorAll('#agents .agt-layer-card'));
    var statusLabel = root.querySelector('[data-agt-status-label]');
    var metricEl = root.querySelector('[data-agt-metric]');
    var presProgress = root.querySelector('[data-agt-pres-progress]');
    var btnBack = root.querySelector('.agt-sc-back');
    var btnPrev = root.querySelector('.agt-sc-nav--prev');
    var btnNext = root.querySelector('.agt-sc-nav--next');
    var slidesViewport = root.querySelector('.agt-sc-slides-viewport');

    if (!stage || !presentation || !nodes.length || !slideEls.length) return;

    var slideMap = {{}};
    slideEls.forEach(function (slide) {{
      var id = slide.getAttribute('data-slide');
      if (id) slideMap[id] = slide;
    }});

    var stepIdx = 0;
    var isPresenting = false;
    var touchStartX = 0;
    var touchStartY = 0;

    function stepFromDetail(detail) {{
      return detailMap[detail] || detail;
    }}

    function indexForStep(step) {{
      var i = STEP_ORDER.indexOf(step);
      return i >= 0 ? i : 0;
    }}

    function clearSlideStates() {{
      slideEls.forEach(function (slide) {{
        slide.classList.remove('is-active');
        slide.setAttribute('aria-hidden', 'true');
      }});
    }}

    function setFleetActive(step) {{
      nodes.forEach(function (node) {{
        var s = node.getAttribute('data-step');
        node.classList.toggle('is-active', s === step);
      }});
      layerCards.forEach(function (card) {{
        var d = stepFromDetail(card.getAttribute('data-detail'));
        card.classList.toggle('is-selected', d === step);
        if (d === step && !isPresenting) {{
          card.scrollIntoView({{ block: 'nearest', behavior: 'smooth' }});
        }}
      }});
      if (statusLabel && labels[step]) {{
        statusLabel.textContent = labels[step];
      }}
      if (metricEl) {{
        var idx = indexForStep(step);
        metricEl.innerHTML = '<strong>' + (idx + 1) + '</strong> / ' + STEP_ORDER.length + ' templates';
      }}
    }}

    function setSlideActive(index) {{
      if (index < 0) index = STEP_ORDER.length - 1;
      if (index >= STEP_ORDER.length) index = 0;
      var targetId = STEP_ORDER[index];
      var targetSlide = slideMap[targetId];
      slideEls.forEach(function (slide) {{
        var isTarget = slide === targetSlide;
        slide.classList.toggle('is-active', isTarget);
        slide.setAttribute('aria-hidden', isTarget ? 'false' : 'true');
      }});
      stepIdx = index;
      setFleetActive(targetId);
      if (presProgress) {{
        presProgress.innerHTML = '<strong>' + (index + 1) + '</strong> / ' + STEP_ORDER.length;
      }}
    }}

    function openPresentation(step) {{
      isPresenting = true;
      stage.classList.add('is-presenting');
      root.classList.add('is-presenting');
      presentation.setAttribute('aria-hidden', 'false');
      setSlideActive(indexForStep(step));
    }}

    function closePresentation() {{
      isPresenting = false;
      stage.classList.remove('is-presenting');
      root.classList.remove('is-presenting');
      presentation.setAttribute('aria-hidden', 'true');
      clearSlideStates();
      setFleetActive(STEP_ORDER[stepIdx]);
    }}

    function nextSlide() {{ if (!isPresenting) return; setSlideActive(stepIdx + 1); }}
    function prevSlide() {{ if (!isPresenting) return; setSlideActive(stepIdx - 1); }}
    function selectStep(step) {{ if (STEP_ORDER.indexOf(step) < 0) return; openPresentation(step); }}

    clearSlideStates();
    presentation.setAttribute('aria-hidden', 'true');
    setFleetActive(STEP_ORDER[0]);

    nodes.forEach(function (node) {{
      var step = node.getAttribute('data-step');
      node.setAttribute('tabindex', '0');
      node.setAttribute('role', 'button');
      node.addEventListener('click', function (e) {{ e.preventDefault(); e.stopPropagation(); selectStep(step); }});
      node.addEventListener('mouseenter', function () {{ if (!isPresenting) setFleetActive(step); }});
      node.addEventListener('mouseleave', function () {{ if (!isPresenting) setFleetActive(STEP_ORDER[0]); }});
      node.addEventListener('keydown', function (e) {{
        if (e.key === 'Enter' || e.key === ' ') {{ e.preventDefault(); selectStep(step); }}
      }});
    }});

    layerCards.forEach(function (card) {{
      var step = stepFromDetail(card.getAttribute('data-detail'));
      card.addEventListener('click', function (e) {{
        e.preventDefault(); e.stopPropagation(); e.stopImmediatePropagation();
        selectStep(step);
      }}, true);
      card.addEventListener('mouseenter', function () {{ if (!isPresenting) setFleetActive(step); }});
      card.addEventListener('mouseleave', function () {{ if (!isPresenting) setFleetActive(STEP_ORDER[0]); }});
    }});

    if (btnBack) btnBack.addEventListener('click', function (e) {{ e.preventDefault(); closePresentation(); }});
    if (btnPrev) btnPrev.addEventListener('click', function (e) {{ e.preventDefault(); prevSlide(); }});
    if (btnNext) btnNext.addEventListener('click', function (e) {{ e.preventDefault(); nextSlide(); }});

    root.addEventListener('keydown', function (e) {{
      if (!isPresenting) return;
      if (e.key === 'ArrowRight') {{ e.preventDefault(); nextSlide(); }}
      if (e.key === 'ArrowLeft') {{ e.preventDefault(); prevSlide(); }}
      if (e.key === 'Escape') {{ e.preventDefault(); closePresentation(); }}
    }});

    if (slidesViewport) {{
      slidesViewport.addEventListener('touchstart', function (e) {{
        if (!isPresenting || !e.touches.length) return;
        touchStartX = e.touches[0].clientX;
        touchStartY = e.touches[0].clientY;
      }}, {{ passive: true }});
      slidesViewport.addEventListener('touchend', function (e) {{
        if (!isPresenting || !e.changedTouches.length) return;
        var dx = e.changedTouches[0].clientX - touchStartX;
        var dy = e.changedTouches[0].clientY - touchStartY;
        if (Math.abs(dx) > Math.abs(dy) && Math.abs(dx) > 40) {{
          if (dx < 0) nextSlide(); else prevSlide();
        }}
      }}, {{ passive: true }});
    }}
  }}

  if (document.readyState === 'loading') {{
    document.addEventListener('DOMContentLoaded', init);
  }} else {{
    init();
  }}
}})();
"""
    (ROOT / "assets" / "agt-showcase.js").write_text(js, encoding="utf-8")


def write_agt_css() -> None:
    base = (ROOT / "assets" / "int-showcase.css").read_text(encoding="utf-8")
    css = base.replace("int-sc", "agt-sc").replace("int-showcase", "agt-showcase")
    css = css.replace("int-vis", "agt-vis").replace("int-layer", "agt-layer")
    css = css.replace("int-split", "agt-split").replace("int-layers-col", "agt-templates-col")
    css = css.replace("#integrations", "#agents")
    css = css.replace("Integrations hub", "Agent templates")
    css = css.replace(".agt-sc-pipeline", ".agt-sc-fleet")
    css = css.replace("--int-x", "--agt-x").replace("--int-y", "--agt-y")
    css = re.sub(
        r"\.agt-sc-node--\w+ \{ --agt-x:.*?;\s*\}\n",
        "",
        css,
    )

    extra = '''
#agents .hub-clear-shell { max-width: 1180px; }

#agents .agt-templates-head {
  font-family: 'Clash Display', sans-serif;
  font-size: 1.05rem;
  font-weight: 600;
  color: #18345d;
  margin: 0 0 0.25rem;
}

#agents .agt-templates-sub {
  font-size: 0.78rem;
  line-height: 1.5;
  color: #64748b;
  margin: 0 0 0.85rem;
}

#agents .agt-templates-col {
  max-height: min(78vh, 600px);
  overflow-y: auto;
  padding-right: 0.35rem;
  scrollbar-width: thin;
}

#agents .agt-layer-steps {
  gap: 0.55rem;
}

#agents .agt-layer-card {
  display: grid;
  grid-template-columns: auto 1fr auto;
  gap: 0.55rem;
  align-items: start;
  padding: 0.75rem 0.85rem;
}

#agents .agt-layer-card-icon {
  font-size: 1.15rem;
  line-height: 1;
  margin-top: 0.1rem;
}

#agents .agt-layer-card-body h3 {
  font-family: 'Clash Display', sans-serif;
  font-size: 0.82rem;
  font-weight: 600;
  color: #0f172a;
  margin: 0.1rem 0 0.2rem;
  line-height: 1.25;
}

#agents .agt-layer-card-body p {
  font-size: 0.68rem;
  line-height: 1.45;
  color: #475569;
  margin: 0;
}

#agents .agt-layer-card-kicker {
  font-size: 0.5rem;
  font-weight: 600;
  letter-spacing: 0.1em;
  text-transform: uppercase;
  color: #4a658b;
}

#agents .agt-layer-card-mode {
  font-size: 0.48rem;
  font-weight: 700;
  letter-spacing: 0.06em;
  text-transform: uppercase;
  color: #18345d;
  padding: 0.18rem 0.38rem;
  border-radius: 999px;
  background: rgba(74, 101, 139, 0.1);
  border: 1px solid rgba(74, 101, 139, 0.18);
  white-space: nowrap;
}

#agents .agt-layer-card.is-selected {
  border-color: #4a658b !important;
  box-shadow: 0 8px 22px rgba(24, 52, 93, 0.12) !important;
}

.agt-sc-node {
  width: clamp(3.8rem, 11vw, 5rem);
}

.agt-sc-node-card {
  padding: 0.32rem 0.36rem;
  text-align: center;
}

.agt-sc-node-icon {
  display: block;
  font-size: 0.85rem;
  line-height: 1;
  margin-bottom: 0.15rem;
}

.agt-sc-node-title {
  display: block;
  font-size: 0.42rem;
  font-weight: 600;
  line-height: 1.2;
  color: #0f172a;
}

.agt-sc-node {
  --agt-x: 50%;
  --agt-y: 50%;
  left: var(--agt-x);
  top: var(--agt-y);
}

.agt-vis-template {
  display: grid;
  gap: 0.35rem;
  justify-items: center;
  text-align: center;
}

.agt-vis-template-icon {
  font-size: 1.35rem;
  line-height: 1;
}

.agt-vis-flow {
  display: flex;
  flex-wrap: wrap;
  gap: 0.28rem;
  justify-content: center;
}

.agt-vis-flow-step {
  font-size: 0.44rem;
  font-weight: 600;
  padding: 0.25rem 0.4rem;
  border-radius: 6px;
  background: #f1f5f9;
  border: 1px solid #e2e8f0;
  color: #64748b;
}

.agt-vis-flow-step.is-live {
  background: rgba(74, 101, 139, 0.12);
  border-color: rgba(74, 101, 139, 0.35);
  color: #18345d;
}

.agt-vis-template-duration {
  font-size: 0.48rem;
  font-weight: 600;
  color: #4a658b;
  letter-spacing: 0.06em;
  text-transform: uppercase;
}

.agt-sc-path-flow--f { animation-duration: 3.7s; animation-delay: -0.5s; }
.agt-sc-path-flow--g { animation-duration: 4.1s; animation-delay: -1.4s; }
.agt-sc-path-flow--h { animation-duration: 3.5s; animation-delay: -2.2s; }
.agt-sc-path-flow--i { animation-duration: 4.3s; animation-delay: -0.9s; }
.agt-sc-path-flow--j { animation-duration: 3.8s; animation-delay: -1.8s; }
.agt-sc-path-flow--k { animation-duration: 4s; animation-delay: -2.6s; }
.agt-sc-path-flow--l { animation-duration: 3.6s; animation-delay: -1.1s; }
.agt-sc-path-flow--m { animation-duration: 4.2s; animation-delay: -2.4s; }

@media (max-width: 960px) {
  #agents .agt-split { grid-template-columns: 1fr; }
  #agents .agt-templates-col { max-height: 280px; }
  .agt-sc-node { width: clamp(3.2rem, 14vw, 4.2rem); }
  .agt-sc-node-title { font-size: 0; }
  .agt-sc-node-icon { font-size: 0.95rem; }
}
'''
    (ROOT / "assets" / "agt-showcase.css").write_text(css + extra, encoding="utf-8")


def main():
    write_agt_css()
    write_agt_js()
    text = INDEX.read_text(encoding="utf-8")

    if 'id="agtShowcase"' not in text:
        m = BLOCK_RE.search(text)
        if not m:
            raise SystemExit("Could not find agents-showcase block")
        text = text[: m.start()] + build_split_html() + "\n" + text[m.end() :]
        print("Replaced agents-showcase with agt-showcase split")
    else:
        print("agt-showcase already present")

    text, n = GRID_RE.subn("", text, count=1)
    if n:
        print("Removed agent hub-clear-grid cards")

    text = text.replace(
        "<h2 class=\"hub-clear-intro-title\">An AI workforce for every enterprise.</h2>",
        "<h2 class=\"hub-clear-intro-title\">Start from a template. Deploy in minutes.</h2>",
    )
    text = text.replace(
        "<p class=\"hub-clear-intro-lead\">EMAAVY deploys voice agents across industries and teams — each with its own voice, flow, and mission. Create as many agents as you need and assign them to the campaigns that matter.</p>",
        "<p class=\"hub-clear-intro-lead\">Fourteen enterprise-ready voice agent templates — sales, support, HR, finance, and events. Pick one to pre-fill your canvas, then customize voice, language, and flows.</p>",
    )

    if "assets/agt-showcase.css" not in text:
        text = text.replace(
            '<link rel="stylesheet" href="assets/int-showcase.css" />',
            '<link rel="stylesheet" href="assets/int-showcase.css" />\n  <link rel="stylesheet" href="assets/agt-showcase.css" />',
            1,
        )
        print("Added agt-showcase.css link")

    if "assets/agt-showcase.js" not in text:
        text = text.replace(
            '<script src="assets/int-showcase.js" defer></script>',
            '<script src="assets/int-showcase.js" defer></script>\n<script src="assets/agt-showcase.js" defer></script>',
            1,
        )
        print("Added agt-showcase.js script")

    if "Agents premium template showcase" not in text:
        text = text.replace("  </style>\n</head>", INLINE_STYLE + "  </style>\n</head>", 1)
        print("Added agents inline overrides")

    m = SLIDES_VIEWPORT_RE.search(text)
    if m:
        text = SLIDES_VIEWPORT_RE.sub(
            lambda match: match.group(1) + "\n" + build_slides() + "\n              " + match.group(2),
            text,
            count=1,
        )
        print("Updated agent slide content")

    INDEX.write_text(text, encoding="utf-8")
    print("Done:", INDEX)


if __name__ == "__main__":
    main()
