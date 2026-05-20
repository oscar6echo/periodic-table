#!/usr/bin/env python3
"""Generate bohr-shell-xxx-2.svg diagrams for elements from elements.json.

Uses color codes from section 6.7 ValenceTable:
  s: #f78166 (orange)
  p: #79c0ff (blue)
  d: #56d364 (green)
  f: #d2a8ff (purple)
"""

import json
import math
import os
import re

# Color codes from section 6.7 ValenceTable.vue
COLORS = {
    "s": "#f78166",
    "p": "#79c0ff",
    "d": "#56d364",
    "f": "#d2a8ff",
}

# Subshell capacities
CAPACITY = {
    "s": 2,
    "p": 6,
    "d": 10,
    "f": 14,
}

# Shell radii (from existing SVGs)
SHELL_RADII = {
    1: 18,
    2: 40,
    3: 62,
    4: 84,
    5: 106,
    6: 128,
    7: 150,
}

# Noble gas configurations for expansion
NOBLE_GAS_CONFIGS = {
    "He": "1s2",
    "Ne": "1s2 2s2 2p6",
    "Ar": "1s2 2s2 2p6 3s2 3p6",
    "Kr": "1s2 2s2 2p6 3s2 3p6 3d10 4s2 4p6",
    "Xe": "1s2 2s2 2p6 3s2 3p6 3d10 4s2 4p6 4d10 5s2 5p6",
    "Rn": "1s2 2s2 2p6 3s2 3p6 3d10 4s2 4p6 4d10 5s2 5p6 4f14 5d10 6s2 6p6",
    "Og": "1s2 2s2 2p6 3s2 3p6 3d10 4s2 4p6 4d10 5s2 5p6 4f14 5d10 6s2 6p6 5f14 6d10 7s2 7p6",
}

# Parse superscript characters to numbers
SUPERSRIPT_MAP = {
    "\u2070": "0",  # ⁰
    "\u00b9": "1",  # ¹
    "\u00b2": "2",  # ²
    "\u00b3": "3",  # ³
    "\u2074": "4",  # ⁴
    "\u2075": "5",  # ⁵
    "\u2076": "6",  # ⁶
    "\u2077": "7",  # ⁷
    "\u2078": "8",  # ⁸
    "\u2079": "9",  # ⁹
}

# Background and styling
BG_COLOR = "#0d1117"
RING_COLOR = "#30363d"
TEXT_COLOR = "#e6edf3"
LABEL_COLOR = "#8b949e"


def expand_noble_gas(config_str):
    """Expand noble gas abbreviations in electron configuration.

    e.g., "[Ar] 3d6 4s2" -> "1s2 2s2 2p6 3s2 3p6 3d6 4s2"
    """
    if not config_str:
        return config_str

    # Find noble gas abbreviations
    for symbol in NOBLE_GAS_CONFIGS:
        if f"[{symbol}]" in config_str:
            noble_config = NOBLE_GAS_CONFIGS[symbol]
            config_str = config_str.replace(f"[{symbol}]", noble_config + " ")

    return config_str


def parse_config(config_str):
    """Parse electron configuration string into dict of {subshell: count}.

    Handles both formats:
      - "1s² 2s² 2p⁶ 3s² 3p⁶"
      - "[He] 2s² 2p⁶"
      - "[Ar] 3d⁶ 4s²"
    """
    if not config_str:
        return {}

    # Expand noble gas abbreviations
    config_str = expand_noble_gas(config_str)

    # Replace superscripts with regular numbers
    for sup, num in SUPERSRIPT_MAP.items():
        config_str = config_str.replace(sup, num)

    # Parse pattern: number + letter + number
    # e.g., "1s2", "2p6", "3d10", "4f14"
    pattern = r"(\d+)([spdf])(\d+)"
    matches = re.findall(pattern, config_str)

    result = {}
    for n, l, count in matches:  # noqa: E741
        key = f"{n}{l}"
        result[key] = int(count)

    return result


def get_max_shell(config_dict):
    """Get the maximum shell number from configuration dict."""
    max_n = 0
    for subshell in config_dict:
        n = int(subshell[0])
        max_n = max(max_n, n)
    return max_n


def get_subshell_type(subshell):
    """Extract subshell type (s, p, d, f) from subshell string like '3d' or '4f'."""
    return subshell[-1]


def get_subshell_n(subshell):
    """Extract principal quantum number from subshell string."""
    return int(subshell[:-1])


def get_shell_subshells(n):
    """Get subshell types that exist for a given principal quantum number n.

    Returns list of subshell types in order s -> p -> d -> f
    """
    subshells = []
    if n >= 1:
        subshells.append("s")
    if n >= 2:
        subshells.append("p")
    if n >= 3:
        subshells.append("d")
    if n >= 4:
        subshells.append("f")
    return subshells


