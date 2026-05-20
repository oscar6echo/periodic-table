// Draw a Bohr shell diagram as a positioned SVG fragment.
// Logic ported from dev/gen/gen_bohr_shells.py generate_svg().
// Returns { body, width, height } — SVG elements in a local (0,0)-origin box,
// with no <svg> wrapper, so the composite builder can place it.

import { CAPACITY, COLORS, SHELL_SUBSHELLS, maxShell } from './electronConfig.js';

const SHELL_RADII = { 1: 18, 2: 40, 3: 62, 4: 84, 5: 106, 6: 128, 7: 150 };
const RING_COLOR = '#30363d';
const LABEL_COLOR = '#8b949e';
const SUBSHELL_ORDER = { s: 0, p: 1, d: 2, f: 3 };
const PAD = 30;

// element: { Z, ... }, config: { "1s": 2, ... } from parseConfig().
// options.showAllSubshells: when true, draw every subshell that exists for each
// shell the element reaches (empty slots included), not just the occupied ones.
export function drawBohrShell(element, config, { showAllSubshells = false } = {}) {
  const Z = element.Z;
  const maxN = maxShell(config);
  const maxRadius = SHELL_RADII[maxN] || 18 * maxN;
  const ringsBox = 2 * (maxRadius + PAD);
  const width = ringsBox;
  const height = ringsBox;
  const cx = width / 2;
  const cy = ringsBox / 2;

  const out = [];

  // Concentric shell rings.
  for (let n = 1; n <= maxN; n++) {
    const r = SHELL_RADII[n] || 18 * n;
    out.push(`<circle cx="${cx}" cy="${cy}" r="${r}" fill="none" stroke="${RING_COLOR}" stroke-width="0.8"/>`);
  }

  // Nucleus — green circle with proton count (matches bohr-shells-ar.svg style).
  out.push(`<circle cx="${cx}" cy="${cy}" r="12" fill="#1c2a1c" stroke="#40a040" stroke-width="1"/>`);
  out.push(`<text x="${cx}" y="${cy}" font-size="7" fill="#80e080" font-family="sans-serif" text-anchor="middle" dominant-baseline="central">${Z}p</text>`);

  // Electrons — one circle per shell, all subshells equally spaced, order s -> p -> d -> f.
  for (let n = 1; n <= maxN; n++) {
    const r = SHELL_RADII[n] || 18 * n;
    let types;
    if (showAllSubshells) {
      types = SHELL_SUBSHELLS[n].slice();
    } else {
      types = SHELL_SUBSHELLS[n].filter((t) => (config[`${n}${t}`] ?? 0) > 0);
    }
    if (types.length === 0) continue;
    types.sort((a, b) => SUBSHELL_ORDER[a] - SUBSHELL_ORDER[b]);

    const totalPositions = types.reduce((sum, t) => sum + CAPACITY[t], 0);
    const positions = [];
    for (let i = 0; i < totalPositions; i++) {
      const angle = (2 * Math.PI * i) / totalPositions;
      // Negate sin for counter-clockwise placement in the SVG coordinate system.
      positions.push([cx + r * Math.cos(angle), cy - r * Math.sin(angle)]);
    }

    let pos = 0;
    for (const t of types) {
      const count = config[`${n}${t}`] ?? 0;
      const cap = CAPACITY[t];
      const color = COLORS[t];
      // Filled positions.
      for (let i = 0; i < count; i++) {
        const [ex, ey] = positions[pos + i];
        out.push(`<circle cx="${ex.toFixed(1)}" cy="${ey.toFixed(1)}" r="3.5" fill="${color}" opacity="0.9"/>`);
      }
      // Empty slots — subdued circle in the subshell color (not gray).
      for (let i = count; i < cap; i++) {
        const [ex, ey] = positions[pos + i];
        out.push(`<circle cx="${ex.toFixed(1)}" cy="${ey.toFixed(1)}" r="2.5" fill="none" stroke="${color}" stroke-width="0.8" opacity="0.5"/>`);
      }
      pos += cap;
    }

    // Subshell labels, stacked vertically just outside this shell's ring.
    types.forEach((t, idx) => {
      const offset = (idx - types.length / 2 + 0.5) * 12;
      const lx = cx + r + 8;
      const ly = cy + offset;
      out.push(`<text x="${lx}" y="${ly.toFixed(1)}" font-size="5.5" fill="${COLORS[t]}" font-family="sans-serif" text-anchor="start" dominant-baseline="central" font-weight="600">${n}${t}</text>`);
    });
  }

  // Shell labels (n=1, n=2, ...) on a vertical line below the center.
  for (let n = 1; n <= maxN; n++) {
    const r = SHELL_RADII[n] || 18 * n;
    out.push(`<text x="${cx}" y="${cy + r + 12}" font-size="5.5" fill="${LABEL_COLOR}" font-family="sans-serif" text-anchor="middle">n=${n}</text>`);
  }

  return { body: out.join('\n'), width, height };
}
