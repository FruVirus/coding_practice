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


def add(a, b):
    n = len(a)
    c = [[0 for _ in range(n)] for _ in range(n)]
    for i in range(n):
        for j in range(n):
            c[i][j] = a[i][j] + b[i][j]
    return c


def split(a):
    a00 = a01 = a10 = a11 = a
    while len(a00) > len(a) / 2:
        a00 = a00[: len(a00) // 2]
        a01 = a01[: len(a01) // 2]
        a10 = a10[len(a10) // 2 :]
        a11 = a11[len(a11) // 2 :]
    while len(a00[0]) > len(a[0]) // 2:
        for i in range(len(a00[0]) // 2):
            a00[i] = a00[i][: len(a00[i]) // 2]
            a01[i] = a01[i][len(a01[i]) // 2 :]
            a10[i] = a10[i][: len(a10[i]) // 2]
            a11[i] = a11[i][len(a11[i]) // 2 :]
    return a00, a01, a10, a11


def smmr(a, b, n):
    assert (n & (n - 1) == 0) and n != 0
    c = [[0 for _ in range(n)] for _ in range(n)]
    if n <= 2:
        c[0][0] = a[0][0] * b[0][0] + a[0][1] * b[1][0]
        c[0][1] = a[0][0] * b[0][1] + a[0][1] * b[1][1]
        c[1][0] = a[1][0] * b[0][0] + a[1][1] * b[1][0]
        c[1][1] = a[1][0] * b[0][1] + a[1][1] * b[1][1]
    else:
        a00, a01, a10, a11 = split(a)
        b00, b01, b10, b11 = split(b)
        mid = n // 2
        c00 = add(smmr(a00, b00, mid), smmr(a01, b10, mid))
        c01 = add(smmr(a00, b01, mid), smmr(a01, b11, mid))
        c10 = add(smmr(a10, b00, mid), smmr(a11, b10, mid))
        c11 = add(smmr(a10, b01, mid), smmr(a11, b11, mid))
        n = len(c00)
        for i in range(n):
            for j in range(n):
                c[i][j] = c00[i][j]
                c[i][j + n] = c01[i][j]
                c[i + n][j] = c10[i][j]
                c[i + n][j + n] = c11[i][j]
    return c
