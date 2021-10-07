"""
Overview
========

Assume two matrices, A and B, of shapes [n, m] and [m, p], respectively. Matrix
multiplication of A and B produces an [n, p] matrix C. In general, matrix multiplication
requires n * p matrix entries, each of which is the sum of m values.

Because each of the triply-nested for-loops runs exactly n iterations, and calculation
of c[i][j] takes constant time, naive matrix multiplication takes Theta(n^3) time.

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


def square_matrix_multiply_recursive(a, b):
    n = len(a)
    assert (n & (n - 1) == 0) and n != 0
    c = [[0 for _ in range(n)] for _ in range(n)]
    if n == 1:
        c[0][0] = a[0][0] * b[0][0]
    else:
        c[0][0] = square_matrix_multiply_recursive(
            a[0][0], b[0][0]
        ) + square_matrix_multiply_recursive(a[0][1], b[1][0])
        c[0][1] = square_matrix_multiply_recursive(
            a[0][0], b[0][1]
        ) + square_matrix_multiply_recursive(a[0][1], b[1][1])
        c[1][0] = square_matrix_multiply_recursive(
            a[1][0], b[0][0]
        ) + square_matrix_multiply_recursive(a[1][1], b[1][0])
        c[1][1] = square_matrix_multiply_recursive(
            a[1][0], b[0][1]
        ) + square_matrix_multiply_recursive(a[1][1], b[1][1])
        pass
    return c


a = [[1, 2, 3], [4, 5, 6]]
b = [[1, 2], [3, 4], [5, 6]]
c = matrix_multiply(a, b)
print(c)
