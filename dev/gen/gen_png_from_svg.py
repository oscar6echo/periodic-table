#!/home/olivier/micromamba/envs/wa/bin/python
"""Convert SVG file(s) to PNG using rsvg-convert.

Usage:
    python gen_png_from_svg.py <file.svg> [--zoom 2] [--dpi 192]
    python gen_png_from_svg.py periodic_table_4_*.svg
"""

import argparse
import subprocess
import sys
from pathlib import Path

RSVG = "/usr/bin/rsvg-convert"


def convert(svg_path: Path, zoom: float, dpi: int) -> Path:
    png_path = svg_path.with_suffix(".png")
    cmd = [RSVG, "--zoom", str(zoom), "--dpi-x", str(dpi), "--dpi-y", str(dpi),
           "--output", str(png_path), str(svg_path)]
    result = subprocess.run(cmd, capture_output=True, text=True)
    if result.returncode != 0:
        print(f"ERROR: {svg_path.name}: {result.stderr.strip()}", file=sys.stderr)
        sys.exit(result.returncode)
    return png_path


def main() -> None:
    parser = argparse.ArgumentParser(description="Convert SVG(s) to PNG via rsvg-convert")
    parser.add_argument("files", nargs="+", type=Path, help="SVG file(s) to convert")
    parser.add_argument("--zoom", type=float, default=2.0,
                        help="Zoom factor (default: 2.0 for 2× resolution)")
    parser.add_argument("--dpi", type=int, default=192,
                        help="Output DPI (default: 192)")
    args = parser.parse_args()

    for svg in args.files:
        if not svg.exists():
            print(f"ERROR: {svg} not found", file=sys.stderr)
            sys.exit(1)
        if svg.suffix.lower() != ".svg":
            print(f"WARNING: {svg} does not have .svg extension, skipping", file=sys.stderr)
            continue
        png = convert(svg, zoom=args.zoom, dpi=args.dpi)
        print(f"{svg.name}  →  {png.name}")


if __name__ == "__main__":
    main()
