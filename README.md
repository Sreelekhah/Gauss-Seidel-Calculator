# Gauss–Seidel Solver

A static web app that solves a 3×3 system of linear equations (Ax = b) using the Gauss-Seidel iterative method. No backend, no build step, no dependencies — it's a single HTML file with inline CSS and JavaScript.

## What it does

Given a coefficient matrix and a constants vector, the app iterates toward a solution:

1. Starts from an initial guess of x = y = z = 0
2. Each iteration updates x, then y (using the new x), then z (using the new x and y)
3. Tracks the largest change across the three variables as the error for that pass
4. Stops early once that error drops below your tolerance, or after the max iteration count

The UI shows:
- The system definition (editable coefficients and constants)
- Tolerance and max-iteration controls
- The current solution once it converges
- A log-scale chart of error vs. iteration, so you can see the convergence rate
- A full iteration-by-iteration table

Diagonal elements can't be zero (division by them is required each pass), and the app checks for that plus generally invalid input before running.

## Usage

Open `index.html` directly in any browser — nothing to install. Edit the matrix, tolerance, or iteration cap, then press **Calculate**. **Reset** restores the default example system.

For local development with a dev server instead of opening the file directly:
```bash
npm run dev
```

## Deploy to Vercel

**CLI (fastest)**
```bash
npm i -g vercel   # skip if already installed
vercel            # creates a preview URL
vercel --prod     # promotes to your production URL
```

**Drag and drop**
Go to https://vercel.com/new and drag this folder in. Vercel auto-detects it as a static site — no framework preset needed.

**GitHub**
```bash
git init
git add .
git commit -m "Gauss-Seidel solver"
git remote add origin <your-repo-url>
git push -u origin main
```
Import the repo at https://vercel.com/new — every push to `main` auto-deploys.

## Files
- `index.html` — the app (markup, styles, and logic all in one file)
- `vercel.json` — static-site config (clean URLs, no trailing slash)
- `package.json` — lets tooling recognize the project; no actual build runs

## Notes on the math

Gauss-Seidel converges reliably when the coefficient matrix is diagonally dominant (each diagonal entry's magnitude exceeds the sum of the other entries in its row). The default example (10, 1, 1 / 2, 10, 1 / 2, 2, 10) satisfies this, which is why it converges quickly. Swapping in a matrix that isn't diagonally dominant may converge slowly, oscillate, or diverge — the error chart will make that visible.
