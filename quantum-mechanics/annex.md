# Annex: Vector Calculus and Mathematical Solutions

This annex provides formal definitions and historical context for the mathematical operators and functions used in the chapters.

## A.1 Cartesian Coordinates ($x, y, z$)

In the familiar 3D grid, the operators are straightforward:

### The Gradient ($\nabla$)

Used for the momentum operator ($\mathbf{p} = -i\hbar\nabla$):
$$\nabla = \mathbf{\hat{x}}\frac{\partial}{\partial x} + \mathbf{\hat{y}}\frac{\partial}{\partial y} + \mathbf{\hat{z}}\frac{\partial}{\partial z}$$

### The Laplacian ($\nabla^2$)

Used for kinetic energy in the Schrödinger equation:
$$\nabla^2 = \frac{\partial^2}{\partial x^2} + \frac{\partial^2}{\partial y^2} + \frac{\partial^2}{\partial z^2}$$

---

## A.2 Spherical Coordinates ($r, \theta, \phi$)

In spherical systems, we define a point by its distance from the origin ($r$), the polar angle from the z-axis ($\theta$), and the azimuthal angle around the xy-plane ($\phi$).

- $x = r \sin\theta \cos\phi$
- $y = r \sin\theta \sin\phi$
- $z = r \cos\theta$

---

## A.3 Derivation: From Cartesian to Spherical

To transform the Laplacian from $x, y, z$ to $r, \theta, \phi$, we use **Metric Scale Factors** ($h$). These factors act as "converters" between a small change in a coordinate (like $d\theta$) and the actual physical distance traveled in space.

### 1. Geometric Origin of the Scale Factors

Imagine moving a point by a tiny amount in each of the three directions. The total displacement $d\mathbf{s}$ is the sum of three arc lengths:

1. **Radial Displacement ($dr$):**
    Moving "outward" by $dr$ moves you exactly $dr$ units in space.
    $$\text{Arc length}_r = 1 \cdot dr \implies \mathbf{h_r = 1}$$
2. **Polar Displacement ($d\theta$):**
    Rotating "down" by $d\theta$ at a distance $r$ traces an arc on a circle of radius $r$.
    $$\text{Arc length}_\theta = r \cdot d\theta \implies \mathbf{h_\theta = r}$$
3. **Azimuthal Displacement ($d\phi$):**
    Rotating "around" the z-axis by $d\phi$. However, your distance from the z-axis is not $r$; it is the "horizontal" projection $r\sin\theta$.
    $$\text{Arc length}_\phi = (r\sin\theta) \cdot d\phi \implies \mathbf{h_\phi = r\sin\theta}$$

### 2. The Gradient

In any orthogonal coordinate system ($q_1, q_2, q_3$), the gradient is defined as:
$$\nabla f = \frac{\mathbf{\hat{q}_1}}{h_1}\frac{\partial f}{\partial q_1} + \frac{\mathbf{\hat{q}_2}}{h_2}\frac{\partial f}{\partial q_2} + \frac{\mathbf{\hat{q}_3}}{h_3}\frac{\partial f}{\partial q_3}$$
Substituting our $h$ factors:
$$\nabla = \mathbf{\hat{r}}\frac{\partial}{\partial r} + \mathbf{\hat{\theta}}\frac{1}{r}\frac{\partial}{\partial \theta} + \mathbf{\hat{\phi}}\frac{1}{r\sin\theta}\frac{\partial}{\partial \phi}$$

### 3. The Laplacian

The Laplacian is the divergence of the gradient ($\nabla \cdot \nabla$). The general formula for a coordinate system with scale factors $h_1, h_2, h_3$ is:
$$\nabla^2 f = \frac{1}{h_1 h_2 h_3} \left[ \frac{\partial}{\partial q_1}\left(\frac{h_2 h_3}{h_1}\frac{\partial f}{\partial q_1}\right) + \frac{\partial}{\partial q_2}\left(\frac{h_1 h_3}{h_2}\frac{\partial f}{\partial q_2}\right) + \frac{\partial}{\partial q_3}\left(\frac{h_1 h_2}{h_3}\frac{\partial f}{\partial q_3}\right) \right]$$

For spherical coordinates, the product $h_r h_\theta h_\phi = r^2\sin\theta$.

