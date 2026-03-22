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
* **$n=6$ ($P$ shell):** $l=0, \dots, 5$ ($s, p, d, f, g, h$). Six subshells ($6s, 6p, 6d, 6f, 6g, 6h$).
* **$n=7$ ($Q$ shell):** $l=0, \dots, 6$ ($s, p, d, f, g, h, i$). Seven subshells ($7s, 7p, 7d, 7f, 7g, 7h, 7i$).

*NOTE*:  
Although higher shells mathematically contain many subshells, no known element in its ground state occupies orbitals beyond $7p$.  
For example, $5g, 6f, 7d$, and above are never used in ground-state chemistry.

## 5.4 The Result: Quantized Energy

By solving the radial equation, we finally derive the exact formula for the energy levels of a Hydrogen-like atom:
$$E_n = -\frac{Z^2 m e^4}{32 \pi^2 \epsilon_0^2 \hbar^2} \frac{1}{n^2}$$

For Hydrogen ($Z=1$), this simplifies to the famous value:
$$E_n = - \frac{13.6 \text{ eV}}{n^2}$$

The negative sign tells us the electron is "trapped" in the atom's potential well. To escape, it must absorb exactly enough energy to reach $E=0$.

### Summary of Energy Levels (Hydrogen, $Z=1$)

| $n$ | Shell | Energy ($E_n$) |
| :--- | :--- | :--- |
| **1** | K | -13.60 eV |
| **2** | L | -3.40 eV |
| **3** | M | -1.51 eV |
| **4** | N | -0.85 eV |
| **5** | O | -0.54 eV |
| **6** | P | -0.38 eV |
| **7** | Q | -0.28 eV |

## 5.5 The Reality: Multi-Electron Atoms

In the Hydrogen model we've discussed, the energy depends **only** on the principal quantum number $n$. This means a $2s$ electron and a $2p$ electron would have the exact same energy (they are "degenerate").

However, in reality, most atoms have more than one electron. This introduces two critical effects that break this degeneracy:

1. **Electron-Electron Repulsion:** Electrons don't just feel the "pull" of the nucleus; they also feel the "push" of other electrons.
2. **Shielding (Screening):** Inner electrons "shield" outer electrons from the full positive charge of the nucleus. An outer electron feels an **Effective Nuclear Charge ($Z_{eff}$)** that is lower than the actual $Z$.
3. **Penetration:** It is a common misconception that subshell shapes ($s, p, d, f$) only affect the *direction* of the electron. In fact, $l$ also changes the **radial probability distribution** (the likelihood of finding the electron at a certain distance).
    * **The Centrifugal Barrier:** High angular momentum ($l$) acts like an outward "force" that keeps electrons away from the center.
    * **Inner Lobes:** Lower $l$ orbitals (especially $s$) have small "peaks" of probability very close to the nucleus (see the "Secondary Peaks" in section 5.7). These "inner lobes" allow the electron to **penetrate** the shielding cloud of inner electrons and feel the full, unshielded pull of the nucleus.
    * **Ultimate Penetration (r=0):** Most importantly, **$s$-orbitals** are the only ones with a non-zero probability of finding the electron *at the very center* of the nucleus. All other orbitals ($p, d, f$) have a "node" at $r=0$, meaning they are strictly forbidden from the center.

    Because $s$-orbitals penetrate deeper than $p$-orbitals (and $p$ deeper than $d$), they are more "tightly bound" and have **lower energy** for the same value of $n$. This creates the subshell splitting seen in the **[Aufbau Principle Diagram](../periodic_table_4_quantum_principles.svg)**:

$$E_{ns} < E_{np} < E_{nd} < E_{nf}$$

This splitting is what causes the "overlap" in the periodic table, such as why the $4s$ subshell fills before the $3d$ subshell.

### Simplified Multi-Electron Energy

While the exact energy levels for multi-electron atoms require complex computer simulations, we can approximate them using the **Effective Nuclear Charge ($Z_{eff}$)**:

$$E_n \approx - \frac{Z_{eff}^2 \cdot 13.6 \text{ eV}}{n^2}$$

Here, $Z_{eff} = Z - \sigma$, where $\sigma$ is a "shielding constant" that represents the push-back from other electrons. For example, a $2s$ electron in Lithium ($Z=3$) might feel a $Z_{eff} \approx 1.28$ because the two $1s$ electrons shield it from the nucleus.

## 5.6 Connection to the Visuals

These radial solutions define the "Layers" of the atom shown in your reference sheets:

1. **[periodic_table_3_orbital_shells.svg](../periodic_table_3_orbital_shells.svg)**: Look at the Bohr shell diagrams. Each circle ($K, L, M, N \dots$) represents a different value of $n$.
2. **[periodic_table_4_quantum_principles.svg](../periodic_table_4_quantum_principles.svg)**: See the "Aufbau Energy Levels" diagram. The vertical spacing of those levels is determined by the combination of the $1/n^2$ base energy and the $l$-dependent splitting we just described.

## 5.7 Most Probable Radius ($r_{mp}$)

While the wavefunction $\psi$ gives the probability amplitude at a specific point, we are often interested in the probability of finding the electron at a certain **distance** $r$ from the nucleus, regardless of direction.

### The Radial Probability Density, $P(r)$

The probability of finding the electron in a thin spherical shell of thickness $dr$ at radius $r$ is:
$$P(r) \, dr = |R_{nl}(r)|^2 \cdot (4\pi r^2 \, dr)$$
Therefore, the **Radial Probability Density** is defined as $P(r) = r^2 |R_{nl}(r)|^2$.

### Calculating the Maximum Likelihood

The most probable radius $r_{mp}$ (where you are most likely to find the electron) corresponds to the peaks of the $P(r)$ curve. To find these peaks, we solve for:
$$\frac{dP}{dr} = 0$$

### Summary of Radial Properties ($a_0 = 1$)

The following table summarizes the key radial characteristics of the hydrogen atom up to $n=5$.

| $n$ | $l$ | Orbital | Node at $r=0$ | Radial Nodes | Main $r_{mp}$ | Secondary Peaks |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| **1** | 0 | 1s | False | False | 1.00 | None |
| **2** | 0 | 2s | False | True (1) | 5.236 | 0.764 |
| | 1 | 2p | True | False | 4.00 | None |
| **3** | 0 | 3s | False | True (2) | 13.07 | 3.82, 0.71 |
| | 1 | 3p | True | True (1) | 12.00 | 3.00 |
| | 2 | 3d | True | False | 9.00 | None |
| **4** | 0 | 4s | False | True (3) | 21.92 | 11.44, 5.14, 1.50 |
| | 1 | 4p | True | True (2) | 20.92 | 10.68, 4.40 |
| | 2 | 4d | True | True (1) | 18.62 | 9.38 |
| | 3 | 4f | True | False | 16.00 | None |
| **5** | 0 | 5s | False | True (4) | 33.00 | 19.55, 10.90, 5.07, 1.48 |
| | 4 | 5g | True | False | 25.00 | None |

## 5.8 Summary of the Radial Logic

1. **Boundary Condition (Infinity):** The electron must stay near the nucleus, forcing an exponential decay.
2. **Boundary Condition (Origin):** Angular momentum ($l$) creates a "centrifugal barrier" that keeps the electron away from the center.
3. **The Result:** The interaction between these two forces quantizes the atom's energy, creating the structured "rows" (periods) of the periodic table.

In the final **[Chapter 6](chap_6.md)**, we add the very last piece of the puzzle—**Spin**—and see how all these pieces click together to build the 118 elements.
