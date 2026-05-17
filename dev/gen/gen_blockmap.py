#!/usr/bin/env python3
"""Generate block-map schematic SVGs for section 6.7.

Outputs:
  docs/public/diagrams/block-map-32col.svg - s|f|d|p true quantum ordering
  docs/public/diagrams/block-map-18col.svg - 18-column practical layout
"""

from pathlib import Path

OUT = Path("/home/olivier/gdrive/dev/periodic-table/docs/public/diagrams")

BG = "#0d1117"
GRID = "#30363d"
MUTE = "#8b949e"
BRIGHT = "#e6edf3"
DIM = "#484f58"
FF = "sans-serif"

COLORS = {"s": "#f78166", "p": "#79c0ff", "d": "#56d364", "f": "#d2a8ff"}
CAP = {"s": 2, "f": 14, "d": 10, "p": 6}

U = 20  # px per element column
RH = 30  # row height
GAP = 3  # inter-block gap

# Per-period fill data: (first_sym, last_sym, count) or None
FILL = [
    {"s": ("H", "He", 2), "f": None, "d": None, "p": None},
    {"s": ("Li", "Be", 2), "f": None, "d": None, "p": ("B", "Ne", 6)},
    {"s": ("Na", "Mg", 2), "f": None, "d": None, "p": ("Al", "Ar", 6)},
    {"s": ("K", "Ca", 2), "f": None, "d": ("Sc", "Zn", 10), "p": ("Ga", "Kr", 6)},
    {"s": ("Rb", "Sr", 2), "f": None, "d": ("Y", "Cd", 10), "p": ("In", "Xe", 6)},
    {
        "s": ("Cs", "Ba", 2),
        "f": ("La", "Yb", 14),
        "d": ("Lu", "Hg", 10),
        "p": ("Tl", "Rn", 6),
    },
    {
        "s": ("Fr", "Ra", 2),
        "f": ("Ac", "No", 14),
        "d": ("Lr", "Cn", 10),
        "p": ("Nh", "Og", 6),
    },
]


def _esc(s):
    return s.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")


def _tx(
    x,
    y,
    text,
    size=9,
    color=BRIGHT,
    anchor="start",
    weight="normal",
    op=1.0,
    baseline="auto",
):
    s = (
        f'  <text x="{x}" y="{y}" font-size="{size}" fill="{color}"'
        f' font-family="{FF}" text-anchor="{anchor}" font-weight="{weight}"'
    )
    if op != 1.0:
        s += f' fill-opacity="{op}"'
    if baseline != "auto":
        s += f' dominant-baseline="{baseline}"'
    s += f">{_esc(text)}</text>"
    return s


def _rx(
    x, y, w, h, fill="none", stroke=GRID, sw=0.5, corner=2, fop=1.0, sop=1.0, dash=""
):
    s = (
        f'  <rect x="{x}" y="{y}" width="{w}" height="{h}" rx="{corner}"'
        f' fill="{fill}" fill-opacity="{fop}"'
        f' stroke="{stroke}" stroke-width="{sw}" stroke-opacity="{sop}"'
    )
    if dash:
        s += f' stroke-dasharray="{dash}"'
    s += "/>"
    return s


def draw_cell(L, bx, by, bw, bt, data):
    color = COLORS[bt]
    bh = RH - 5
    ry = by + 2
    mid = by + RH // 2 + 1
    if data:
        first, last, _count = data
        L.append(
            _rx(bx, ry, bw, bh, fill=color, stroke=color, sw=0.7, fop=0.18, sop=0.75)
        )
        L.append(_tx(bx + 4, mid, first, size=9, color=color, baseline="middle"))
        L.append(
            _tx(
                bx + bw - 4,
                mid,
                last,
                size=9,
                color=color,
                anchor="end",
                op=0.8,
                baseline="middle",
            )
        )
    else:
        L.append(
            _rx(bx, ry, bw, bh, fill="none", stroke=GRID, sw=0.5, sop=0.5, dash="4,2")
        )


def draw_hdr(L, bx, bw, bt, ly, by, label=None):
    color = COLORS[bt]
    cx = bx + bw // 2
    L.append(
        _tx(
            cx,
            ly,
            label or f"{bt} · {CAP[bt]}",
            size=10,
            color=color,
            anchor="middle",
            weight="700",
        )
    )
    L.append(_rx(bx, by, bw, 8, fill=color, stroke=color, sw=0.6, fop=0.22, sop=0.65))


def draw_plabel(L, pnum, row_y, lx):
    mid = row_y + RH // 2 + 1
    L.append(
        _tx(lx, mid, str(pnum), size=9, color=MUTE, anchor="middle", baseline="middle")
    )


