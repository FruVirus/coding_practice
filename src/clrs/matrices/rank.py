"""
Overview
========

Rank is the number of independent columns/rows of a matrix. If a column/row is a
multiple of another column/row or is a combination or other columns/rows, then that
column/row is not independent and does not contribute to the rank of a matrix.

Rank can be found by performing Gaussian elimination on the input matrix and then
counting the number of non-zero elements on the diagonal. After we perform Gaussian
elimination, the resulting matrix is in row echelon form.

Complexity
==========

O(n^2) time complexity
"""


def rank(a):
    n, m = len(a), len(a[0])
    assert n == m
    curr_rank = m
    for r in range(curr_rank):
        if a[r][r] != 0:
            for c in range(n):
                if c != r:
                    multiplier = a[c][r] / a[r][r]
                    for i in range(curr_rank):
                        a[c][i] -= multiplier * a[r][i]
        else:
            for i in range(r + 1, n):
                if a[i][r] != 0:
                    swap_rows(a, r, i, curr_rank)
                    break
            else:
                curr_rank -= 1
                for i in range(n):
                    a[i][r] = a[i][curr_rank]
    return curr_rank


def swap_rows(a, r1, r2, c):
    for i in range(c):
        a[r1][i], a[r2][i] = a[r2][i], a[r1][i]
