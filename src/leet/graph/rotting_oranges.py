"""
Rotting Oranges
---------------

You are given an m x n grid where each cell can have one of three values:

    - 0 representing an empty cell,
    - 1 representing a fresh orange, or
    - 2 representing a rotten orange.

Every minute, any fresh orange that is 4-directionally adjacent to a rotten orange
becomes rotten.

Return the minimum number of minutes that must elapse until no cell has a fresh orange.
If this is impossible, return -1.

Intuition
---------

We use a delimiter (i.e., (None, None)) in the queue to separate cells on different
levels. In this way, we only need one queue for the iteration. As an alternative, one
can create a queue for each level and alternate between the queues, though technically
the initialization and the assignment of each queue could consume some extra time.

Complexity
==========

Time
----

orangesRotting_one(grid): O(m * n).
orangesRotting_two(grid): O((m * n)^2).

Space
-----

orangesRotting_one(grid): O(m * n).
orangesRotting_two(grid): O(1).
"""


# Standard Library
from collections import deque


def sol_one(grid):
    m, n, fresh, minutes, queue = len(grid), len(grid[0]), 0, -1, deque()
    for row in range(m):
        for col in range(n):
            if grid[row][col] == 2:
                queue.append((row, col))
            elif grid[row][col] == 1:
                fresh += 1
    queue.append((None, None))
    while queue:
        row, col = queue.popleft()
        if row is None:
            minutes += 1
            if queue:
                queue.append((None, None))
        else:
            for x, y in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                r, c = row + x, col + y
                if 0 <= r < m and 0 <= c < n and grid[r][c] == 1:
                    grid[r][c] = 2
                    fresh -= 1
                    queue.append((r, c))
    return minutes if fresh == 0 else -1


def sol_two(grid):
    m, n, minutes, keep_going = len(grid), len(grid[0]), 2, True
    while keep_going:
        keep_going = False
        for row in range(m):
            for col in range(n):
                if grid[row][col] == minutes:
                    for x, y in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                        r, c = row + x, col + y
                        if 0 <= r < m and 0 <= c < n and grid[r][c] == 1:
                            grid[r][c] = minutes + 1
                            keep_going = True
        if keep_going:
            minutes += 1
    for row in range(m):
        for col in range(n):
            if grid[row][col] == 1:
                return -1
    return minutes - 2
