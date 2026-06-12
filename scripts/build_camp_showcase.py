#!/usr/bin/env python3
"""Replace campaigns section with premium camp-showcase panel in index.html."""
from __future__ import annotations

import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
INDEX = ROOT / "index.html"

sys.path.insert(0, str(Path(__file__).resolve().parent))
from campaign_showcase import CAMPAIGN_STEPS, NODE_LAYOUT  # noqa: E402


def svg_point(x_pct: float, y_pct: float) -> tuple[int, int]:
    return int(x_pct * 6), int(y_pct * 6)


def build_paths() -> str:
    lines = []
    mods = ["", " camp-sc-path-flow--b", " camp-sc-path-flow--c", " camp-sc-path-flow--d", " camp-sc-path-flow--e"]
    cx, cy = 300, 300
    for i, step in enumerate(CAMPAIGN_STEPS):
        x, y = NODE_LAYOUT[step["id"]]
        sx, sy = svg_point(x, y)
        qx = (cx + sx) // 2
        qy = (cy + sy) // 2
        d = f"M{cx} {cy} Q{qx} {qy} {sx} {sy}"
        fid = step["id"]
        mod = mods[i] if i < len(mods) else ""
        lines.append(f'                <path class="camp-sc-path-soft" data-camp-link="{fid}" d="{d}"/>')
        lines.append(f'                <path class="camp-sc-path" data-camp-link="{fid}" d="{d}"/>')
        lines.append(f'                <path class="camp-sc-path-flow{mod}" data-camp-link="{fid}" d="{d}"/>')
    return "\n".join(lines)


def build_nodes() -> str:
    cards = []
    for i, step in enumerate(CAMPAIGN_STEPS):
        x, y = NODE_LAYOUT[step["id"]]
        active = " is-active" if i == 0 else ""
        short = step["title"].split("—")[0].strip()
        if len(short) > 16:
            short = step["kicker"].title()
        cards.append(
            f'''                <article class="camp-sc-node camp-sc-node--{step["id"]}{active}" data-step="{step["id"]}" style="--camp-x: {x}%; --camp-y: {y}%;">
                  <div class="camp-sc-node-card">
                    <span class="camp-sc-node-icon" aria-hidden="true">{step["icon"]}</span>
                    <span class="camp-sc-node-title">{short}</span>
                  </div>
                </article>'''
        )
    return "\n".join(cards)


def build_layer_cards() -> str:
    variants = ["a", "b", "c", "d", "e"]
    items = []
    for i, step in enumerate(CAMPAIGN_STEPS):
        v = variants[i]
        num = f"{i + 1:02d}"
        items.append(
            f'''          <li class="camp-layer-card camp-layer-card--{v} reveal" data-detail="camp-{step["id"]}" tabindex="0">
            <span class="camp-layer-card-icon" aria-hidden="true">{step["icon"]}</span>
            <div class="camp-layer-card-body">
              <span class="camp-layer-card-kicker">Step {num} · {step["kicker"]}</span>
              <h3>{step["title"]}</h3>
              <p>{step["short"]}</p>
            </div>
            <span class="camp-layer-card-tag">{step["kicker"]}</span>
          </li>'''
        )
    return "\n".join(items)


