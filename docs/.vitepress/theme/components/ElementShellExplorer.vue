<script setup>
import { ref, computed, nextTick, onMounted, onBeforeUnmount } from 'vue'
import { withBase } from 'vitepress'
import PanZoomViewer from './PanZoomViewer.vue'
import { parseConfig } from '../lib/electronConfig.js'
import { buildShellDiagramsSvg } from '../lib/shellDiagramsSvg.js'

const elements = ref([])
const orbitalEnergies = ref({})
const selected = ref(null)
const showAll = ref(true)
const showEmptySubshells = ref(false)
const query = ref('')
const open = ref(false)
const rootEl = ref(null)
const listEl = ref(null)

const sliderZ = computed({
  get: () => selected.value?.Z ?? 1,
  set: (val) => {
    const el = elements.value.find(e => e.Z === Number(val))
    if (el) selected.value = el
  },
})

const filtered = computed(() => {
  const q = query.value.trim().toLowerCase()
  if (!q) return elements.value
  return elements.value.filter(el =>
    String(el.Z).startsWith(q) ||
    el.symbol.toLowerCase().includes(q) ||
    el.name.toLowerCase().includes(q)
  )
})

const config = computed(() =>
  selected.value ? parseConfig(selected.value['Electron configuration']) : {}
)
const diagramsSvg = computed(() =>
  selected.value
    ? buildShellDiagramsSvg(selected.value, config.value, {
        showAllSubshells: showAll.value,
        showEmptySubshells: showEmptySubshells.value,
        orbitalEnergies: orbitalEnergies.value,
      })
    : ''
)
const isAnomaly = computed(() => selected.value?.['Aufbau anomaly'] === 'Yes (★)')

function selectElement(el) {
  selected.value = el
  query.value = ''
  open.value = false
}

function onEnter() {
  if (filtered.value.length) selectElement(filtered.value[0])
}

async function openDropdown() {
  open.value = true
  await nextTick()
  listEl.value?.querySelector('li.selected')?.scrollIntoView({ block: 'nearest' })
}

function onDocClick(e) {
  if (rootEl.value && !rootEl.value.contains(e.target)) open.value = false
}

onMounted(async () => {
  try {
    const [elemRes, energyRes] = await Promise.all([
      fetch(withBase('/data/elements.json')),
      fetch(withBase('/data/orbital_energies.json')),
    ])
    elements.value = await elemRes.json()
    orbitalEnergies.value = await energyRes.json()
    selected.value = elements.value.find(e => e.symbol === 'Fe') || elements.value[0]
  } catch (e) {
    console.error('ElementShellExplorer: failed to load data', e)
  }
  document.addEventListener('click', onDocClick)
})
onBeforeUnmount(() => document.removeEventListener('click', onDocClick))
</script>

<template>
  <div class="ese-wrapper" ref="rootEl">
    <div class="ese-controls">
      <div class="ese-top-row">
        <div class="ese-combo">
          <input
            v-model="query"
            type="text"
            class="ese-input"
            :placeholder="selected ? `${selected.Z} · ${selected.symbol} · ${selected.name}` : 'Search by Z, symbol, or name…'"
            autocomplete="off"
            spellcheck="false"
            @focus="openDropdown"
            @keydown.enter.prevent="onEnter"
            @keydown.esc="open = false"
          />
          <ul v-if="open" ref="listEl" class="ese-list">
            <li
              v-for="el in filtered"
              :key="el.Z"
              class="ese-option"
              :class="{ selected: selected && el.Z === selected.Z }"
              @click="selectElement(el)"
            >
              <span class="opt-z">{{ el.Z }}</span>
              <span class="opt-sym">{{ el.symbol }}</span>
              <span class="opt-name">{{ el.name }}</span>
              <span class="opt-cfg">{{ el['Electron configuration'] }}</span>
              <span class="opt-pg">{{ el['Period / Group (18-col)'] }}</span>
              <span class="opt-star">{{ el['Aufbau anomaly'] === 'Yes (★)' ? '★' : '' }}</span>
            </li>
            <li v-if="!filtered.length" class="ese-empty">No match</li>
          </ul>
        </div>

        <div class="ese-checks">
          <label class="ese-toggle">
            <input type="checkbox" v-model="showAll" />
            show all subshells
          </label>
          <label class="ese-toggle">
            <input type="checkbox" v-model="showEmptySubshells" />
            show empty subshells <span class="ese-badge">energy ladder only</span>
          </label>
        </div>
      </div>

      <div class="ese-slider-row">
        <input type="range" min="1" max="118" v-model="sliderZ" class="ese-slider" />
        <span class="ese-slider-info">
          <span class="si-z">{{ selected?.Z }}</span>
          <span class="si-sym">{{ selected?.symbol }}</span>
          <span class="si-name">{{ selected?.name }}</span>
        </span>
      </div>
    </div>

    <div v-if="selected" class="ese-header">
      <span class="hdr-name">{{ selected.name }}</span>
      <span class="hdr-z">Z = {{ selected.Z }}</span>
      <span class="hdr-cfg">{{ selected['Electron configuration'] }}</span>
      <span v-if="isAnomaly" class="hdr-badge">★ Aufbau exception</span>
    </div>

    <div v-if="selected" class="ese-panels">
      <PanZoomViewer :svg-markup="diagramsSvg" />
    </div>
  </div>
