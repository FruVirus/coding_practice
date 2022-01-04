"""
Overview
========

The Miller-Rabin primality test tests if a number, n, is a prime, where n is an odd
integer greater than 2. The test uses an auxiliary procedure witness(a, n) that returns
True iff a is a "witness" to the composite-ness of n---that is, if it is possible using
a to prove that n is composite.

The Miller-Rabin test computes a^(n - 1) mod n by first computing a^u mod n and then
squaring the result t time successively.

The Miller-Rabin test relies on Fermat's theorem, which states that if p is prime, then
a^(p - 1) is congruent to 1 (mod p) for all a in Z_star_p. Thus, if a^(p - 1) is NOT
congruent to 1 (mod p), then p is composite.

The if-block inside the for-loop of witness() returns True if x_prev != 1 but
x_next == 1 because this is a contradiction since x_prev != +/- 1 (mod p) but
x_next == x_prev^2 = 1 (mod p). In addition, x_prev cannot be equal to n - 1.

The Miller-Rabin procedure is a probabilistic search for a proof that n is composite.
The main loop picks up to s random values of a. If one of the a's picked is a witness
to the composite-ness of n, then we are definitely sure that n is NOT a prime. If there
are no witnesses in s trials, then the procedure assumes that this is because no
witnesses exist, and therefore it assumes that n is prime. This result is likely to be
correct if s is large enough, but there is still a tiny chance that the procedure may
be unlucky in its choice of a's and that witnesses do exist even though none has been
found.

For any odd integer n > 2 and positive integer s, the probability that the Miller-Rabin
test errs is at most 2^(-s). In other words, if n is prime, the Miller-Rabin test always
reports prime, and if n is composite, the chance that the Miller-Rabin test reports
prime is at most 2^(-s). s >= 9 should suffice (see pg. 974 of CLRS).

Complexity
==========

If n is a beta-bit number,

O(s * beta) arithmetic operations
O(s * beta^3) bit operations
"""

# Standard Library
import random

# Repository Library
from src.clrs.selected_topics.number_theoretic_algorithms.modular_arithmetic.mod_exp import (  # noqa: E501
    mod_exp,
)


def get_tu(n):
    assert n % 2 != 0
    x = n - 1
    t = 1
    u = x // 2 ** t
    while u % 2 == 0 or 2 ** t * u != x:
        t += 1
        u = x // 2 ** t
    return t, u


def witness(a, n):
    t, u = get_tu(n)
    x_prev = mod_exp(a, u, n)
    x_next = x_prev ** 2 % n
    for _ in range(t):
        if x_next == 1 and x_prev not in [1, n - 1]:
            return True
        x_prev, x_next = x_next, x_prev ** 2 % n
    return x_next != 1


def miller_rabin(n, s=9):
    for _ in range(s):
        if witness(random.randrange(1, n), n):
            return False
    return True
