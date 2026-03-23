# Chapter 3: Stepping into 3D (The Hydrogen Atom)

In the previous chapter, we saw how trapping a particle in a 1D box forced its energy to become "quantized." While this taught us the core logic of quantum mechanics, real atoms are not 1D boxes—they are 3D spheres with a central nucleus pulling on an electron.

To solve the Hydrogen atom, we must upgrade our math from a simple line to a three-dimensional landscape.

## 3.1 The Problem with Cartesian Coordinates

In Chapter 1, we saw the general 3D Schrödinger Equation:

$$-\frac{\hbar^2}{2m}\nabla^2\Psi + V\Psi = E\Psi$$

If we use standard Cartesian coordinates ($x, y, z$), the Laplacian operator $\nabla^2$ is simple:

$$\nabla^2 = \frac{\partial^2}{\partial x^2} + \frac{\partial^2}{\partial y^2} + \frac{\partial^2}{\partial z^2}$$

However, the **Potential Energy ($V$)** of an atom is defined by the attraction between the positive nucleus and the negative electron (the Coulomb potential):

$$V(r) = -\frac{e^2}{4\pi\epsilon_0 r}$$

Notice that this potential depends *only* on the distance $r$ from the center. In $x, y, z$, that distance is $r = \sqrt{x^2 + y^2 + z^2}$. If we tried to solve the equation this way, the variables would be hopelessly tangled together. The math would be a nightmare.

## 3.2 The Solution: Spherical Coordinates

Because atoms are naturally spherical, we switch to **Spherical Coordinates**. Instead of describing a point as "Left/Right, Up/Down, Forward/Back," we describe it using:

* **$r$ (Radius):** Distance from the nucleus ($0 \to \infty$).
* **$\theta$ (Polar Angle):** Angle down from the "North Pole" ($0 \to \pi$).
* **$\phi$ (Azimuthal Angle):** Angle around the "Equator" ($0 \to 2\pi$).

In these coordinates, the Laplacian operator ($\nabla^2$) looks much more intimidating:

$$\nabla^2 = \frac{1}{r^2} \frac{\partial}{\partial r} \left(r^2 \frac{\partial}{\partial r}\right) + \frac{1}{r^2 \sin \theta} \frac{\partial}{\partial \theta} \left(\sin \theta \frac{\partial}{\partial \theta}\right) + \frac{1}{r^2 \sin^2 \theta} \frac{\partial^2}{\partial \phi^2}$$

For the full mathematical context and derivation of these operators, please see the **[Annex](annex.md)**.

## 3.3 The Math of Separation

We employ **Separation of Variables** by assuming the wave function $\Psi$ is a product of two independent parts:

$$\Psi(r, \theta, \phi) = R(r) \cdot Y(\theta, \phi)$$

**Why is this separation valid?**
This is not just a guess; it's a consequence of **Spherical Symmetry**. In an atom, the potential $V(r)$ depends only on the distance from the center. Because the "pull" of the nucleus is identical in every direction, the radial motion of the electron and its angular orientation can be treated as independent mathematical degrees of freedom.

### Step 1: Substitution

Now, we substitute this product into the Time-Independent Schrödinger Equation:

$$-\frac{\hbar^2}{2m} \nabla^2(RY) + V(r)(RY) = E(RY)$$

When the derivatives in $\nabla^2$ act on the product $RY$:

* The radial derivatives only act on $R(r)$ (treating $Y$ as a constant).
* The angular derivatives only act on $Y(\theta, \phi)$ (treating $R$ as a constant).

### Step 2: Isolating the Variables

To simplify the algebra, we define the **Angular Term** ($\mathcal{A}$) as the part of the Laplacian that acts only on the angles (see Annex):

$$\mathcal{A} = \frac{1}{\sin \theta} \frac{\partial}{\partial \theta} \left(\sin \theta \frac{\partial}{\partial \theta}\right) + \frac{1}{\sin^2 \theta} \frac{\partial^2}{\partial \phi^2}$$

Now, we perform the untangling:

