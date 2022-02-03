"""
28.2 Inverting matrices
=======================

Although in practice we do not generally use matrix inverses to solve systems of linear
equations, preferring instead to use more numerically stable techniques such as LUP
decomposition, sometimes we need to compute a matrix inverse.

Computing a matrix inverse from an LUP decomposition
----------------------------------------------------

Suppose that we have an LUP decomposition of a matrix A in the form of three matrices L,
U, and P such that PA = LU. Using lup_solver(), we can solve an equation of the form
Ax = b in time Theta(n^2). Since the LUP decomposition depends on A and not b, we can
run lup_solver() on a second set of equations of the form Ax = b' in additional time
Theta(n^2). In general, once we have the LUP decomposition of A, we can solve, in time
Theta(k * n^2), k versions of the equation Ax = b that differ only in b.

We can think of the equation

AX = I_n,

which defines the matrix X, the inverse of A, as a set of n distinct equations of the
form Ax = b. We would call lup_solver() to solve each of the n columns of X after having
obtained the LUP decomposition of A.

LUP decomposition takes Theta(n^3) time. Calling lup_solver() takes Theta(n^2) but we
have to call it n times. Thus, the total time for inverting a matrix using LUP
decomposition is Theta(n^3).

Intuition
---------

The general formula for computing the inverse of a matrix A is:

A^(-1) = Adjoint(A) / det(A)

The inverse of a 2 x 2 matrix A is:

[d -b
 -c a] / det(A)

The determinant of a 2 x 2 matrix A is:

det(A) = a * d - b * c

Adjoint
-------

The adjoint of a matrix is the transpose of the cofactor element matrix of the given
matrix.

Cofactor
--------

The cofactor of an element is calculated by multiplying the determinant of the minor
with -1 to the exponent of the sum of the row and column elements in order
representation of that element.

cofactor of a_ij = (-1)^(i + j) x minor(a_ij)

Determinant
-----------

The determinant of a matrix is the single unique value representation of a matrix. The
determinant of a matrix can be calculated with reference to any row or column of a given
matrix. The determinant of a matrix is equal to the summation of the product of the
elements and its cofactors, or a particular row or column of the matrix.

Minor
-----

The minor is defined for every element of a matrix. The minor of a particular element is
obtained after eliminating the row and column containing the element.

Non-Singular Matrix
-------------------

A matrix whose determinant value is not equal to zero. For a non-singular matrix,
det(A) != 0. A non-singular matrix is called an invertible matrix since its inverse can
be calculated.

Singular Matrix
---------------

A matrix having a determinant value of zero is referred to as a singular matrix. For a
singular matrix A, det(A) = 0. The inverse of a singular matrix does not exist.

Transpose
---------

The transpose of a matrix A, A.T, is such that the rows and columns of A are swapped.
Note that in transpose(), *a flattens the 2D matrix into a sequence of lists. zip(*a)
then allows us to iterate over the corresponding elements in each list in the sequence.
map(list, zip(*a)) then converts the zipped elements from tuples to lists. The final
list(map(list, zip(*a))) then converts a back to a 2D matrix.

Complexity
==========

Time
----

invert() and invert_lup(): Theta(n^3).
"""

# Repository Library
from src.clrs.selected_topics.matrix_operations.lup_solver import lup_decomp, lup_solver


def cofactor(a):
    return [
        [((-1) ** (r + c)) * det(minor(a, r, c)) for c in range(len(a))]
        for r in range(len(a))
    ]


def det(a):
    if len(a) == 2:
        return a[0][0] * a[1][1] - a[0][1] * a[1][0]
    return sum(((-1) ** c) * a[0][c] * det(minor(a, 0, c)) for c in range(len(a)))


def minor(a, r, c):
    return [row[:c] + row[c + 1 :] for row in a[:r] + a[r + 1 :]]


def transpose(a):
    return list(map(list, zip(*a)))


def invert(a):
    det_ = det(a)
    assert det_ != 0
    if len(a) == 2:
        return [[a[1][1] / det_, -a[0][1] / det_], [-a[1][0] / det_, a[0][0] / det_]]
    adjoint = transpose(cofactor(a))
    n = len(adjoint)
    for r in range(n):
        for c in range(n):
            adjoint[r][c] /= det_
    return adjoint


def invert_lup(a):
    n = len(a)
    inv = [[0] * n for _ in range(n)]
    p = lup_decomp(a)
    for i in range(n):
        b = [0] * n
        b[i] = 1
        inv[i] = lup_solver(a, b, p, decomp=False)
    return transpose(inv)
