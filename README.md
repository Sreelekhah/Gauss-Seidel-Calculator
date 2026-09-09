# Gauss–Seidel Solver

A static, single-page Gauss-Seidel linear system calculator. No backend, no build step — it's one HTML file with inline CSS/JS.

## Deploy to Vercel

**Option A — Vercel CLI (fastest)**
```bash
npm i -g vercel   # skip if already installed
cd gauss-seidel-vercel
vercel            # follow prompts, creates a preview URL
vercel --prod     # promote to your production URL
```

**Option B — Drag and drop**
Go to https://vercel.com/new, drag this folder in. Vercel auto-detects it as a static site — no framework preset needed.

**Option C — GitHub**
```bash
git init
git add .
git commit -m "Gauss-Seidel solver"
git remote add origin <your-repo-url>
git push -u origin main
```
Then import the repo at https://vercel.com/new — every push to `main` auto-deploys.

## Local preview
```bash
npm run dev
```
or just open `index.html` directly in a browser.

## Files
- `index.html` — the app
- `vercel.json` — static-site config (clean URLs, no trailing slash)
- `package.json` — lets tooling recognize the project; no actual build runs
