"""
Overview
========

Although in practice we do not generally use matrix inverses to solve systems of linear
equations, preferring instead to use more numerically stable techniques such as LUP
decomposition, sometimes we need to compute a matrix inverse.

The general formula for computing the inverse of a matrix A is:

A^(-1) = Adjoint(A) / det(A)

Adjoint
-------

The adjoint of a matrix is the transpose of the cofactor element matrix of the given
matrix.

Cofactor
--------

The cofactor of an element is calculated by multiplying the minor with -1 to the
exponent of the sum of the row and column elements in order representation of that
element.

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
the determinant obtained after eliminating the row and column containing the element.

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

Theta(n^3) time complexity
"""


def det(a):
    if len(a) == 2:
        return a[0][0] * a[1][1] - a[0][1] * a[1][0]
    return sum(((-1) ** c) * a[0][c] * det(minor(a, 0, c)) for c in range(len(a)))


def minor(a, i, j):
    return [row[:j] + row[j + 1 :] for row in a[:i] + a[i + 1 :]]


def transpose(a):
    return list(map(list, zip(*a)))


def invert_matrix(a):
    n, det_ = len(a), det(a)
    assert det_ != 0
    if n == 2:
        return [
            [a[1][1] / det_, -1 * a[0][1] / det_],
            [-1 * a[1][0] / det_, a[0][0] / det_],
        ]
    cofactors = [
        [((-1) ** (r + c)) * det(minor(a, r, c)) for c in range(n)] for r in range(n)
    ]
    adjoint = transpose(cofactors)
    n = len(adjoint)
    for r in range(n):
        for c in range(n):
            adjoint[r][c] = adjoint[r][c] / det_
    return adjoint


a = [[4, -2, 1], [5, 0, 3], [-1, 2, 6]]
print(invert_matrix(a))
