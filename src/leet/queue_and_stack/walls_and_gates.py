"""
Walls and Gates
---------------

You are given an m x n grid rooms initialized with these three possible values.

    -1 A wall or an obstacle.
    0 A gate.
    INF Infinity means an empty room.

Fill each empty room with the distance to its nearest gate. If it is impossible to reach
a gate, it should be filled with INF.

Complexity
==========

Time
----

wallsAndGates(rooms): O(m * n).

Space
-----

wallsAndGates(rooms): O(m * n).
"""

# Standard Library
from collections import deque


def sol(rooms):
    m, n, queue = len(rooms), len(rooms[0]), deque()
    for row in range(m):
        for col in range(n):
            if rooms[row][col] == 0:
                queue.append((row, col))
    while queue:
        row, col = queue.popleft()
        for x, y in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            r, c = row + x, col + y
            if 0 <= r < m and 0 <= c < n and rooms[r][c] == float("inf"):
                rooms[r][c] = rooms[row][col] + 1
                queue.append((r, c))
