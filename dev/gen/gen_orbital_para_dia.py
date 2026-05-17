#!/usr/bin/env python3
"""Generate orbital-box SVG for the paramagnetic/diamagnetic section (6.5)."""
from pathlib import Path

OUT = Path(__file__).parent.parent / "docs/public/diagrams/orbital-para-dia.svg"

# --- theme (GitHub dark palette, matching the site) --------------------------
BG_BASE  = "#0d1117"
BG_ALT   = "#161b22"
BG_HDR   = "#161b22"
C_BORDER = "#30363d"
C_TEXT1  = "#e6edf3"
C_TEXT2  = "#8b949e"
C_TEXT3  = "#6e7681"
C_SYM    = "#58a6ff"   # brand blue for element symbols
C_UP     = "#e6edf3"   # up-arrow colour (bright)
C_DN     = "#6e7681"   # down-arrow colour (muted)
C_BOX_F  = "#161b22"   # orbital box fill
C_BOX_S  = "#444c56"   # orbital box stroke
C_PARA   = "#f0883e"   # orange  — paramagnetic
C_DIA    = "#58a6ff"   # blue    — diamagnetic

# --- orbital data -------------------------------------------------------------
# (symbol, 1s, 2s, 2p_a, 2p_b, 2p_c)
# box values: 0=empty  1=↑ (singly occupied)  2=↑↓ (paired)
ATOMS = [
    ("H",  1, 0, 0, 0, 0),
    ("He", 2, 0, 0, 0, 0),
    ("Li", 2, 1, 0, 0, 0),
    ("Be", 2, 2, 0, 0, 0),
    ("B",  2, 2, 1, 0, 0),
    ("C",  2, 2, 1, 1, 0),
    ("N",  2, 2, 1, 1, 1),
    ("O",  2, 2, 2, 1, 1),
    ("F",  2, 2, 2, 2, 1),
    ("Ne", 2, 2, 2, 2, 2),
]

# --- layout ------------------------------------------------------------------
ROW_H  = 40
HDR_H  = 46
BW, BH = 38, 26   # orbital box size
BGAP   = 5        # gap between 2p boxes

# column centres (x)
CX_SYM   = 28
CX_1S    = 90
CX_2S    = 150
CX_2P_C  = 240     # centre of 3-box 2p group
CX_2P    = [CX_2P_C - (BW + BGAP), CX_2P_C, CX_2P_C + (BW + BGAP)]
CX_UNP   = 335
CX_PD    = 445

SVG_W = CX_PD + 60
SVG_H = HDR_H + len(ATOMS) * ROW_H + 8

# --- helpers -----------------------------------------------------------------
parts: list[str] = []
add = parts.append


def hline(y: int, x1: int = 0, x2: int | None = None, width: float = 1.0,
          opacity: float = 1.0) -> None:
    x2 = x2 or SVG_W
    add(f'<line x1="{x1}" y1="{y}" x2="{x2}" y2="{y}" '
        f'stroke="{C_BORDER}" stroke-width="{width}" opacity="{opacity}"/>')


def txt(x: float, y: float, s: str, fill: str, size: int = 13,
        weight: str = "normal", anchor: str = "middle",
        family: str = "ui-sans-serif,system-ui,sans-serif") -> None:
    add(f'<text x="{int(x)}" y="{int(y)}" text-anchor="{anchor}" '
        f'dominant-baseline="central" fill="{fill}" font-size="{size}" '
        f'font-weight="{weight}" font-family="{family}">{s}</text>')


def orbital_box(cx: float, cy: float, fill: int) -> None:
    bx = round(cx - BW / 2)
    by = round(cy - BH / 2)
    add(f'<rect x="{bx}" y="{by}" width="{BW}" height="{BH}" rx="3" '
        f'fill="{C_BOX_F}" stroke="{C_BOX_S}" stroke-width="1.2"/>')
    if fill == 1:
        _arrow_up(cx, cy, C_UP)
    elif fill == 2:
        _arrow_up(cx - 6, cy, C_UP)
        _arrow_dn(cx + 6, cy, C_DN)


def _arrow_up(x: float, cy: float, color: str) -> None:
    x, cy = round(x), round(cy)
    add(f'<line x1="{x}" y1="{cy+9}" x2="{x}" y2="{cy-5}" '
        f'stroke="{color}" stroke-width="1.8" stroke-linecap="round"/>')
    add(f'<polygon points="{x},{cy-10} {x-3.5},{cy-4} {x+3.5},{cy-4}" fill="{color}"/>')


