# Deploy EMAAVY to GitHub Pages

## Live URL

**https://developeremaavyai365.github.io/EMAAVY/**

This URL updates automatically after each successful push to `main`.

---

## Quick deploy

```powershell
cd "c:\Users\DELL\Desktop\New folder (3)\emaavy"

python scripts/prepare_github_pages.py
python scripts/qa_audit.py

git add -A
git commit -m "Update EMAAVY site"
git push origin main
```

1. Open [Actions](https://github.com/developeremaavyai365/EMAAVY/actions) on GitHub
2. Wait for **Deploy to GitHub Pages** to finish (green checkmark)
3. Visit **https://developeremaavyai365.github.io/EMAAVY/**

---

## First-time setup (if starting fresh)

### 1. Create repository

1. Go to [github.com/new](https://github.com/new)
2. Name: `EMAAVY` (or your choice)
3. Visibility: **Public** (required for free `github.io` hosting)
4. Create without adding a README

### 2. Push from local

```powershell
git remote add origin https://github.com/YOUR_USERNAME/EMAAVY.git
git branch -M main
git push -u origin main
```

### 3. Enable GitHub Pages

1. Repo → **Settings** → **Pages**
2. **Build and deployment** → **Source** → **GitHub Actions**
3. After first push, workflow `.github/workflows/pages.yml` deploys the site

---

## How deployment works

- Workflow: `.github/workflows/pages.yml`
- Triggers: push to `main`, or manual **workflow_dispatch**
- Artifact: entire repository root (static HTML/CSS/JS)
- Entry point: `index.html`

---

## Pre-push checklist

```powershell
python scripts/qa_audit.py
```

Expect: `DEPLOYMENT READY` with 0 CRITICAL issues.

---

## Notes

- **Custom domain**: Settings → Pages → Custom domain (optional)
- **404**: `404.html` is included; configure host to serve it for missing routes
- **Legacy HTML** at repo root (`index1.html`, etc.) are not linked from production nav—safe to ignore or delete later
- **Forms**: client-side only until backend is connected

---

## Troubleshooting

| Problem | Fix |
|---------|-----|
| 404 on home | Ensure `index.html` exists at repo root |
| Styles missing | Check browser network tab for 404 on `assets/` paths |
| Pages not updating | Wait 2–5 min; check Actions tab for failed workflow |
| Wrong default page | GitHub Pages serves `index.html` first—no `jekyll` build needed |
