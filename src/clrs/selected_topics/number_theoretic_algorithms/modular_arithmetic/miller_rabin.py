"""
31.8 Primality testing
======================

The Miller-Rabin randomized primality test
------------------------------------------

The Miller-Rabin primality test overcomes the problems of the simple test PSEUDOPRIME
with two modifications:

- It tries several randomly chosen base values a instead of just one base value.
- While computing each modular exponentiation, it looks for a nontrivial square root of
1, modulo n, during the final set of squarings. If it finds one, it stops and returns
COMPOSITE.

The Miller-Rabin primality test tests if a number, n, is a prime, where n is an odd
integer greater than 2 and conducts the test for s trials, where s is the number of
randomly chosen base values from Z_n_star to be tried. A random number generator is used
to choose a random integer a satisfying 1 <= a <= n - 1. The test uses an auxiliary
procedure witness(a, n) that returns True iff a is a "witness" to the composite-ness of
n---that is, if it is possible using a to prove that n is composite. The test
witness(a, n) is an extension of, but more effective than, the test

a^(n - 1) != 1 mod n

that formed the basis (using a = 2) for PSEUDOPRIME. Let n - 1 = 2^t * u where t >= 1
and u is odd; i.e., the binary representation of the odd integer u followed by exactly
t zeros. Therefore, a^(n - 1) = (a^u)^2^t mod n, so that we can compute a^(n - 1) mod n
by first computing a^u mod n and then squaring the result t times successively.

witness() computes a^(n - 1) mod n by first computing a^u mod n (using mod_exp()) and
then squaring the result t times in a row in the for-loop. In other words, the sequence
of x values in the for-loop satisfies the equation x_i = a^(2^i * u) mod n for
i = 0, 1, ..., t, so that when the for-loop exits, we have x_t = a^(n - 1) mod n. During
the execution of the for-loop, the loop may terminate early if a nontrivial square root
of 1 has just been discovered.

If witness(a, n) returns True, then we know for sure that n is composite using a as a
witness.

The Miller-Rabin test relies on Fermat's theorem, which states that if p is prime, then
a^(p - 1) is congruent to 1 mod p for all a in Z_star_p. Thus, if a^(p - 1) is NOT
congruent to 1 mod p, then p is composite.

The if-block inside the for-loop of witness() returns True if x_prev != 1 but
x_next == 1 because this is a contradiction since x_prev != +/- 1 mod p but
x_next == x_prev^2 = 1 mod p. In addition, x_prev cannot be equal to n - 1.

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

Assume n is a beta-bit number.

Time
----

miller_rabin(): O(s * beta) arithmetic operations, O(s * beta^3) bit operations.
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
    for _ in range(1, t):
        if x_next == 1 and x_prev != 1:
            return True
        x_prev, x_next = x_next, x_prev ** 2 % n
    return x_next != 1


def miller_rabin(n, s=9):
    for _ in range(s):
        if witness(random.randrange(1, n), n):
            return False
    return True
