# Chapter 4: The Shapes of Probability (The Angular Solution)

In Chapter 3, we successfully separated the Schrödinger equation into a Radial part ($R$) and an Angular part ($Y$). Now, we dive into the math of the angles.

Solving this equation will reveal why electrons don't just sit in simple spheres, but instead occupy the complex "dumbbells" and "donuts" that define the $p, d,$ and $f$ blocks of the periodic table.

## 4.1 The Angular Equation

From our separation in Chapter 3, we have the following equation for $Y(\theta, \phi)$:
$$\frac{1}{\sin \theta} \frac{\partial}{\partial \theta} \left(\sin \theta \frac{\partial Y}{\partial \theta}\right) + \frac{1}{\sin^2 \theta} \frac{\partial^2 Y}{\partial \phi^2} = -l(l+1)Y$$

Notice that this equation is independent of the nucleus's charge ($Z$) or the particle's mass ($m$). This means the *shapes* of orbitals are universal—a $p$-orbital in Hydrogen looks exactly like a $p$-orbital in Gold.

## 4.2 Splitting the Angles Again

To solve for $Y(\theta, \phi)$, we apply **Separation of Variables** one more time. We assume that the angular function is itself a product of two independent functions:
$$Y(\theta, \phi) = \Theta(\theta) \cdot \Phi(\phi)$$

**Why is this separation valid?**
This works because the $\theta$ and $\phi$ operators in the Laplacian are "orthogonal." Changing the angle around the equator ($\phi$) doesn't change the radius or the angle from the pole ($\theta$). Mathematically, the variables are independent parts of the same spherical surface.

By substituting this product into our angular equation and multiplying by $\sin^2\theta / (\Theta\Phi)$, we can pull the $\phi$ terms to one side:
$$\underbrace{\frac{\sin \theta}{\Theta} \frac{d}{d \theta} \left(\sin \theta \frac{d\Theta}{d \theta}\right) + l(l+1)\sin^2 \theta}_{\text{Depends only on } \theta} = \underbrace{-\frac{1}{\Phi} \frac{d^2\Phi}{d\phi^2}}_{\text{Depends only on } \phi}$$

Just as before, for both sides to stay equal, they must equal a constant. We call this constant **$m_l^2$**.

**Why the "Squared" Integer?**
Mathematically, a second-order derivative that returns the negative of itself ($\Phi'' = -C\Phi$) has sine and cosine solutions. By choosing a squared constant ($m_l^2$), we ensure the solution is in the form of a harmonic wave. And as we'll see in the next section, the "boundary" of $360^\circ$ will force $m_l$ to be a whole integer.

## 4.3 Solving for $\phi$: The Magnetic Quantum Number ($m_l$)

The equation for $\Phi$ is the simplest differential equation in quantum mechanics:
$$\frac{d^2\Phi}{d\phi^2} = -m_l^2\Phi$$

The solution is a complex exponential: $\Phi(\phi) = e^{im_l\phi}$.

**The Physical Constraint:**
If you rotate $360^\circ$ ($2\pi$ radians) around an atom, you must end up exactly where you started. Therefore, $\Phi(\phi)$ must equal $\Phi(\phi + 2\pi)$.
$$e^{im_l\phi} = e^{im_l(\phi + 2\pi)} \implies e^{i2\pi m_l} = 1$$
This is only true if **$m_l$ is an integer** ($\dots -2, -1, 0, 1, 2 \dots$). This $m_l$ is our second **Quantum Number**, the Magnetic Quantum Number, which determines the orbital's orientation in space.

## 4.4 Solving for $\theta$: The Orbital Quantum Number ($l$)

The equation for $\Theta(\theta)$ is much more challenging:
$$\sin \theta \frac{d}{d \theta} \left(\sin \theta \frac{d\Theta}{d \theta}\right) + [l(l+1)\sin^2 \theta - m_l^2]\Theta = 0$$

This is a famous mathematical equation known as the **Associated Legendre Equation**. Its solutions are the **Associated Legendre Polynomials**, $P_l^{m_l}(\cos\theta)$:

$$P_l^{m_l}(x) = \frac{(-1)^{m_l}}{2^l l!} (1-x^2)^{m_l/2} \frac{d^{l+m_l}}{dx^{l+m_l}} (x^2-1)^l$$

