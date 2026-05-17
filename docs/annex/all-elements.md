---
layout: page
---

<script setup>
import { ref, onMounted, computed } from 'vue'
import { withBase } from 'vitepress'

const elements = ref([])
const search = ref('')
const sortKey = ref('Z')
const sortDir = ref(1)

const props = ['symbol', 'name', 'Z', 'Category', 'Block', 'Atomic mass',
  'Electron configuration', 'Valence config', 'Aufbau anomaly',
  'Electronegativity (EN)', '1st ionization energy (IE1)',
  'Melting point', 'Boiling point', 'Density',
  'Electron affinity', 'Discovery year',
  'Common oxidation states', 'Key uses / notes']

const filtered = computed(() => {
  let list = [...elements.value]
  if (search.value) {
    const q = search.value.toLowerCase()
    list = list.filter(e => props.some(p => {
      const v = e[p]
      return v && String(v).toLowerCase().includes(q)
    }))
  }
  list.sort((a, b) => {
    const ak = a[sortKey.value]
    const bk = b[sortKey.value]
    if (ak === undefined && bk === undefined) return 0
    if (ak === undefined) return 1
    if (bk === undefined) return -1
    const an = parseFloat(ak)
    const bn = parseFloat(bk)
    if (!isNaN(an) && !isNaN(bn)) return (an - bn) * sortDir.value
    return String(ak).localeCompare(String(bk)) * sortDir.value
  })
  return list
})

function toggleSort(key) {
  if (sortKey.value === key) sortDir.value *= -1
  else { sortKey.value = key; sortDir.value = 1 }
}

function arrow(key) {
  return sortKey.value === key ? (sortDir.value === 1 ? ' ↑' : ' ↓') : ''
}

onMounted(async () => {
  const res = await fetch(withBase('/data/elements.json'))
  elements.value = await res.json()
})
</script>

<div class="page-header">
  <h1 class="page-title">All Elements</h1>
  <p class="page-subtitle">All 118 elements with physical, chemical, and quantum properties.</p>
</div>

<details class="legend" open>
<summary>Legend &amp; Column Notes</summary>
<div class="legend-body">
<div class="legend-grid">

  <div class="legend-section">
    <div class="legend-title">Categories (11)</div>
    <div class="cat-list">
      <span>Alkali metal</span>
      <span>Alkaline earth metal</span>
      <span>Transition metal</span>
      <span>Post-transition metal</span>
      <span>Metalloid</span>
      <span>Nonmetal</span>
      <span>Halogen</span>
      <span>Noble gas</span>
      <span>Lanthanide</span>
      <span>Actinide</span>
      <span>Unknown (predicted)</span>
    </div>
  </div>

  <div class="legend-section">
    <div class="legend-title">Blocks</div>
    <div class="block-list">
      <div><span class="block-tag block-s">s</span> Groups 1–2 + He — valence e⁻ in s subshell</div>
      <div><span class="block-tag block-p">p</span> Groups 13–18 — valence e⁻ in p subshell</div>
      <div><span class="block-tag block-d">d</span> Groups 3–12 (transition metals) — d subshell filling</div>
      <div><span class="block-tag block-f">f</span> Lanthanides &amp; actinides — f subshell filling</div>
    </div>
  </div>

  <div class="legend-section legend-section--wide">
    <div class="legend-title">Column notes</div>
    <dl class="col-notes">
      <dt>Valence config</dt>
      <dd>outermost subshells only — the chemically active electrons (e.g. 2s²2p⁴ for O)</dd>
      <dt>Anomaly ★</dt>
      <dd>Aufbau / Madelung exception — 10 elements (Cr, Cu, Nb, Mo, Ru, Rh, Pd, Ag, Pt, Au) adopt a configuration that deviates from the n+ℓ filling rule to gain extra stability via a half-filled or fully filled d subshell (e.g. Cr: [Ar] 3d⁵4s¹ instead of [Ar] 3d⁴4s²)</dd>
      <dt>EN</dt>
      <dd>Pauling electronegativity — dimensionless scale; F = 3.98 (highest), Cs = 0.79 (lowest)</dd>
      <dt>IE1 (eV)</dt>
      <dd>1st ionization energy — minimum energy to remove one electron from a neutral gas-phase atom; 1 eV = 96.485 kJ mol⁻¹</dd>
      <dt>Oxidation states</dt>
      <dd>formal charge assuming fully ionic bonds (+2 = donates 2 e⁻; −1 = accepts 1 e⁻)</dd>
      <dt>Melting / Boiling</dt>
      <dd>in °C at standard pressure (101.325 kPa)</dd>
      <dt>Density</dt>
      <dd>in g/cm³ for solids &amp; liquids; g/L for gases — unit included in cell value</dd>
      <dt>El. affinity</dt>
      <dd>energy released (eV) when a neutral atom gains one electron; blank if thermodynamically unstable or unmeasured</dd>
    </dl>
  </div>

