"""
Overview
========

We want to factor an integer n into a product of primes. Trial division by all integers
up to R is guaranteed to factor completely any number up to R^2. For the same amount of
work, the Pollard's rho heuristic factors any number up to R^4 (unless we are unlucky).

Since the procedure is only a heuristic, neither its running time or its success is
guaranteed, although the procedure is highly effective in practice. Another advantage of
the pollard-rho procedure is that it uses only a constant number of memory locations.

Complexity
==========


"""

# Standard Library
import random

# Repository Library
from src.clrs.numerics.gcd import gcd


def pollard_rho(n):
    i = 1
    xi = random.randrange(0, n)
    y = xi
    k = 2
    factors = []
    while True:
        i += 1
        xi = (xi ** 2 - 1) % n
        d = gcd(y - xi, n)[0]
        if d != 1 and d != n:
            factors.append(d)
        if i == k:
            y, k = xi, 2 * k
