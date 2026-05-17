# Quiz

## Question 1 — Valid or Invalid Quantum Numbers?

For each set of quantum numbers below, state whether it is **valid** or **invalid**, and explain why.

Recall the allowed ranges:

| Quantum number | Symbol | Allowed values |
| :--- | :---: | :--- |
| Principal | $n$ | $1, 2, 3, \ldots$ (positive integers only) |
| Angular momentum | $\ell$ | $0, 1, \ldots, n-1$ |
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