1. **Expand with the Angular Term:**
    We write the Laplacian as $\nabla^2 = \frac{1}{r^2} \frac{\partial}{\partial r} \left(r^2 \frac{\partial}{\partial r}\right) + \frac{1}{r^2} \mathcal{A}$. Substituting $RY$:

    $$-\frac{\hbar^2}{2m} \left[ \frac{Y}{r^2} \frac{d}{dr} \left(r^2 \frac{dR}{dr}\right) + \frac{R}{r^2} \mathcal{A}Y \right] + V(r)RY = ERY$$

2. **Multiply by $-2mr^2 / \hbar^2$:**
    This removes the $1/r^2$ from the Laplacian terms and clears the kinetic energy constants:

    $$Y \frac{d}{dr} \left(r^2 \frac{dR}{dr}\right) + R \mathcal{A}Y - \frac{2mr^2}{\hbar^2} V(r)RY = -\frac{2mr^2}{\hbar^2} ERY$$

3. **Divide by $RY$:**
    This "shuffles" the variables into their respective corners:

    $$\frac{1}{R} \frac{d}{dr} \left(r^2 \frac{dR}{dr}\right) + \frac{1}{Y} \mathcal{A}Y - \frac{2mr^2}{\hbar^2} V(r) = -\frac{2mr^2}{\hbar^2} E$$

4. **Final Rearrangement and Substitution of $\mathcal{A}$:**
    We move everything related to $r$ to the left and everything related to the angles to the right, and substitute the full definition of $\mathcal{A}$ back in:

    $$\underbrace{\frac{1}{R} \frac{d}{dr} \left(r^2 \frac{dR}{dr}\right) + \frac{2mr^2}{\hbar^2} [E - V(r)]}_{\text{Radial Side (only } r)} = \underbrace{-\frac{1}{Y} \left[ \frac{1}{\sin \theta} \frac{\partial}{\partial \theta} \left(\sin \theta \frac{\partial Y}{\partial \theta}\right) + \frac{1}{\sin^2 \theta} \frac{\partial^2 Y}{\partial \phi^2} \right]}_{\text{Angular Side (only } \theta, \phi)}$$

### Step 3: The Logic of the Separation Constant

Here is the "magic" of the math: the left side of this equation is a function of *only* $r$, while the right side is a function of *only* the angles.

If you change $r$, the left side might change, but the right side cannot (because it doesn't have $r$ in it). For both sides to stay equal for *all* points in space, they must both be equal to a fixed number—a **Separation Constant**.

**Why $l(l+1)$?**
Mathematically, we could call this constant anything (like $C$). However, physicists have already solved the "Angular Side" of this equation. They found that for the angular solutions ($Y$) to be physically valid—meaning they don't go to infinity and they wrap around the sphere smoothly—the constant must take the form $l(l+1)$, where $l$ is an integer ($0, 1, 2, \dots$).

By using $l(l+1)$ now, we are "looking ahead" to ensure our atom is physically realistic.

## 3.4 The Result: Two Independent Equations

We have now successfully "ripped" the Schrödinger equation into two manageable pieces:

### 1. The Angular Equation (Shapes)

This equation determines the geometry of the orbital:

$$\frac{1}{\sin \theta} \frac{\partial}{\partial \theta} \left(\sin \theta \frac{\partial Y}{\partial \theta}\right) + \frac{1}{\sin^2 \theta} \frac{\partial^2 Y}{\partial \phi^2} = -l(l+1)Y$$

Solving this will give us the **Spherical Harmonics**, which define the $s, p, d, f$ shapes.

### 2. The Radial Equation (Energy)

This equation determines the electron's distance and total energy:

$$\frac{d}{dr} \left(r^2 \frac{dR}{dr}\right) - \frac{2mr^2}{\hbar^2} [V(r) - E]R = l(l+1)R$$

Solving this will give us the **Energy Shells** ($n=1, 2, 3 \dots$) and the "rows" of your periodic table.

## 3.4 What's Next?

We have just turned one impossible 3D problem into two manageable 1D problems.

In the next two chapters, we will solve these individually. From the **Angular Equation**, we will see the shapes of the $p$ and $d$ orbitals emerge. From the **Radial Equation**, we will derive the exact energy levels that make up the rows of your periodic table.