def build_slides() -> str:
    slides = []
    for i, step in enumerate(CAMPAIGN_STEPS):
        num = f"{i + 1:02d}"
        points = "".join(f"\n                  <li>{p}</li>" for p in step["points"])
        outcomes = "".join(f'\n                  <span class="camp-sc-slide-outcome">{o}</span>' for o in step["outcomes"])
        usecases = "".join(f"\n                    <li>{u}</li>" for u in step["usecases"])
        flow = "".join(
            f'\n                    <span class="camp-vis-flow-step{" is-live" if j == 0 else ""}">{s}</span>'
            for j, s in enumerate(step["flow"])
        )
        shot_block = ""
        if step.get("shot"):
            shot_block = f'''
                <figure class="camp-sc-slide-shot">
                  <img src="{step["shot"]}" alt="{step["shot_alt"]}" width="1024" height="640" loading="lazy" decoding="async" />
                </figure>'''
        slides.append(
            f'''              <article class="camp-sc-slide" data-slide="{step["id"]}" role="tabpanel" aria-hidden="true">
                <span class="camp-sc-slide-kicker">{num} — {step["kicker"]}</span>
                <h3 class="camp-sc-slide-headline">{step["title"]}</h3>
                <p class="camp-sc-slide-desc">{step["desc"]}</p>
                <p class="camp-sc-slide-detail">{step["detail"]}</p>
                <div class="camp-sc-slide-visual">
                  <div class="camp-vis-program">
                    <span class="camp-vis-program-icon" aria-hidden="true">{step["icon"]}</span>
                    <div class="camp-vis-flow">{flow}
                    </div>
                    <span class="camp-vis-program-label">{step["kicker"]}</span>
                  </div>{shot_block}
                </div>
                <ul class="camp-sc-slide-points">{points}
                </ul>
                <div class="camp-sc-slide-outcomes">{outcomes}
                </div>
                <div class="camp-sc-slide-usecases">
                  <span class="camp-sc-slide-usecases-label">Ideal for</span>
                  <ul class="camp-sc-slide-usecase-list">{usecases}
                  </ul>
                </div>
              </article>'''
        )
    return "\n".join(slides)


def build_section_html() -> str:
    n = len(CAMPAIGN_STEPS)
    return f'''<!-- CAMPAIGNS SHOWCASE (legacy anchor: #bento) --> <section id="campaigns" class="hub-zone hub-zone--4 hub-zone--clear hub-zone--campaigns">
  <span id="bento" class="visually-hidden-anchor" aria-hidden="true"></span>
  <div class="hub-zone-bg" aria-hidden="true"></div>
  <div class="hub-zone-header reveal">
    <span class="hub-zone-index">04</span>
    <p class="hub-zone-title">Campaigns</p>
  </div>
  <div class="hub-clear-shell reveal" id="campaigns-emaavy">
    <header class="hub-clear-intro">
      <h2 class="hub-clear-intro-title">Launch outbound and inbound programs in guided steps.</h2>
      <p class="hub-clear-intro-lead">EMAAVY's campaign builder mirrors the live product — choose your type, upload contacts, assign agents, and monitor progress from one command center.</p>
    </header>
    <div class="camp-split reveal">
      <div class="camp-steps-col" aria-label="Campaign capabilities">
        <p class="camp-steps-head">How campaigns work</p>
        <p class="camp-steps-sub">Click any step to explore the product flow — dashboard, types, wizard, and live control.</p>
        <ol class="camp-layer-steps">
{build_layer_cards()}
        </ol>
      </div>
      <div class="camp-showcase-col">
        <div class="camp-showcase" id="campShowcase" tabindex="0" aria-label="EMAAVY campaign builder — live preview" aria-live="polite">
          <div class="camp-sc-stage">
            <div class="camp-sc-hub">
              <div class="camp-sc-ambient" aria-hidden="true"></div>
              <div class="camp-sc-grid" aria-hidden="true"></div>
              <svg class="camp-sc-paths" viewBox="0 0 600 600" aria-hidden="true">
                <defs>
                  <linearGradient id="camp-sc-path-gradient" x1="0%" y1="0%" x2="100%" y2="100%">
                    <stop offset="0%" stop-color="#18345d" stop-opacity="0.35"/>
                    <stop offset="50%" stop-color="#4a658b" stop-opacity="0.65"/>
                    <stop offset="100%" stop-color="#5a7d9e" stop-opacity="0.4"/>
                  </linearGradient>
                </defs>
{build_paths()}
              </svg>
              <div class="camp-sc-core" aria-hidden="true">
                <div class="camp-sc-core-body">
                  <span class="camp-sc-core-label">Emaavy</span>
                  <span class="camp-sc-core-sub">Campaigns</span>
                </div>
              </div>
              <div class="camp-sc-nodes">
{build_nodes()}
              </div>
              <div class="camp-sc-status">
                <span class="camp-sc-status-live"><span class="camp-sc-status-dot" aria-hidden="true"></span><span data-camp-status-label>Campaign Command Center</span></span>
                <span class="camp-sc-status-metric" data-camp-metric><strong>1</strong> / {n} steps</span>
              </div>
            </div>
            <div class="camp-sc-presentation" aria-label="Campaign capability detail" aria-hidden="true">
              <div class="camp-sc-toolbar">
                <button type="button" class="camp-sc-back" aria-label="Return to hub view">← Hub</button>
                <span class="camp-sc-progress" data-camp-pres-progress><strong>1</strong> / {n}</span>
                <div class="camp-sc-nav-group">
                  <button type="button" class="camp-sc-nav camp-sc-nav--prev" aria-label="Previous step">←</button>
                  <button type="button" class="camp-sc-nav camp-sc-nav--next" aria-label="Next step">→</button>
                </div>
              </div>
              <div class="camp-sc-slides-viewport">
{build_slides()}
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
    <div class="hub-clear-cta reveal">
      <a href="book-demo.html" class="hub-btn-primary">Start a campaign</a>
      <a href="login.html" class="hub-btn-secondary">Open workspace</a>
    </div>
  </div>
</section>'''


