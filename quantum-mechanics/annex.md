# Annex: Vector Calculus Operators

This annex provides the formal definitions of the gradient ($\nabla$) and Laplacian ($\nabla^2$) operators used throughout the chapters.

## A.1 Cartesian Coordinates ($x, y, z$)

In the familiar 3D grid, the operators are straightforward:

### The Gradient ($\nabla$)

Used for the momentum operator ($\mathbf{p} = -i\hbar\nabla$):
$$\nabla = \mathbf{\hat{x}}\frac{\partial}{\partial x} + \mathbf{\hat{y}}\frac{\partial}{\partial y} + \mathbf{\hat{z}}\frac{\partial}{\partial z}$$

### The Laplacian ($\nabla^2$)

Used for kinetic energy in the Schrödinger equation:
$$\nabla^2 = \frac{\partial^2}{\partial x^2} + \frac{\partial^2}{\partial y^2} + \frac{\partial^2}{\partial z^2}$$

---

## A.3 Derivation: From Cartesian to Spherical

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

## A.4 Associated Legendre Polynomials

In Chapter 4, the solution to the $\theta$ equation involves **Associated Legendre Polynomials**, denoted as $P_l^{m_l}(\cos\theta)$.

### Historical Context

These polynomials were not invented for quantum mechanics. They were developed by the French mathematician **Adrien-Marie Legendre (1752–1833)** in the late 18th century.

Legendre was studying **Celestial Mechanics**—specifically, how to calculate the gravitational potential of a planet or a star. He discovered that when you try to solve the Laplacian ($\nabla^2$) for any spherical object, these specific polynomials naturally emerge as the only stable solutions. Schrödinger "borrowed" this 150-year-old math because an atom, like a planet, is a spherically symmetric system.

### Physical Interpretation of $l$ and $m_l$

To visualize how these polynomials shape an atom, think of the wave function as a pattern of "vibrations" on the surface of a sphere.

- **The Degree ($l$): Polar Complexity**
    The degree $l$ determines the number of **polar nodes**—circular "dead zones" where the electron cannot exist. Specifically, there are always $l - |m_l|$ horizontal nodal circles (like lines of latitude).
    *Example:* If $l=1$ (a $p$-orbital), there is one major nodal plane. This splits the sphere into two distinct lobes. If $l=2$ (a $d$-orbital), the increased degree creates two nodal surfaces, resulting in a more complex four-lobed pattern.

- **The Order ($m_l$): Azimuthal Complexity**
    The order $m_l$ determines how the wave function "wraps" around the equator. It creates **vertical nodal planes** (like lines of longitude). Specifically, there are $|m_l|$ vertical nodal planes.
    *Example:* If $m_l=0$, there are no vertical nodal planes, meaning the orbital is "smooth" as you rotate around the $z$-axis (cylindrical symmetry). If $m_l=2$, the orbital has two vertical planes slicing it like a cake, forcing the electron into four distinct segments around the equator.

### Visualizing the Solutions in Desmos 3D

Because these functions are difficult to draw by hand, you can visualize them interactively using the **[Desmos 3D Calculator](https://www.desmos.com/3d)**.

**Important:** In Desmos 3D, typing `rho` represents the spherical radius. To see the classic "lobed" shapes of atomic orbitals, we plot the **Real Spherical Harmonics** (the absolute value of the angular probability).

The following formulas have been **normalized** so that each orbital has a maximum radius of approximately 1, making them easy to compare at the same scale. You can also find these pre-loaded in this **[Custom Desmos 3D Orbital Grapher](https://www.desmos.com/3d/qhbfggpwst)**.

**Understanding the Labels:**
The labels like $p_x$ or $d_{xy}$ are the Cartesian translations of the spherical math, telling chemists which axes the lobes point along. The formulas are sorted below by $m_l$ in pairs ($+1$ and $-1$, $+2$ and $-2$), because the positive and negative versions of an order share the exact same fundamental shape, just rotated around the axis.

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

*(Tip: In Desmos, wrapping the function in absolute value bars `|...|` ensures the radius is always positive, which creates the physical boundaries of the electron clouds you see in chemistry textbooks.)*