</div>
</div>
</details>

<div class="search-bar">
  <input v-model="search" placeholder="Search by name, symbol, Z, category, or any property..." class="search-input" />
  <span class="count">{{ filtered.length }} / {{ elements.length }} elements</span>
</div>

<div class="table-wrapper">
  <table class="elements-table">
    <thead>
      <tr>
        <th @click="toggleSort('Z')" class="sortable th-num">Z{{ arrow('Z') }}</th>
        <th @click="toggleSort('symbol')" class="sortable th-ctr">Symbol{{ arrow('symbol') }}</th>
        <th @click="toggleSort('name')" class="sortable th-left">Name{{ arrow('name') }}</th>
        <th @click="toggleSort('Category')" class="sortable th-left">Category{{ arrow('Category') }}</th>
        <th @click="toggleSort('Block')" class="sortable th-ctr">Block{{ arrow('Block') }}</th>
        <th class="th-num">Mass</th>
        <th class="th-left">Electron Config</th>
        <th class="th-left">Valence</th>
        <th @click="toggleSort('Aufbau anomaly')" class="sortable th-ctr">Anomaly{{ arrow('Aufbau anomaly') }}</th>
        <th @click="toggleSort('Electronegativity (EN)')" class="sortable th-num">EN{{ arrow('Electronegativity (EN)') }}</th>
        <th @click="toggleSort('1st ionization energy (IE1)')" class="sortable th-num">IE1 (eV){{ arrow('1st ionization energy (IE1)') }}</th>
        <th class="th-left">Oxidation States</th>
        <th class="th-right">Melting (°C)</th>
        <th class="th-right">Boiling (°C)</th>
        <th class="th-left">Density</th>
        <th class="th-right">El. Affinity (eV)</th>
        <th @click="toggleSort('Discovery year')" class="sortable th-num">Discovery{{ arrow('Discovery year') }}</th>
        <th class="th-left">Uses / Notes</th>
      </tr>
    </thead>
    <tbody>
      <tr v-for="el in filtered" :key="el.Z">
        <td class="td-num">{{ el.Z }}</td>
        <td class="td-sym">{{ el.symbol }}</td>
        <td class="td-left">{{ el.name }}</td>
        <td class="td-left">{{ el.Category }}</td>
        <td class="td-ctr">
          <span :class="'block-tag block-' + (el.Block || '').toLowerCase()">{{ el.Block }}</span>
        </td>
        <td class="td-num">{{ el['Atomic mass'] }}</td>
        <td class="td-mono">{{ el['Electron configuration'] }}</td>
        <td class="td-mono">{{ el['Valence config'] }}</td>
        <td class="td-ctr">
          <span v-if="el['Aufbau anomaly'] === 'Yes (★)'" class="anomaly-tag">★</span>
          <span v-else class="dash">—</span>
        </td>
        <td class="td-num">{{ el['Electronegativity (EN)'] }}</td>
        <td class="td-num">{{ el['1st ionization energy (IE1)'] }}</td>
        <td class="td-left">{{ el['Common oxidation states'] }}</td>
        <td class="td-right">{{ el['Melting point'] }}</td>
        <td class="td-right">{{ el['Boiling point'] }}</td>
        <td class="td-left">{{ el['Density'] }}</td>
        <td class="td-right">{{ el['Electron affinity'] }}</td>
        <td class="td-num">{{ el['Discovery year'] }}</td>
        <td class="td-notes">{{ el['Key uses / notes'] }}</td>
      </tr>
    </tbody>
  </table>
</div>

<style>
/* ---- Page header ---- */
.page-header {
  margin-bottom: 28px;
}
.page-title {
  font-size: 32px;
  font-weight: 700;
  letter-spacing: -0.02em;
  line-height: 1.2;
  color: var(--vp-c-text-1);
  margin: 0 0 10px;
  padding: 0;
  border: none;
}
.page-subtitle {
  font-size: 16px;
  color: var(--vp-c-text-2);
  line-height: 1.6;
  margin: 0;
}

