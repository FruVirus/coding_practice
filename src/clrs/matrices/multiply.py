"""
Overview
========

Assume two matrices, A and B, of shapes [n, m] and [m, p], respectively. Matrix
multiplication of A and B produces an [n, p] matrix C. In general, matrix multiplication
requires n * p matrix entries, each of which is the sum of m values.

Because each of the triply-nested for-loops runs exactly n iterations, and calculation
of c[i][j] takes constant time, naive matrix multiplication takes Theta(n * m * p) time.

We can also use a divide-and-conquer algorithm to compute the matrix product if we
assume that n is an exact power of 2 in each of the n x n matrices A and B. We make this
assumption because in each divide step, we will divide n x n matrices into four
n / 2 x n / 2 matrices, and by assuming that n is an exact power of 2, we are guaranteed
that as long as n >= 2, the dimension n / 2 is an integer. The divide-and-conquer
algorithm also runs in Theta(n^3) time.

Complexity
==========

Theta(n^3) time complexity
"""


def matrix_multiply(a, b):
    n, n_acols, m, n_bcols = len(a), len(a[0]), len(b), len(b[0])
    assert n_acols == m
    c = [[0 for _ in range(n)] for _ in range(n_bcols)]
    for i in range(n):
        for j in range(n_bcols):
            for k in range(n_acols):
                c[i][j] += a[i][k] * b[k][j]
    return c


def smmr(a, b):
    n, n_acols, m, n_bcols = len(a), len(a[0]), len(b), len(b[0])
    assert n_acols == m
    c = [[0 for _ in range(n)] for _ in range(n_bcols)]
    mmr(a, b, crow1, col1, A, row2, col2, B, C)
    return c


def mmr(row1, col1, A, row2, col2, B, C):
    # Note that below variables are static
    # i and j are used to know current cell of
    # result matrix C[][]. k is used to know
    # current column number of A[][] and row
    # number of B[][] to be multiplied
    global i
    global j
    global k

    # If all rows traversed.
    if (i >= row1):
        return

    # If i < row1
    if (j < col2):
        if (k < col1):
            C[i][j] += A[i][k] * B[k][j]
            k += 1
            multiplyMatrixRec(row1, col1, A,
                              row2, col2, B, C)

        k = 0
        j += 1
        multiplyMatrixRec(row1, col1, A,
                          row2, col2, B, C)

    j = 0
    i += 1
    multiplyMatrixRec(row1, col1, A,
                      row2, col2, B, C)


a = [[1, 2, 3], [4, 5, 6]]
b = [[1, 2], [3, 4], [5, 6]]
c = matrix_multiply(a, b)
print(c)
a = [[1, 2], [3, 4]]
b = [[1, 2], [3, 4]]
c = smmr(a, b)
print(c)
