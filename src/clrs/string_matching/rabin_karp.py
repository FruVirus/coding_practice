"""
Overview
========

Rabin-Karp is a string-matching algorithm that performs well in practice and also
generalizes to other algorithms for related problems, such as two-dimensional pattern
matching.

rabin_karp() assumes all characters are interpreted as radix-d digits.

If the expected number of valid shifts is small (i.e., we expect few valid matches) and
we choose the prime q  to be larger than the length of the pattern, then we can expect
the Rabin-Karp algorithm to use only O(n + m) = O(n) matching time since m <= n.

Complexity
==========

Theta(m) preprocessing time. Theta((n - m + 1) * m) matching time.
"""

# Repository Library
from src.clrs.numerics.next_prime import is_prime, next_prime


def rabin_karp(t, p, radix, q=13):
    if not is_prime(q):
        q = next_prime(q)
    assert radix * q < 2 ** radix - 1
    n, m = len(t), len(p)
    h, p_, t_ = radix ** (m - 1) % q, 0, 0
    for i in range(m):
        p_, t_ = radix * p_ + int(p[i]), radix * t_ + int(t[i])
    p_ %= q
    t_ %= q
    indices = []
    for s in range(n - m):
        if p_ == t_ and p == t[s : s + m]:
            indices.append(s)
        if s < n - m:
            t_ = (radix * (t_ - int(t[s]) * h) + int(t[s + m])) % q
    return indices
