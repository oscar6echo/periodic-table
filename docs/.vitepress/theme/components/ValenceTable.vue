<script setup>
import { ref, computed, onMounted } from 'vue'

const SUPS = { '⁰':0, '¹':1, '²':2, '³':3, '⁴':4, '⁵':5, '⁶':6, '⁷':7, '⁸':8, '⁹':9 }
const MAX = { s: 2, p: 6, d: 10, f: 14 }
const COLORS = { s: '#f78166', p: '#79c0ff', d: '#56d364', f: '#d2a8ff' }
const SUBSHELLS = ['s', 'p', 'd', 'f']

// Match <shell_number><subshell_letter><superscript_count> in the original unicode string.
// We must NOT normalize superscripts first — regular digits (shell numbers like "2" in "2p")
// must stay separate from electron counts (superscript digits like "²").
const SUBSHELL_RE = /\d+([spdf])([⁰¹²³⁴⁵⁶⁷⁸⁹]+)/g
const supToNum = s => parseInt(s.split('').map(c => SUPS[c]).join(''))

function parseValenceConfig(config) {
  if (!config) return { s: null, p: null, d: null, f: null }
  const result = { s: null, p: null, d: null, f: null }
  SUBSHELL_RE.lastIndex = 0
  let m
  while ((m = SUBSHELL_RE.exec(config)) !== null) {
    const type = m[1]
    const count = supToNum(m[2])
    result[type] = (result[type] ?? 0) + count
  }
  return result
}

const elements = ref([])
const search = ref('')

const enriched = computed(() =>
  elements.value.map(el => ({
    ...el,
    counts: parseValenceConfig(el['Valence config']),
    isAnomaly: el['Aufbau anomaly'] === 'Yes (★)'
  }))
)

const filtered = computed(() => {
  const q = search.value.trim().toLowerCase()
  if (!q) return enriched.value
  return enriched.value.filter(el =>
    String(el.Z).startsWith(q) ||
    el.symbol.toLowerCase().includes(q) ||
    el.name.toLowerCase().includes(q)
  )
})

onMounted(async () => {
  try {
    const res = await fetch('/periodic-table/data/elements.json')
    elements.value = await res.json()
  } catch (e) {
    console.error('ValenceTable: failed to load elements.json', e)
  }
})
</script>

<template>
  <div class="vt-wrapper">
    <div class="vt-search">
      <input
        v-model="search"
        type="text"
        placeholder="Search by Z, symbol, or name…"
        class="vt-input"
        autocomplete="off"
        spellcheck="false"
      />
      <span class="vt-count">{{ filtered.length }} / 118</span>
    </div>

    <div class="vt-scroll">
      <table class="vt-table">
        <thead>
          <tr>
            <th class="col-z">Z</th>
            <th class="col-sym">Symbol</th>
            <th class="col-name">Name</th>
            <th
              v-for="sub in SUBSHELLS"
              :key="sub"
              class="col-sub"
              :style="`color: ${COLORS[sub]}`"
            >{{ sub }}</th>
          </tr>
        </thead>
        <tbody>
          <tr
            v-for="el in filtered"
            :key="el.Z"
            :class="{ 'row-anomaly': el.isAnomaly }"
          >
            <td class="col-z">{{ el.Z }}</td>
            <td class="col-sym">
              {{ el.symbol }}<span v-if="el.isAnomaly" class="anomaly-star" title="Aufbau exception">★</span>
            </td>
            <td class="col-name">{{ el.name }}</td>
            <td v-for="sub in SUBSHELLS" :key="sub" class="col-sub">
              <template v-if="el.counts[sub] !== null">
                <div class="fill-cell" :style="`--bar-color: ${COLORS[sub]}`">
                  <div class="fill-bar">
                    <div class="fill-track"></div>
                    <div
                      class="fill-filled"
                      :style="`width: ${(el.counts[sub] / MAX[sub]) * 100}%`"
                    ></div>
                  </div>
                  <span class="fill-label">{{ el.counts[sub] }}/{{ MAX[sub] }}</span>
                </div>
              </template>
              <span v-else class="fill-absent">—</span>
            </td>
          </tr>
        </tbody>
      </table>
    </div>
  </div>
</template>

<style scoped>
.vt-wrapper {
  font-family: var(--vp-font-family-mono, ui-monospace, monospace);
  font-size: 13px;
  border: 1px solid #30363d;
  border-radius: 8px;
  overflow: hidden;
  background: #0d1117;
  margin: 1.5rem 0;
}

.vt-search {
  display: flex;
  align-items: center;
  gap: 12px;
  padding: 10px 12px;
  border-bottom: 1px solid #30363d;
  background: #161b22;
}

.vt-input {
  flex: 1;
  background: #0d1117;
  border: 1px solid #30363d;
  border-radius: 5px;
  color: #e6edf3;
  padding: 6px 10px;
  font-size: 13px;
  font-family: inherit;
  outline: none;
}
.vt-input:focus {
  border-color: #58a6ff;
  box-shadow: 0 0 0 2px rgba(88, 166, 255, 0.15);
}
.vt-input::placeholder {
  color: #484f58;
}

.vt-count {
  color: #6e7681;
  font-size: 12px;
  white-space: nowrap;
}

.vt-scroll {
  min-height: 300px;
  max-height: 62vh;
  overflow-y: auto;
  overflow-x: auto;
}

.vt-table {
  width: 100%;
  border-collapse: collapse;
  table-layout: fixed;
}

thead th {
  position: sticky;
  top: 0;
  background: #161b22;
  border-bottom: 2px solid #30363d;
  padding: 7px 6px;
  text-align: center;
  font-weight: 700;
  letter-spacing: 0.05em;
  z-index: 2;
}

.col-z   { width: 38px; text-align: right; }
.col-sym { width: 58px; text-align: center; }
.col-name { width: 118px; text-align: left; padding-left: 8px; }
.col-sub { width: 92px; text-align: left; padding: 4px 4px; }

tbody tr {
  border-bottom: 1px solid #21262d;
}
tbody tr:hover {
  background: #161b22;
}
tbody tr.row-anomaly {
  border-left: 3px solid #f0b030;
}

td {
  padding: 4px 6px;
  vertical-align: middle;
  color: #e6edf3;
}

td.col-z {
  color: #6e7681;
  text-align: right;
}
td.col-sym {
  font-weight: 600;
  text-align: center;
}
td.col-name {
  color: #c9d1d9;
  padding-left: 8px;
}

.anomaly-star {
  color: #f0b030;
  margin-left: 2px;
  font-size: 10px;
  vertical-align: super;
}

.fill-cell {
  display: flex;
  align-items: center;
  gap: 5px;
}

.fill-bar {
  flex: 1;
  height: 10px;
  position: relative;
  border-radius: 3px;
  overflow: hidden;
  min-width: 30px;
}

.fill-track {
  position: absolute;
  inset: 0;
  background: var(--bar-color);
  opacity: 0.18;
}

.fill-filled {
  position: absolute;
  left: 0;
  top: 0;
  bottom: 0;
  background: var(--bar-color);
  opacity: 0.85;
  border-radius: 3px;
  min-width: 2px;
}

.fill-label {
  font-size: 11px;
  color: #6e7681;
  white-space: nowrap;
  min-width: 30px;
  text-align: right;
}

.fill-absent {
  display: block;
  text-align: center;
  color: #30363d;
}
</style>
