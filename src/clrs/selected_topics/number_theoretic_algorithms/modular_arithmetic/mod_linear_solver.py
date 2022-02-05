"""
31.4 Solving modular linear equations
=====================================

We want to find the solution to the equation:

    ax = b mod n,

where a > 0 and n > 0. We assume that a, b, and n are given, and we wish to find all
values of x, modulo n, that satisfy the equation. The equation may have zero, one, or
more than one such solution.

1. The equation is solvable for the unknown x iff d | b, where d = gcd(a, n).

2. The equation either has d distinct solutions modulo n, where d = gcd(a, n), or it has
no solutions.

3. If d | b, then the equation has as one of its solutions the value x0, where
x0 = x' * (b / d) mod n and x' is the x coefficient returned by gcd(a, n).

4. If the equation is solvable (i.e., d | b, where d = gcd(a, n) and x0 is any
solution), then the equation has exactly d distinct solutions, modulo n, given by
xi = x' + i * (n / d) for i = 0, 1, ..., d - 1.

If gcd(a, n) = 1, then this means that a and n are relatively prime.

Corollary 31.25

For any n > 1, if gcd(a, n) = 1, then the equation ax = b mod n has a unique solution,
modulo n (for any value of b). This is because gcd(a, n) = 1 = d.

Corollary 31.26

For any n > 1, if gcd(a, n) = 1, then the equation ax = 1 mod n has a unique solution,
modulo n. Otherwise, it has no solution. Furthermore, the x we are looking for is a
multiplicative inverse of a, modulo n.

Intuition
---------

For example, gcd(5, 11) = (1, -2, 1) means that 1 = 5 * -2 + 11 * 1. In this example,
-2 mod 11 = 9 mod 11 is also the multiplicative inverse of 5 mod 11 since
1 mod 11 = 5 * -2 mod 11 = 1. In other words, when we apply the modulo operation, -2 is
the multiplicative inverse of 5 since 5 * -2 = 1. This only applies if we invoked
gcd(a, n) and d = 1 as returned by gcd()---in this case, x is a multiplicative inverse
of a in Z_n.

Complexity
==========

Time
----

mod_linear_solver(): O(lg n + gcd(a, n)) = O(lg n + O(lg b) recursive calls).
"""

# Repository Library
from src.clrs.selected_topics.number_theoretic_algorithms.modular_arithmetic.gcd import (  # noqa: E501
    gcd,
)


def mod_linear_solver(a, b, n):
    assert a > 0 and n > 0
    d, x = gcd(a, n)[:2]
    if b % d == 0:
        x0 = x * (b / d) % n
        return [(x0 + i * (n / d)) % n for i in range(d)]
    return None
