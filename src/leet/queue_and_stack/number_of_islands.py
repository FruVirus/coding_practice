"""
Number of Islands
-----------------

Given an m x n 2D binary grid grid which represents a map of '1's (land) and '0's
(water), return the number of islands.

An island is surrounded by water and is formed by connecting adjacent lands horizontally
or vertically. You may assume all four edges of the grid are all surrounded by water.

Complexity
==========

Time
----

numIslands(grid): O(m * n).

Space
-----

numIslands(grid): O(min(m, n)).
"""

# Standard Library
from collections import deque


def sol(grid):
    m, n, num_islands = len(grid), len(grid[0]), 0
    for row in range(m):
        for col in range(n):
            if grid[row][col] != "1":
                continue
            num_islands += 1
            grid[row][col] = 0
            queue = deque([(row, col)])
            while queue:
                r, c = queue.popleft()
                for x, y in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                    i, j = r + x, c + y
                    if 0 <= i < m and 0 <= j < n and grid[i][j] == "1":
                        grid[i][j] = "0"
                        queue.append((i, j))
    return num_islands