INLINE_STYLE = '''
  /* Campaigns premium showcase */
  body[data-page="home"] #campaigns .camp-showcase {
    padding: 4px !important;
    border-radius: 24px !important;
    background: linear-gradient(145deg, #4a658b 0%, #18345d 42%, #5a7d9e 100%) !important;
    box-shadow:
      0 0 0 1px rgba(74, 101, 139, 0.45),
      0 22px 52px -14px rgba(24, 52, 93, 0.32),
      0 0 40px -10px rgba(74, 101, 139, 0.28) !important;
  }
  body[data-page="home"] #campaigns .camp-sc-stage:not(.is-presenting) .camp-sc-hub {
    display: block !important;
    visibility: visible !important;
    opacity: 1 !important;
  }
  body[data-page="home"] #campaigns .camp-sc-stage.is-presenting .camp-sc-hub,
  body[data-page="home"] #campaigns .camp-sc-stage.is-presenting .camp-sc-ambient,
  body[data-page="home"] #campaigns .camp-sc-stage.is-presenting .camp-sc-grid,
  body[data-page="home"] #campaigns .camp-sc-stage.is-presenting .camp-sc-paths,
  body[data-page="home"] #campaigns .camp-sc-stage.is-presenting .camp-sc-nodes,
  body[data-page="home"] #campaigns .camp-sc-stage.is-presenting .camp-sc-core {
    display: none !important;
    visibility: hidden !important;
    opacity: 0 !important;
    pointer-events: none !important;
  }
  body[data-page="home"] #campaigns .camp-sc-presentation {
    display: none !important;
    visibility: hidden !important;
    opacity: 0 !important;
    pointer-events: none !important;
  }
  body[data-page="home"] #campaigns .camp-sc-stage.is-presenting .camp-sc-presentation {
    display: flex !important;
    flex-direction: column !important;
    visibility: visible !important;
    opacity: 1 !important;
    pointer-events: auto !important;
    z-index: 20 !important;
    background: linear-gradient(165deg, #f8fafc 0%, #f1f5f9 48%, #eef2f7 100%) !important;
  }
  body[data-page="home"] #campaigns .camp-sc-stage.is-presenting .camp-sc-slide.is-active {
    display: flex !important;
    flex-direction: column !important;
  }
  body[data-page="home"] #campaigns .camp-sc-stage.is-presenting .camp-sc-slide:not(.is-active) {
    display: none !important;
  }
  body[data-page="home"] #campaigns .camp-sc-slide-usecase-list li::before,
  body[data-page="home"] #campaigns .camp-sc-slide-points li::before {
    display: block !important;
    visibility: visible !important;
    opacity: 1 !important;
    content: "" !important;
  }
  body[data-page="home"] #campaigns .camp-sc-stage.is-presenting {
    min-height: 520px !important;
  }
  body[data-page="home"] #campaigns .camp-sc-slide-shot::before,
  body[data-page="home"] #campaigns .camp-sc-slide-shot::after,
  body[data-page="home"] #campaigns .camp-vis-flow-step::before,
  body[data-page="home"] #campaigns .camp-vis-flow-step::after {
    display: block !important;
    visibility: visible !important;
    content: none !important;
  }
'''


