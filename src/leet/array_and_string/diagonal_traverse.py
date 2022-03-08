"""
Diagonal Traverse
-----------------

Given an m x n matrix mat, return an array of all the elements of the array in a
diagonal order.

Complexity
==========

Time
----

findDiagonalOrder(mat): O(m * n).

Space
-----

findDiagonalOrder(mat): O(m * n).
"""

# pylint: disable=C0200


def sol(mat):
    diag, sol = {}, []
    for i in range(len(mat)):
        for j in range(len(mat[i])):
            if i + j not in diag:
                diag[i + j] = [mat[i][j]]
            else:
                diag[i + j].append(mat[i][j])
    for diag_level, diag_elements in diag.items():
        sol.extend(diag_elements if diag_level % 2 != 0 else reversed(diag_elements))
    return sol
