// Compose the Bohr shell diagram and the subshell energy ladder side by side
// into a single SVG, so they share one pan/zoom viewer and one viewBox.

import { drawBohrShell } from './bohrShellSvg.js';
import { drawEnergyLevels } from './energyLevelSvg.js';

const BG = '#0d1117';
const MARGIN = 24;
const GAP = 36;
const TITLE_H = 36;
const BOHR_SCALE = 1.815;
const ENERGY_SCALE = 0.85;

export function buildShellDiagramsSvg(element, config, options = {}) {
  const bohr = drawBohrShell(element, config, options);
  const energy = drawEnergyLevels(element, config);

  const bohrW = bohr.width * BOHR_SCALE;
  const bohrH = bohr.height * BOHR_SCALE;
  const energyW = energy.width * ENERGY_SCALE;
  const energyH = energy.height * ENERGY_SCALE;

  const contentH = Math.max(bohrH, energyH);
  const totalH = TITLE_H + contentH;
  const totalW = MARGIN + bohrW + GAP + energyW + MARGIN;

  const bohrX = MARGIN;
  const bohrY = TITLE_H + (contentH - bohrH) / 2;
  const energyX = MARGIN + bohrW + GAP;
  const energyY = TITLE_H + (contentH - energyH) / 2;

  const out = [];
  out.push('<?xml version="1.0" encoding="utf-8"?>');
  out.push(`<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 ${totalW.toFixed(1)} ${totalH.toFixed(1)}">`);
  out.push(`<rect width="${totalW.toFixed(1)}" height="${totalH.toFixed(1)}" fill="${BG}"/>`);
  out.push(`<text x="${(totalW / 2).toFixed(1)}" y="${TITLE_H - 10}" font-size="22" fill="#6e7681" font-family="sans-serif" text-anchor="middle">Bohr shell model &amp; Subshell energy ladder</text>`);
  out.push(`<g transform="translate(${bohrX.toFixed(1)} ${bohrY.toFixed(1)}) scale(${BOHR_SCALE})">`);
  out.push(bohr.body);
  out.push('</g>');
  out.push(`<g transform="translate(${energyX.toFixed(1)} ${energyY.toFixed(1)}) scale(${ENERGY_SCALE})">`);
  out.push(energy.body);
  out.push('</g>');
  out.push('</svg>');
  return out.join('\n') + '\n';
}
