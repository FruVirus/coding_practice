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
    for row in range(curr_rank):
        if a[row][row] != 0:
            for col in range(n):
                if col != row:
                    multiplier = a[col][row] / a[row][row]
                    for i in range(curr_rank):
                        a[col][i] -= multiplier * a[row][i]
        else:
            reduce = True
            for i in range(row + 1, n):
                if a[i][row] != 0:
                    swap_rows(a, row, i, curr_rank)
                    reduce = False
                    break
            if reduce:
                curr_rank -= 1
                for i in range(n):
                    a[i][row] = a[i][curr_rank]
            row -= 1
    return curr_rank


def swap_rows(a, row1, row2, col):
    for i in range(col):
        a[row1][i], a[row2][i] = a[row2][i], a[row1][i]
