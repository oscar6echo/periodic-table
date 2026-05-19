# Periodic Table & Quantum Mechanics

A VitePress documentation site covering atomic structure, quantum mechanics, and electron configuration — built around two hand-crafted SVG periodic tables and a 6-chapter quantum mechanics course.

**Live site → [oscar6echo.github.io/periodic-table](https://oscar6echo.github.io/periodic-table/)**

---

## Site overview

| Section | URL | Contents |
| --- | --- | --- |
| **18-column Table** | `/tables/table-18col` | Interactive pan/zoom viewer — conventional layout with electron configs, blocks, and periods |
| **32-column Table** | `/tables/table-32col` | Interactive pan/zoom viewer — Janet (long-form) layout, s/f/d/p blocks in Aufbau order |
| **Chapters 0–7** | `/chapters/…` | Quantum mechanics course from the Schrödinger equation to the periodic table |
| **Math Annex** | `/annex/math` | Vector calculus, spherical harmonics, formal definitions |
| **All Elements** | `/annex/all-elements` | Searchable/sortable table of all 118 elements with physical, chemical, and quantum data |
| **Links** | `/annex/links` | Curated external references |

### Quantum mechanics chapters

| Chapter | Title | Key topics |
| :--- | :--- | :--- |
| **Introduction** | Setting the scene | Motivation, scope |
| **1 — The Schrödinger Equation** | The heart of QM | Wave functions, operators, probability |
| **2 — Particle in a 1D Box** | First quantisation | Boundary conditions, energy levels |
| **3 — The 3D Hydrogen Atom** | Full solution | Spherical coordinates, separation of variables |
| **4 — Angular Solutions** | Orbital shapes | Legendre polynomials, $s/p/d/f$ shapes |
| **5 — Radial Solutions** | Energy shells | Laguerre polynomials, $r_\text{mp}$, shell structure |
| **6 — Spin & Periodic Table** | The final piece | Spin, Pauli principle, Aufbau, Hund's rule, Mendeleev vs Janet |
| **Quiz** | Self-assessment | 10 questions covering all chapters |

---

## Repository layout

```txt
.
├── dev/
│   ├── gen/                     # Python scripts that generate site assets (SVGs, JSON)
│   └── math/                    # Symbolic wavefunction scripts (SymPy) + output
├── docs/
│   ├── .vitepress/
│   │   ├── config.mjs           # VitePress configuration
│   │   └── theme/
│   │       └── components/
│   │           ├── PanZoomViewer.vue   # Interactive SVG viewer (D3-powered)
│   │           └── ValenceTable.vue    # Valence fill bar chart component
│   ├── annex/                   # Math reference, all-elements table, links
│   ├── chapters/                # QM chapters (Markdown + MathJax)
│   ├── tables/                  # Periodic table viewer pages
│   ├── public/
│   │   ├── data/
│   │   │   └── elements.json    # All 118 elements — physical, chemical, quantum data
│   │   ├── diagrams/            # 24 standalone SVG diagrams (orbitals, Aufbau, Bohr shells…)
│   │   ├── icons/               # Hero and feature icons
│   │   └── tables/
│   │       ├── periodic_table_18col.svg   # 18-column periodic table
│   │       └── periodic_table_32col.svg   # 32-column (Janet) periodic table
│   └── index.md                 # Home page
├── package.json
└── pnpm-lock.yaml
```

---

## Local development

```bash
pnpm install          # install dependencies (Node 20+, pnpm)
pnpm docs:dev         # dev server at http://localhost:5173
pnpm docs:build       # production build → docs/.vitepress/dist
pnpm docs:preview     # preview production build
```

---

## Deployment

Pushes to `main` that touch `docs/**`, `package.json`, or `pnpm-lock.yaml` automatically redeploy to GitHub Pages via `.github/workflows/deploy-pages.yml`.

**One-time setup:** in repo **Settings → Pages → Source**, select **GitHub Actions**.
