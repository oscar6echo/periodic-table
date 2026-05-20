// Electron-configuration parsing and Aufbau utilities.
// Logic ported from dev/gen/gen_bohr_shells.py.

export const CAPACITY = { s: 2, p: 6, d: 10, f: 14 };

// Subshell type colors (GitHub dark palette, matching section 6.7 ValenceTable).
export const COLORS = { s: '#f78166', p: '#79c0ff', d: '#56d364', f: '#d2a8ff' };

// Madelung (n+l) filling order — the 19 subshells that exist in practice, 1s first.
export const FILLING_ORDER = [
  '1s', '2s', '2p', '3s', '3p', '4s', '3d', '4p', '5s', '4d',
  '5p', '6s', '4f', '5d', '6p', '7s', '5f', '6d', '7p',
];

// Subshell types that exist in practice, grouped by principal shell n.
export const SHELL_SUBSHELLS = {
  1: ['s'],
  2: ['s', 'p'],
  3: ['s', 'p', 'd'],
  4: ['s', 'p', 'd', 'f'],
  5: ['s', 'p', 'd', 'f'],
  6: ['s', 'p', 'd'],
  7: ['s', 'p'],
};

const NOBLE_GAS_CONFIGS = {
  He: '1s2',
  Ne: '1s2 2s2 2p6',
  Ar: '1s2 2s2 2p6 3s2 3p6',
  Kr: '1s2 2s2 2p6 3s2 3p6 3d10 4s2 4p6',
  Xe: '1s2 2s2 2p6 3s2 3p6 3d10 4s2 4p6 4d10 5s2 5p6',
  Rn: '1s2 2s2 2p6 3s2 3p6 3d10 4s2 4p6 4d10 5s2 5p6 4f14 5d10 6s2 6p6',
  Og: '1s2 2s2 2p6 3s2 3p6 3d10 4s2 4p6 4d10 5s2 5p6 4f14 5d10 6s2 6p6 5f14 6d10 7s2 7p6',
};

const SUPERSCRIPTS = {
  '⁰': '0', '¹': '1', '²': '2', '³': '3', '⁴': '4',
  '⁵': '5', '⁶': '6', '⁷': '7', '⁸': '8', '⁹': '9',
};

// Expand a noble-gas abbreviation, e.g. "[Ar] 3d6 4s2" -> "1s2 2s2 ... 3p6 3d6 4s2".
export function expandNobleGas(configStr) {
  if (!configStr) return configStr;
  let out = configStr;
  for (const [symbol, noble] of Object.entries(NOBLE_GAS_CONFIGS)) {
    if (out.includes(`[${symbol}]`)) {
      out = out.replace(`[${symbol}]`, noble + ' ');
    }
  }
  return out;
}

// Parse an electron-configuration string into { "1s": 2, "2s": 2, "2p": 6, ... },
// keyed by <n><subshell>. Handles noble-gas cores and Unicode superscripts.
export function parseConfig(configStr) {
  if (!configStr) return {};
  let str = expandNobleGas(configStr);
  for (const [sup, digit] of Object.entries(SUPERSCRIPTS)) {
    str = str.split(sup).join(digit);
  }
  const result = {};
  const re = /(\d+)([spdf])(\d+)/g;
  let m;
  while ((m = re.exec(str)) !== null) {
    const key = `${m[1]}${m[2]}`;
    result[key] = (result[key] ?? 0) + parseInt(m[3], 10);
  }
  return result;
}

// Predict the ground-state configuration for atomic number Z by filling
// electrons strictly in Madelung (n+l) order. Returns the same dict shape
// as parseConfig — used to diff against the actual config for exception marks.
export function predictAufbauConfig(Z) {
  const result = {};
  let remaining = Z;
  for (const key of FILLING_ORDER) {
    if (remaining <= 0) break;
    const type = key[key.length - 1];
    const fill = Math.min(remaining, CAPACITY[type]);
    result[key] = fill;
    remaining -= fill;
  }
  return result;
}

// Highest principal shell n that holds at least one electron.
export function maxShell(config) {
  let max = 0;
  for (const key of Object.keys(config)) {
    const n = parseInt(key[0], 10);
    if (n > max) max = n;
  }
  return max;
}

// Subshell keys (e.g. "3d", "4s") whose actual count differs from the
// Aufbau prediction for the given Z. Used to mark Aufbau exceptions.
export function deviatingSubshells(Z, config) {
  const predicted = predictAufbauConfig(Z);
  const keys = new Set([...Object.keys(predicted), ...Object.keys(config)]);
  const out = [];
  for (const key of keys) {
    if ((predicted[key] ?? 0) !== (config[key] ?? 0)) out.push(key);
  }
  return out;
}