/* ---- Legend ---- */
details.legend {
  border: 1px solid var(--vp-c-border);
  border-radius: 8px;
  margin-bottom: 20px;
  background: var(--vp-c-bg-elv);
}
details.legend summary {
  padding: 10px 16px;
  cursor: pointer;
  font-weight: 600;
  font-size: 14px;
  color: var(--vp-c-text-1);
  user-select: none;
  list-style: none;
}
details.legend summary::before {
  content: '▶ ';
  font-size: 10px;
  color: var(--vp-c-text-3);
  margin-right: 4px;
}
details.legend[open] summary::before {
  content: '▼ ';
}
.legend-body {
  padding: 12px 16px 16px;
  border-top: 1px solid var(--vp-c-border);
}
.legend-grid {
  display: flex;
  gap: 28px;
  flex-wrap: wrap;
  align-items: flex-start;
}
.legend-section {
  min-width: 190px;
}
.legend-section--wide {
  flex: 1;
  min-width: 340px;
}
.legend-title {
  font-weight: 700;
  font-size: 11px;
  text-transform: uppercase;
  letter-spacing: 0.07em;
  color: var(--vp-c-text-3);
  margin-bottom: 8px;
}
.cat-list {
  display: flex;
  flex-direction: column;
  gap: 3px;
  font-size: 13px;
  color: var(--vp-c-text-2);
}
.block-list {
  display: flex;
  flex-direction: column;
  gap: 7px;
  font-size: 13px;
  color: var(--vp-c-text-2);
}
.block-list > div {
  display: flex;
  align-items: center;
  gap: 8px;
}
.col-notes {
  display: grid;
  grid-template-columns: max-content 1fr;
  gap: 5px 14px;
  font-size: 13px;
  margin: 0;
}
.col-notes dt {
  font-weight: 600;
  color: var(--vp-c-text-1);
  white-space: nowrap;
  padding-top: 1px;
}
.col-notes dd {
  color: var(--vp-c-text-2);
  margin: 0;
  padding-top: 1px;
}

/* ---- Search bar ---- */
.search-bar {
  display: flex;
  align-items: center;
  gap: 12px;
  margin-bottom: 16px;
  flex-wrap: wrap;
}
.search-input {
  flex: 1;
  min-width: 280px;
  padding: 8px 14px;
  border: 1px solid var(--vp-c-border);
  border-radius: 8px;
  background: var(--vp-c-bg-elv);
  color: var(--vp-c-text-1);
  font-size: 14px;
  outline: none;
}
.search-input:focus {
  border-color: var(--vp-c-brand-1);
}
.count {
  font-size: 13px;
  color: var(--vp-c-text-3);
  white-space: nowrap;
}

/* ---- Table ---- */
.table-wrapper {
  overflow-x: scroll;
  overflow-y: auto;
  max-height: 1600px;
  border: 1px solid var(--vp-c-border);
  border-radius: 8px;
}
.elements-table {
  width: 100%;
  border-collapse: collapse;
  font-size: 14px;
  line-height: 1.4;
  min-width: 1900px;
}
.elements-table thead {
  position: sticky;
  top: 0;
  z-index: 2;
}
.elements-table th {
  background: var(--vp-c-bg-elv);
  color: var(--vp-c-text-1);
  padding: 8px 10px;
  white-space: nowrap;
  border-bottom: 2px solid var(--vp-c-border);
  font-size: 13px;
  font-weight: 600;
}
.elements-table th.sortable {
  cursor: pointer;
  user-select: none;
}
.elements-table th.sortable:hover {
  color: var(--vp-c-brand-1);
}
.elements-table td {
  padding: 6px 10px;
  border-bottom: 1px solid #21262d;
  vertical-align: top;
}
.elements-table tbody tr:hover {
  background: #1c2128;
}

/* th alignment */
.th-num   { text-align: right; }
.th-ctr   { text-align: center; }
.th-left  { text-align: left; }
.th-right { text-align: right; }

/* td alignment */
.td-num   { text-align: right;  white-space: nowrap; }
.td-ctr   { text-align: center; white-space: nowrap; }
.td-left  { text-align: left; }
.td-right { text-align: right;  white-space: nowrap; }
.td-sym   { font-weight: 700; color: var(--vp-c-brand-1); text-align: center; white-space: nowrap; }
.td-mono  { font-family: monospace; font-size: 13px; }
.td-notes { max-width: 260px; font-size: 13px; color: var(--vp-c-text-2); }
.dash     { color: var(--vp-c-text-3); font-size: 16px; }

.block-tag {
  display: inline-block;
  padding: 1px 8px;
  border-radius: 4px;
  font-size: 12px;
  font-weight: 600;
}
.block-s { background: #1a0a0a; color: #f78166; border: 1px solid #f7816640; }
.block-p { background: #0a1a00; color: #79c0ff; border: 1px solid #79c0ff40; }
.block-d { background: #0a1428; color: #56d364; border: 1px solid #56d36440; }
.block-f { background: #1e0840; color: #d2a8ff; border: 1px solid #d2a8ff40; }

.anomaly-tag {
  color: #f0b030;
  font-size: 16px;
}
</style>
