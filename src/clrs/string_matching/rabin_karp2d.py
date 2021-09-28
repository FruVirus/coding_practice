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

For 2D, the idea is to find the hash of each column in t and p and compare the hash
values. For any column, if hash values are equal, then check for the corresponding row
values.

Complexity
==========

Theta(m) preprocessing time. Theta((n - m + 1) * m) matching time.
"""

# Repository Library
from src.clrs.numerics.next_prime import is_prime, next_prime
from src.clrs.string_matching.rabin_karp import (
    check_equal,
    col_hash,
    col_rolling_hash,
    row_hash,
)


def row_rolling_hash(t_list, t, next_row, prows, radix, q):
    for i, t_ in enumerate(t_list):
        t_ = (t_ * radix + ord(t[next_row][i])) % q
        t_ -= (radix ** prows * ord(t[next_row - prows][i])) % q
        t_list[i] = t_ % q


def rabin_karp2d(t, p, radix=256, q=101):
    if not is_prime(q):
        q = next_prime(q)
    assert radix * q < 2 ** radix - 1
    trows, prows, tcols, pcols = len(t), len(p), len(t[0]), len(p[0])
    t_list, p_list = row_hash(t, p, tcols, pcols, prows, radix, q)
    n_tcols, n_pcols = len(t_list), len(p_list)
    indices, p_ = [], col_hash(p_list, n_pcols, radix, q)
    for i in range(prows - 1, trows):
        col, t_ = 0, col_hash(t_list, n_pcols, radix, q)
        if p_ == t_:
            check_equal(t, p, i + 1 - prows, col, pcols, prows, indices)
        for j in range(n_pcols, n_tcols):
            col, t_ = col + 1, col_rolling_hash(t_list, t_, j, n_pcols, radix, q)
            if p_ == t_:
                check_equal(t, p, i + 1 - prows, col, pcols, prows, indices)
        if i + 1 < trows:
            row_rolling_hash(t_list, t, i + 1, prows, radix, q)
    return indices