def write_camp_css() -> None:
    base = (ROOT / "assets" / "int-showcase.css").read_text(encoding="utf-8")
    css = base.replace("int-sc", "camp-sc").replace("int-showcase", "camp-showcase")
    css = css.replace("int-vis", "camp-vis").replace("int-layer", "camp-layer")
    css = css.replace("int-split", "camp-split").replace("int-layers-col", "camp-steps-col")
    css = css.replace("#integrations", "#campaigns")
    css = css.replace("Integrations hub", "Campaign builder")
    css = css.replace(".camp-sc-pipeline", ".camp-sc-hub")
    css = css.replace("--int-x", "--camp-x").replace("--int-y", "--camp-y")
    css = re.sub(r"\.camp-sc-node--\w+ \{ --camp-x:.*?;\s*\}\n", "", css)

    extra = '''
.visually-hidden-anchor {
  position: absolute;
  width: 1px;
  height: 1px;
  padding: 0;
  margin: -1px;
  overflow: hidden;
  clip: rect(0, 0, 0, 0);
  white-space: nowrap;
  border: 0;
}

#campaigns .hub-clear-shell { max-width: 1180px; }

#campaigns .camp-steps-head {
  font-family: 'Clash Display', sans-serif;
  font-size: 1.05rem;
  font-weight: 600;
  color: #18345d;
  margin: 0 0 0.25rem;
}

#campaigns .camp-steps-sub {
  font-size: 0.78rem;
  line-height: 1.5;
  color: #64748b;
  margin: 0 0 0.85rem;
}

#campaigns .camp-steps-col {
  max-height: min(78vh, 560px);
  overflow-y: auto;
  padding-right: 0.35rem;
  scrollbar-width: thin;
}

#campaigns .camp-layer-steps {
  list-style: none;
  margin: 0;
  padding: 0;
  display: flex;
  flex-direction: column;
  gap: 0.55rem;
}

#campaigns .camp-layer-card {
  display: grid;
  grid-template-columns: auto 1fr auto;
  gap: 0.55rem;
  align-items: start;
  padding: 0.75rem 0.85rem;
  list-style: none;
}

#campaigns .camp-layer-card-icon {
  font-size: 1.15rem;
  line-height: 1;
  margin-top: 0.1rem;
}

#campaigns .camp-layer-card-body h3 {
  font-family: 'Clash Display', sans-serif;
  font-size: 0.82rem;
  font-weight: 600;
  color: #0f172a;
  margin: 0.1rem 0 0.2rem;
  line-height: 1.25;
}

#campaigns .camp-layer-card-body p {
  font-size: 0.68rem;
  line-height: 1.45;
  color: #475569;
  margin: 0;
}

#campaigns .camp-layer-card-kicker {
  font-size: 0.5rem;
  font-weight: 600;
  letter-spacing: 0.1em;
  text-transform: uppercase;
  color: #4a658b;
}

#campaigns .camp-layer-card-tag {
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

#campaigns .camp-layer-card.is-selected {
  border-color: #4a658b !important;
  box-shadow: 0 8px 22px rgba(24, 52, 93, 0.12) !important;
}

.camp-sc-node {
  position: absolute;
  left: var(--camp-x);
  top: var(--camp-y);
  transform: translate(-50%, -50%);
  z-index: 4;
  width: clamp(3.8rem, 11vw, 5rem);
  cursor: pointer;
  pointer-events: auto;
}

.camp-sc-node-card {
  padding: 0.32rem 0.36rem;
  text-align: center;
  border-radius: 10px;
  background: rgba(255, 255, 255, 0.94);
  border: 1px solid rgba(74, 101, 139, 0.22);
  box-shadow: 0 6px 18px rgba(24, 52, 93, 0.1);
  transition: transform 0.2s ease, box-shadow 0.2s ease, border-color 0.2s ease;
}

.camp-sc-node.is-active .camp-sc-node-card,
.camp-sc-node:hover .camp-sc-node-card {
  border-color: #4a658b;
  box-shadow: 0 10px 24px rgba(24, 52, 93, 0.16);
  transform: scale(1.04);
}

.camp-sc-node-icon {
  display: block;
  font-size: 0.85rem;
  line-height: 1;
  margin-bottom: 0.15rem;
}

.camp-sc-node-title {
  display: block;
  font-size: 0.48rem;
  font-weight: 700;
  letter-spacing: 0.04em;
  text-transform: uppercase;
  color: #18345d;
  line-height: 1.2;
}

.camp-sc-slide-visual {
  display: grid;
  grid-template-columns: minmax(0, 0.9fr) minmax(0, 1.1fr);
  gap: 0.75rem;
  align-items: start;
  margin: 0.65rem 0 0.85rem;
}

.camp-vis-program {
  display: flex;
  flex-direction: column;
  align-items: center;
  gap: 0.45rem;
  padding: 0.85rem;
  border-radius: 12px;
  background: linear-gradient(165deg, #f8fafc 0%, #eef2f7 100%);
  border: 1px solid rgba(74, 101, 139, 0.15);
}

.camp-vis-program-icon {
  font-size: 1.35rem;
  line-height: 1;
}

.camp-vis-flow {
  display: flex;
  flex-wrap: wrap;
  gap: 0.3rem;
  justify-content: center;
}

.camp-vis-flow-step {
  font-size: 0.52rem;
  font-weight: 600;
  letter-spacing: 0.04em;
  text-transform: uppercase;
  color: #64748b;
  padding: 0.2rem 0.42rem;
  border-radius: 999px;
  background: rgba(255, 255, 255, 0.9);
  border: 1px solid rgba(148, 163, 184, 0.35);
}

.camp-vis-flow-step.is-live {
  color: #18345d;
  border-color: #4a658b;
  background: rgba(74, 101, 139, 0.12);
}

.camp-vis-program-label {
  font-size: 0.5rem;
  font-weight: 700;
  letter-spacing: 0.1em;
  text-transform: uppercase;
  color: #4a658b;
}

.camp-sc-slide-shot {
  margin: 0;
  border-radius: 10px;
  overflow: hidden;
  border: 1px solid rgba(74, 101, 139, 0.18);
  box-shadow: 0 8px 22px rgba(24, 52, 93, 0.1);
}

.camp-sc-slide-shot img {
  display: block;
  width: 100%;
  height: auto;
  max-height: 140px;
  object-fit: cover;
  object-position: top center;
}

#campaigns .hub-clear-cta {
  display: flex;
  flex-wrap: wrap;
  gap: 0.65rem;
  justify-content: center;
  margin-top: 1.5rem;
}

@media (max-width: 900px) {
  .camp-sc-slide-visual {
    grid-template-columns: 1fr;
  }
}
'''
    (ROOT / "assets" / "camp-showcase.css").write_text(css + extra, encoding="utf-8")