def generate_svg(element, config_dict, output_path):
    """Generate SVG for a single element's Bohr shell diagram.

    Electrons for all subshells in each shell are placed on a single circle
    with equal angular spacing. Positions are assigned in order: s -> p -> d -> f.
    """
    # symbol = element['symbol']
    # name = element['name']
    # z = element['Z']

    # Calculate viewBox based on max shell
    max_shell = get_max_shell(config_dict)
    max_radius = SHELL_RADII.get(max_shell, 18 * max_shell)

    # Center point
    center_x = 200
    center_y = 200

    # ViewBox: give some padding
    padding = 30
    viewbox_x = center_x - max_radius - padding
    viewbox_y = center_y - max_radius - padding
    viewbox_width = 2 * (max_radius + padding)
    viewbox_height = 2 * (max_radius + padding)

    # Sort subshells by n, then by subshell type order: s -> p -> d -> f
    subshell_type_order = {"s": 0, "p": 1, "d": 2, "f": 3}
    subshells = sorted(
        config_dict.keys(),
        key=lambda s: (get_subshell_n(s), subshell_type_order.get(s[-1], 4)),
    )

    # Group subshells by shell for labeling
    subshells_by_shell = {}
    for subshell in subshells:
        n = get_subshell_n(subshell)
        if n not in subshells_by_shell:
            subshells_by_shell[n] = []
        subshells_by_shell[n].append(subshell)

    # Build SVG
    svg_lines = []
    svg_lines.append('<?xml version="1.0" encoding="utf-8"?>')
    svg_lines.append(
        f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="{viewbox_x} {viewbox_y} {viewbox_width} {viewbox_height}">'
    )

    # Background rectangle
    svg_lines.append(
        f'<rect x="{viewbox_x}" y="{viewbox_y}" width="{viewbox_width}" height="{viewbox_height}" fill="{BG_COLOR}"/>'
    )

    # Draw shell rings (concentric circles)
    for n in range(1, max_shell + 1):
        radius = SHELL_RADII.get(n, 18 * n)
        svg_lines.append(
            f'<circle cx="{center_x}" cy="{center_y}" r="{radius}" fill="none" stroke="{RING_COLOR}" stroke-width="0.8"/>'
        )

    # For each shell, place all subshell electrons on a single circle
    for n in sorted(subshells_by_shell.keys()):
        radius = SHELL_RADII.get(n, 18 * n) or 0

        # Get all subshells for this shell, sorted by subshell type order: s -> p -> d -> f
        # Use a custom sort key to ensure s comes before p, p before d, d before f
        subshell_type_order = {"s": 0, "p": 1, "d": 2, "f": 3}
        shell_subshells = sorted(
            subshells_by_shell[n], key=lambda s: subshell_type_order.get(s[-1], 4)
        )

        # Calculate total number of positions (sum of all subshell capacities in this shell)
        total_positions = sum(CAPACITY[get_subshell_type(ss)] for ss in shell_subshells)

        # Generate all positions at equal angular spacing
        # Angle for position i: 2*pi*i/total_positions
        # Use negative sin for y to get counter-clockwise (anti-clockwise) in SVG coordinate system
        all_positions = []
        for i in range(total_positions):
            angle = 2 * math.pi * i / total_positions
            x = center_x + radius * math.cos(angle)
            y = center_y - radius * math.sin(angle)  # Negate for counter-clockwise
            all_positions.append((x, y))

        # Assign positions to subshells in order s -> p -> d -> f
        current_position = 0
        for subshell in shell_subshells:
            subshell_type = get_subshell_type(subshell)
            count = config_dict.get(subshell, 0)
            capacity = CAPACITY[subshell_type]
            color = COLORS[subshell_type]

            # Draw electrons (filled positions)
            for i in range(count):
                ex, ey = all_positions[current_position + i]
                svg_lines.append(
                    f'<circle cx="{ex:.1f}" cy="{ey:.1f}" r="3.5" fill="{color}" opacity="0.9"/>'
                )

            # Draw empty slots
            for i in range(count, capacity):
                ex, ey = all_positions[current_position + i]
                svg_lines.append(
                    f'<circle cx="{ex:.1f}" cy="{ey:.1f}" r="2.5" fill="none" stroke="{RING_COLOR}" stroke-width="0.6" opacity="0.5"/>'
                )

            current_position += capacity

        # Draw subshell labels for this shell
        # Vertical offset for multiple subshells in same shell
        for idx, subshell in enumerate(shell_subshells):
            subshell_type = get_subshell_type(subshell)
            color = COLORS[subshell_type]
            offset = (idx - len(shell_subshells) / 2 + 0.5) * 12
            label_x = center_x + radius + 8
            label_y = center_y + offset
            svg_lines.append(
                f'<text x="{label_x}" y="{label_y}" font-size="5.5" fill="{color}" font-family="sans-serif" text-anchor="start" dominant-baseline="central" font-weight="600">{subshell}</text>'
            )

    # Draw shell labels (n=1, n=2, etc.) on a vertical line below center
    for n in range(1, max_shell + 1):
        radius = SHELL_RADII.get(n, 18 * n)
        label_x = center_x
        label_y = center_y + radius + 12
        svg_lines.append(
            f'<text x="{label_x}" y="{label_y}" font-size="5.5" fill="{LABEL_COLOR}" font-family="sans-serif" text-anchor="middle">n={n}</text>'
        )

    # Close SVG
    svg_lines.append("</svg>")

    # Write to file
    with open(output_path, "w") as f:
        f.write("\n".join(svg_lines) + "\n")

    print(f"Generated: {output_path}")


def main():
    # Load elements data
    elements_file = "docs/public/data/elements.json"
    with open(elements_file, "r") as f:
        elements = json.load(f)

    # Elements to generate
    target_elements = ["H", "Ne", "Ar", "C", "Fe", "Se", "Nd"]

    # Output directory
    output_dir = "docs/public/diagrams"
    os.makedirs(output_dir, exist_ok=True)

    # Generate for each element
    for symbol in target_elements:
        element = next((e for e in elements if e["symbol"] == symbol), None)
        if not element:
            print(f"Warning: Element {symbol} not found in {elements_file}")
            continue

        # Parse electron configuration
        electron_config = element.get("Electron configuration", "")
        config_dict = parse_config(electron_config)

        if not config_dict:
            print(
                f"Warning: Could not parse configuration for {symbol}: {electron_config}"
            )
            continue

        # Generate SVG
        output_path = os.path.join(output_dir, f"bohr-shells-{symbol.lower()}-2.svg")
        generate_svg(element, config_dict, output_path)


if __name__ == "__main__":
    main()
