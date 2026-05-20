// Draw a subshell energy-level diagram as a positioned SVG fragment.
//
// When orbital energy data is available (NIST LDA, Z ≤ 92), subshells are
// placed on a two-zone scale:
//   • Upper zone (linear, 0 to −30 eV)  — valence / near-valence levels
//   • Core zone  (compressed)            — deep core levels, not to scale
//   • Schematic zone (top, optional)     — unoccupied subshells in Madelung order
//
// Falls back to uniform Madelung spacing for elements with no energy data (Z > 92).

import { CAPACITY, COLORS, FILLING_ORDER, deviatingSubshells } from './electronConfig.js';

const BOX_FILL = '#161b22';
const C_UP    = '#e6edf3';
const C_DN    = '#6e7681';
const C_MUTED = '#6e7681';
const C_AXIS  = '#e060b0';
const C_SEP   = '#444c56';
const C_ANN   = '#6e7681';
const GOLD    = '#f0b030';

const BW   = 24;   // orbital box width
const BH   = 22;   // orbital box height
const BGAP = 3;    // gap between boxes in a group
const AX   = 44;   // x-position of the energy axis line
const RIGHT_MARGIN = 34;
const COL_X = { s: 70, p: 120, d: 224, f: 382 };

// Two-zone energy scale
const UPPER_EV = 30;   // linear zone covers 0 to −UPPER_EV eV
const UPPER_PX = 340;  // SVG pixels for the linear upper zone
const CORE_PX  = 130;  // SVG pixels for the compressed core zone
const EMPTY_PX = 80;   // SVG pixels for the schematic unoccupied zone
const SEP_PX   = 14;   // height of each sawtooth separator stripe
const PAD_TOP  = 10;
const PAD_BOT  = 12;

function orbitalCount(type) { return CAPACITY[type] / 2; }
function groupWidth(type) {
  const n = orbitalCount(type);
  return n * BW + (n - 1) * BGAP;
}
const WIDTH = COL_X.f + groupWidth('f') + RIGHT_MARGIN;

function arrowUp(x, cy, color) {
  return (
    `<line x1="${x}" y1="${cy + 7}" x2="${x}" y2="${cy - 4}" stroke="${color}" stroke-width="1.7" stroke-linecap="round"/>` +
    `<polygon points="${x},${cy - 8} ${x - 3},${cy - 3} ${x + 3},${cy - 3}" fill="${color}"/>`
  );
}
function arrowDown(x, cy, color) {
  return (
    `<line x1="${x}" y1="${cy - 7}" x2="${x}" y2="${cy + 4}" stroke="${color}" stroke-width="1.7" stroke-linecap="round"/>` +
    `<polygon points="${x},${cy + 8} ${x - 3},${cy + 3} ${x + 3},${cy + 3}" fill="${color}"/>`
  );
}

// Sawtooth line used to mark scale breaks between zones.
function zigzag(y) {
  const segs = 26;
  const dx = WIDTH / segs;
  const amp = 2.8;
  const pts = [`0,${y}`];
  for (let i = 1; i <= segs; i++) {
    pts.push(`${(i * dx).toFixed(1)},${(y + (i % 2 === 0 ? -amp : amp)).toFixed(1)}`);
  }
  return `<polyline points="${pts.join(' ')}" fill="none" stroke="${C_SEP}" stroke-width="1.1"/>`;
}

