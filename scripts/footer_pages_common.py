"""Shared HTML shell and blocks for EMAAVY footer subpages."""
from __future__ import annotations

import html
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

FONTS = """  <link rel="preconnect" href="https://fonts.googleapis.com" />
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin />
  <link href="https://api.fontshare.com/v2/css?f[]=clash-display@400,500,600,700&f[]=general-sans@300,400,500,600&display=swap" rel="stylesheet" />"""

HEAD_BASE = """  <link rel="stylesheet" href="{base}assets/navbar-tokens.css" />
  <link rel="stylesheet" href="{base}assets/nav.css" />
  <link rel="stylesheet" href="{base}assets/masthead-flex.css" />
  <link rel="stylesheet" href="{base}assets/navbar-typography.css" />
  <link rel="stylesheet" href="{base}assets/emaavy-type-tokens.css" />
  <link rel="stylesheet" href="{base}assets/site.css" />
  <link rel="stylesheet" href="{base}assets/emaavy-theme.css" />
  <link rel="stylesheet" href="{base}assets/responsive-system.css" />
  <link rel="stylesheet" href="{base}assets/section-heading.css" />
  <link rel="stylesheet" href="{base}assets/brand-logo.css" />
  <link rel="stylesheet" href="{base}assets/footer-premium.css" />
  <link rel="stylesheet" href="{base}assets/footer-page.css" />
  <link rel="icon" href="{base}assets/brand/emaavy-logo.svg" type="image/svg+xml" />"""

SCRIPTS = """  <script src="{base}assets/routes.js"></script>
  <script src="{base}assets/components.js"></script>
  <script src="{base}assets/nav.js"></script>"""


def e(text: str) -> str:
    return html.escape(text, quote=True)


def shell(title: str, description: str, route: str, base: str, content: str, body_class: str = "") -> str:
    bc = f' class="{body_class}"' if body_class else ""
    desc = e(description)
    return f"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0" />
  <title>{e(title)} — EMAAVY</title>
  <meta name="description" content="{desc}" />
  <meta name="robots" content="index, follow" />
  <meta property="og:title" content="{e(title)} — EMAAVY" />
  <meta property="og:description" content="{desc}" />
{FONTS}
{HEAD_BASE.format(base=base)}
</head>
<body data-base="{base}" data-route="{route}"{bc}>
  <div id="site-nav-root"></div>
  <main class="page-main footer-doc-page">
{content}
  </main>
  <div id="site-footer-root"></div>
{SCRIPTS.format(base=base)}
</body>
</html>
"""


def breadcrumb(base: str, crumbs: list[tuple[str, str | None]]) -> str:
    parts = []
    for label, href in crumbs:
        if href:
            parts.append(f'<a href="{base}{href}">{e(label)}</a>')
        else:
            parts.append(f"<span>{e(label)}</span>")
    inner = ' <span aria-hidden="true"> / </span> '.join(parts)
    return f"""        <nav class="breadcrumb" aria-label="Breadcrumb">{inner}</nav>"""


def hero(kicker: str, h1: str, lead: str, base: str, crumbs: list[tuple[str, str | None]], stats: list[tuple[str, str]] | None = None) -> str:
    stats_html = ""
    if stats:
        boxes = "".join(f'<div class="stat-box"><b>{e(b)}</b><span>{e(s)}</span></div>' for b, s in stats)
        stats_html = f'\n        <div class="stat-row telephony-hero-stats">{boxes}</div>'
    return f"""    <section class="page-hero telephony-hero footer-doc-hero">
      <div class="container">
        <span class="page-kicker">{e(kicker)}</span>
        <h1>{e(h1)}</h1>
        <p class="telephony-hero-lead">{lead}</p>{stats_html}
      </div>
    </section>"""


def prose_section(section_id: str, num: str, tag: str, h2: str, paragraphs: list[str], alt: bool = False) -> str:
    cls = "page-section alt" if alt else "page-section"
    sid = f' id="{section_id}"' if section_id else ""
    ps = "".join(f"<p>{p}</p>" for p in paragraphs)
    return f"""    <section{sid} class="{cls}">
      <div class="container">
        <article class="capability-block footer-doc-block">
          <div class="capability-block-inner">
            <div class="capability-meta">
              <span class="capability-num">{num}</span>
              <span class="capability-tag">{e(tag)}</span>
            </div>
            <div class="capability-content">
              <h2>{e(h2)}</h2>
              {ps}
            </div>
          </div>
        </article>
      </div>
    </section>"""


def code_block(code: str, lang: str = "") -> str:
    lang_attr = f' data-lang="{e(lang)}"' if lang else ""
    return f'<pre class="footer-code-block"{lang_attr}><code>{e(code)}</code></pre>'


def api_endpoint_section(
    section_id: str,
    num: str,
    title: str,
    overview: str,
    method: str,
    endpoint: str,
    curl: str,
    request_json: str | None,
    responses: list[tuple[str, str, str]],
) -> str:
    req = code_block(curl, "bash")
    body = ""
    if request_json:
        body = f"""
              <h3>Request body</h3>
              {code_block(request_json, "json")}"""
    resp_html = ""
    for status, label, body_text in responses:
        resp_html += f"""
            <div class="footer-api-response footer-api-response--{status.replace(' ', '')}">
              <div class="footer-api-response-head"><strong>{e(status)}</strong> — {e(label)}</div>
              {code_block(body_text, "json")}
            </div>"""
    return f"""    <section id="{section_id}" class="page-section alt">
      <div class="container footer-api-wrap">
        <article class="footer-api-card">
          <div class="footer-api-meta">
            <span class="capability-num">{num}</span>
            <span class="footer-api-method">{e(method)}</span>
            <code class="footer-api-path">{e(endpoint)}</code>
          </div>
          <h2>{e(title)}</h2>
          <p class="footer-api-overview">{overview}</p>
          <h3>Example request</h3>
          {req}{body}
          <h3>Responses</h3>
          <div class="footer-api-responses">{resp_html}
          </div>
        </article>
      </div>
    </section>"""


def feature_list_section(section_id: str, num: str, tag: str, h2: str, intro: str, items: list[str], alt: bool = False) -> str:
    cls = "page-section alt" if alt else "page-section"
    lis = "".join(f"<li>{item}</li>" for item in items)
    return f"""    <section id="{section_id}" class="{cls}">
      <div class="container">
        <article class="capability-block footer-doc-block">
          <div class="capability-block-inner">
            <div class="capability-meta">
              <span class="capability-num">{num}</span>
              <span class="capability-tag">{e(tag)}</span>
            </div>
            <div class="capability-content">
              <h2>{e(h2)}</h2>
              <p>{intro}</p>
              <ul class="footer-feature-list">{lis}</ul>
            </div>
          </div>
        </article>
      </div>
    </section>"""


def related_links(base: str, links: list[tuple[str, str]]) -> str:
    anchors = "".join(f'<a href="{base}{path}" class="footer-related-pill">{e(label)}</a>' for label, path in links)
    return f"""    <section class="page-section">
      <div class="container">
        <h2 class="footer-related-head">Related documentation</h2>
        <div class="footer-related-row">{anchors}</div>
      </div>
    </section>"""
