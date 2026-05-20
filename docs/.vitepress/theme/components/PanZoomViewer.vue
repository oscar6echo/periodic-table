<template>
  <div class="viewer-container" :class="{ fullscreen: isFullscreen }" ref="container">
    <div class="toolbar">
      <button class="btn" @click="fitToView">Fit</button>
      <button class="btn" @click="zoomTo100">100%</button>
      <button class="btn" @click="zoomIn">＋</button>
      <button class="btn" @click="zoomOut">－</button>
      <span class="zoom-level">{{ Math.round(zoomLevel * 100) }}%</span>
      <button class="btn fs-btn" @click="toggleFullscreen" :title="isFullscreen ? 'Exit fullscreen' : 'Fullscreen'">⛶</button>
    </div>
    <div ref="viewport" class="viewport">
      <svg ref="svgEl"></svg>
      <div v-if="loading" class="loading">Loading…</div>
    </div>
  </div>
</template>

<script setup>
import { ref, onMounted, onBeforeUnmount, watch, nextTick } from 'vue'
import { withBase } from 'vitepress'
import * as d3 from 'd3'

const props = defineProps({
  svgSrc: { type: String, default: '' },
  svgMarkup: { type: String, default: '' },
})

const emit = defineEmits(['toggle-fullscreen'])

const container = ref(null)
const viewport = ref(null)
const svgEl = ref(null)
const loading = ref(true)
const zoomLevel = ref(1)
const isFullscreen = ref(false)

let svgW = 1100
let svgH = 800
let zoom
let resizeObserver
let svgLoaded = false

function setAspectHeight() {
  if (!container.value || !viewport.value || isFullscreen.value || !svgLoaded) return
  const vw = viewport.value.clientWidth
  if (!vw) return
  const toolbar = container.value.querySelector('.toolbar')
  const toolbarH = toolbar ? toolbar.offsetHeight : 40
  const idealVpH = vw * svgH / svgW
  const maxVpH = window.innerHeight * 0.85 - toolbarH
  container.value.style.height = (Math.min(idealVpH, maxVpH) + toolbarH) + 'px'
}

function fitToView(animated = true) {
  if (!svgEl.value) return
  const vw = viewport.value.clientWidth || window.innerWidth
  const vh = viewport.value.clientHeight || window.innerHeight
  const scale = Math.min(vw / svgW, vh / svgH) * 0.98
  const tx = (vw - svgW * scale) / 2
  const ty = 8
  const sel = d3.select(svgEl.value)
  const target = animated ? sel.transition().duration(300) : sel
  target.call(zoom.transform, d3.zoomIdentity.translate(tx, ty).scale(scale))
}

function zoomTo100() {
  if (!svgEl.value) return
  const vw = viewport.value.clientWidth
  const vh = viewport.value.clientHeight
  d3.select(svgEl.value).transition().duration(300)
    .call(zoom.transform, d3.zoomIdentity.translate(vw / 2 - svgW / 2, vh / 2 - svgH / 2))
}

function zoomIn() {
  if (!svgEl.value) return
  d3.select(svgEl.value).transition().duration(200).call(zoom.scaleBy, 1.5)
}

function zoomOut() {
  if (!svgEl.value) return
  d3.select(svgEl.value).transition().duration(200).call(zoom.scaleBy, 1 / 1.5)
}

function toggleFullscreen() {
  emit('toggle-fullscreen')
}

function onFullscreenChange() {
  isFullscreen.value = !!document.fullscreenElement
  if (!isFullscreen.value) {
    nextTick(() => { setAspectHeight(); nextTick(() => fitToView(false)) })
  }
}

function onKeyDown(e) {
  if (e.key === 'f' || e.key === '0') { e.preventDefault(); fitToView() }
  if (e.key === '1') { e.preventDefault(); zoomTo100() }
  if (e.key === '+' || e.key === '=') { e.preventDefault(); zoomIn() }
  if (e.key === '-') { e.preventDefault(); zoomOut() }
}