</template>

<style scoped>
.ese-wrapper {
  font-family: var(--vp-font-family-base, ui-sans-serif, system-ui, sans-serif);
  border: 1px solid #30363d;
  border-radius: 8px;
  background: #0d1117;
  margin: 1.5rem 0;
  padding: 12px;
}

.ese-controls {
  display: flex;
  flex-direction: column;
  gap: 0;
}

.ese-top-row {
  display: flex;
  align-items: center;
  gap: 16px;
}

.ese-combo {
  position: relative;
  flex: 1;
  min-width: 240px;
}

.ese-checks {
  display: flex;
  flex-direction: column;
  gap: 6px;
}

.ese-slider-row {
  display: flex;
  align-items: center;
  gap: 12px;
  margin-top: 10px;
}
.ese-slider {
  flex: 1;
  accent-color: #58a6ff;
  cursor: pointer;
}
.ese-slider-info {
  display: flex;
  gap: 8px;
  align-items: center;
  min-width: 160px;
}
.si-z    { color: #6e7681; font-size: 13px; min-width: 28px; text-align: right; }
.si-sym  { font-weight: 700; color: #58a6ff; font-size: 15px; min-width: 30px; }
.si-name { color: #e6edf3; font-size: 13px; }

.ese-input {
  width: 100%;
  background: #161b22;
  border: 1px solid #30363d;
  border-radius: 5px;
  color: #e6edf3;
  padding: 7px 10px;
  font-size: 13px;
  font-family: inherit;
  outline: none;
}
.ese-input:focus {
  border-color: #58a6ff;
  box-shadow: 0 0 0 2px rgba(88, 166, 255, 0.15);
}
.ese-input::placeholder {
  color: #8b949e;
}

.ese-list {
  position: absolute;
  top: calc(100% + 4px);
  left: 0;
  right: 0;
  z-index: 20;
  margin: 0;
  padding: 4px;
  list-style: none;
  max-height: 200px;
  overflow-y: auto;
  background: #161b22;
  border: 1px solid #30363d;
  border-radius: 6px;
  box-shadow: 0 8px 24px rgba(0, 0, 0, 0.5);
}

.ese-option {
  display: grid;
  grid-template-columns: 36px 44px 1fr 1.4fr 52px 16px;
  align-items: center;
  gap: 8px;
  padding: 5px 8px;
  border-radius: 4px;
  cursor: pointer;
  font-size: 12px;
  white-space: nowrap;
}
.ese-option:hover {
  background: #21262d;
}
.ese-option.selected {
  background: #1f2937;
}

.opt-z { color: #6e7681; text-align: right; }
.opt-sym { font-weight: 700; color: #58a6ff; }
.opt-name { color: #e6edf3; overflow: hidden; text-overflow: ellipsis; }
.opt-cfg {
  color: #8b949e;
  font-family: var(--vp-font-family-mono, ui-monospace, monospace);
  overflow: hidden;
  text-overflow: ellipsis;
}
.opt-pg { color: #6e7681; text-align: center; }
.opt-star { color: #f0b030; text-align: center; }

.ese-empty {
  padding: 8px;
  color: #6e7681;
  font-size: 12px;
  text-align: center;
}

.ese-toggle {
  display: flex;
  align-items: center;
  gap: 6px;
  color: #c9d1d9;
  font-size: 13px;
  cursor: pointer;
  user-select: none;
  white-space: nowrap;
}
.ese-toggle input {
  cursor: pointer;
  accent-color: #58a6ff;
}
.ese-badge {
  font-size: 10px;
  color: #8b949e;
  border: 1px solid #30363d;
  border-radius: 3px;
  padding: 1px 5px;
  margin-left: 2px;
}

.ese-header {
  display: flex;
  align-items: center;
  gap: 14px;
  flex-wrap: wrap;
  margin-top: 12px;
  padding: 8px 4px 0;
}
.hdr-name { font-weight: 700; color: #e6edf3; font-size: 15px; }
.hdr-z { color: #8b949e; font-size: 13px; }
.hdr-cfg {
  color: #79c0ff;
  font-family: var(--vp-font-family-mono, ui-monospace, monospace);
  font-size: 13px;
}
.hdr-badge {
  color: #f0b030;
  border: 1px solid #f0b030;
  background: rgba(240, 176, 48, 0.12);
  border-radius: 4px;
  padding: 2px 8px;
  font-size: 12px;
  font-weight: 600;
}

.ese-panels {
  margin-top: 12px;
}
</style>
