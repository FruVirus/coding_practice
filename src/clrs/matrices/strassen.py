"""
Overview
========

Assume two matrices, A and B, of shapes [n, m] and [m, p], respectively. Matrix
multiplication of A and B produces an [n, p] matrix C. In general, matrix multiplication
requires n * p matrix entries, each of which is the sum of m values.

Because each of the triply-nested for-loops runs exactly n iterations, and calculation
of c[i][j] takes constant time, naive matrix multiplication takes Theta(n * m * p) time.

Strassen's method is to perform only 7 matrix multiplications instead of 8 as in the
naive recursive algorithm. The cost of eliminating one matrix multiplication will be
several new additions of n / 2 x n / 2 matrices, but still only a constant number of
additions.

Strassen's Method
-----------------

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

Complexity
==========

Theta(n^(lg(7))) = Theta(n^2.81) time complexity
"""


# Third Party Library
import numpy as np


def split(a):
    n, m = len(a), len(a[0])
    n_new, m_new = n // 2, m // 2
    return (
        a[:n_new][:m_new],
        a[:n_new][m_new:],
        a[n_new:][:m_new],
        a[n_new:][m_new:],
    )


def strassen(x, y):
    if len(x) == 1:
        return x * y
    a, b, c, d = split(x)
    e, f, g, h = split(y)
    p1 = strassen(a, f - h)
    p2 = strassen(a + b, h)
    p3 = strassen(c + d, e)
    p4 = strassen(d, g - e)
    p5 = strassen(a + d, e + h)
    p6 = strassen(b - d, g + h)
    p7 = strassen(a - c, e + f)
    c11 = p5 + p4 - p2 + p6
    c12 = p1 + p2
    c21 = p3 + p4
    c22 = p1 + p5 - p3 - p7
    c = np.vstack((np.hstack((c11, c12)), np.hstack((c21, c22))))
    return c


x = [[1, 2], [3, 4]]
y = [[1, 2], [3, 4]]
z = strassen(x, y)
print(z)
