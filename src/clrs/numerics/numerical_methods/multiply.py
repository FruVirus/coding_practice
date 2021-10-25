"""
Overview
========

Multiplying two n-digit numbers in radix r and base n can be done using recursion by
breaking the problem in half-sized numbers and multiplying until we reach a size that
fits into the word length of our machine. The naive implementation conducts 4
multiplications of n / 2 numbers and has complexity Theta(n^2).

Karatsuba's algorithm conducts three multiplications of n / 2 numbers and has complexity
Theta(n^(lg(3)).

Complexity
==========

Theta(n^2) time complexity for naive
Theta(n^(lg(3)) time complexity for Karatsuba
"""


def multiply(x, y, is_naive=False):
    if len(str(x)) == 1 or len(str(y)) == 1:
        return x * y
    n = max(len(str(x)), len(str(y)))
    n2 = n // 2
    x1, x0 = x // 10 ** n2, x % 10 ** n2
    y1, y0 = y // 10 ** n2, y % 10 ** n2
    z0, z2 = multiply(x0, y0), multiply(x1, y1)
    if is_naive:
        z1 = multiply(x0, y1) + multiply(x1, y0)
        return z0 + z1 * 10 ** n2 + z2 * 10 ** (2 * n2)
    z1 = multiply(x0 + x1, y0 + y1)
    return z0 + (z1 - z2 - z0) * 10 ** n2 + z2 * 10 ** (2 * n2)
