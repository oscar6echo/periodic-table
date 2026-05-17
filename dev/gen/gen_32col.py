#!/usr/bin/env python3
"""Generate periodic_table_2_32col.svg — 32-column long-form periodic table."""

WIDTH = 1048
HEIGHT = 520
CELL_W = 30
CELL_H = 52
COL_SPACING = 32  # CELL_W + 2px gap
ROW_SPACING = 54  # CELL_H + 2px gap

TABLE_TOP_Y = 68
BLOCK_BANNER_Y = 41
COL_LABEL_Y = 46

BG = "#0d1117"
FF = "sans-serif"

STRIP = {"s": "#f78166", "p": "#79c0ff", "d": "#56d364", "f": "#d2a8ff"}

CAT = {
    "alkali": ("#4a1010", "#c04040", "#ffb0b0"),
    "aearth": ("#3a0840", "#b040a0", "#f0a8e8"),
    "trans": ("#0a1e40", "#3a70c0", "#90c0ff"),
    "ptrans": ("#062818", "#208050", "#80e8a8"),
    "metalloid": ("#2a1a00", "#a07010", "#f0d060"),
    "nonmetal": ("#162200", "#508010", "#b0e860"),
    "halogen": ("#3a1000", "#c05020", "#ffb870"),
    "noble": ("#1e0840", "#7030c0", "#d098ff"),
    "lanthanide": ("#002030", "#1880b0", "#70d8f8"),
    "actinide": ("#200038", "#8828b8", "#d088ff"),
    "unknown": ("#222222", "#555555", "#aaaaaa"),
}

GOLD = "#f0b030"

ANOMALY = {24, 29, 41, 42, 44, 45, 46, 47, 78, 79}

# Unicode superscripts
# ⁰=\u2070 ¹=\u00b9 ²=\u00b2 ³=\u00b3 ⁴=\u2074 ⁵=\u2075 ⁶=\u2076 ⁷=\u2077 ⁸=\u2078 ⁹=\u2079
# 10 = ¹⁰ = \u00b9\u2070
# 14 = ¹⁴ = \u00b9\u2074

