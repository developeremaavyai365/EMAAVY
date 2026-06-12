# EMAAVY

**The Enterprise AI Operating System for voice, campaigns, and call intelligence.**

EMAAVY is a production-ready static marketing and product website for an enterprise voice-AI platform. It covers voice agents, campaign orchestration, integrations, call lifecycle, case studies, API documentation, pricing, and conversion flows—optimized for GitHub Pages and mobile devices.

---

## Live site

**https://developeremaavyai365.github.io/EMAAVY/**

| Page | URL |
|------|-----|
| Home | [/EMAAVY/](https://developeremaavyai365.github.io/EMAAVY/) |
| Login | [/EMAAVY/login.html](https://developeremaavyai365.github.io/EMAAVY/login.html) |
| Book a demo | [/EMAAVY/book-demo.html](https://developeremaavyai365.github.io/EMAAVY/book-demo.html) |
| Pricing | [/EMAAVY/pages/pricing.html](https://developeremaavyai365.github.io/EMAAVY/pages/pricing.html) |
| Integrations | [/EMAAVY/pages/integrations/index.html](https://developeremaavyai365.github.io/EMAAVY/pages/integrations/index.html) |
| Documentation | [/EMAAVY/pages/documentation.html](https://developeremaavyai365.github.io/EMAAVY/pages/documentation.html) |

Deployment is automatic on every push to `main` via GitHub Actions (see [Deploy](#deploy-to-github-pages)).

---

## What’s included

| Area | Description |
|------|-------------|
| **Landing page** | Hero command-center orbit, six interactive showcases (HIW, Integrations, Agents, Campaigns, Flows, Lifecycle) |
| **Voice agents** | 16 template pages + workforce hub |
| **Integrations** | Telephony, LLM, STT, TTS, tools/CRM — 34 partner pages |
| **Call lifecycle** | Ring → transcribe → analyze → act → learn |
| **Case studies** | Mudita, NextCall, FleetIQ |
| **API docs** | 9 API reference pages under `pages/api-docs/` |
| **Product features** | Dashboard, campaigns, RAG, integrations ecosystem |
| **Auth & conversion** | Login, book-a-demo, pricing, contact, FAQ |
| **404 page** | Branded not-found page with recovery links |

**113+ production HTML pages** — static HTML, CSS, and vanilla JavaScript. No backend required for hosting.

---

## Tech stack

- **Frontend** — Semantic HTML5, modular CSS, vanilla JS
- **Typography** — Clash Display + General Sans (Fontshare)
- **Navigation** — Central route registry in `assets/routes.js`, shared nav/footer via `assets/components.js`
- **Showcases** — Orbit command center + section showcases (`*-showcase.js/css`)
- **Responsive** — `assets/responsive-system.css` (320px → 4K)
- **Hosting** — GitHub Pages via `.github/workflows/pages.yml`
- **Generators** — Python scripts in `scripts/` for page regeneration

---

## Project structure

```
emaavy/
├── index.html              # Landing page (GitHub Pages entry)
├── login.html              # Login / signup
├── book-demo.html          # Demo booking
├── 404.html                # Custom not-found page
├── assets/
│   ├── routes.js           # Navigation & route registry
│   ├── components.js       # Shared masthead + footer
│   ├── responsive-system.css
│   ├── hero-command-center.js/css
│   ├── *-showcase.js/css   # Section showcases
│   └── brand/              # Logo assets
├── pages/
│   ├── agents/             # Agent templates (16+)
│   ├── integrations/       # Partner pages (34)
│   ├── api-docs/           # API reference (9)
│   ├── product/            # Product feature pages (9)
│   ├── call-lifecycle/     # Lifecycle stages (6)
│   ├── case-studies/       # Customer stories
│   ├── faq/                # FAQ topics
│   ├── company/            # Company & resources
│   └── legal/              # Terms, privacy
├── scripts/                # Build, patch, and QA utilities
├── .github/workflows/pages.yml
├── PRE_PRODUCTION_AUDIT_REPORT.md
└── DEPLOY.md
```

---

## Local development

### Quick start (recommended)

```powershell
cd path\to\emaavy
python -m http.server 8080
```

Open **http://localhost:8080**

### Pre-push QA

```powershell
python scripts/qa_audit.py
```

Validates routes, assets, JS syntax, and security. Expect **DEPLOYMENT READY** before pushing.

### Regenerate pages

```powershell
python scripts/build_footer_pages.py
python scripts/build_integrations_index.py
python scripts/patch_responsive_assets.py
python scripts/prepare_github_pages.py
```

---

## Deploy to GitHub Pages

### Automatic (configured)

Every push to `main` triggers **Deploy to GitHub Pages** (GitHub Actions).

1. Ensure **Settings → Pages → Source** is **GitHub Actions**
2. Push to `main`
3. Wait for the green checkmark in **Actions**
4. Live at **https://developeremaavyai365.github.io/EMAAVY/**

### Manual push

```powershell
cd path\to\emaavy
python scripts/prepare_github_pages.py
python scripts/qa_audit.py
git add -A
git commit -m "Update EMAAVY site"
git push origin main
```

See [DEPLOY.md](DEPLOY.md) for first-time setup and troubleshooting.

---

## Key scripts

| Script | Purpose |
|--------|---------|
| `scripts/qa_audit.py` | Pre-production audit (routes, assets, JS, security) |
| `scripts/prepare_github_pages.py` | Normalize links for GitHub Pages hosting |
| `scripts/patch_responsive_assets.py` | Inject responsive CSS across all HTML pages |
| `scripts/build_footer_pages.py` | Generate API docs, product, company, legal pages |
| `scripts/build_integrations_index.py` | Regenerate integrations hub |
| `scripts/remove_breadcrumbs.py` | Strip breadcrumbs from subpages |

---

## Design system

| Token | Value | Usage |
|-------|-------|--------|
| Deep navy | `#18345d` | Headlines, emphasis |
| Bolt slate | `#4a658b` | Accents, buttons, links |
| Steel blue | `#5a7d9e` | Gradients, highlights |
| Surface | `#ffffff` / `#f8fafc` | Backgrounds, cards |

Shared styles: `assets/emaavy-theme.css`, `assets/site.css`, `assets/nav.css`, `assets/footer-premium.css`.

---

## Quality assurance

Pre-production audit completed May 2026:

- ✓ 113 pages audited
- ✓ 23/23 JS files pass syntax check
- ✓ All routes resolve
- ✓ Responsive system deployed
- ✓ Security scan clean
- **Score: 95/100 — Deployment ready**

Full report: [PRE_PRODUCTION_AUDIT_REPORT.md](PRE_PRODUCTION_AUDIT_REPORT.md)

---

## Browser support

- Chrome / Edge 90+
- Firefox 90+
- Safari 15+

Uses modern CSS (`:has()`, `clamp()`, flex/grid). JavaScript required for navigation and showcases.

---

## Security

This is a **marketing website only**. Do not commit API keys, `.env` files, or production credentials.

Forms (login, demo, contact) are client-side demos—connect a backend before production auth.

---

## Repository

**GitHub:** [developeremaavyai365/EMAAVY](https://github.com/developeremaavyai365/EMAAVY)

**Live:** [developeremaavyai365.github.io/EMAAVY](https://developeremaavyai365.github.io/EMAAVY/)

---

## License

Copyright © EMAAVY. All rights reserved.

Proprietary marketing material unless otherwise stated by the owner.
