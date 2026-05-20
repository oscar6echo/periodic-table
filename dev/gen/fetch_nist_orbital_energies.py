"""
Scrape orbital eigenvalues (LDA) from NIST Atomic Reference Data for
Electronic Structure Calculations (H–U, Z=1–92).

NIST URL: .../atomic-reference-data-electronic-7-{NIST_INDEX}
The NIST index is NOT Z-1; the correct Z→index mapping is hardcoded below.
Units: Hartree → converted to eV (1 Ha = 27.211386 eV)

Output: docs/public/data/orbital_energies.json
Format: { "Z": { "subshell": energy_eV, ... }, ... }
"""

import json
import time
import re
import sys
from pathlib import Path

import requests
from bs4 import BeautifulSoup

HARTREE_TO_EV = 27.211386

BASE_URL = (
    "https://www.nist.gov/pml/atomic-reference-data-electronic-structure-calculations/"
    "atomic-reference-data-electronic-7-{index}"
)

OUT_PATH = Path(__file__).parent.parent.parent / "docs/public/data/orbital_energies.json"

# Correct Z → NIST page index mapping (scraped from NIST element list page)
Z_TO_NIST_INDEX = {
     1:  0,  2:  1,  3:  2,  4:  3,  5:  4,  6:  5,  7: 91,  8:  6,
     9:  7, 10:  8, 11:  9, 12: 10, 13: 11, 14: 12, 15: 13, 16: 14,
    17: 15, 18: 16, 19: 18, 20: 19, 21: 20, 22: 21, 23: 22, 24: 23,
    25: 24, 26: 25, 27: 26, 28: 27, 29: 28, 30: 29, 31: 30, 32: 31,
    33: 32, 34: 33, 35: 34, 36: 35, 37: 36, 38: 37, 39: 38, 40: 17,
    41: 39, 42: 40, 43: 41, 44: 42, 45: 43, 46: 44, 47: 45, 48: 46,
    49: 47, 50: 48, 51: 49, 52: 50, 53: 51, 54: 52, 55: 53, 56: 54,
    57: 55, 58: 74, 59: 75, 60: 76, 61: 77, 62: 78, 63: 79, 64: 80,
    65: 81, 66: 82, 67: 83, 68: 84, 69: 85, 70: 86, 71: 87, 72: 56,
    73: 57, 74: 58, 75: 59, 76: 60, 77: 61, 78: 62, 79: 63, 80: 64,
    81: 65, 82: 66, 83: 67, 84: 68, 85: 69, 86: 70, 87: 71, 88: 72,
    89: 73, 90: 88, 91: 89, 92: 90,
}

# Standard subshell labels we care about (LDA uses plain nl notation)
SUBSHELL_RE = re.compile(r"^(\d[spdf])$")


def parse_element_page(z: int) -> dict[str, float]:
    """Fetch NIST page for element Z and return {subshell: energy_eV} for LDA neutral atom."""
    nist_index = Z_TO_NIST_INDEX[z]
    url = BASE_URL.format(index=nist_index)
    resp = requests.get(url, timeout=30)
    resp.raise_for_status()

    soup = BeautifulSoup(resp.text, "html.parser")

    # Page has two tables: table[0] = neutral atom, table[1] = singly ionized
    # We only want the neutral atom (table[0]).
    tables = soup.find_all("table")
    if not tables:
        return {}

    table = tables[0]
    rows = table.find_all("tr")
    if not rows:
        return {}

    headers = [th.get_text(strip=True) for th in rows[0].find_all(["th", "td"])]

    # Find the LDA column (first of the four approximations)
    lda_col = None
    for i, h in enumerate(headers):
        if h.strip().upper() == "LDA":
            lda_col = i
            break
    if lda_col is None:
        return {}

    orbital_energies: dict[str, float] = {}
    for row in rows[1:]:
        cells = row.find_all(["th", "td"])
        if len(cells) <= lda_col:
            continue
        label = cells[0].get_text(strip=True)
        val_str = cells[lda_col].get_text(strip=True)

        # Accept labels like 1s, 2p, 3d, 4f only
        if not SUBSHELL_RE.match(label):
            continue
        try:
            val_ha = float(val_str)
        except ValueError:
            continue

        orbital_energies[label] = round(val_ha * HARTREE_TO_EV, 4)

    return orbital_energies


def main():
    # Always start fresh (old data used wrong URL mapping)
    data: dict[str, dict[str, float]] = {}
    errors = []

    for z in range(1, 93):
        key = str(z)
        try:
            energies = parse_element_page(z)
            data[key] = energies
            subshells = list(energies.keys())
            print(f"  Z={z:3d}  subshells={subshells}  4s={energies.get('4s','–'):>10}  3d={energies.get('3d','–'):>10} eV")
        except Exception as e:
            print(f"  Z={z:3d}  ERROR: {e}", file=sys.stderr)
            errors.append(z)

        # Save after every element
        with open(OUT_PATH, "w") as f:
            json.dump(data, f, indent=2)

        time.sleep(0.4)  # polite rate limit

    print(f"\nDone. {len(data)} elements written to {OUT_PATH}")
    if errors:
        print(f"Errors for Z={errors}")


if __name__ == "__main__":
    main()
