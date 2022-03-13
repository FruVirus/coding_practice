"""
01 Matrix
---------

Given an m x n binary matrix mat, return the distance of the nearest 0 for each cell.

The distance between two adjacent cells is 1.

Complexity
==========

Time
----

updateMatrix(mat): O(m * n).

Space
-----

updateMatrix(mat): O(1).
"""

# Standard Library
from collections import deque


def sol(mat):
    m, n, queue = len(mat), len(mat[0]), deque()
    for row in range(m):
        for col in range(n):
            if mat[row][col] == 0:
                queue.append((row, col))
            else:
                mat[row][col] = float("inf")
    while queue:
        row, col = queue.popleft()
        for x, y in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            r, c = row + x, col + y
            if 0 <= r < m and 0 <= c < n and mat[r][c] == float("inf"):
                mat[r][c] = mat[row][col] + 1
                queue.append((r, c))
    return mat