ELEMENTS = [
    # (Z, symbol, name, period, col, category, block, valence_config)
    (1, "H", "Hydrogen", 1, 1, "nonmetal", "s", "1s\u00b9"),
    (2, "He", "Helium", 1, 32, "noble", "s", "1s\u00b2"),
    (3, "Li", "Lithium", 2, 1, "alkali", "s", "2s\u00b9"),
    (4, "Be", "Beryllium", 2, 2, "aearth", "s", "2s\u00b2"),
    (5, "B", "Boron", 2, 27, "metalloid", "p", "2p\u00b9"),
    (6, "C", "Carbon", 2, 28, "nonmetal", "p", "2p\u00b2"),
    (7, "N", "Nitrogen", 2, 29, "nonmetal", "p", "2p\u00b3"),
    (8, "O", "Oxygen", 2, 30, "nonmetal", "p", "2p\u2074"),
    (9, "F", "Fluorine", 2, 31, "halogen", "p", "2p\u2075"),
    (10, "Ne", "Neon", 2, 32, "noble", "p", "2s\u00b22p\u2076"),
    (11, "Na", "Sodium", 3, 1, "alkali", "s", "3s\u00b9"),
    (12, "Mg", "Magnesium", 3, 2, "aearth", "s", "3s\u00b2"),
    (13, "Al", "Aluminum", 3, 27, "ptrans", "p", "3p\u00b9"),
    (14, "Si", "Silicon", 3, 28, "metalloid", "p", "3p\u00b2"),
    (15, "P", "Phosphor.", 3, 29, "nonmetal", "p", "3p\u00b3"),
    (16, "S", "Sulfur", 3, 30, "nonmetal", "p", "3p\u2074"),
    (17, "Cl", "Chlorine", 3, 31, "halogen", "p", "3p\u2075"),
    (18, "Ar", "Argon", 3, 32, "noble", "p", "3s\u00b23p\u2076"),
    (19, "K", "Potassium", 4, 1, "alkali", "s", "4s\u00b9"),
    (20, "Ca", "Calcium", 4, 2, "aearth", "s", "4s\u00b2"),
    (21, "Sc", "Scandium", 4, 17, "trans", "d", "3d\u00b94s\u00b2"),
    (22, "Ti", "Titanium", 4, 18, "trans", "d", "3d\u00b24s\u00b2"),
    (23, "V", "Vanadium", 4, 19, "trans", "d", "3d\u00b34s\u00b2"),
    (24, "Cr", "Chromium", 4, 20, "trans", "d", "3d\u20754s\u00b9"),
    (25, "Mn", "Manganese", 4, 21, "trans", "d", "3d\u20754s\u00b2"),
    (26, "Fe", "Iron", 4, 22, "trans", "d", "3d\u20764s\u00b2"),
    (27, "Co", "Cobalt", 4, 23, "trans", "d", "3d\u20774s\u00b2"),
    (28, "Ni", "Nickel", 4, 24, "trans", "d", "3d\u20784s\u00b2"),
    (29, "Cu", "Copper", 4, 25, "trans", "d", "3d\u00b9\u20704s\u00b9"),
    (30, "Zn", "Zinc", 4, 26, "trans", "d", "3d\u00b9\u20704s\u00b2"),
    (31, "Ga", "Gallium", 4, 27, "ptrans", "p", "4p\u00b9"),
    (32, "Ge", "Germanium", 4, 28, "metalloid", "p", "4p\u00b2"),
    (33, "As", "Arsenic", 4, 29, "metalloid", "p", "4p\u00b3"),
    (34, "Se", "Selenium", 4, 30, "nonmetal", "p", "4p\u2074"),
    (35, "Br", "Bromine", 4, 31, "halogen", "p", "4p\u2075"),
    (36, "Kr", "Krypton", 4, 32, "noble", "p", "4s\u00b24p\u2076"),
    (37, "Rb", "Rubidium", 5, 1, "alkali", "s", "5s\u00b9"),
    (38, "Sr", "Strontium", 5, 2, "aearth", "s", "5s\u00b2"),
    (39, "Y", "Yttrium", 5, 17, "trans", "d", "4d\u00b95s\u00b2"),
    (40, "Zr", "Zirconium", 5, 18, "trans", "d", "4d\u00b25s\u00b2"),
    (41, "Nb", "Niobium", 5, 19, "trans", "d", "4d\u20745s\u00b9"),
    (42, "Mo", "Molybdenum", 5, 20, "trans", "d", "4d\u20755s\u00b9"),
    (43, "Tc", "Technetium", 5, 21, "trans", "d", "4d\u20755s\u00b2"),
    (44, "Ru", "Ruthenium", 5, 22, "trans", "d", "4d\u20775s\u00b9"),
    (45, "Rh", "Rhodium", 5, 23, "trans", "d", "4d\u20785s\u00b9"),
    (46, "Pd", "Palladium", 5, 24, "trans", "d", "4d\u00b9\u2070"),
    (47, "Ag", "Silver", 5, 25, "trans", "d", "4d\u00b9\u20705s\u00b9"),
    (48, "Cd", "Cadmium", 5, 26, "trans", "d", "4d\u00b9\u20705s\u00b2"),
    (49, "In", "Indium", 5, 27, "ptrans", "p", "5p\u00b9"),
    (50, "Sn", "Tin", 5, 28, "ptrans", "p", "5p\u00b2"),
    (51, "Sb", "Antimony", 5, 29, "metalloid", "p", "5p\u00b3"),
    (52, "Te", "Tellurium", 5, 30, "metalloid", "p", "5p\u2074"),
    (53, "I", "Iodine", 5, 31, "halogen", "p", "5p\u2075"),
    (54, "Xe", "Xenon", 5, 32, "noble", "p", "5s\u00b25p\u2076"),
    (55, "Cs", "Cesium", 6, 1, "alkali", "s", "6s\u00b9"),
    (56, "Ba", "Barium", 6, 2, "aearth", "s", "6s\u00b2"),
    (57, "La", "Lanthanum", 6, 17, "lanthanide", "d", "5d\u00b96s\u00b2"),
    (58, "Ce", "Cerium", 6, 3, "lanthanide", "f", "4f\u00b95d\u00b96s\u00b2"),
    (59, "Pr", "Praseo.", 6, 4, "lanthanide", "f", "4f\u00b36s\u00b2"),
    (60, "Nd", "Neodymium", 6, 5, "lanthanide", "f", "4f\u20746s\u00b2"),
    (61, "Pm", "Promethium", 6, 6, "lanthanide", "f", "4f\u20756s\u00b2"),
    (62, "Sm", "Samarium", 6, 7, "lanthanide", "f", "4f\u20766s\u00b2"),
    (63, "Eu", "Europium", 6, 8, "lanthanide", "f", "4f\u20776s\u00b2"),
    (64, "Gd", "Gadolinium", 6, 9, "lanthanide", "f", "4f\u20775d\u00b96s\u00b2"),
    (65, "Tb", "Terbium", 6, 10, "lanthanide", "f", "4f\u20796s\u00b2"),
    (66, "Dy", "Dysprosium", 6, 11, "lanthanide", "f", "4f\u00b9\u20706s\u00b2"),
    (67, "Ho", "Holmium", 6, 12, "lanthanide", "f", "4f\u00b9\u00b96s\u00b2"),
    (68, "Er", "Erbium", 6, 13, "lanthanide", "f", "4f\u00b9\u00b26s\u00b2"),
    (69, "Tm", "Thulium", 6, 14, "lanthanide", "f", "4f\u00b9\u00b36s\u00b2"),
    (70, "Yb", "Ytterbium", 6, 15, "lanthanide", "f", "4f\u00b9\u20746s\u00b2"),
    (71, "Lu", "Lutetium", 6, 16, "lanthanide", "f", "4f\u00b9\u20745d\u00b96s\u00b2"),
    (72, "Hf", "Hafnium", 6, 18, "trans", "d", "5d\u00b26s\u00b2"),
    (73, "Ta", "Tantalum", 6, 19, "trans", "d", "5d\u00b36s\u00b2"),
    (74, "W", "Tungsten", 6, 20, "trans", "d", "5d\u20746s\u00b2"),
    (75, "Re", "Rhenium", 6, 21, "trans", "d", "5d\u20756s\u00b2"),
    (76, "Os", "Osmium", 6, 22, "trans", "d", "5d\u20766s\u00b2"),
    (77, "Ir", "Iridium", 6, 23, "trans", "d", "5d\u20776s\u00b2"),
    (78, "Pt", "Platinum", 6, 24, "trans", "d", "5d\u20796s\u00b9"),
    (79, "Au", "Gold", 6, 25, "trans", "d", "5d\u00b9\u20706s\u00b9"),
    (80, "Hg", "Mercury", 6, 26, "trans", "d", "5d\u00b9\u20706s\u00b2"),
    (81, "Tl", "Thallium", 6, 27, "ptrans", "p", "6p\u00b9"),
    (82, "Pb", "Lead", 6, 28, "ptrans", "p", "6p\u00b2"),
    (83, "Bi", "Bismuth", 6, 29, "ptrans", "p", "6p\u00b3"),
    (84, "Po", "Polonium", 6, 30, "ptrans", "p", "6p\u2074"),
    (85, "At", "Astatine", 6, 31, "halogen", "p", "6p\u2075"),
    (86, "Rn", "Radon", 6, 32, "noble", "p", "6s\u00b26p\u2076"),
    (87, "Fr", "Francium", 7, 1, "alkali", "s", "7s\u00b9"),
    (88, "Ra", "Radium", 7, 2, "aearth", "s", "7s\u00b2"),
    (89, "Ac", "Actinium", 7, 17, "actinide", "d", "6d\u00b97s\u00b2"),
    (90, "Th", "Thorium", 7, 3, "actinide", "f", "6d\u00b27s\u00b2"),
    (91, "Pa", "Protactinium", 7, 4, "actinide", "f", "5f\u00b26d\u00b97s\u00b2"),
    (92, "U", "Uranium", 7, 5, "actinide", "f", "5f\u00b36d\u00b97s\u00b2"),
    (93, "Np", "Neptunium", 7, 6, "actinide", "f", "5f\u20746d\u00b97s\u00b2"),
    (94, "Pu", "Plutonium", 7, 7, "actinide", "f", "5f\u20767s\u00b2"),
    (95, "Am", "Americium", 7, 8, "actinide", "f", "5f\u20777s\u00b2"),
    (96, "Cm", "Curium", 7, 9, "actinide", "f", "5f\u20776d\u00b97s\u00b2"),
    (97, "Bk", "Berkelium", 7, 10, "actinide", "f", "5f\u20797s\u00b2"),
    (98, "Cf", "Californium", 7, 11, "actinide", "f", "5f\u00b9\u20707s\u00b2"),
    (99, "Es", "Einsteinium", 7, 12, "actinide", "f", "5f\u00b9\u00b97s\u00b2"),
    (100, "Fm", "Fermium", 7, 13, "actinide", "f", "5f\u00b9\u00b27s\u00b2"),
    (101, "Md", "Mendelevium", 7, 14, "actinide", "f", "5f\u00b9\u00b37s\u00b2"),
    (102, "No", "Nobelium", 7, 15, "actinide", "f", "5f\u00b9\u20747s\u00b2"),
    (103, "Lr", "Lawrencium", 7, 16, "actinide", "f", "5f\u00b9\u20747s\u00b27p\u00b9"),
    (104, "Rf", "Rutherford.", 7, 18, "unknown", "d", "6d\u00b27s\u00b2"),
    (105, "Db", "Dubnium", 7, 19, "unknown", "d", "6d\u00b37s\u00b2"),
    (106, "Sg", "Seaborgium", 7, 20, "unknown", "d", "6d\u20747s\u00b2"),
    (107, "Bh", "Bohrium", 7, 21, "unknown", "d", "6d\u20757s\u00b2"),
    (108, "Hs", "Hassium", 7, 22, "unknown", "d", "6d\u20767s\u00b2"),
    (109, "Mt", "Meitnerium", 7, 23, "unknown", "d", "6d\u20777s\u00b2"),
    (110, "Ds", "Darmstadt.", 7, 24, "unknown", "d", "6d\u20797s\u00b2"),
    (111, "Rg", "Roentgenium", 7, 25, "unknown", "d", "6d\u00b9\u20707s\u00b9"),
    (112, "Cn", "Copernicium", 7, 26, "unknown", "d", "6d\u00b9\u20707s\u00b2"),
    (113, "Nh", "Nihonium", 7, 27, "unknown", "p", "7p\u00b9"),
    (114, "Fl", "Flerovium", 7, 28, "unknown", "p", "7p\u00b2"),
    (115, "Mc", "Moscovium", 7, 29, "unknown", "p", "7p\u00b3"),
    (116, "Lv", "Livermorium", 7, 30, "unknown", "p", "7p\u2074"),
    (117, "Ts", "Tennessine", 7, 31, "unknown", "p", "7p\u2075"),
    (118, "Og", "Oganesson", 7, 32, "unknown", "p", "7s\u00b27p\u2076"),
]


