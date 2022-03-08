"""
Diagonal Traverse
-----------------

Given an m x n matrix, return all elements of the matrix in spiral order.

Complexity
==========

Time
----

spiralOrder(matrix): O(m * n).

Space
-----

spiralOrder(matrix): O(1).
"""


def sol(matrix):
    m, n = len(matrix), len(matrix[0])
    i, j, direction, sol = 0, -1, 1, []
    while m * n > 0:
        for _ in range(n):
            j += direction
            sol.append(matrix[i][j])
        m -= 1
        for _ in range(m):
            i += direction
            sol.append(matrix[i][j])
        n -= 1
        direction *= -1
    return sol
