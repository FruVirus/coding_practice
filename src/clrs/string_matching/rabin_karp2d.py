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
from src.clrs.string_matching.rabin_karp import (
    check_equal,
    col_hash,
    col_rolling_hash,
    init,
)


def row_rolling_hash(t_list, t, next_row, prows, radix, q):
    for i, t_ in enumerate(t_list):
        t_ = (t_ * radix + ord(t[next_row][i])) % q
        t_ -= (radix ** prows * ord(t[next_row - prows][i])) % q
        t_list[i] = t_ % q


def rabin_karp2d(t, p, radix=256, q=101):
    t, p, t_list, n_tcols, n_pcols, trows, prows, pcols, p_, indices = init(
        t, p, radix, q
    )
    for i in range(prows - 1, trows):
        col, t_ = 0, col_hash(t_list, n_pcols, radix, q)
        check_equal(t, p, t_, p_, i + 1 - prows, col, pcols, prows, indices)
        for j in range(n_pcols, n_tcols):
            col, t_ = col + 1, col_rolling_hash(t_list, t_, j, n_pcols, radix, q)
            check_equal(t, p, t_, p_, i + 1 - prows, col, pcols, prows, indices)
        if i + 1 < trows:
            row_rolling_hash(t_list, t, i + 1, prows, radix, q)
    return indices