def _arrow_dn(x: float, cy: float, color: str) -> None:
    x, cy = round(x), round(cy)
    add(f'<line x1="{x}" y1="{cy-9}" x2="{x}" y2="{cy+5}" '
        f'stroke="{color}" stroke-width="1.8" stroke-linecap="round"/>')
    add(f'<polygon points="{x},{cy+10} {x-3.5},{cy+4} {x+3.5},{cy+4}" fill="{color}"/>')


def badge(cx: float, cy: float, label: str, color: str) -> None:
    bw, bh = 108, 22
    bx, by = round(cx - bw / 2), round(cy - bh / 2)
    add(f'<rect x="{bx}" y="{by}" width="{bw}" height="{bh}" rx="4" '
        f'fill="{color}22" stroke="{color}" stroke-width="1"/>')
    add(f'<text x="{round(cx)}" y="{round(cy)}" text-anchor="middle" '
        f'dominant-baseline="central" fill="{color}" font-size="11" '
        f'font-weight="600" font-family="ui-sans-serif,system-ui,sans-serif">'
        f'{label}</text>')


def count_unpaired(row: tuple) -> int:
    return sum(1 for v in row[1:] if v == 1)


# --- render ------------------------------------------------------------------
add(f'<svg xmlns="http://www.w3.org/2000/svg" '
    f'viewBox="0 0 {SVG_W} {SVG_H}" width="{SVG_W}" height="{SVG_H}">')

# background
add(f'<rect width="{SVG_W}" height="{SVG_H}" fill="{BG_BASE}" rx="8"/>')

# outer border
add(f'<rect x="0.5" y="0.5" width="{SVG_W-1}" height="{SVG_H-1}" rx="7.5" '
    f'fill="none" stroke="{C_BORDER}" stroke-width="1"/>')

# header background
add(f'<rect width="{SVG_W}" height="{HDR_H}" fill="{BG_HDR}" rx="8"/>')
add(f'<rect y="{HDR_H - 8}" width="{SVG_W}" height="8" fill="{BG_HDR}"/>')
hline(HDR_H, width=1.5)

# alternating row backgrounds
for i in range(len(ATOMS)):
    ry = HDR_H + i * ROW_H
    bg = BG_ALT if i % 2 == 0 else BG_BASE
    add(f'<rect x="0" y="{ry}" width="{SVG_W}" height="{ROW_H}" fill="{bg}"/>')

# row separator lines
for i in range(1, len(ATOMS)):
    hline(HDR_H + i * ROW_H, width=0.5, opacity=0.5)

# --- header labels ---
hcy = HDR_H // 2
txt(CX_SYM,   hcy, "Atom",     C_TEXT2, size=11, weight="600")
txt(CX_1S,    hcy, "1s",       C_TEXT1, size=13, weight="700",
    family="ui-monospace,Menlo,Monaco,monospace")
txt(CX_2S,    hcy, "2s",       C_TEXT1, size=13, weight="700",
    family="ui-monospace,Menlo,Monaco,monospace")
txt(CX_2P_C,  hcy, "2p",       C_TEXT1, size=13, weight="700",
    family="ui-monospace,Menlo,Monaco,monospace")
txt(CX_UNP,   hcy, "Unpaired", C_TEXT2, size=11, weight="600")
txt(CX_PD,    hcy, "Para/Dia", C_TEXT2, size=11, weight="600")

# --- data rows ---
for i, row in enumerate(ATOMS):
    sym, s1, s2, pa, pb, pc = row
    cy = HDR_H + i * ROW_H + ROW_H // 2
    unp = count_unpaired(row)
    is_para = unp > 0

    txt(CX_SYM, cy, sym, C_SYM, size=14, weight="700",
        family="ui-monospace,Menlo,Monaco,monospace")
    orbital_box(CX_1S, cy, s1)
    orbital_box(CX_2S, cy, s2)
    for j, pv in enumerate([pa, pb, pc]):
        orbital_box(CX_2P[j], cy, pv)

    uc = C_PARA if unp > 0 else C_TEXT3
    txt(CX_UNP, cy, str(unp), uc, size=14, weight="700")

    if is_para:
        badge(CX_PD, cy, "paramagnetic", C_PARA)
    else:
        badge(CX_PD, cy, "diamagnetic", C_DIA)

add("</svg>")

# --- write -------------------------------------------------------------------
OUT.parent.mkdir(parents=True, exist_ok=True)
OUT.write_text("\n".join(parts) + "\n")
print(f"Written {SVG_W}×{SVG_H}px → {OUT}")
