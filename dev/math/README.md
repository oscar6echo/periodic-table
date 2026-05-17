# Quantum Mechanics Scripts

This directory contains the Python tools used to generate the symbolic mathematical data for the educational series.

## Available Scripts

The folder contains two primary SymPy-based generators:

1. **`radial_wavefunctions.py`**
    * **Purpose:** Generates the normalized radial wavefunctions $R_{nl}(r)$ for all 19 ground-state subshells (from $1s$ up to $7p$).
    * **Logic:** Implements generalized Laguerre polynomials and normalization constants.
    * **Output:** Symbolic formulas simplified with $a_0 = 1$.

2. **`angular_wavefunctions.py`**
    * **Purpose:** Generates the real forms of spherical harmonics $Y_{lm}(\theta, \phi)$ for $s, p, d,$ and $f$ orbitals.
    * **Convention:** Uses the Desmos 3D convention (`phi` for polar, `theta` for azimuthal).
    * **Output:** Symbolic trigonometric expressions for orbital orientations (e.g., $p_x, p_y, p_z, d_{xz}, \dots$).

## How to Run

Ensure you have a Python environment with `sympy` installed.

```bash
# Set your python path (example using micromamba)
PYTHON_BIN=/home/olivier/micromamba/envs/wa/bin/python

# Run the Radial Wavefunction generator
$PYTHON_BIN radial_wavefunctions.py

# Run the Angular Wavefunction generator
$PYTHON_BIN angular_wavefunctions.py
```

## Generated Data

The pre-computed outputs of these scripts are stored in the **`scripts/output/`** folder:

* **`radial_output.txt`**: Complete list of radial formulas for all occupied shells.
* **`angular_output.txt`**: Real-form angular orientation formulas for $l=0$ to $3$.
