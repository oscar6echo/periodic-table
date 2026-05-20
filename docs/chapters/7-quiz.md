# Quiz

## Question 1 — Valid or Invalid Quantum Numbers?

For each set of quantum numbers below, state whether it is **valid** or **invalid**, and explain why.

Recall the allowed ranges:

| Quantum number | Symbol | Allowed values |
| :--- | :---: | :--- |
| Principal | $n$ | $1, 2, 3, \ldots$ (positive integers only) |
| Azimuthal | $\ell$ | $0, 1, \ldots, n-1$ |
| Magnetic | $m_\ell$ | $-\ell, \ldots, 0, \ldots, +\ell$ |
| Spin | $m_s$ | $+\tfrac{1}{2}$ or $-\tfrac{1}{2}$ only |

---

**Set A:** $n = 1,\ \ell = 1$

::: details Answer

**Invalid.** $\ell$ must satisfy $0 \le \ell \le n - 1$. For $n = 1$, the only allowed value is $\ell = 0$. Setting $\ell = 1$ violates this constraint — there is no $p$ subshell in the first shell.

:::

---

**Set B:** $n = 2,\ \ell = 1,\ m_\ell = -1,\ m_s = +\tfrac{3}{2}$

::: details Answer

**Invalid.** The spin quantum number $m_s$ can only take the values $+\tfrac{1}{2}$ or $-\tfrac{1}{2}$. The value $+\tfrac{3}{2}$ is not allowed — it would correspond to a higher spin than an electron possesses. The other three numbers ($n = 2$, $\ell = 1$, $m_\ell = -1$) are all valid on their own.

:::

---

**Set C:** $n = 3,\ \ell = 1,\ m_\ell = 2$

::: details Answer

**Invalid.** $m_\ell$ must satisfy $-\ell \le m_\ell \le +\ell$. For $\ell = 1$, the allowed values are $m_\ell \in \{-1,\ 0,\ +1\}$. The value $m_\ell = 2$ lies outside this range.

:::

---

**Set D:** $n = 0$

::: details Answer

**Invalid.** $n$ must be a positive integer: $n \ge 1$. Zero is not a valid principal quantum number — there is no zeroth shell.

:::

---

## Question 2 — Ground-State Configuration of Calcium

What is the ground-state electron configuration of Calcium (Ca, $Z = 20$)?

::: details Answer

$$1s^2\ 2s^2\ 2p^6\ 3s^2\ 3p^6\ 4s^2$$

**Why $4s$ before $3d$?** The Madelung (diagonal) rule fills subshells in order of increasing $n + \ell$:

- $4s$: $n + \ell = 4 + 0 = 4$
- $3d$: $n + \ell = 3 + 2 = 5$

Since $4 < 5$, the $4s$ subshell is lower in energy for light atoms and fills first. After $3p^6$ (at $Z = 18$, argon), the next two electrons go into $4s$, completing the configuration above.

The shorthand notation using the previous noble gas is:

$$[\text{Ar}]\ 4s^2$$

Calcium is the last element before the $3d$ transition metals begin filling. At $Z = 21$ (Scandium), the first $3d$ electron appears.

:::

---

## Question 3 — Meaning of the Wave Function

The wave function $\Psi$ is complex-valued, yet every measurement of a quantum system returns a real number. What does $\Psi$ represent, and how is a real, observable prediction extracted from it?

::: details Answer

The wave function is **not** itself an observable quantity — it is a **probability amplitude**. The observable is its absolute square,

$$|\Psi(\mathbf{r}, t)|^2 = \Psi^*\Psi,$$

which is real and non-negative. $|\Psi(\mathbf{r}, t)|^2\,dV$ gives the **probability** of finding the particle in the small volume $dV$ around $\mathbf{r}$ at time $t$.

Because the particle must be found *somewhere*, $\Psi$ is **normalized** so that the total probability is 1:

$$\int |\Psi|^2 \, dV = 1.$$

The complex phase of $\Psi$ never shows up in a single measurement, but it is essential: it governs how quantum states **interfere**, which is what makes quantum mechanics differ from a classical probability theory.

:::

---

## Question 4 — Particle in a Box: Energies

A particle is confined to a one-dimensional box of length $L$.

**(a)** What is the ratio $E_3 / E_1$ of the third energy level to the ground state?
**(b)** Why can the particle never have exactly zero energy?

::: details Answer

**(a)** The allowed energies are

$$E_n = \frac{n^2 \pi^2 \hbar^2}{2mL^2},$$

so $E_n \propto n^2$. Therefore

$$\frac{E_3}{E_1} = \frac{3^2}{1^2} = 9.$$

**(b)** The lowest allowed state is $n = 1$, not $n = 0$. Setting $n = 0$ gives $\psi(x) = A\sin(0) = 0$ everywhere — a particle that exists nowhere. The smallest genuine standing wave fits half a wavelength across the box and still carries

$$E_1 = \frac{\pi^2 \hbar^2}{2mL^2} > 0.$$

This irreducible **zero-point energy** is a direct consequence of confinement: a perfectly localized, perfectly motionless particle is forbidden by the uncertainty principle.

:::

---

## Question 5 — Why Spherical Coordinates?

Why is the Schrödinger equation for the hydrogen atom solved in spherical coordinates rather than Cartesian, and what two equations does separation of variables produce?

::: details Answer

The Coulomb potential depends **only** on the distance from the nucleus:

$$V(r) = -\frac{e^2}{4\pi\epsilon_0 \, r}.$$