- **The $r$ term:** $\frac{\partial}{\partial r}(r \cdot r\sin\theta \cdot \frac{1}{1} \frac{\partial f}{\partial r}) = \sin\theta \frac{\partial}{\partial r}(r^2 \frac{\partial f}{\partial r})$
- **The $\theta$ term:** $\frac{\partial}{\partial \theta}(1 \cdot r\sin\theta \cdot \frac{1}{r} \frac{\partial f}{\partial \theta}) = \frac{\partial}{\partial \theta}(\sin\theta \frac{\partial f}{\partial \theta})$
- **The $\phi$ term:** $\frac{\partial}{\partial \phi}(1 \cdot r \cdot \frac{1}{r\sin\theta} \frac{\partial f}{\partial \phi}) = \frac{1}{\sin\theta} \frac{\partial^2 f}{\partial \phi^2}$

---

## A.4 Associated Legendre Polynomials, $P_l^{m_l}(x)$

In Chapter 4, the solution to the $\theta$ equation involves **Associated Legendre Polynomials**, $P_l^{m_l}(\cos\theta)$.

### Historical Context

These polynomials were not invented for quantum mechanics. They were developed by the French mathematician **Adrien-Marie Legendre (1752–1833)** in the late 18th century.

Legendre was studying **Celestial Mechanics**—specifically, how to calculate the gravitational potential of a planet or a star. He discovered that when you try to solve the Laplacian ($\nabla^2$) for any spherical object, these specific polynomials naturally emerge as the only stable solutions. Schrödinger "borrowed" this 150-year-old math because an atom, like a planet, is a spherically symmetric system.

### Why use a 3D plot for 2D angles?

The angular part of the wavefunction, $Y(\theta, \phi)$, depends only on two angles and mathematically exists only on the surface of a unit sphere. To visualize this abstract function in our 3D space, physicists use a specific mapping:

1. **Mapping Value to Distance:** We set the distance from the origin (the radius $\rho$ in our plots) equal to the absolute value of the function: $\rho = |Y_l^{m_l}(\theta, \phi)|$.
2. **Directional Probability:** This creates a surface where the "bulge" in a specific direction $( \theta, \phi )$ is proportional to the probability of finding the electron in that direction.
3. **Independence from Radius:** It is crucial to understand that these 3D shapes represent **only the angular likelihood**. They are completely independent of the radial part $R(r)$ discussed in Chapter 5. In a real atom, the electron's position is a combination of this angular shape and the radial "shells."

### Physical Interpretation of $l$ and $m_l$

To visualize how these polynomials shape an atom, think of the wave function as a pattern of "vibrations" on the surface of a sphere.

- **The Degree ($l$): Polar Complexity**
    The degree $l$ determines the number of **polar nodes**—circular "dead zones" where the electron cannot exist. Specifically, there are always $l - |m_l|$ horizontal nodal circles (like lines of latitude).
- **The Order ($m_l$): Azimuthal Complexity**
    The order $m_l$ determines how the wave function "wraps" around the equator. It creates **vertical nodal planes** (like lines of longitude). Specifically, there are $|m_l|$ vertical nodal planes.

### Visualizing the Solutions in Desmos 3D

> **Custom Viewer Introduction:**  
> **Title:** 3D Atomic Orbital Visualizer (Angular Harmonics)  
> **Description:** This interactive graph plots the angular probability density $|Y_l^{m_l}(\theta, \phi)|^2$ of the hydrogen atom. By mapping the probability value to the spherical radius ($\rho$), we reveal the characteristic lobes and nodes that define the $s, p, d,$ and $f$ subshells. Note that these shapes represent the directional "likelihood" of finding an electron, independent of its distance from the nucleus.

**Important:** In Desmos 3D, typing `rho` represents the spherical radius. To see the classic "lobed" shapes of atomic orbitals, we plot the **Real Spherical Harmonics** (the absolute value of the angular probability).