// Draw label and orbital boxes for one subshell centred at cy.
function drawSubshell(out, key, cy, config, deviating) {
  const n       = key[0];
  const type    = key[1];
  const color   = COLORS[type];
  const electrons = config[key] ?? 0;
  const occupied  = electrons > 0;
  const nOrb    = orbitalCount(type);
  const groupX  = COL_X[type];
  const gw      = groupWidth(type);

  if (deviating.has(key)) {
    out.push(`<rect x="${groupX - 4}" y="${cy - BH / 2 - 4}" width="${gw + 8}" height="${BH + 8}" rx="4" fill="none" stroke="${GOLD}" stroke-width="1.3"/>`);
    out.push(`<text x="${groupX + gw + 11}" y="${cy}" font-size="12" fill="${GOLD}" font-family="sans-serif" text-anchor="middle" dominant-baseline="central">★</text>`);
  }

  // Subshell label
  out.push(`<text x="${groupX - 9}" y="${cy}" font-size="11" fill="${occupied ? color : C_MUTED}" font-family="ui-monospace,Menlo,monospace" font-weight="${occupied ? 700 : 400}" text-anchor="end" dominant-baseline="central">${n}${type}</text>`);

  // Orbital boxes with Hund-filled spin arrows
  const paired  = Math.max(0, electrons - nOrb);
  const singles = Math.min(electrons, nOrb);
  for (let o = 0; o < nOrb; o++) {
    const boxX  = groupX + o * (BW + BGAP);
    const boxCx = boxX + BW / 2;
    out.push(`<rect x="${boxX}" y="${cy - BH / 2}" width="${BW}" height="${BH}" rx="3" fill="${BOX_FILL}" stroke="${color}" stroke-width="1.2" opacity="${occupied ? 1 : 0.35}"/>`);
    if (o < paired)       { out.push(arrowUp(boxCx - 5, cy, C_UP)); out.push(arrowDown(boxCx + 5, cy, C_DN)); }
    else if (o < singles) { out.push(arrowUp(boxCx, cy, C_UP)); }
  }
}

// element: { Z, 'Aufbau anomaly', … }  config: { '1s': 2, … }
// options.orbitalEnergies: { "Z": { "1s": eV, … }, … }  (from orbital_energies.json)
// options.showEmptySubshells: boolean
export function drawEnergyLevels(element, config, options = {}) {
  const { orbitalEnergies = {}, showEmptySubshells = false } = options;
  const energies = orbitalEnergies[String(element.Z)] ?? {};
  const hasData  = Object.keys(energies).length > 0;

  const isAnomaly = element['Aufbau anomaly'] === 'Yes (★)';
  const deviating = isAnomaly ? new Set(deviatingSubshells(element.Z, config)) : new Set();

  // ── No NIST data (Z > 92): fall back to uniform Madelung spacing ──────────
  if (!hasData) return drawUniform(config, deviating);

  // ── Classify subshells ────────────────────────────────────────────────────
  const occupiedKeys = FILLING_ORDER.filter(k => (config[k] ?? 0) > 0);
  const emptyKeys    = showEmptySubshells
    ? FILLING_ORDER.filter(k => (config[k] ?? 0) === 0)
    : [];

  // Split occupied subshells into valence (upper zone) and core (compressed zone).
  // Shallowest core goes at the top of the core zone.
  const valenceKeys = occupiedKeys.filter(k => energies[k] != null && energies[k] >= -UPPER_EV);
  const coreKeys    = occupiedKeys
    .filter(k => energies[k] != null && energies[k] < -UPPER_EV)
    .sort((a, b) => energies[b] - energies[a]);

  // ── Compute vertical zone layout (y increases downward in SVG) ────────────
  let y = PAD_TOP;

  const showEmpty = emptyKeys.length > 0;
  const emptyTop  = y;
  if (showEmpty) y += EMPTY_PX + SEP_PX;

  const upperTop = y;
  const upperBot = y + UPPER_PX;
  y = upperBot;

  const showCore = coreKeys.length > 0;
  let coreTop = 0;
  if (showCore) { y += SEP_PX; coreTop = y; y += CORE_PX; }

  const HEIGHT = y + PAD_BOT;

  // ── Y-coordinate helpers ──────────────────────────────────────────────────
  // 0 eV → upperTop,  −UPPER_EV → upperBot
  const yVal   = ev => upperTop + UPPER_PX * (-ev) / UPPER_EV;
  // Core subshells evenly spaced, shallowest at top
  const yCore  = i  => coreTop + CORE_PX * (i + 0.5) / coreKeys.length;
  // Empty subshells evenly spaced; first Madelung empty at bottom (nearest to 0 eV)
  const yEmpty = i  => emptyTop + EMPTY_PX * (1 - (i + 0.5) / emptyKeys.length);

  const out = [];

  // ── Zone separators ───────────────────────────────────────────────────────
  if (showEmpty) {
    out.push(zigzag(emptyTop + EMPTY_PX + SEP_PX / 2));
    out.push(`<text x="${WIDTH / 2}" y="${emptyTop + EMPTY_PX + SEP_PX * 0.82}" font-size="12" fill="${C_ANN}" font-family="sans-serif" text-anchor="middle">unoccupied — schematic order only</text>`);
  }
  if (showCore) {
    out.push(zigzag(upperBot + SEP_PX / 2));
    out.push(`<text x="${WIDTH / 2}" y="${upperBot + SEP_PX * 0.82}" font-size="12" fill="${C_ANN}" font-family="sans-serif" text-anchor="middle">core levels — compressed, not to scale</text>`);
  }

  // ── Energy axis (upper zone only) ─────────────────────────────────────────
  out.push(`<line x1="${AX}" y1="${upperTop}" x2="${AX}" y2="${upperBot}" stroke="${C_AXIS}" stroke-width="1.5"/>`);
  out.push(`<polygon points="${AX - 4},${upperTop + 6} ${AX + 4},${upperTop + 6} ${AX},${upperTop - 3}" fill="${C_AXIS}"/>`);

  // Tick marks at 0, −10, −20, −30 eV
  for (const absEv of [0, 10, 20, 30]) {
    const ty  = yVal(-absEv);
    const lbl = absEv === 0 ? '0' : `−${absEv}`;
    out.push(`<line x1="${AX - 5}" y1="${ty}" x2="${AX}" y2="${ty}" stroke="${C_AXIS}" stroke-width="1"/>`);
    out.push(`<text x="${AX - 7}" y="${ty}" font-size="12" fill="${C_AXIS}" font-family="sans-serif" text-anchor="end" dominant-baseline="central">${lbl}</text>`);
  }

  // Axis label "eV" (rotated)
  const axMid = (upperTop + upperBot) / 2;
  out.push(`<text x="${AX - 18}" y="${axMid}" font-size="13" fill="${C_AXIS}" font-family="sans-serif" text-anchor="middle" transform="rotate(-90 ${AX - 18} ${axMid})">eV</text>`);

  // Faint dashed line at 0 eV (ionization threshold)
  out.push(`<line x1="${AX}" y1="${upperTop}" x2="${WIDTH - 10}" y2="${upperTop}" stroke="${C_AXIS}" stroke-width="0.5" stroke-dasharray="3,5" opacity="0.3"/>`);

  // ── Draw subshells ────────────────────────────────────────────────────────
  for (const key of valenceKeys) {
    drawSubshell(out, key, yVal(energies[key]), config, deviating);
  }
  coreKeys.forEach((key, i)  => drawSubshell(out, key, yCore(i),  config, deviating));
  emptyKeys.forEach((key, i) => drawSubshell(out, key, yEmpty(i), config, deviating));

  return { body: out.join('\n'), width: WIDTH, height: HEIGHT };
}

