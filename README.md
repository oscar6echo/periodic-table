# Periodic Table

A set of hand-crafted SVG reference sheets covering atomic structure, quantum mechanics, and electron configuration — plus a browser-based pan/zoom viewer.

**Live viewer → [oscar6echo.github.io/periodic-table](https://oscar6echo.github.io/periodic-table/)**

---

## SVG sheets

| File  Contents |
| ------ | ---------- |
| `periodic_table_1_full.svg` | Full 18-column periodic table with electron configurations, blocks, and periods |
| `periodic_table_2_32col.svg` | 32-column (Janet) layout — s/f/d/p blocks in natural Aufbau order |
| `periodic_table_3_orbital_shells.svg` | Bohr shell diagrams, orbital box diagrams (paramagnetism), valence electron fills for all 118 elements |
| `periodic_table_4_quantum_principles.svg` | The four quantum numbers, orbital shapes, Aufbau energy levels, Hund's rule, exceptions (Cr, Cu), block map |

---

## Viewer

Open the interactive pan/zoom viewer locally:

```bash
./serve.sh          # serves on http://localhost:8765 and opens the browser
./serve.sh 9000     # custom port
```

Or visit the [GitHub Pages deployment](https://oscar6echo.github.io/periodic-table/) directly.

**Controls:** scroll to zoom · drag to pan · `f` fit · `1` 100% · `+`/`-` step zoom

---

## Tooling

| Script | Purpose |
| -------- | --------- |
| `gen_png_from_svg.py` | Render any SVG to PNG via `rsvg-convert` (`--zoom`, `--dpi` options) |
| `gen_orbital_section.py` | Generate the orbital box diagram section in sheet 3 |
| `gen_32col.py` | Generate the 32-column layout (sheet 2) |
| `gen_orbital.py` | Generate Bohr shell diagrams (sheet 3) |

```bash
# Example: render all sheets to PNG at 2× resolution
/home/olivier/micromamba/envs/wa/bin/python gen_png_from_svg.py periodic_table_*.svg
```

---

## Deployment

Pushes to `main` that touch any `.svg`, `view_svg.html`, or `view_svg.js` automatically redeploy to GitHub Pages via the workflow in `.github/workflows/deploy-pages.yml`.

**One-time setup:** in the repo **Settings → Pages → Source**, select **GitHub Actions**.
