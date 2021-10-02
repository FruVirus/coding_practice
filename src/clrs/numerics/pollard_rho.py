"""
Overview
========

We want to factor an integer n into a product of primes. Trial division by all integers
up to R is guaranteed to factor completely any number up to R^2. For the same amount of
work, the Pollard's rho heuristic factors any number up to R^4 (unless we are unlucky).

Since the procedure is only a heuristic, neither its running time or its success is
guaranteed, although the procedure is highly effective in practice. Another advantage of
the pollard-rho procedure is that it uses only a constant number of memory locations.

Pollard's rho heuristic never prints an incorrect answer; any number it prints is a
non-trivial divisor of n. Pollard's rho might not print anything at all though; it comes
with no guarantee that it will print any divisors. However, we have good reason to
expect that the heuristic will print a factor p of n after Theta(sqrt(p)) iterations of
the while loop.

Eventually, pollard_rho will start to repeat values---it can then exit at this point.

Complexity
==========

Theta(sqrt(p)) arithmetic operations, where p is a factor of n
"""

# Standard Library
import random

# Repository Library
from src.clrs.numerics.gcd import gcd


def pollard_rho(n, num_factors=10, max_iters=10000):
    i, k, factors = 1, 2, []
    x = random.randrange(0, n)
    y = x
    while True:
        if len(factors) == num_factors or i == max_iters:
            return factors
        i += 1
        x = (x ** 2 - 1) % n
        d = gcd(y - x, n)[0]
        if d != 1 and d != n and d not in factors:
            factors.append(d)
        if i == k:
            y, k = x, 2 * k
