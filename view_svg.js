// ── Periodic Table SVG Viewer ────────────────────────────────────────────────
// Pan: click-drag.  Zoom: scroll wheel or +/- buttons.
// File: selectable via dropdown; ?file=<name> URL param overrides default.

const viewer = d3.select("#viewer");
const loading = document.getElementById("loading");
const zoomDisp = document.getElementById("zoom-level");
const select = document.getElementById("file-select");

// ── honour ?file= URL param ───────────────────────────────────────────────────
const urlFile = new URLSearchParams(globalThis.location.search).get("file");
if (urlFile) {
    const opt = [...select.options].find((o) => o.value === urlFile);
    if (opt) opt.selected = true;
}

// ── zoom behaviour (created once, reused) ────────────────────────────────────
const zoom = d3.zoom()
    .scaleExtent([0.05, 40])
    .on("zoom", ({ transform }) => {
        d3.select("#content-group").attr("transform", transform);
        zoomDisp.textContent = `${Math.round(transform.k * 100)}%`;
    });

viewer.call(zoom);

// Disable double-click zoom (we keep it simple: scroll only)
viewer.on("dblclick.zoom", null);

// ── load & inline an SVG file ─────────────────────────────────────────────────
function loadSVG(filename) {
    loading.classList.remove("hidden");

    // Remove previous content
    viewer.selectAll("g#content-group").remove();
    viewer.selectAll("defs#imported-defs").remove();

    fetch(filename)
        .then((r) => {
            if (!r.ok) throw new Error(`HTTP ${r.status}: ${filename}`);
            return r.text();
        })
        .then((svgText) => {
            const parser = new DOMParser();
            const doc = parser.parseFromString(svgText, "image/svg+xml");
            const srcSVG = doc.querySelector("svg");

            if (!srcSVG) throw new Error("No <svg> element found in file.");

            // Read source dimensions
            const vb = srcSVG.getAttribute("viewBox");
            let svgW, svgH;
            if (vb) {
                [, , svgW, svgH] = vb.trim().split(/[\s,]+/).map(Number);
            } else {
                svgW = parseFloat(srcSVG.getAttribute("width")) || 1100;
                svgH = parseFloat(srcSVG.getAttribute("height")) || 800;
            }

            // Move <defs> into the viewer SVG so markers/gradients resolve
            const importedDefs = document.createElementNS(
                "http://www.w3.org/2000/svg",
                "defs",
            );
            importedDefs.id = "imported-defs";
            srcSVG.querySelectorAll("defs").forEach((d) => {
                Array.from(d.children).forEach((child) =>
                    importedDefs.appendChild(document.importNode(child, true))
                );
            });
            viewer.node().insertBefore(importedDefs, viewer.node().firstChild);

            // Put all non-defs children into a single <g>
            const g = viewer.append("g").attr("id", "content-group");
            Array.from(srcSVG.children).forEach((child) => {
                if (child.tagName.toLowerCase() !== "defs") {
                    g.node().appendChild(document.importNode(child, true));
                }
            });

            // Fit to viewport
            fitToView(svgW, svgH);
            loading.classList.add("hidden");
        })
        .catch((err) => {
            loading.textContent = `Error: ${err.message}`;
            console.error(err);
        });
}

// ── fit content to current viewport size ─────────────────────────────────────
let _svgW = 1100, _svgH = 800; // remembered for re-fit on resize

function fitToView(w, h) {
    if (w) _svgW = w;
    if (h) _svgH = h;
    const vw = viewer.node().clientWidth || globalThis.innerWidth;
    const vh = viewer.node().clientHeight || globalThis.innerHeight;
    const scale = Math.min(vw / _svgW, vh / _svgH) * 0.96;
    const tx = (vw - _svgW * scale) / 2;
    const ty = (vh - _svgH * scale) / 2;
    const t = d3.zoomIdentity.translate(tx, ty).scale(scale);
    viewer.call(zoom.transform, t);
}

// ── toolbar buttons ───────────────────────────────────────────────────────────
document.getElementById("btn-fit").addEventListener("click", () => fitToView());
document.getElementById("btn-100").addEventListener("click", () => {
    const vw = viewer.node().clientWidth;
    const vh = viewer.node().clientHeight;
    viewer.call(
        zoom.transform,
        d3.zoomIdentity.translate(vw / 2 - _svgW / 2, vh / 2 - _svgH / 2).scale(
            1,
        ),
    );
});
document.getElementById("btn-in").addEventListener(
    "click",
    () => viewer.transition().duration(250).call(zoom.scaleBy, 1.5),
);
document.getElementById("btn-out").addEventListener(
    "click",
    () => viewer.transition().duration(250).call(zoom.scaleBy, 1 / 1.5),
);

// ── file selector ─────────────────────────────────────────────────────────────
select.addEventListener("change", () => loadSVG(select.value));

// ── keyboard shortcuts ────────────────────────────────────────────────────────
globalThis.addEventListener("keydown", (e) => {
    if (e.key === "0" || e.key === "f") fitToView();
    if (e.key === "1") document.getElementById("btn-100").click();
    if (e.key === "+" || e.key === "=") {
        document.getElementById("btn-in").click();
    }
    if (e.key === "-") document.getElementById("btn-out").click();
});

// ── refit on window resize ────────────────────────────────────────────────────
globalThis.addEventListener("resize", () => fitToView());

// ── initial load ──────────────────────────────────────────────────────────────
loadSVG(select.value);
