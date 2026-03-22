import sympy as sp
from typing import List, Tuple, Any, cast
from math import factorial as fact


def generalized_laguerre(n: int, alpha: int, x: sp.Expr) -> sp.Expr:
    """
    Computes the Generalized Laguerre Polynomial L_n^alpha(x).

    The radial part of the hydrogenic wavefunction is defined by these polynomials.
    Formula: L_n^alpha(x) = sum_{k=0}^n (-1)^k * (n+alpha choose n-k) * x^k / k!
    """
    # Use Any for the accumulator to satisfy Pylance reportOperatorIssue
    # regarding SymPy's operator overloading on sp.Expr.
    expr: Any = sp.S.Zero
    for k in range(n + 1):
        # Using math.factorial for integer arguments.
        num = fact(n + alpha)
        den = fact(n - k) * fact(alpha + k) * fact(k)
        coeff = num // den

        # Treat components as Any during multiplication to bypass stub limitations.
        neg_one_pwr: Any = sp.S((-1) ** k)
        s_coeff: Any = sp.S(coeff)
        x_pwr: Any = x**k

        term: Any = neg_one_pwr * s_coeff * x_pwr
        expr += term

    return cast(sp.Expr, expr)


def radial_wavefunction(n: int, ell: int) -> sp.Expr:
    """
    Computes the normalized radial wavefunction R_nl(r) for the Hydrogen atom.

    Inputs:
        n: Principal quantum number (1, 2, 3...)
        ell: Azimuthal quantum number (0, 1, ..., n-1)

    Returns:
        A sympy expression in terms of r and a0.
    """
    r, a0 = sp.symbols("r a0", real=True, positive=True)

    # Dimensionless variable rho = 2r / (n * a0)
    # Using Any for intermediate math to avoid Pylance operator issues.
    rho: Any = sp.S(2) * r / (sp.S(n) * a0)

    # Normalization constant N_nl
    # Formula: sqrt((2/na0)^3 * (n-l-1)! / (2n * (n+l)!))
    num_val = fact(n - ell - 1)
    den_val = 2 * n * fact(n + ell)

    # Use sp.S to ensure the division and sqrt are handled by SymPy
    norm: Any = sp.sqrt((sp.S(2) / (sp.S(n) * a0)) ** 3 * sp.S(num_val) / sp.S(den_val))

    # Associated Laguerre part: L_{n-ell-1}^{2ell+1}(rho)
    poly: Any = generalized_laguerre(n - ell - 1, 2 * ell + 1, cast(sp.Expr, rho))

    # R_nl(r) = N_nl * exp(-rho/2) * rho^ell * L(rho)
    exponent: Any = -rho / sp.S(2)
    rho_pwr: Any = rho**ell
    wf_exp: Any = sp.exp(exponent)

    wf: Any = norm * wf_exp * rho_pwr * poly

    return cast(sp.Expr, sp.simplify(wf))


def main() -> None:
    """
    Main execution to generate and display wavefunctions for specific states.
    """
    # Define shells we want to generate
    # Note: 5g (5,4) exists mathematically but is not occupied in ground state atoms.
    # 6s, 6p, 6d, 7s, 7p are occupied in elements like Cs, Rn, Fr, Og.
    states: List[Tuple[int, int, str]] = [
        (6, 0, "6s"),
        (6, 1, "6p"),
        (6, 2, "6d"),
        (7, 0, "7s"),
        (7, 1, "7p"),
    ]

    print("Hydrogenic Radial Wavefunctions (R_nl)")
    print("======================================\n")

    for n, ell, label in states:
        wf = radial_wavefunction(n, ell)
        print(f"--- {label} (n={n}, l={ell}) ---")
        # Print pretty version and LaTeX version
        print("Expression:")
        sp.pprint(wf)
        print("\nLaTeX:")
        print(sp.latex(wf))
        print("\n")


if __name__ == "__main__":
    main()