The following formulas have been **normalized** so that each orbital has a maximum radius of approximately 1. You can find these pre-loaded in this **[Custom Desmos 3D Orbital Grapher](https://www.desmos.com/3d/qhbfggpwst)**.

**$l=0$ ($s$-orbital):**

- $m_l=0$ ($s$): `rho = 1`

**$l=1$ ($p$-orbitals):**

- $m_l=0$ ($p_z$): `rho = |cos(phi)|`
- $m_l=+1$ ($p_x$): `rho = |sin(phi)*cos(theta)|`
- $m_l=-1$ ($p_y$): `rho = |sin(phi)*sin(theta)|`

**$l=2$ ($d$-orbitals):**

- $m_l=0$ ($d_{z^2}$): `rho = 0.5 * |3*cos^2(phi) - 1|`
- $m_l=+1$ ($d_{xz}$): `rho = |2*sin(phi)*cos(phi)*cos(theta)|`
- $m_l=-1$ ($d_{yz}$): `rho = |2*sin(phi)*cos(phi)*sin(theta)|`
- $m_l=+2$ ($d_{x^2-y^2}$): `rho = |sin^2(phi)*cos(2*theta)|`
- $m_l=-2$ ($d_{xy}$): `rho = |sin^2(phi)*sin(2*theta)|`

**$l=3$ ($f$-orbitals):**

- $m_l=0$ ($f_{z^3}$): `rho = 0.5 * |5*cos^3(phi) - 3*cos(phi)|`
- $m_l=+1$ ($f_{xz^2}$): `rho = 0.73 * |sin(phi)*(5*cos^2(phi) - 1)*cos(theta)|`
- $m_l=-1$ ($f_{yz^2}$): `rho = 0.73 * |sin(phi)*(5*cos^2(phi) - 1)*sin(theta)|`
- $m_l=+2$ ($f_{z(x^2-y^2)}$): `rho = 2.6 * |sin^2(phi)*cos(phi)*cos(2*theta)|`
- $m_l=-2$ ($f_{zxy}$): `rho = 2.6 * |sin^2(phi)*cos(phi)*sin(2*theta)|`
- $m_l=+3$ ($f_{x(x^2-3y^2)}$): `rho = |sin^3(phi)*cos(3*theta)|`
- $m_l=-3$ ($f_{y(3x^2-y^2)}$): `rho = |sin^3(phi)*sin(3*theta)|`

---

## A.5 Associated Laguerre Polynomials, $L_q^p(x)$

In Chapter 5, the solution to the radial equation involves **Associated Laguerre Polynomials**, $L_{n-l-1}^{2l+1}(x)$.

### Historical Context

These were developed by the French mathematician **Edmond Laguerre (1834–1886)**. His polynomials are the only solutions that satisfy the radial Schrödinger equation while remaining finite at the origin ($r=0$) and decaying to zero at infinity ($r \to \infty$).

### Physical Interpretation of $n$ and $l$

The radial part of the wavefunction determines the "reach" of the electron and its internal structure.

- **The Principal Quantum Number ($n$): Energy Shells**
    As $n$ increases, the electron has more energy and is likely to be found further from the nucleus. This creates the "layers" or shells of the atom.
- **Radial Nodes: Onion Layers**
    The number of **radial nodes** is given by $n - l - 1$. These are spherical surfaces where the probability of finding the electron is zero.

### Visualizing the Radial Solutions in Desmos 3D

> **Custom Viewer Introduction:**  
> **Title:** 3D Radial Node Visualizer (Energy Shells)  
> **Description:** This graph visualizes the radial part of the wavefunction $R_{nl}(r)$ and its probability density. By plotting isosurfaces where $(R_{nl})^2$ is constant, we can see the internal "onion-layer" structure of the atom. The gaps between the shells represent radial nodes—regions where the electron probability drops to zero, a direct consequence of the energy quantization for a bound electron.

**Important:** First define the radius $r = \sqrt{x^2 + y^2 + z^2}$. Then, define the radial wavefunction $R_{nl}(r)$. Finally, plot the probability density squared $(R_{nl})^2 = c$, where $c$ is a small constant (e.g., $0.01$).

The following formulas for $R_{nl}(r)$ use atomic units ($a_0 = 1$):

**$n=1$ (K Shell):**

- **$1s$ ($l=0$):** `R_10 = 2 * exp(-r)`

**$n=2$ (L Shell):**

- **$2s$ ($l=0$):** `R_20 = (1/sqrt(8)) * (2 - r) * exp(-r/2)`
- **$2p$ ($l=1$):** `R_21 = (1/sqrt(24)) * r * exp(-r/2)`

**$n=3$ (M Shell):**

- **$3s$ ($l=0$):** `R_30 = (2 / (81*sqrt(3))) * (27 - 18*r + 2*r^2) * exp(-r/3)`
- **$3p$ ($l=1$):** `R_31 = (8 / (81*sqrt(6))) * r * (6 - r) * exp(-r/3)`
- **$3d$ ($l=2$):** `R_32 = (4 / (81*sqrt(30))) * r^2 * exp(-r/3)`
