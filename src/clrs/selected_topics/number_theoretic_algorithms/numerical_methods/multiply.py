"""
Overview
========

Multiplying two n-digit numbers in radix r and base n can be done using recursion by
breaking the problem in half-sized numbers and multiplying until we reach a size that
fits into the word length of our machine. The naive implementation conducts 4
multiplications of n / 2 numbers and has complexity Theta(n^2).

Karatsuba's algorithm conducts three multiplications of n / 2 numbers and has complexity
Theta(n^(lg 3)).

Intuition
---------

Given two numbers x and y to multiply in a given base, we can decompose each number as
follows:

denom = base ** (n // 2), where n is the longest length between x and y
x = x // denom + x % denom
y = y // denom + y % denom

where x // denom and y // denom correspond to the high half of the numbers x and y and
x % denom and y % denom correspond to the low half of the numbers x and y.

For example, if we are in base 10 and x = 1234, then n = 4 and
denom = 10 ** (4 // 2) = 100. 1234 = 1234 // 100 + 1234 % 100 = 12 + 34 = 1234.

In this case, z = x * y = (x // denom + x % denom) * (y // denom + y % denom) =
(x1 + x0) * (y1 + y0) = x1 * y1 + x0 * y1 + x1 * y0 + x0 * y0. Thus, in the naive
approach, there are four multiply operations to carry out.

In Karatsuba's approach, there are only three multiplies as follows:

z0 = x0 * y0
z2 = x1 * y1
z1 = (x0 + x1) * (y0 + y1) - z0 - z2
   = x0 * y1 + x1 * y0.

Complexity
==========

Time
----

multiply(): Theta(n^2) for naive approach and Theta(n^(lg 3) Karatsuba approach.
"""


def multiply(x, y, base=10, is_naive=False):
    n, m = len(str(x)), len(str(y))
    if min(n, m) == 1:
        return x * y
    n2 = max(n, m) // 2
    denom = base ** n2
    x1, x0, y1, y0 = x // denom, x % denom, y // denom, y % denom
    z0, z2 = multiply(x0, y0), multiply(x1, y1)
    if is_naive:
        z1 = multiply(x0, y1) + multiply(x1, y0)
    else:
        z1 = multiply(x0 + x1, y0 + y1) - z0 - z2
    return z0 + z1 * base ** n2 + z2 * base ** (2 * n2)