function renderSvgText(svgText) {
  loading.value = true
  svgLoaded = false
  svgW = 1100
  svgH = 800

  const svg = d3.select(svgEl.value)
  svg.selectAll('g#content-group').remove()
  svg.selectAll('defs#imported-defs').remove()
  svg.selectAll('text.svg-error').remove()

  try {
    const parser = new DOMParser()
    const doc = parser.parseFromString(svgText, 'image/svg+xml')
    const srcSvg = doc.querySelector('svg')
    if (!srcSvg) throw new Error('No <svg> found')

    const vb = srcSvg.getAttribute('viewBox')
    if (vb) {
      const parts = vb.trim().split(/[\s,]+/).map(Number)
      svgW = parts[2] || 1100
      svgH = parts[3] || 800
    }

    const importedDefs = document.createElementNS('http://www.w3.org/2000/svg', 'defs')
    importedDefs.id = 'imported-defs'
    srcSvg.querySelectorAll('defs').forEach(d => {
      Array.from(d.children).forEach(child => importedDefs.appendChild(document.importNode(child, true)))
    })
    svgEl.value.insertBefore(importedDefs, svgEl.value.firstChild)

    const g = svg.append('g').attr('id', 'content-group')
    Array.from(srcSvg.children).forEach(child => {
      if (child.tagName.toLowerCase() !== 'defs') {
        g.node().appendChild(document.importNode(child, true))
      }
    })

    svgLoaded = true
    setAspectHeight()
    nextTick(() => fitToView(false))
    loading.value = false
  } catch (err) {
    loading.value = false
    console.error('SVG render error:', err)
    showError(`Error rendering SVG: ${err.message}`)
  }
}

function showError(message) {
  d3.select(svgEl.value).append('text')
    .attr('class', 'svg-error')
    .attr('x', 20).attr('y', 30)
    .attr('fill', '#f85149').attr('font-size', '14')
    .text(message)
}

function loadSVG(src) {
  loading.value = true
  fetch(src)
    .then(r => { if (!r.ok) throw new Error(`HTTP ${r.status}`); return r.text() })
    .then(renderSvgText)
    .catch(err => {
      loading.value = false
      console.error('SVG load error:', err)
      showError(`Error loading ${src}: ${err.message}`)
    })
}

onMounted(() => {
  zoom = d3.zoom()
    .scaleExtent([0.05, 40])
    .on('zoom', (event) => {
      d3.select(svgEl.value).select('#content-group').attr('transform', event.transform)
      zoomLevel.value = event.transform.k
    })

  const svg = d3.select(svgEl.value)
  svg.call(zoom)
  svg.on('dblclick.zoom', null)

  resizeObserver = new ResizeObserver(() => {
    setAspectHeight()
    nextTick(() => fitToView(false))
  })
  resizeObserver.observe(viewport.value)

  document.addEventListener('fullscreenchange', onFullscreenChange)
  window.addEventListener('keydown', onKeyDown)
  if (props.svgMarkup) renderSvgText(props.svgMarkup)
  else if (props.svgSrc) loadSVG(withBase(props.svgSrc))
})

onBeforeUnmount(() => {
  resizeObserver?.disconnect()
  document.removeEventListener('fullscreenchange', onFullscreenChange)
  window.removeEventListener('keydown', onKeyDown)
})

watch(() => props.svgSrc, (src) => { if (src) loadSVG(withBase(src)) })
watch(() => props.svgMarkup, (markup) => { if (markup) renderSvgText(markup) })
</script>

<style scoped>
.viewer-container {
  background: #0d1117;
  border: 1px solid #30363d;
  border-radius: 8px;
  display: flex;
  flex-direction: column;
  min-height: 300px;
  position: relative;
  overflow: hidden;
}
.viewer-container.fullscreen {
  border-radius: 0;
  flex: 1;
}

.toolbar {
  display: flex;
  align-items: center;
  gap: 8px;
  padding: 6px 12px;
  background: #161b22;
  border-bottom: 1px solid #30363d;
  flex-shrink: 0;
  flex-wrap: wrap;
}

.btn {
  background: #21262d;
  color: #e6edf3;
  border: 1px solid #30363d;
  border-radius: 6px;
  padding: 4px 10px;
  font-size: 12px;
  cursor: pointer;
  user-select: none;
  font-family: inherit;
}
.btn:hover {
  background: #30363d;
  border-color: #58a6ff;
}

.fs-btn {
  margin-left: auto;
}

.zoom-level {
  font-size: 11px;
  color: #6e7681;
  min-width: 48px;
  text-align: right;
}

.viewport {
  flex: 1;
  overflow: hidden;
  cursor: grab;
  min-height: 200px;
}
.viewport:active {
  cursor: grabbing;
}

.viewport > svg {
  width: 100%;
  height: 100%;
  display: block;
}

.loading {
  position: absolute;
  inset: 0;
  display: flex;
  align-items: center;
  justify-content: center;
  background: #0d1117cc;
  font-size: 14px;
  color: #8b949e;
  pointer-events: none;
  font-family: sans-serif;
}
</style>
