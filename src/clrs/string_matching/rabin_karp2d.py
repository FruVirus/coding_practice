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


def check_equal(t, p, row, col, pcols, prows, indices):
    t = [t[i][col : pcols + col] for i in range(row, prows + row)]
    if t == p:
        indices.append([row, col])


def col_hash(t, p, tcols, pcols, prows, radix, q):
    p_list, t_list = [], []
    for list_, a, cols in zip((p_list, t_list), (p, t), (pcols, tcols)):
        for i in range(cols):
            h = 0
            for j in range(prows - 1, -1, -1):
                h += radix ** (prows - j - 1) * ord(a[j][i]) % q
            list_.append(h % q)
    return p_list, t_list


def col_rolling_hash(t_list, t_, col, n_pcols, radix, q):
    t_ = (t_ * radix + t_list[col]) % q
    t_ -= (radix ** n_pcols * t_list[col - n_pcols]) % q
    t_ %= q
    return t_


def row_hash(list_, n_pcols, radix, q):
    h = 0
    for i in range(n_pcols):
        h += (radix ** (n_pcols - i - 1) * list_[i]) % q
    return h % q


def row_rolling_hash(t_list, t, next_row, prows, radix, q):
    for i, t_ in enumerate(t_list):
        t_ = (t_ * radix + ord(t[next_row][i])) % q
        t_ -= (radix ** prows * ord(t[next_row - prows][i])) % q
        t_ %= q
        t_list[i] = t_
    return t_list


def rabin_karp2d(t, p, radix=256, q=101):
    if not is_prime(q):
        q = next_prime(q)
    assert radix * q < 2 ** radix - 1
    indices = []
    trows, prows, tcols, pcols = len(t), len(p), len(t[0]), len(p[0])
    p_list, t_list = col_hash(t, p, tcols, pcols, prows, radix, q)
    n_pcols, n_tcols = len(p_list), len(t_list)
    p_ = row_hash(p_list, n_pcols, radix, q)
    for i in range(prows - 1, trows):
        col, t_ = 0, row_hash(t_list, n_pcols, radix, q)
        if p_ == t_:
            check_equal(t, p, i + 1 - prows, col, pcols, prows, indices)
        for j in range(n_pcols, n_tcols):
            col, t_ = col + 1, col_rolling_hash(t_list, t_, j, n_pcols, radix, q)
            if p_ == t_:
                check_equal(t, p, i + 1 - prows, col, pcols, prows, indices)
        if i + 1 < trows:
            t_list = row_rolling_hash(t_list, t, i + 1, prows, radix, q)
    return indices
