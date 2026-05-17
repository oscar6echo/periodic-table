# Math Reference

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

## A.4 Associated Legendre Polynomials, $P_l^{m_l}(x)$ {#associated-legendre-polynomials}

In Chapter 4, the solution to the $\theta$ equation involves **Associated Legendre Polynomials**, $P_l^{m_l}(\cos\theta)$.

### Formal Definition

These polynomials can be expressed using **Rodrigues' Formula**:

$$P_l^{m_l}(x) = \frac{(-1)^{m_l}}{2^l l!} (1-x^2)^{m_l/2} \frac{d^{l+m_l}}{dx^{l+m_l}} (x^2-1)^l$$

### Historical Context

These polynomials were not invented for quantum mechanics. They were developed by the French mathematician **Adrien-Marie Legendre (1752–1833)** in the late 18th century. Legendre was studying **Celestial Mechanics**—specifically, the gravitational potential of planets. Schrödinger adopted this math because atoms, like planets, are spherically symmetric systems.

### Why use a 3D plot for 2D angles?

The angular part of the wavefunction, $Y(\theta, \phi)$, depends only on two angles. To visualize it in 3D:

1. **Mapping:** We set the radius $\rho$ in our plots equal to the absolute value: $\rho = |Y_l^{m_l}(\theta, \phi)|$.
2. **Interpretation:** The surface "bulge" in a specific direction indicates the probability of finding the electron there.
3. **Independence:** These shapes represent **only the angular likelihood** and are independent of the radial "shells" $R(r)$ discussed in Chapter 5.

### Visualizing the Solutions in Desmos 3D

