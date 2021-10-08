"""
Overview
========

Rank is the number of independent columns/rows of a matrix. If a column/row is a
multiple of another column/row or is a combination or other columns/rows, then that
column/row is not independent and does not contribute to the rank of a matrix.

Rank can be found by performing Gaussian elimination on the input matrix and then
counting the number of non-zero elements on the diagonal. After we perform Gaussian
elimination, the resulting matrix is in row echelon form.

A matrix is full row rank when each of the rows of the matrix are linearly independent
and full column rank when each of the columns of the matrix are linearly independent.
For a square matrix these two concepts are equivalent and we say the matrix is full rank
if all rows and columns are linearly independent. A square matrix is full rank if and
only if its determinant is nonzero.

For a non-square matrix with m rows and n columns, it will always be the case that
either the rows or columns (whichever is larger in number) are linearly dependent. Hence
when we say that a non-square matrix is full rank, we mean that the row and column rank
are as high as possible, given the shape of the matrix. So if there are more rows than
columns (m > n), then the matrix is full rank if the matrix is full column rank.

In addition, the diagonal elements of the matrix returned by gaussian_elimination() can
be used to determine if the passed in matrix a is positive-definite. A matrix is
positive definite if it’s symmetric and all its pivots (the diagonal elements in the
returned matrix) are positive.

Complexity
==========

O(n^3 + 2n - 3) / 3 time complexity
"""


def gaussian_elimination(a):
    n, m = len(a), len(a[0])
    curr_rank = m
    for r in range(curr_rank):
        if a[r][r] != 0:
            for c in range(m):
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
    return a, curr_rank


def swap_rows(a, r1, r2, c):
    for i in range(c):
        a[r1][i], a[r2][i] = a[r2][i], a[r1][i]
