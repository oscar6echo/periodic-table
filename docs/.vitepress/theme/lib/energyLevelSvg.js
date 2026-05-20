// Draw a subshell energy-level diagram as a positioned SVG fragment.
// Subshells are stacked in Madelung (n+l) filling order (1s at the bottom).
// Each subshell shows its orbitals as boxes filled with up/down spin arrows;
// box-group width is proportional to subshell capacity.
// Returns { body, width, height } — SVG elements in a local (0,0)-origin box,
// with no <svg> wrapper, so the composite builder can place it.

import { CAPACITY, COLORS, FILLING_ORDER, deviatingSubshells } from './electronConfig.js';

const BOX_FILL = '#161b22';
const C_UP = '#e6edf3'; // up-arrow — bright
const C_DN = '#6e7681'; // down-arrow — muted
const C_MUTED = '#6e7681';
const C_AXIS = '#e060b0';
const GOLD = '#f0b030';

const BW = 24; // orbital box width
const BH = 22; // orbital box height
const BGAP = 3; // gap between orbital boxes
const ROW_H = 30;
const TOP = 8;
const BOTTOM = 14;
const AX = 34; // energy-axis x
const RIGHT_MARGIN = 34;

const COL_X = { s: 70, p: 120, d: 224, f: 382 };

function orbitalCount(type) {
  return CAPACITY[type] / 2;
}

function groupWidth(type) {
  const n = orbitalCount(type);
  return n * BW + (n - 1) * BGAP;
}

const HEIGHT = TOP + FILLING_ORDER.length * ROW_H + BOTTOM;
const WIDTH = COL_X.f + groupWidth('f') + RIGHT_MARGIN;

// Lowest-energy subshell (1s) sits at the bottom.
function rowCenterY(rowIndex) {
  return HEIGHT - BOTTOM - rowIndex * ROW_H - ROW_H / 2;
}

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

// element: { Z, "Aufbau anomaly", ... }, config: { "1s": 2, ... } from parseConfig().
export function drawEnergyLevels(element, config) {
  const isAnomaly = element['Aufbau anomaly'] === 'Yes (★)';
  const deviating = isAnomaly ? new Set(deviatingSubshells(element.Z, config)) : new Set();

  const out = [];

  // Energy axis (points up: low energy at the bottom).
  const axTop = rowCenterY(FILLING_ORDER.length - 1) - ROW_H / 2;
  const axBottom = rowCenterY(0) + ROW_H / 2;
  out.push(`<line x1="${AX}" y1="${axBottom}" x2="${AX}" y2="${axTop}" stroke="${C_AXIS}" stroke-width="1.5"/>`);
  out.push(`<polygon points="${AX - 4},${axTop + 6} ${AX + 4},${axTop + 6} ${AX},${axTop - 3}" fill="${C_AXIS}"/>`);
  const axMid = (axTop + axBottom) / 2;
  out.push(`<text x="${AX - 9}" y="${axMid}" font-size="9" fill="${C_AXIS}" font-family="sans-serif" text-anchor="middle" transform="rotate(-90 ${AX - 9} ${axMid})">energy</text>`);

  // Subshell rows, bottom (1s) to top (7p).
  FILLING_ORDER.forEach((key, rowIndex) => {
    const n = key[0];
    const type = key[1];
    const cy = rowCenterY(rowIndex);
    const electrons = config[key] ?? 0;
    const occupied = electrons > 0;
    const color = COLORS[type];
    const nOrb = orbitalCount(type);
    const groupX = COL_X[type];
    const gw = groupWidth(type);

    // Aufbau-exception highlight around the box group.
    if (deviating.has(key)) {
      out.push(`<rect x="${groupX - 4}" y="${cy - BH / 2 - 4}" width="${gw + 8}" height="${BH + 8}" rx="4" fill="none" stroke="${GOLD}" stroke-width="1.3"/>`);
      out.push(`<text x="${groupX + gw + 11}" y="${cy}" font-size="12" fill="${GOLD}" font-family="sans-serif" text-anchor="middle" dominant-baseline="central">★</text>`);
    }

    // Subshell label.
    out.push(`<text x="${groupX - 9}" y="${cy}" font-size="11" fill="${occupied ? color : C_MUTED}" font-family="ui-monospace,Menlo,monospace" font-weight="${occupied ? 700 : 400}" text-anchor="end" dominant-baseline="central">${n}${type}</text>`);

    // Orbital boxes with Hund-filled spin arrows.
    const paired = Math.max(0, electrons - nOrb); // orbitals holding a pair
    const singles = Math.min(electrons, nOrb); // orbitals holding at least one
    for (let o = 0; o < nOrb; o++) {
      const boxX = groupX + o * (BW + BGAP);
      const boxCx = boxX + BW / 2;
      out.push(`<rect x="${boxX}" y="${cy - BH / 2}" width="${BW}" height="${BH}" rx="3" fill="${BOX_FILL}" stroke="${color}" stroke-width="1.2" opacity="${occupied ? 1 : 0.5}"/>`);
      if (o < paired) {
        out.push(arrowUp(boxCx - 5, cy, C_UP));
        out.push(arrowDown(boxCx + 5, cy, C_DN));
      } else if (o < singles) {
        out.push(arrowUp(boxCx, cy, C_UP));
      }
    }
  });

  return { body: out.join('\n'), width: WIDTH, height: HEIGHT };
}