For a detailed derivation and historical context of these polynomials, see **[Annex A.4](annex.md#a4-associated-legendre-polynomials)**.

**The Physical Constraint:**
For these polynomials to remain finite (not blow up to infinity at the poles), the constant $l$ must be an integer, and it must satisfy:
$$l \geq |m_l|$$

This gives us our third **Quantum Number**, the Orbital Angular Momentum Quantum Number ($l$). It determines the "subshell" ($s, p, d, f$).

### The Hierarchy of Quantum Numbers

Because of the restriction $|m_l| \leq l$, each subshell has a specific number of orientations:

* **$l=0$ ($s$-subshell):** $m_l$ can only be $0$. (1 orientation, a sphere)
* **$l=1$ ($p$-subshell):** $m_l$ can be $-1, 0, 1$. (3 orientations, dumbbells)
* **$l=2$ ($d$-subshell):** $m_l$ can be $-2, -1, 0, 1, 2$. (5 orientations)
* **$l=3$ ($f$-subshell):** $m_l$ can be $-3, -2, -1, 0, 1, 2, 3$. (7 orientations)

**Wait, what about $l \ge 4$?**
Mathematically, $l$ can be $4, 5, 6 \dots$ ($g, h, i$ subshells). However, none of the 118 known elements in the **Periodic Table** require these subshells to house their electrons in their ground state. They are mathematically possible but physically unoccupied in the "base model" of our universe.

## 4.5 The Spherical Harmonics ($Y_l^{m_l}$)

When we combine $\Theta$ and $\Phi$, we get the **Spherical Harmonics**:
$$Y_l^{m_l}(\theta, \phi) \propto P_l^{m_l}(\cos\theta) e^{im_l\phi}$$

These functions are the "building blocks" of atomic shapes. By plotting the probability density ($|Y|^2$), we reveal the specific geometries of the subshells.

> **Interactive Visualization:** You can interact with and rotate these exact mathematical shapes using this **[Custom Desmos 3D Orbital Grapher](https://www.desmos.com/3d/qhbfggpwst)**. For the explicit formulas used to generate them, see the **[Annex](annex.md)**.

* **$l=0$ ($s$-orbital):** Spherically symmetric. There are no angular nodes, so the probability of finding the electron is identical in every direction from the nucleus.
* **$l=1$ ($p$-orbitals):** Lobed symmetry. Each has a single nodal plane passing through the nucleus, dividing the orbital into two distinct lobes. These align perfectly along the $x, y,$ or $z$ axes ($p_x, p_y, p_z$).
* **$l=2$ ($d$-orbitals):** Quadrant symmetry. Most have two perpendicular nodal planes that cross at the nucleus, creating a four-lobed structure. One exception ($d_{z^2}$) has two conical nodal surfaces, resulting in two lobes with a "toroidal" ring around the center.
* **$l=3$ ($f$-orbitals):** Octant symmetry. These have three nodal surfaces, resulting in highly complex eight-lobed or multi-ringed geometries.

## 4.6 Connection to the Visuals

You can see these mathematical solutions visualized in your reference sheets:

1. **[periodic_table_4_quantum_principles.svg](../periodic_table_4_quantum_principles.svg)**: Look at the "Orbital Shapes" section. The spheres and dumbbells shown there are the literal plots of these $Y_l^{m_l}$ functions.
2. **[periodic_table_3_orbital_shells.svg](../periodic_table_3_orbital_shells.svg)**: Note how the number of "boxes" in each subshell ($1$ for $s$, $3$ for $p$, $5$ for $d$) corresponds exactly to the number of allowed $m_l$ values we just derived.

## 4.7 Summary of the Angular Logic

1. **Boundary Condition (Rotation):** Requires $m_l$ to be an integer.
2. **Boundary Condition (Finiteness):** Requires $l$ to be an integer $\geq |m_l|$.
3. **The Result:** The geometry of the periodic table blocks ($s, p, d, f$) is a direct physical manifestation of these angular symmetries.

Next, in **Chapter 5**, we will solve the **Radial Equation** to find the energy of these shells and finally understand the "Rows" of the table.
