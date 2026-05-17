import sympy as sp
from typing import Any, cast


def get_real_spherical_harmonic(ell: int, m: int) -> sp.Expr:
    """
    Computes the real part of the spherical harmonic Y_lm.
    Note: For visualization, we often use the absolute value of the real forms.

    This script uses the Desmos 3D convention:
    - phi: polar angle (from z-axis)
    - theta: azimuthal angle (around xy-plane)
    """
    theta, phi = sp.symbols("theta phi", real=True)

    # Cast the SymPy function to Any to bypass Pylance's attribute access checks
    # on dynamically generated SymPy classes.
    Ynm_func: Any = sp.Ynm
    ynm_raw: Any = Ynm_func(ell, m, phi, theta)
    ynm: Any = ynm_raw.expand(complex=True)

    if m == 0:
        re_func: Any = sp.re
        return cast(sp.Expr, re_func(ynm))

    elif m > 0:
        # Real part (e.g. px, dxz)
        # Linear combination: (Y_lm + (-1)^m * Y_l,-m) / sqrt(2)
        ynm_neg_raw: Any = Ynm_func(ell, -m, phi, theta)
        ynm_neg: Any = ynm_neg_raw.expand(complex=True)
        phase: Any = sp.S((-1) ** m)
        sqrt2: Any = sp.sqrt(sp.S(2))
        res: Any = (ynm + phase * ynm_neg) / sqrt2
        simplify_func: Any = sp.simplify
        re_func_inner: Any = sp.re
        return cast(sp.Expr, simplify_func(re_func_inner(res)))

    else:
        # Imaginary part (e.g. py, dyz)
        # Linear combination: (Y_l|m| - (-1)^|m| * Y_l,-|m|) / (i * sqrt(2))
        m_abs = abs(m)
        ynm_pos_raw: Any = Ynm_func(ell, m_abs, phi, theta)
        ynm_pos: Any = ynm_pos_raw.expand(complex=True)
        ynm_neg_inner_raw: Any = Ynm_func(ell, -m_abs, phi, theta)
        ynm_neg_inner: Any = ynm_neg_inner_raw.expand(complex=True)
        phase_inner: Any = sp.S((-1) ** m_abs)
        sqrt2_inner: Any = sp.sqrt(sp.S(2))
        res_im: Any = (ynm_pos + phase_inner * ynm_neg_inner) / sqrt2_inner
        simplify_func_im: Any = sp.simplify
        im_func: Any = sp.im
        return cast(sp.Expr, simplify_func_im(im_func(res_im)))


def main() -> None:
    """
    Generates the angular part formulas for s, p, d, f orbitals.
    Outputs both plain text and Desmos-friendly LaTeX (normalized).
    """
    print("Angular Wavefunctions (Spherical Harmonics - Real Forms)")
    print("Convention: phi=polar, theta=azimuthal")
    print("========================================================\n")

    for ell in range(4):
        label = ["s", "p", "d", "f"][ell]
        print(f"--- {label}-orbitals (l={ell}) ---")

        for m in range(-ell, ell + 1):
            expr: Any = get_real_spherical_harmonic(ell, m)
            trigsimp_func: Any = sp.trigsimp
            simplified: Any = trigsimp_func(expr)
            print(f"m={m}: {simplified}")

            # Generate LaTeX for Desmos (absolute value)
            latex_str = sp.latex(simplified)
            # Desmos uses |...| for absolute value
            print(f"LaTeX: \\rho = \\left| {latex_str} \\right|")
        print("")


if __name__ == "__main__":
    main()
