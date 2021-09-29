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


def check_equal(t, p, t_, p_, row, col, pcols, prows, indices, is_2d=True):
    if p_ != t_:
        return
    if not is_2d:
        t, p = [t], [p]
    t = [t[i][col : col + pcols] for i in range(row, row + prows)]
    if p == t:
        indices.append([row, col])


def col_hash(list_, n_pcols, radix, q):
    h = 0
    for i in range(n_pcols):
        h += (radix ** (n_pcols - i - 1) * list_[i]) % q
    return h % q


def col_rolling_hash(t_list, t_, col, n_pcols, radix, q):
    t_ = (t_ * radix + t_list[col]) % q
    t_ -= (radix ** n_pcols * t_list[col - n_pcols]) % q
    t_ %= q
    return t_


def init(t, p, radix, q, is_2d=True):
    if not is_prime(q):
        q = next_prime(q)
    assert radix * q < 2 ** radix - 1
    if is_2d:
        trows, prows, tcols, pcols = len(t), len(p), len(t[0]), len(p[0])
        t_list, p_list = row_hash(t, p, tcols, pcols, prows, radix, q)
    else:
        trows, prows, tcols, pcols = 1, 1, len(t), len(p)
        t_list, p_list = row_hash([t], [p], tcols, pcols, prows, radix, q)
    n_tcols, n_pcols = len(t_list), len(p_list)
    indices, p_ = [], col_hash(p_list, n_pcols, radix, q)
    return t_list, n_tcols, n_pcols, trows, prows, pcols, p_, indices


def row_hash(t, p, tcols, pcols, prows, radix, q):
    t_list, p_list = [], []
    for list_, a, cols in zip((t_list, p_list), (t, p), (tcols, pcols)):
        for i in range(cols):
            h = 0
            for j in range(prows - 1, -1, -1):
                h += (radix ** (prows - j - 1) * ord(a[j][i])) % q
            list_.append(h % q)
    return t_list, p_list


def rabin_karp(t, p, radix=256, q=101):
    t_list, n_tcols, n_pcols, _, prows, pcols, p_, indices = init(t, p, radix, q, False)
    col, t_ = 0, col_hash(t_list, n_pcols, radix, q)
    for i in range(n_pcols, n_tcols):
        check_equal(t, p, t_, p_, 0, col, pcols, prows, indices, False)
        col, t_ = col + 1, col_rolling_hash(t_list, t_, i, n_pcols, radix, q)
    return indices
