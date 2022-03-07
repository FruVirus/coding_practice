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

updateMatrix(mat): O(m * n).
"""

# Standard Library
from collections import deque


def sol(mat):
    m, n = len(mat), len(mat[0])
    dist, queue = [[float("inf")] * n for _ in range(m)], deque()
    for row in range(m):
        for col in range(n):
            if mat[row][col] == 0:
                dist[row][col] = 0
                queue.append((row, col))
    while queue:
        row, col = queue.popleft()
        for x, y in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            r, c = row + x, col + y
            if 0 <= r < m and 0 <= c < n and dist[r][c] > dist[row][col]:
                dist[r][c] = dist[row][col] + 1
                queue.append((r, c))
    return dist
