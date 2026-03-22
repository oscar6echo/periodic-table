# Chapter 5: The Energy Shells (The Radial Solution)

In the previous chapters, we solved the "Angular" half of the atom, which gave us the shapes of the orbitals ($s, p, d, f$). Now, we tackle the "Radial" half: the part that determines how far the electron is from the nucleus and, most importantly, its total energy.

Solving this final equation will reveal the "Energy Shells" that form the rows of the periodic table.

## 5.1 The Radial Equation

From our separation in Chapter 3, we have the following equation for $R(r)$:
$$\frac{d}{dr} \left(r^2 \frac{dR}{dr}\right) - \frac{2mr^2}{\hbar^2} [V(r) - E]R = l(l+1)R$$

Here, $V(r)$ is the **Coulomb Potential**, the electrostatic "pull" of the nucleus:
$$V(r) = -\frac{Ze^2}{4\pi\epsilon_0 r}$$

Unlike the angular equation, which was universal for all spheres, the radial equation depends on the specific physical properties of the atom: the charge of the nucleus ($Z$) and the total energy ($E$).

## 5.2 The Strategy: Asymptotic Behavior

This equation is notoriously difficult to solve because $V(r)$ becomes infinite at $r=0$. To crack it, physicists look at the "asymptotic" behavior—how the electron behaves when it is very far away.

1. **At large distances ($r \to \infty$):** The potential $V(r)$ becomes negligible. The equation looks like a simple decay. The solution must die out exponentially ($e^{-r}$) so the electron stays "bound" to the atom.
2. **At small distances ($r \to 0$):** The angular momentum term $l(l+1)$ dominates, preventing the electron from simply collapsing into the nucleus.

By combining these two behaviors, we assume a solution in the form of a power series multiplied by an exponential decay.

## 5.3 Solving for $r$: The Laguerre Polynomials

The math leads us to another set of famous 18th-century functions: the **Associated Laguerre Polynomials**, $L_{n-l-1}^{2l+1}(x)$:

$$L_q^p(x) = \frac{e^x x^{-p}}{q!} \frac{d^q}{dx^q} (e^{-x} x^{q+p})$$

For the specific values of $n$ and $l$ used in the Hydrogen atom, see **[Annex A.5](annex.md#a5-associated-laguerre-polynomials)**.

**The Physical Constraint:**
Just like the particle in a box (Chapter 2), the math only works if we introduce a new integer to keep the solution from blowing up to infinity. This is our fourth and final spatial **Quantum Number**:

**$n$ (The Principal Quantum Number)**

For the math to stay stable, $n$ must be an integer, and it must always be larger than the orbital angular momentum $l$. This creates the following hierarchy:

* **$n=1$ ($K$ shell):** $l=0$ ($s$). One subshell ($1s$).
* **$n=2$ ($L$ shell):** $l=0, 1$ ($s, p$). Two subshells ($2s, 2p$).
* **$n=3$ ($M$ shell):** $l=0, 1, 2$ ($s, p, d$). Three subshells ($3s, 3p, 3d$).
* **$n=4$ ($N$ shell):** $l=0, 1, 2, 3$ ($s, p, d, f$). Four subshells ($4s, 4p, 4d, 4f$).
* **$n=5$ ($O$ shell):** $l=0, 1, 2, 3, 4$ ($s, p, d, f, g$). Five subshells ($5s, 5p, 5d, 5f, 5g$).

*(Note: Although $n=5$ can mathematically hold a $g$-orbital, as mentioned in Chapter 4, no known element actually fills a $g$ subshell in its ground state.)*

## 5.4 The Result: Quantized Energy

By solving the radial equation, we finally derive the exact formula for the energy levels of a Hydrogen-like atom:
$$E_n = -\frac{Z^2 m e^4}{32 \pi^2 \epsilon_0^2 \hbar^2} \frac{1}{n^2}$$

For Hydrogen ($Z=1$), this simplifies to the famous value:
$$E_n = - \frac{13.6 \text{ eV}}{n^2}$$

The negative sign tells us the electron is "trapped" in the atom's potential well. To escape, it must absorb exactly enough energy to reach $E=0$.

This energy quantization is a direct result of the boundary conditions imposed on the **Associated Laguerre Polynomials** ($L_{n-l-1}^{2l+1}$):
$$L_q^p(x) = \frac{e^x x^{-p}}{q!} \frac{d^q}{dx^q} (e^{-x} x^{q+p})$$

> **Interactive Visualization:** You can visualize these "onion layers" and radial nodes in 3D using this **[Custom Desmos 3D Radial Grapher](https://TBD)**. Set a higher value for $n$ and $l=0$ to see the radial shells clearly. For the explicit formulas used to generate them, see the **[Annex A.5](annex.md#a5-associated-laguerre-polynomials)**.

## 5.5 Connection to the Visuals

These radial solutions define the "Layers" of the atom shown in your reference sheets:

1. **[periodic_table_3_orbital_shells.svg](../periodic_table_3_orbital_shells.svg)**: Look at the Bohr shell diagrams. Each circle ($K, L, M, N \dots$) represents a different value of $n$.
2. **[periodic_table_4_quantum_principles.svg](../periodic_table_4_quantum_principles.svg)**: See the "Aufbau Energy Levels" diagram. The vertical spacing of those levels is determined exactly by the $1/n^2$ energy formula we just derived.

## 5.6 Summary of the Radial Logic

1. **Boundary Condition (Infinity):** The electron must stay near the nucleus, forcing an exponential decay.
2. **Boundary Condition (Origin):** Angular momentum ($l$) creates a "centrifugal barrier" that keeps the electron away from the center.
3. **The Result:** The interaction between these two forces quantizes the atom's energy, creating the structured "rows" (periods) of the periodic table.

In the final **Chapter 6**, we will add the very last piece of the puzzle—**Spin**—and see how all these pieces click together to build the 118 elements.