def col_x(c):
    """1-based column index -> left x of cell."""
    return 12 + (c - 1) * COL_SPACING


def period_y(p):
    """1-based period -> top y of cell row."""
    return TABLE_TOP_Y + (p - 1) * ROW_SPACING


def xml_escape(s):
    return (
        s.replace("&", "&amp;")
        .replace("<", "&lt;")
        .replace(">", "&gt;")
        .replace('"', "&quot;")
    )


def generate_svg():
    lines = []

    def emit(s=""):
        lines.append(s)

    # SVG header
    emit(
        f'<svg xmlns="http://www.w3.org/2000/svg" width="{WIDTH}" height="{HEIGHT}" viewBox="0 0 {WIDTH} {HEIGHT}">'
    )
    emit(f'  <rect width="{WIDTH}" height="{HEIGHT}" fill="{BG}"/>')
    emit()

    # Title
    emit("  <!-- Title -->")
    emit(
        f'  <text x="524" y="16" font-size="11" font-weight="700" fill="#e6edf3" text-anchor="middle" font-family="{FF}">Periodic Table \u2014 32-Column Long Form</text>'
    )
    emit(
        f'  <text x="524" y="28" font-size="7.5" fill="#8b949e" text-anchor="middle" font-family="{FF}">All 118 elements \u00b7 s/p/d/f blocks \u00b7 valence electron configurations \u00b7 \u2605 marks ground-state electron configuration anomalies</text>'
    )
    emit()

    # Block banners
    emit("  <!-- Block banners -->")
    banner_h = 20
    banner_y = BLOCK_BANNER_Y

    banners = [
        # (x, width, fill, stroke, text)
        (12, 62, "#1a0a0a", "#c04040", "s-block  (ns)"),
        (
            76,
            446,
            "#001a28",
            "#1880b0",
            "f-block (lanthanides / actinides)  \u00b7  (n\u22122)f",
        ),
        (
            524,
            318,
            "#0a1428",
            "#3a70c0",
            "d-block (transition metals)  \u00b7  (n\u22121)d",
        ),
        (844, 190, "#0a1a00", "#508010", "p-block  (np)"),
    ]

    for bx, bw, bfill, bstroke, btext in banners:
        emit(
            f'  <rect x="{bx}" y="{banner_y}" width="{bw}" height="{banner_h}" rx="2" fill="{bfill}" stroke="{bstroke}" stroke-width="0.5" opacity="0.9"/>'
        )
        cx = bx + bw // 2
        emit(
            f'  <text x="{cx}" y="{banner_y + 15}" font-size="5.5" fill="#c9d1d9" text-anchor="middle" font-family="{FF}">{xml_escape(btext)}</text>'
        )
    emit()

    # Column number labels
    emit("  <!-- Column labels -->")
    # s-block cols 1-2
    for c in [1, 2]:
        cx = col_x(c) + CELL_W // 2
        emit(
            f'  <text x="{cx}" y="{COL_LABEL_Y}" font-size="5" fill="#8b949e" text-anchor="middle" font-family="{FF}">{c}</text>'
        )
    # f-block cols 3-16, labeled f1-f14
    for c in range(3, 17):
        cx = col_x(c) + CELL_W // 2
        fn = c - 2
        emit(
            f'  <text x="{cx}" y="{COL_LABEL_Y}" font-size="5" fill="#8b949e" text-anchor="middle" font-family="{FF}">f{fn}</text>'
        )
    # d-block cols 17-26, labeled 3-12
    for c in range(17, 27):
        cx = col_x(c) + CELL_W // 2
        dn = c - 14  # col17->3, col26->12
        emit(
            f'  <text x="{cx}" y="{COL_LABEL_Y}" font-size="5" fill="#8b949e" text-anchor="middle" font-family="{FF}">{dn}</text>'
        )
    # p-block cols 27-32, labeled 13-18
    for c in range(27, 33):
        cx = col_x(c) + CELL_W // 2
        pn = c - 14  # col27->13, col32->18
        emit(
            f'  <text x="{cx}" y="{COL_LABEL_Y}" font-size="5" fill="#8b949e" text-anchor="middle" font-family="{FF}">{pn}</text>'
        )
    emit()

    # Block divider dashed vertical lines
    emit("  <!-- Block dividers -->")
    divider_y1 = 64
    divider_y2 = 444
    for dx in [75, 523, 843]:
        emit(
            f'  <line x1="{dx}" y1="{divider_y1}" x2="{dx}" y2="{divider_y2}" stroke="#30363d" stroke-width="0.8" stroke-dasharray="3,2"/>'
        )
    emit()

    # Period labels
    emit("  <!-- Period labels -->")
    for p in range(1, 8):
        py_center = period_y(p) + CELL_H // 2
        emit(
            f'  <text x="9" y="{py_center}" font-size="6" fill="#8b949e" text-anchor="middle" dominant-baseline="central" font-family="{FF}">{p}</text>'
        )
    emit()

    # Ghost cells (empty grid positions)
    emit("  <!-- Ghost cells -->")
    # Build set of filled (period, col) positions
    filled = set()
    for elem in ELEMENTS:
        _, _, _, period, col, _, _, _ = elem
        filled.add((period, col))

    ghost_ranges = [
        (1, range(2, 32)),  # period 1: cols 2-31 empty
        (2, range(3, 27)),  # period 2: cols 3-26 empty
        (3, range(3, 27)),  # period 3: cols 3-26 empty
        (4, range(3, 17)),  # period 4: cols 3-16 empty (f-block)
        (5, range(3, 17)),  # period 5: cols 3-16 empty (f-block)
    ]

    for gp, gcols in ghost_ranges:
        gy = period_y(gp)
        for gc in gcols:
            if (gp, gc) not in filled:
                gx = col_x(gc)
                emit(
                    f'  <rect x="{gx}" y="{gy}" width="{CELL_W}" height="{CELL_H}" rx="2" fill="none" stroke="#1e2530" stroke-width="0.4"/>'
                )
    emit()

    # Element cells
    emit("  <!-- Element cells -->")
    for elem in ELEMENTS:
        Z, sym, name, period, col, cat, block, config = elem
        x = col_x(col)
        y = period_y(period)
        fill, stroke, text_col = CAT[cat]
        strip_col = STRIP[block]

        emit("  <!-- Z={Z} {sym} -->")
        # Background rect
        emit(
            f'  <rect x="{x}" y="{y}" width="{CELL_W}" height="{CELL_H}" rx="3" fill="{fill}" stroke="{stroke}" stroke-width="0.6"/>'
        )
        # Atomic number
        emit(
            f'  <text x="{x + 2}" y="{y + 7}" font-size="5.5" fill="{text_col}" opacity="0.65" font-family="{FF}">{Z}</text>'
        )
        # Symbol (centered)
        emit(
            f'  <text x="{x + 15}" y="{y + 23}" font-size="11" font-weight="700" fill="{text_col}" text-anchor="middle" dominant-baseline="central" font-family="{FF}">{xml_escape(sym)}</text>'
        )
        # Name
        name_esc = xml_escape(name)
        emit(
            f'  <text x="{x + 15}" y="{y + 35}" font-size="5" fill="{text_col}" opacity="0.75" text-anchor="middle" font-family="{FF}">{name_esc}</text>'
        )
        # Valence config
        config_esc = xml_escape(config)
        emit(
            f'  <text x="{x + 15}" y="{y + 43}" font-size="4.5" fill="{text_col}" opacity="0.85" text-anchor="middle" font-family="{FF}">{config_esc}</text>'
        )
        # s/p/d/f color strip at bottom
        emit(
            f'  <rect x="{x + 1}" y="{y + 48}" width="28" height="3" rx="1" fill="{strip_col}" opacity="0.7"/>'
        )
        # Anomaly marker
        if Z in ANOMALY:
            emit(
                f'  <text x="{x + 24}" y="{y + 8}" font-size="6" fill="{GOLD}" font-family="{FF}">\u2605</text>'
            )

    emit()

    # Categories legend
    emit("  <!-- Legend -->")
    legend_y1 = 460
    legend_y2 = 475

    legend_items = [
        ("alkali", "Alkali metals"),
        ("aearth", "Alkaline earth"),
        ("trans", "Transition metals"),
        ("ptrans", "Post-transition"),
        ("metalloid", "Metalloids"),
        ("nonmetal", "Nonmetals"),
        ("halogen", "Halogens"),
        ("noble", "Noble gases"),
        ("lanthanide", "Lanthanides"),
        ("actinide", "Actinides"),
        ("unknown", "Unknown"),
    ]

    # Row 1: first 6 items
    row1 = legend_items[:6]
    # Row 2: remaining items + anomaly marker
    row2 = legend_items[6:]

    total_w_per_item = 90
    sq = 7

    # Row 1
    n1 = len(row1)
    start_x1 = (WIDTH - n1 * total_w_per_item) // 2
    for i, (cat_key, cat_label) in enumerate(row1):
        lx = start_x1 + i * total_w_per_item
        fill, stroke, _ = CAT[cat_key]
        emit(
            f'  <rect x="{lx}" y="{legend_y1}" width="{sq}" height="{sq}" rx="1" fill="{fill}" stroke="{stroke}" stroke-width="0.5"/>'
        )
        emit(
            f'  <text x="{lx + sq + 2}" y="{legend_y1 + 6}" font-size="6" fill="#8b949e" font-family="{FF}">{cat_label}</text>'
        )

    # Row 2 (includes anomaly marker)
    row2_items = row2 + [("_anomaly", "\u2605 Config anomaly")]
    n2 = len(row2_items)
    start_x2 = (WIDTH - n2 * total_w_per_item) // 2
    for i, (cat_key, cat_label) in enumerate(row2_items):
        lx = start_x2 + i * total_w_per_item
        if cat_key == "_anomaly":
            emit(
                f'  <text x="{lx}" y="{legend_y2 + 6}" font-size="7" fill="{GOLD}" font-family="{FF}">\u2605</text>'
            )
            emit(
                f'  <text x="{lx + sq + 2}" y="{legend_y2 + 6}" font-size="6" fill="#8b949e" font-family="{FF}">{xml_escape(cat_label[2:])}</text>'
            )
        else:
            fill, stroke, _ = CAT[cat_key]
            emit(
                f'  <rect x="{lx}" y="{legend_y2}" width="{sq}" height="{sq}" rx="1" fill="{fill}" stroke="{stroke}" stroke-width="0.5"/>'
            )
            emit(
                f'  <text x="{lx + sq + 2}" y="{legend_y2 + 6}" font-size="6" fill="#8b949e" font-family="{FF}">{cat_label}</text>'
            )

    emit()

    # Footnote
    emit("  <!-- Footnote -->")
    emit(
        f'  <text x="524" y="496" font-size="5.5" fill="#484f58" text-anchor="middle" font-family="{FF}">La (57) and Ac (89) shown in d-block col 17 per [Xe]5d\u00b96s\u00b2 / [Rn]6d\u00b97s\u00b2 configs \u00b7 Lu (71) and Lr (103) end the f-block</text>'
    )

    emit("</svg>")

    return "\n".join(lines)


if __name__ == "__main__":
    import os

    out_path = "/home/olivier/gdrive/dev/periodic-table/docs/public/tables/periodic_table_32col.svg"
    svg_content = generate_svg()
    with open(out_path, "w", encoding="utf-8") as f:
        f.write(svg_content)
    size = os.path.getsize(out_path)
    print(f"Written: {out_path}")
    print(f"File size: {size:,} bytes")
    print("Done.")