// Fallback: uniform Madelung spacing (for Z > 92 where no NIST data exists).
function drawUniform(config, deviating) {
  const ROW_H = 30, TOP = 8, BOT = 14;
  const HEIGHT = TOP + FILLING_ORDER.length * ROW_H + BOT;
  const rowY   = i => HEIGHT - BOT - i * ROW_H - ROW_H / 2;

  const out    = [];
  const axTop  = rowY(FILLING_ORDER.length - 1) - ROW_H / 2;
  const axBot  = rowY(0) + ROW_H / 2;
  out.push(`<line x1="${AX}" y1="${axBot}" x2="${AX}" y2="${axTop}" stroke="${C_AXIS}" stroke-width="1.5"/>`);
  out.push(`<polygon points="${AX - 4},${axTop + 6} ${AX + 4},${axTop + 6} ${AX},${axTop - 3}" fill="${C_AXIS}"/>`);
  const axMid = (axTop + axBot) / 2;
  out.push(`<text x="${AX - 9}" y="${axMid}" font-size="13" fill="${C_AXIS}" font-family="sans-serif" text-anchor="middle" transform="rotate(-90 ${AX - 9} ${axMid})">energy</text>`);

  FILLING_ORDER.forEach((key, i) => drawSubshell(out, key, rowY(i), config, deviating));

  return { body: out.join('\n'), width: WIDTH, height: HEIGHT };
}
