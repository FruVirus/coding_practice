"""
Overview
========

For 2D, the idea is to find the hash of each column in t and p and compare the hash
values. For any column, if hash values are equal, then check for the corresponding row
values.

Intuition
---------

We extend Rabin Karp to 2D by calculating the hashes for each column just as in the 1D
case, and then treating the hashes in each as the characters and hashing again.

Complexity
==========

Time
----

rabin_karp(): Theta(m * m) preprocessing, Theta((n - m + 1) * m^2)/Theta(m^2 * n)
worst/average case matching.
"""

# Repository Library
from src.clrs.selected_topics.string_matching.rabin_karp import (
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
