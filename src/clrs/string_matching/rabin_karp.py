"""Rabin-Karp is a string-matching algorithm that performs well in practice and also
generalizes to other algorithms for related problems, such as two-dimensional pattern
matching.

rabin_karp() assumes all characters are interpreted as radix-d digits.

If the expected number of valid shifts is small (i.e., we expect few valid matches) and
we choose the prime q  to be larger than the length of the pattern, then we can expect
the Rabin-Karp algorithm to use only O(n + m) = O(n) matching time since m <= n.

Rabin-Karp: Theta(m) preprocessing time. Theta((n - m + 1) * m) matching time.
"""

# Repository Library
from src.clrs.hash_tables.hash_chain import is_prime, next_prime


def rabin_karp(t, p, d, q=13):
    n, m = len(t), len(p)
    if not is_prime(q):
        q = next_prime(q)
    assert d * q < 2 ** d - 1
    h, p_, t_ = d ** (m - 1) % q, 0, 0
    for i in range(m):
        p_ = d * p_ + int(p[i])
        t_ = d * t_ + int(t[i])
    p_ %= q
    t_ %= q
    count = 0
    for s in range(n - m):
        print(p_, t_, t[s : s + m])
        if p_ == t_ and p == t[s : s + m]:
            count += 1
        if s < n - m:
            t_ = (d * (t_ - int(t[s]) * h) + int(t[s + m])) % q
    return count


print(rabin_karp("2359023141526739921", "31415", 10))
