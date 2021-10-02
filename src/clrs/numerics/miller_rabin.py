"""
Overview
========

The Miller-Rabin primality test tests if a number, n, is a prime, where n is an odd
integer greater than 2. The test uses an auxiliary procedure witness(a, n) that returns
True iff a is a "witness" to the composite-ness of n---that is, if it is possible using
a to prove that n is composite.

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

A "non-trivial square root of 1" means the following. 1 is congruent to 9 mod 8, thus 3
is a non-trivial square of 1 mod 8.

Complexity
==========

If n is a beta-bit number,

O(s * beta) arithmetic operations
O(s * beta^3) bit operations
"""

# Standard Library
import random

# Repository Library
from src.clrs.numerics.mod_exp import mod_exp


def get_t_u(n):
    assert n % 2 != 0
    x = n - 1
    t = 1
    u = x // 2 ** t
    while True:
        if x % 2 ** t == 0 and u % 2 != 0 and 2 ** t * u == x:
            break
        t += 1
        u = x // 2 ** t
    return t, u


def witness(a, n):
    t, u = get_t_u(n)
    x_next, x_prev = None, mod_exp(a, u, n)
    for _ in range(t):
        x_next = x_prev ** 2 % n
        if x_next == 1 and x_prev != 1 and x_prev != n - 1:
            return True
    if x_next != 1:
        return True
    return False


def miller_rabin(n, s=9):
    for _ in range(s):
        a = random.randrange(1, n)
        if witness(a, n):
            return False
    return True