In Cartesian coordinates that distance is $r = \sqrt{x^2 + y^2 + z^2}$, which tangles all three variables together. Spherical coordinates match the natural **spherical symmetry** of the atom, so the potential involves $r$ alone.

Writing the wave function as a product $\Psi(r,\theta,\phi) = R(r)\,Y(\theta,\phi)$ and separating splits one hard 3-D problem into two simpler ones:

- the **radial equation** (in $r$) — determines the energy levels and the principal quantum number $n$;
- the **angular equation** (in $\theta, \phi$) — determines the orbital shapes and the quantum numbers $\ell$ and $m_\ell$.

The two equations are linked by the **separation constant** $\ell(\ell+1)$.

:::

---

## Question 6 — Orbitals in a Subshell

For the $d$ subshell:

**(a)** What are the allowed values of $m_\ell$?
**(b)** How many orbitals does the subshell contain?
**(c)** How many electrons can it hold in total?

::: details Answer

A $d$ subshell has $\ell = 2$.

**(a)** $m_\ell$ takes every integer from $-\ell$ to $+\ell$:

$$m_\ell \in \{-2,\ -1,\ 0,\ +1,\ +2\}.$$

**(b)** Each value of $m_\ell$ labels one orbital, so there are $2\ell + 1 = 5$ orbitals.

**(c)** By the Pauli exclusion principle each orbital holds 2 electrons (opposite spins), giving

$$2(2\ell + 1) = 10 \text{ electrons}$$

— exactly the width of the $d$-block.

:::

---

## Question 7 — Nodes of a 3p Orbital

How many **radial** nodes and how many **angular** nodes does a $3p$ orbital have? What is the total number of nodes?

::: details Answer

A $3p$ orbital has $n = 3$ and $\ell = 1$.

- **Angular nodes** $= \ell = 1$ — one nodal plane through the nucleus, which is what splits a $p$ orbital into two lobes.
- **Radial nodes** $= n - \ell - 1 = 3 - 1 - 1 = 1$ — one spherical shell of zero probability.
- **Total nodes** $= n - 1 = 2$.

The rule **total nodes $= n - 1$** holds for every orbital. The value of $\ell$ decides how many of those nodes are angular; the remainder, $n - \ell - 1$, are radial.

:::

---

## Question 8 — Hydrogen Energy and Subshell Splitting

**(a)** Using $E_n = -13.6\ \text{eV}\,/\,n^2$, find the energy of the $n = 2$ level of hydrogen.
**(b)** In hydrogen the $2s$ and $2p$ subshells have the *same* energy, but in a multi-electron atom $2s$ lies *below* $2p$. Why?

::: details Answer

**(a)**

$$E_2 = -\frac{13.6\ \text{eV}}{2^2} = -\frac{13.6\ \text{eV}}{4} = -3.40\ \text{eV}.$$

**(b)** In hydrogen — a single electron — the energy depends only on $n$, so $2s$ and $2p$ are **degenerate**. In a multi-electron atom this degeneracy is broken by **penetration** and **shielding**. The $2s$ radial distribution has a small inner peak that lets the electron penetrate the $1s$ core and feel a larger effective nuclear charge $Z_\text{eff}$. The $2p$ orbital has a node at $r = 0$ and is held further out, so it is shielded more effectively. Penetrating deeper, the $2s$ electron is more tightly bound — lower in energy — hence $E_{2s} < E_{2p}$.

:::

---

## Question 9 — Hund's Rule and Nitrogen

State the **Pauli exclusion principle** and **Hund's rule**. Then apply them to nitrogen ($Z = 7$): give its ground-state $2p$ occupation, the number of unpaired electrons, and whether it is paramagnetic or diamagnetic.

::: details Answer

- **Pauli exclusion principle:** no two electrons in an atom may share all four quantum numbers $(n, \ell, m_\ell, m_s)$. Hence an orbital holds at most 2 electrons, with opposite spins.
- **Hund's rule:** within a subshell, electrons occupy separate orbitals with parallel spins before any orbital is doubly filled — this minimizes electron–electron repulsion.

Nitrogen's configuration is $1s^2\ 2s^2\ 2p^3$. The three $2p$ electrons each take a different $2p$ orbital with parallel spins:

$$2p:\quad \uparrow\ \ \uparrow\ \ \uparrow$$

That leaves **3 unpaired electrons**, so nitrogen is **paramagnetic**. With its half-filled $2p$ subshell, it is in fact the most paramagnetic atom of period 2.

:::

---

## Question 10 — Why Periods 6 and 7 Hold 32 Elements

Periods 6 and 7 of the periodic table each contain 32 elements. Derive this number from the quantum-mechanical subshell capacities.

::: details Answer

A period corresponds to filling one complete set of subshells in Aufbau order. Each subshell holds $2(2\ell + 1)$ electrons:

$$s = 2,\quad p = 6,\quad d = 10,\quad f = 14.$$

Periods 6 and 7 are the first to draw on **all four** block types — they fill an $s$, an $f$, a $d$ and a $p$ subshell:

$$2 + 14 + 10 + 6 = 32.$$

For period 6 the sequence is $6s \to 4f \to 5d \to 6p$; for period 7 it is $7s \to 5f \to 6d \to 7p$. The 14 contributed by the $f$ subshell is exactly the length of the lanthanide and actinide rows.

(Periods 4–5 omit the $f$ block and hold $2 + 10 + 6 = 18$; periods 2–3 omit both $f$ and $d$ and hold $2 + 6 = 8$.)

:::
