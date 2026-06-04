# Deploy EMAAVY to GitHub Pages (live link)

Your site is a static HTML site. After you push to GitHub and turn on Pages, everyone gets a link like:

**`https://YOUR_USERNAME.github.io/REPO_NAME/`**

---

## One-time setup (about 5 minutes)

### 1. Create a GitHub repository

1. Go to [https://github.com/new](https://github.com/new)
2. Name it (e.g. `emaavy` or `emaavy-website`)
3. Choose **Public**
4. Do **not** add a README if GitHub offers one (you already have code locally)
5. Click **Create repository**

### 2. Push this project from your PC

In PowerShell, from this folder:

```powershell
cd "c:\Users\DELL\Desktop\New folder (3)\emaavy"

python scripts/prepare_github_pages.py

git add -A
git commit -m "Prepare site for GitHub Pages with index.html landing"

git remote add origin https://github.com/YOUR_USERNAME/YOUR_REPO_NAME.git
git branch -M main
git push -u origin main
```

Replace `YOUR_USERNAME` and `YOUR_REPO_NAME` with your GitHub username and repo name.

### 3. Enable GitHub Pages

1. Open your repo on GitHub → **Settings** → **Pages**
2. Under **Build and deployment** → **Source**, choose **GitHub Actions**
3. After the first push, open **Actions** and wait for **Deploy to GitHub Pages** to finish (green checkmark)

### 4. Your live URL

GitHub shows the URL on **Settings → Pages**, usually:

`https://YOUR_USERNAME.github.io/YOUR_REPO_NAME/`

Share that link. The home page is `index.html` (your full landing experience).

---

## Updating the live site later

```powershell
cd "c:\Users\DELL\Desktop\New folder (3)\emaavy"
# edit files, then:
python scripts/prepare_github_pages.py
git add -A
git commit -m "Update site"
git push
```

Pages redeploys automatically within a few minutes.

---

## Notes

- **Custom domain**: Settings → Pages → Custom domain (optional).
- **Private repo**: GitHub Pages on free plans requires a **public** repo for `github.io` hosting.
- Local file `emaavy_white_blue (2).html` is still the source; the script copies it to `index.html` for hosting.
