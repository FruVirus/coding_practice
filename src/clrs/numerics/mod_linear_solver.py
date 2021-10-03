"""
Overview
========

We want to find the solution to the equation:

    ax = b (mod n)

where a, b, and n are given integers and a > 0 and n > 0. We wish to find all values of
x, modulo n, that satisfy the equation. The equation may have zero, one, or more than
one such solution. This problem has several applications; for example, we shall use it
as part of the procedure for finding keys in the RSA public-key crypto system.

1. The equation is solvable for the unknown x iff d | b, where d = gcd(a, n).

2. The equation either has d distinct solutions modulo n, where d = gcd(a, n), or it has
no solutions.

3. If d | b, then the equation has as one of its solutions the value x0, where:

    x0 = x'(b / d) mod n

where x' is the x coefficient returned by gcd(a, n).

4. If the equation is solvable (i.e., d | b, where d = gcd(a, n) and x0 is any
solution), then the equation has exactly d distinct solutions, modulo n, given by
xi = x- + i(n / d) for i = 0, 1, ..., d - 1.

Complexity
==========

O(lg(n) + gcd(a, n)) = O(lg(n) + O(lg(b)) recursive calls)
"""

# Repository Library
from src.clrs.numerics.gcd import gcd


def mod_linear_solver(a, b, n):
    assert a > 0 and n > 0
    d, x = gcd(a, n)[:2]
    solutions = None
    if b % d == 0:
        x0 = x * (b / d) % n
        solutions = [(x0 + i * (n / d)) % n for i in range(d)]
    return solutions
