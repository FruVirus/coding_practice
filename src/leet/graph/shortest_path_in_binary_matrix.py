"""
Shortest Path in Binary Matrix
------------------------------

Given an n x n binary matrix grid, return the length of the shortest clear path in the
matrix. If there is no clear path, return -1.

A clear path in a binary matrix is a path from the top-left cell (i.e., (0, 0)) to the
bottom-right cell (i.e., (n - 1, n - 1)) such that:

    - All the visited cells of the path are 0.
    - All the adjacent cells of the path are 8-directionally connected (i.e., they are
different and they share an edge or a corner).

The length of a clear path is the number of visited cells of this path.

Complexity
==========

Time
----

shortestPathBinaryMatrix(grid): O(n), where n is the number of cells in the grid.

Space
-----

shortestPathBinaryMatrix(grid): O(n).
"""


# Standard Library
from collections import deque


def sol(grid):
    if grid[0][0] == 1 or grid[-1][-1] == 1:
        return -1
    n, queue, visited = len(grid), deque([(0, 0, 1)]), {(0, 0)}
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1), (-1, -1), (-1, 1), (1, -1), (1, 1)]
    while queue:
        row, col, dist = queue.popleft()
        if row == col == n - 1:
            return dist
        for x, y in directions:
            r, c = row + x, col + y
            if 0 <= r < n and 0 <= c < n and (r, c) not in visited and grid[r][c] == 0:
                visited.add((r, c))
                queue.append((r, c, dist + 1))
    return -1