::: tip Visualize the solutions? 🤔
**[3D Atomic Orbital Visualizer](https://www.desmos.com/3d/qhbfggpwst)** — Interactive graph plotting angular probability density $|Y_l^{m_l}|^2$.

**⚠️ Notation alert:** In standard textbooks (and Chapter 4), $\theta$ is polar and $\phi$ is azimuthal. **In Desmos 3D these names are swapped**: `phi` is polar, `theta` is azimuthal. The formulas below use the Desmos convention.
:::

| Subshell | $m_l$ | Name | Formula (Desmos convention) |
| :---: | :---: | :--- | :--- |
| $s$ ($l=0$) | $0$ | — | `rho = 1` |
| $p$ ($l=1$) | $0$ | $p_z$ | `rho = \|cos(phi)\|` |
| | $+1$ | $p_x$ | `rho = \|sin(phi)*cos(theta)\|` |
| | $-1$ | $p_y$ | `rho = \|sin(phi)*sin(theta)\|` |
| $d$ ($l=2$) | $0$ | $d_{z^2}$ | `rho = 0.5 * \|3*cos^2(phi) - 1\|` |
| | $+1$ | $d_{xz}$ | `rho = \|2*sin(phi)*cos(phi)*cos(theta)\|` |
| | $-1$ | $d_{yz}$ | `rho = \|2*sin(phi)*cos(phi)*sin(theta)\|` |
| | $+2$ | $d_{x^2-y^2}$ | `rho = \|sin^2(phi)*cos(2*theta)\|` |
| | $-2$ | $d_{xy}$ | `rho = \|sin^2(phi)*sin(2*theta)\|` |
| $f$ ($l=3$) | $0$ | $f_{z^3}$ | `rho = 0.5 * \|5*cos^3(phi) - 3*cos(phi)\|` |
| | $+1$ | $f_{xz^2}$ | `rho = 0.73 * \|sin(phi)*(5*cos^2(phi) - 1)*cos(theta)\|` |
| | $-1$ | $f_{yz^2}$ | `rho = 0.73 * \|sin(phi)*(5*cos^2(phi) - 1)*sin(theta)\|` |
| | $+2$ | $f_{z(x^2-y^2)}$ | `rho = 2.6 * \|sin^2(phi)*cos(phi)*cos(2*theta)\|` |
| | $-2$ | $f_{zxy}$ | `rho = 2.6 * \|sin^2(phi)*cos(phi)*sin(2*theta)\|` |
| | $+3$ | $f_{x(x^2-3y^2)}$ | `rho = \|sin^3(phi)*cos(3*theta)\|` |
| | $-3$ | $f_{y(3x^2-y^2)}$ | `rho = \|sin^3(phi)*sin(3*theta)\|` |

---

## A.5 Associated Laguerre Polynomials, $L_q^p(x)$ {#associated-laguerre-polynomials}

In Chapter 5, the solution to the radial equation involves **Associated Laguerre Polynomials**, $L_{n-l-1}^{2l+1}(x)$.

### Historical Context

These were developed by the French mathematician **Edmond Laguerre (1834–1886)**. His polynomials are the only solutions that satisfy the radial Schrödinger equation while remaining finite at the origin ($r=0$) and decaying to zero at infinity ($r \to \infty$).

### Physical Interpretation: Onion Layers

The number of **radial nodes** is $n - l - 1$. These are spherical shells where probability is zero. A $2s$ orbital ($1$ node) looks like a sphere inside another sphere.

### Visualizing the Radial Solutions in Desmos 3D

::: tip Visualize the solutions? 🤔
**[3D Radial Node Visualizer](https://www.desmos.com/calculator/yngjiz1sk0)** — Plotting isosurfaces of $(R_{nl})^2$ to reveal the "onion-layer" and radial node structure.
:::

First define $r = \sqrt{x^2 + y^2 + z^2}$. These formulas use atomic units ($a_0 = 1$). Plot $(R_{nl})^2 = c$ (try $c = 0.01$).

| Shell | Orbital | Radial function |
| :---: | :--- | :--- |
| K | $1s$ | `R_10 = 2 * exp(-r)` |
| L | $2s$ | `R_20 = (sqrt(2)/4) * (2 - r) * exp(-r/2)` |
| | $2p$ | `R_21 = (sqrt(6)/12) * r * exp(-r/2)` |
| M | $3s$ | `R_30 = (2*sqrt(3)/27) * (3 - 2*r) * exp(-r/3)` |
| | $3p$ | `R_31 = (2*sqrt(6)/243) * r * (6 - r) * exp(-r/3)` |
| | $3d$ | `R_32 = (2*sqrt(30)/1215) * r^2 * exp(-r/3)` |
| N | $4s$ | `R_40 = (1/32) * (r^2 - 6*r + 8) * exp(-r/4)` |
| | $4p$ | `R_41 = (sqrt(15)/192) * r * (4 - r) * exp(-r/4)` |
| | $4d$ | `R_42 = (sqrt(5)/3840) * r^2 * (12 - r) * exp(-r/4)` |
| | $4f$ | `R_43 = (sqrt(35)/26880) * r^3 * exp(-r/4)` |
| O | $5s$ | `R_50 = (2*sqrt(5)/625) * (4*r^2 - 20*r + 25) * exp(-r/5)` |
| | $5p$ | `R_51 = (2*sqrt(30)/46875) * r * (6*r^2 - 75*r + 250) * exp(-r/5)` |
| | $5d$ | `R_52 = (2*sqrt(70)/46875) * r^2 * (15 - 2*r) * exp(-r/5)` |
| | $5f$ | `R_53 = (2*sqrt(70)/1640625) * r^3 * (20 - r) * exp(-r/5)` |
| | $5g$ | `R_54 = (1/(15000*sqrt(70))) * (2r/5)^4 * exp(-r/5)`<br>*(never occupied in ground state)* |
| P | $6s$ | `R_60 = (sqrt(6)/2916) * (-2*r^3 + 30*r^2 - 135*r + 162) * exp(-r/6)` |
| | $6p$ | `R_61 = (sqrt(210)/306180) * r * (-r^3 + 30*r^2 - 315*r + 945) * exp(-r/6)` |
| | $6d$ | `R_62 = (sqrt(105)/306180) * r^2 * (r^2 - 21*r + 126) * exp(-r/6)` |
| Q | $7s$ | `R_70 = (2*sqrt(7)/117649) * (-40*r^3 + 476*r^2 - 2058*r + 2401) * exp(-r/7)` |
| | $7p$ | `R_71 = (4*sqrt(21)/2470629) * r * (-8*r^3 + 196*r^2 - 1715*r + 4802) * exp(-r/7)` |

---

## A.6 Summary: The Four Quantum Numbers

| Number | Symbol | Allowed Values | Physical Meaning |
| :--- | :---: | :--- | :--- |
| **Principal** | $n$ | $1, 2, 3, \dots$ | Shell number, size and energy of the orbital. |
| **Azimuthal** | $l$ | $0, 1, \dots, n-1$ | Subshell shape ($s, p, d, f$). Orbital angular momentum. |
| **Magnetic** | $m_l$ | $-l, \dots, +l$ | Orbital orientation in space. |
| **Spin** | $m_s$ | $+\frac{1}{2}, -\frac{1}{2}$ | Intrinsic angular momentum (Spin-Up or Spin-Down). |
