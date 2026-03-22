from math import factorial as fact
from typing import Any, List, Tuple, cast

import sympy as sp


def generalized_laguerre(n: int, alpha: int, x: sp.Expr) -> sp.Expr:
    """
    Computes the Generalized Laguerre Polynomial L_n^alpha(x).

    The radial part of the hydrogenic wavefunction is defined by these polynomials.
    Formula: L_n^alpha(x) = sum_{k=0}^n (-1)^k * (n+alpha choose n-k) * x^k / k!
    """
    # Use Any for the accumulator to satisfy Pylance reportOperatorIssue
    expr: Any = sp.S.Zero
    for k in range(n + 1):
        num = fact(n + alpha)
        den = fact(n - k) * fact(alpha + k) * fact(k)
        coeff = num // den

        neg_one_pwr: Any = sp.S((-1) ** k)
        s_coeff: Any = sp.S(coeff)
        x_pwr: Any = x**k

        term: Any = neg_one_pwr * s_coeff * x_pwr
        expr += term

    return cast(sp.Expr, expr)


def radial_wavefunction(n: int, _l: int) -> sp.Expr:
    """
    Computes the normalized radial wavefunction R_nl(r) for the Hydrogen atom.
    Assumes a0 = 1 for simplicity in output.
    """
    r = sp.Symbol("r", real=True, positive=True)
    # a0 = sp.S.One  # Setting a0 = 1

    # Dimensionless variable rho = 2r / (n * a0)
    rho: Any = sp.S(2) * r / sp.S(n)

    # Normalization constant N_nl
    num_val = fact(n - _l - 1)
    den_val = 2 * n * fact(n + _l)
    norm: Any = sp.sqrt((sp.S(2) / sp.S(n)) ** 3 * sp.S(num_val) / sp.S(den_val))

    # Associated Laguerre part
    poly: Any = generalized_laguerre(n - _l - 1, 2 * _l + 1, cast(sp.Expr, rho))

    exponent: Any = -rho / sp.S(2)
    rho_pwr: Any = rho**_l
    wf_exp: Any = sp.exp(exponent)

    wf: Any = norm * wf_exp * rho_pwr * poly

    return cast(sp.Expr, sp.simplify(wf))


def main() -> None:
    """
    Generates all ground-state radial _l (up to Z=118).
    """
    states: List[Tuple[int, int, str]] = [
        (1, 0, "1s"),
        (2, 0, "2s"),
        (2, 1, "2p"),
        (3, 0, "3s"),
        (3, 1, "3p"),
        (3, 2, "3d"),
        (4, 0, "4s"),
        (4, 1, "4p"),
        (4, 2, "4d"),
        (4, 3, "4f"),
        (5, 0, "5s"),
        (5, 1, "5p"),
        (5, 2, "5d"),
        (5, 3, "5f"),
        (6, 0, "6s"),
        (6, 1, "6p"),
        (6, 2, "6d"),
        (7, 0, "7s"),
        (7, 1, "7p"),
    ]

    print("Hydrogenic Radial Wavefunctions (R_nl) with a0=1")
    print("================================================\n")

    for n, _l, label in states:
        wf = radial_wavefunction(n, _l)
        print(f"--- {label} ---")
        print(wf)
        print("")


if __name__ == "__main__":
    main()
