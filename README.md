# EMAAVY

**The Enterprise AI Operating System for voice, campaigns, and call intelligence.**

EMAAVY is a static marketing and product website for an enterprise voice-AI platform. It presents the full product story—voice agents, campaign orchestration, integrations, call lifecycle, case studies, and pricing—in a fast, professional, deployment-ready format suitable for GitHub Pages.

---

## Live site

After GitHub Pages is enabled, the site is available at:

**https://developeremaavyai365.github.io/EMAAVY/**

> Replace the URL above if you use a custom domain or a different repository name.

---

## What this repository includes

| Area | Description |
|------|-------------|
| **Landing page** | Full-scroll homepage with hero video showcase, product hubs, and CTAs |
| **Voice agents** | Workforce hub and role pages (sales, support, inbound, outbound) |
| **Campaigns** | Interactive campaign builder showcase and guided workflow preview |
| **Integrations** | Telephony, LLM, STT, TTS, and tools/CRM partner pages |
| **Call lifecycle** | Ring → transcribe → analyze → act → learn journey |
| **Case studies** | Customer outcome stories with detail pages |
| **Auth & conversion** | Login, book-a-demo, pricing, documentation, and contact flows |

The site is **static HTML, CSS, and JavaScript**—no application server or database is required to host it.

---

## Tech stack

- **Markup & styling** — Semantic HTML5, modular CSS, responsive layout
- **Scripting** — Vanilla JavaScript (navigation, showcases, hero video player)
- **Typography** — Clash Display, General Sans (Fontshare / Google Fonts)
- **Assets** — Optimized PNG screenshots, SVG logos, hero MP4 tour video
- **Routing** — Central nav registry in `assets/routes.js`
- **Hosting** — GitHub Pages via GitHub Actions
- **Tooling** — Python scripts for page generation and deploy preparation

---

## Project structure

```
emaavy/
├── index.html                 # Landing page (GitHub Pages entry)
├── login.html                 # Login screen
├── book-demo.html             # Book a demo
├── assets/                    # Global styles, scripts, images, video
│   ├── routes.js              # Navigation & route registry
│   ├── site.css               # Shared design tokens & components
│   ├── hero-video.js          # Hero video player (mute/unmute)
│   └── video/
│       └── emaavy-hero.mp4    # Platform tour video
├── pages/                     # Product & marketing subpages
│   ├── agents/
│   ├── integrations/
│   ├── call-lifecycle/
│   ├── case-studies/
│   ├── faq/
│   └── …
├── scripts/                   # Build & maintenance utilities
│   ├── prepare_github_pages.py
│   └── build_hero_video.py
├── .github/workflows/
│   └── pages.yml              # GitHub Pages deploy workflow
└── DEPLOY.md                  # Extended deployment notes
```

---

## Local development

### Option 1 — Open directly

Open `index.html` in a modern browser (Chrome, Edge, or Firefox).

> Some features (routing, fetches) work best with a local server. Use Option 2 for full behavior.

### Option 2 — Local static server (recommended)

**Python**

```powershell
cd path\to\emaavy
python -m http.server 8080
```

Then visit **http://localhost:8080**

**Node.js (if installed)**

```powershell
npx serve .
```

---

## Deploy to GitHub Pages

### Prerequisites

- A GitHub account and repository (this project uses `EMAAVY`)
- Git installed locally
- Repository set to **Public** (required for free `github.io` hosting)

### First-time deploy

```powershell
cd path\to\emaavy

python scripts/prepare_github_pages.py

git add -A
git commit -m "Prepare site for GitHub Pages"
git push origin main
```

1. On GitHub, open **Settings → Pages**
2. Under **Build and deployment**, set **Source** to **GitHub Actions**
3. Wait for the **Deploy to GitHub Pages** workflow to complete (Actions tab)

The workflow file is at `.github/workflows/pages.yml`. It publishes the repository root as a static site on every push to `main`.

### Subsequent updates

```powershell
python scripts/prepare_github_pages.py
git add -A
git commit -m "Update site content"
git push
```

Deployment typically completes within a few minutes.

For more detail, see [DEPLOY.md](DEPLOY.md).

---

## Maintenance scripts

| Script | Purpose |
|--------|---------|
| `scripts/prepare_github_pages.py` | Syncs landing content to `index.html` and normalizes internal links for hosting |
| `scripts/build_hero_video.py` | Rebuilds `assets/video/emaavy-hero.mp4` from platform screenshots |
| `scripts/build_*.py` | Generators for agents, integrations, case studies, and other hub pages |

Run scripts from the repository root:

```powershell
python scripts/prepare_github_pages.py
python scripts/build_hero_video.py
```

---

## Hero video

The homepage hero uses a cinematic platform tour (`assets/video/emaavy-hero.mp4`) with:

- Autoplay (muted by default)
- Volume on/off control
- Chapter labels (Dashboard, Campaigns, AI Agents, Integrations)

**Replace the video:** overwrite `assets/video/emaavy-hero.mp4` with your own recording (MP4, H.264, 1920×1080 recommended).

**Regenerate from screenshots:**

```powershell
python scripts/build_hero_video.py
```

---

## Design system

| Token | Value | Usage |
|-------|-------|--------|
| Primary navy | `#18345D` | Headlines, emphasis |
| Secondary slate | `#4A658B` | Accents, buttons, links |
| Surface | `#FFFFFF` / `#F8FAFC` | Backgrounds, cards |
| Success | `#3ECF8E` | Live indicators, campaigns accent |

Shared components live under `assets/` (`site.css`, `nav.css`, `hub-clear.css`, showcase styles).

---

## Browser support

- Chrome / Edge 90+
- Firefox 90+
- Safari 15+

Uses modern CSS (`:has()`, `clamp()`, flex/grid) and HTML5 video. JavaScript is required for navigation and interactive showcases.

---

## Security note

This repository is a **marketing website only**. Do not commit:

- API keys or secrets
- `.env` files
- Production login credentials
- Customer data

---

## Repository

**GitHub:** [developeremaavyai365/EMAAVY](https://github.com/developeremaavyai365/EMAAVY)

---

## License

Copyright © EMAAVY. All rights reserved.

This project is proprietary marketing material unless otherwise stated by the owner.
"# EMAAVY" 