def write_camp_js() -> None:
    ids = [s["id"] for s in CAMPAIGN_STEPS]
    labels = {s["id"]: s["title"] for s in CAMPAIGN_STEPS}
    detail_map = {f"camp-{s['id']}": s["id"] for s in CAMPAIGN_STEPS}
    n = len(ids)
    js = f"""(function () {{
  'use strict';

  var STEP_ORDER = {ids!r};
  var labels = {labels!r};
  var detailMap = {detail_map!r};

  function init() {{
    var root = document.getElementById('campShowcase');
    if (!root) return;

    var stage = root.querySelector('.camp-sc-stage');
    var presentation = root.querySelector('.camp-sc-presentation');
    var nodes = Array.prototype.slice.call(root.querySelectorAll('.camp-sc-node'));
    var slideEls = Array.prototype.slice.call(root.querySelectorAll('.camp-sc-slide'));
    var layerCards = Array.prototype.slice.call(document.querySelectorAll('#campaigns .camp-layer-card'));
    var statusLabel = root.querySelector('[data-camp-status-label]');
    var metricEl = root.querySelector('[data-camp-metric]');
    var presProgress = root.querySelector('[data-camp-pres-progress]');
    var btnBack = root.querySelector('.camp-sc-back');
    var btnPrev = root.querySelector('.camp-sc-nav--prev');
    var btnNext = root.querySelector('.camp-sc-nav--next');
    var slidesViewport = root.querySelector('.camp-sc-slides-viewport');

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

    function setHubActive(step) {{
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
      if (statusLabel && labels[step]) statusLabel.textContent = labels[step];
      if (metricEl) {{
        var idx = indexForStep(step);
        metricEl.innerHTML = '<strong>' + (idx + 1) + '</strong> / {n} steps';
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
      setHubActive(targetId);
      if (presProgress) presProgress.innerHTML = '<strong>' + (index + 1) + '</strong> / {n}';
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
      setHubActive(STEP_ORDER[stepIdx]);
    }}

    function nextSlide() {{ if (!isPresenting) return; setSlideActive(stepIdx + 1); }}
    function prevSlide() {{ if (!isPresenting) return; setSlideActive(stepIdx - 1); }}
    function selectStep(step) {{ if (STEP_ORDER.indexOf(step) < 0) return; openPresentation(step); }}

    clearSlideStates();
    presentation.setAttribute('aria-hidden', 'true');
    setHubActive(STEP_ORDER[0]);

    nodes.forEach(function (node) {{
      var step = node.getAttribute('data-step');
      node.addEventListener('click', function () {{ selectStep(step); }});
      node.setAttribute('tabindex', '0');
      node.setAttribute('role', 'button');
      node.addEventListener('keydown', function (e) {{
        if (e.key === 'Enter' || e.key === ' ') {{ e.preventDefault(); selectStep(step); }}
      }});
    }});

    layerCards.forEach(function (card) {{
      function activate() {{
        var d = card.getAttribute('data-detail');
        if (d) selectStep(stepFromDetail(d));
      }}
      card.addEventListener('click', activate);
      card.addEventListener('keydown', function (e) {{
        if (e.key === 'Enter' || e.key === ' ') {{ e.preventDefault(); activate(); }}
      }});
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
    (ROOT / "assets" / "camp-showcase.js").write_text(js, encoding="utf-8")


SECTION_RE = re.compile(
    r"<!-- CAMPAIGNS SHOWCASE.*?</section>",
    re.DOTALL,
)


def patch_index() -> None:
    text = INDEX.read_text(encoding="utf-8")
    new_section = build_section_html()
    if not SECTION_RE.search(text):
        raise SystemExit("Could not find campaigns section in index.html")
    text = SECTION_RE.sub(new_section, text, count=1)

    text = text.replace(
        'href="assets/campaigns-showcase.css"',
        'href="assets/camp-showcase.css"',
    )
    text = text.replace(
        'src="assets/campaigns-showcase.js"',
        'src="assets/camp-showcase.js"',
    )

    if "camp-showcase.css" not in text:
        text = text.replace(
            'href="assets/agt-showcase.css"',
            'href="assets/agt-showcase.css" />\n  <link rel="stylesheet" href="assets/camp-showcase.css"',
        )

    if "camp-showcase.js" not in text:
        text = text.replace(
            'src="assets/agt-showcase.js"',
            'src="assets/agt-showcase.js" defer></script>\n  <script src="assets/camp-showcase.js"',
        )

    if "Campaigns premium showcase" not in text:
        text = text.replace(
            "body[data-page=\"home\"] .demo-video {",
            INLINE_STYLE + "\n  body[data-page=\"home\"] .demo-video {",
        )

    INDEX.write_text(text, encoding="utf-8")


def main():
    write_camp_css()
    write_camp_js()
    patch_index()
    print(f"OK: campaigns premium showcase ({len(CAMPAIGN_STEPS)} steps)")


if __name__ == "__main__":
    main()