# ── 32-column true form ───────────────────────────────────────────────────────


def gen_32col():
    LM = 28
    TM = 34
    BM = 10

    s_x = LM
    s_w = CAP["s"] * U
    f_x = s_x + s_w + GAP
    f_w = CAP["f"] * U
    d_x = f_x + f_w + GAP
    d_w = CAP["d"] * U
    p_x = d_x + d_w + GAP
    p_w = CAP["p"] * U
    right = p_x + p_w

    W = right + 12
    H = TM + len(FILL) * RH + BM

    L = [
        f'<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H}"'
        f' viewBox="0 0 {W} {H}">',
        f'  <rect width="{W}" height="{H}" fill="{BG}"/>',
        "",
        "  <!-- Block headers -->",
    ]
    for bx, bw, bt in [
        (s_x, s_w, "s"),
        (f_x, f_w, "f"),
        (d_x, d_w, "d"),
        (p_x, p_w, "p"),
    ]:
        draw_hdr(L, bx, bw, bt, 14, 20)

    L.append("")
    L.append("  <!-- Period rows -->")
    for i, fill in enumerate(FILL):
        row_y = TM + i * RH
        draw_plabel(L, i + 1, row_y, lx=LM - 8)
        draw_cell(L, s_x, row_y, s_w, "s", fill["s"])
        draw_cell(L, f_x, row_y, f_w, "f", fill["f"])
        draw_cell(L, d_x, row_y, d_w, "d", fill["d"])
        draw_cell(L, p_x, row_y, p_w, "p", fill["p"])

    L.append("</svg>")
    return "\n".join(L)


# ── 18-column practical form ──────────────────────────────────────────────────


def gen_18col():
    LM = 28
    TM = 34
    BM = 10

    s_x = LM
    s_w = CAP["s"] * U
    d_x = s_x + s_w + GAP
    d_w = CAP["d"] * U
    p_x = d_x + d_w + GAP
    p_w = CAP["p"] * U
    right = p_x + p_w

    f_x = d_x  # f aligns under d (group 3)
    f_w = CAP["f"] * U

    W = max(right, f_x + f_w) + 12

    main_end = TM + len(FILL) * RH
    sep_y = main_end + 8
    f_hdr_y = sep_y + 16
    f_bar_y = sep_y + 22
    f_rows_y = sep_y + 34
    H = f_rows_y + 2 * RH + BM

    L = [
        f'<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H}"'
        f' viewBox="0 0 {W} {H}">',
        f'  <rect width="{W}" height="{H}" fill="{BG}"/>',
        "",
        "  <!-- Main body headers -->",
    ]
    for bx, bw, bt in [(s_x, s_w, "s"), (d_x, d_w, "d"), (p_x, p_w, "p")]:
        draw_hdr(L, bx, bw, bt, 14, 20)

    L.append("")
    L.append("  <!-- Period rows -->")
    for i, fill in enumerate(FILL):
        row_y = TM + i * RH
        draw_plabel(L, i + 1, row_y, lx=LM - 8)
        draw_cell(L, s_x, row_y, s_w, "s", fill["s"])
        draw_cell(L, d_x, row_y, d_w, "d", fill["d"])
        draw_cell(L, p_x, row_y, p_w, "p", fill["p"])

    L.append("")
    L.append("  <!-- f-block separator -->")
    L.append(
        f'  <line x1="{LM}" y1="{sep_y}" x2="{right}" y2="{sep_y}"'
        f' stroke="{GRID}" stroke-width="0.5" stroke-dasharray="4,3"/>'
    )

    L.append("")
    L.append("  <!-- f-block header -->")
    draw_hdr(
        L,
        f_x,
        f_w,
        "f",
        f_hdr_y,
        f_bar_y,
        label="f · 14  —  periods 6 & 7  (extracted)",
    )

    L.append("")
    L.append("  <!-- f-block rows -->")
    for i, p in enumerate([6, 7]):
        row_y = f_rows_y + i * RH
        draw_plabel(L, p, row_y, lx=LM - 8)
        draw_cell(L, f_x, row_y, f_w, "f", FILL[p - 1]["f"])

    L.append("</svg>")
    return "\n".join(L)


if __name__ == "__main__":
    OUT.mkdir(parents=True, exist_ok=True)
    for name, fn in [
        ("block-map-32col.svg", gen_32col),
        ("block-map-18col.svg", gen_18col),
    ]:
        path = OUT / name
        svg = fn()
        path.write_text(svg, encoding="utf-8")
        print(f"Written {path}  ({path.stat().st_size:,} B)")
