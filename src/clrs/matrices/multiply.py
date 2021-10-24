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

Strassen's Method
-----------------

Strassen's method is to perform only 7 matrix multiplications instead of 8 as in the
naive recursive algorithm. The cost of eliminating one matrix multiplication will be
several new additions of n / 2 x n / 2 matrices, but still only a constant number of
additions.

1. Divide the input matrices A and B and output matrix C into n / 2 x n / 2
sub-matrices. This step takes Theta(1) time by index calculation.

2. Create 10 matrices S1, S2, ..., S10, each of which is n / 2 and n / 2 and is the sum
or difference of two matrices created in step 1. We can create all 10 matrices in
Theta(n^) time.

3. Using the sub-matrices created in step 1 and the 10 matrices created in step 2,
recursively compute seven matrix products P1, P2, ..., P7. Each matrix Pi is
n / 2 x n / 2.

4. Compute the desired sub-matrices C11, C12, C21, C22 of the result matrix C by
adding and subtracting various combinations of the Pi matrices. We can compute all four
sub-matrices in Theta(n^2) time.

From a practical point of view, Strassen's algorithm is often not the method of choice
for matrix multiplication, for four reasons:

1. The constant factor hidden in the Theta(n^(lg(7))) running time is larger than the
constant factor in the Theta(n^3) time for the naive matrix multiplication algorithm.

2. When the matrices are sparse, methods tailored for sparse matrices are faster.

3. Strassen's algorithm is not quite as numerically stable as the naive algorithm.

4. The sub-matrices formed at the levels of recursion consume space.

c00 = p + s - t + v
c01 = r + t
c10 = q + s
c11 = p + r - q + u
p = (a00 + a11) * (b00 + b11)
q = (a10 + a11) * b00
r = a00 * (b01 - b11)
s = a11 * (b10 - b00)
t = (a00 + a10) * b11
u = (a10 - a00) * (b00 + b01)
v = (a01 - a11) * (b10 + b11)

Complexity
==========

Theta(n^3) time complexity
"""


def mm(a, b):
    rowa, cola, rowb, colb = len(a), len(a[0]), len(b), len(b[0])
    assert cola == rowb
    x = [[0] * colb for _ in range(rowa)]
    for ra in range(rowa):
        for cb in range(colb):
            for ca in range(cola):
                x[ra][cb] += a[ra][ca] * b[ca][cb]
    return x


def add(a, b):
    n = len(a)
    x = [[0] * n for _ in range(n)]
    for r in range(n):
        for c in range(n):
            x[r][c] = a[r][c] + b[r][c]
    return x


def split(a):
    a00 = a01 = a10 = a11 = a
    while len(a00) > len(a) // 2:
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
    x = [[0] * n for _ in range(n)]
    if n <= 2:
        x[0][0] = a[0][0] * b[0][0] + a[0][1] * b[1][0]
        x[0][1] = a[0][0] * b[0][1] + a[0][1] * b[1][1]
        x[1][0] = a[1][0] * b[0][0] + a[1][1] * b[1][0]
        x[1][1] = a[1][0] * b[0][1] + a[1][1] * b[1][1]
    else:
        (a00, a01, a10, a11), (b00, b01, b10, b11), mid = split(a), split(b), n // 2
        c00 = add(smmr(a00, b00, mid), smmr(a01, b10, mid))
        c01 = add(smmr(a00, b01, mid), smmr(a01, b11, mid))
        c10 = add(smmr(a10, b00, mid), smmr(a11, b10, mid))
        c11 = add(smmr(a10, b01, mid), smmr(a11, b11, mid))
        n = len(c00)
        for r in range(n):
            for c in range(n):
                x[r][c] = c00[r][c]
                x[r][c + n] = c01[r][c]
                x[r + n][c] = c10[r][c]
                x[r + n][c + n] = c11[r][c]
    return x
