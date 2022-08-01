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

There are several ways to implement the BFS algorithm.

    - One way would be that we run a two-level nested loop, with the outer loop
iterating each level on the tree, and with the inner loop iterating each node within a
single level.
    - We could also implement BFS with a single loop though. The trick is that we append
the nodes to be visited into a queue and we separate nodes of different levels with a
sort of delimiter (e.g. an empty node). The delimiter marks the end of a level, as well
as the beginning of a new level.

Approach One

Starting from the top rotten orange, the contamination would propagate layer by layer
(or level by level), until it reaches the farthest fresh oranges. The number of minutes
that are elapsed would be equivalent to the number of levels in the graph that we
traverse during the propagation.

Approach Two

As one might recall from the previous BFS implementation, its space complexity is mainly
due to the queue that we were using to keep the order for the visits of cells. In order
to achieve O(1) space complexity, we then need to eliminate the queue in the BFS.

The idea is that at each round of the BFS, we mark the cells to be visited in the input
grid with a specific timestamp. By round, we mean a snapshot in time where a group of
oranges turns rotten.

1. Starting from the beginning (with timestamp=2), the cells that are marked with the
value 2 contain rotten oranges. From this moment on, we adopt a rule stating as "the
cells that have the value of the current timestamp (i.e. 2) should be visited at this
round of BFS.".

2. For each of the cell that is marked with the current timestamp, we then go on to mark
its neighbor cells that hold a fresh orange with the next timestamp
(i.e., timestamp += 1). This in-place modification serves the same purpose as the queue
variable in the previous BFS implementation, which is to select the candidates to visit
for the next round.

3. At this moment, we should have timestamp=3, and meanwhile we also have the cells to
be visited at this round marked out. We then repeat the above step (2) until there is no
more new candidates generated in the step (2) (i.e. the end of BFS traversal).

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
    m, n = len(grid), len(grid[0])
    num_fresh, minutes, queue = 0, -1, deque()
    for row in range(m):
        for col in range(n):
            if grid[row][col] == 2:
                queue.append((row, col))
            elif grid[row][col] == 1:
                num_fresh += 1
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
                    num_fresh -= 1
                    queue.append((r, c))
    return minutes if num_fresh == 0 else -1


def sol_two(grid):
    m, n = len(grid), len(grid[0])
    minutes, keep_going = 2, True
    while keep_going:
        keep_going = False
        for row in range(m):
            for col in range(n):
                if grid[row][col] != minutes:
                    continue
                for x, y in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                    r, c = row + x, col + y
                    if 0 <= r < m and 0 <= c < n and grid[r][c] == 1:
                        grid[r][c] = minutes + 1
                        keep_going = True
        if keep_going:
            minutes += 1
    if any(grid[row][col] == 1 for row in range(m) for col in range(n)):
        return -1
    return minutes - 2
