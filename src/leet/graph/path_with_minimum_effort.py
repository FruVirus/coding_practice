"""
Path With Minimum Effort
------------------------

You are a hiker preparing for an upcoming hike. You are given heights, a 2D array of
size rows x columns, where heights[row][col] represents the height of cell (row, col).
You are situated in the top-left cell, (0, 0), and you hope to travel to the
bottom-right cell, (rows - 1, columns - 1) (i.e., 0-indexed). You can move up, down,
left, or right, and you wish to find a route that requires the minimum effort.

A route's effort is the maximum absolute difference in heights between two consecutive
cells of the route.

Return the minimum effort required to travel from the top-left cell to the bottom-right
cell.

Intuition
---------

Binary Search Approach

Our aim to find the minimum effort required to travel from source cell to destination
cell. We know from the given constraints that the maximum height could be 10^6. So we
know that our required absolute difference values would between 0 and 10^6. We could use
Binary Search and reduce our search space by half. Given the lower bound as 0 and upper
bound as 10^6, we could repeatedly calculate the middle value. Let this middle value be
mid. We could divide our search space based on the following condition,

    - If there exists a path from the source cell to the destination cell with the
effort less than the value mid, we know that the required minimum effort value lies
between lower bound 0 and mid.
    - Similarly, if there doesn't exist any path from a source cell to destination cell
with the effort less than the value mid, we know that the required minimum effort value
lies between mid and upper bound 10^6.

To find if there exists a path from the source cell to the destination cell for a given
mid value, we could use simple graph traversal. In this approach, we use Breath First
Search traversal.

Dijkstra Approach

If we observe, the problem is similar to finding the shortest path from a source cell to
a destination cell. Here, the shortest path is the one with minimum absolute difference
between every adjacent cells in that path. Also, since there is height associated with
each cell, simple BFS traversal won't be sufficient.

The absolute difference between adjacent cells A and B can be perceived as the weight of
an edge from cell A to cell B. Thus, we could use Dijkstra's Algorithm which is used to
find the shortest path in a weighted graph with a slight modification of criteria for
the shortest path.

We use a differenceMatrix of size row * col where each cell represents the minimum
effort required to reach that cell from all the possible paths. Also, we initialize all
the cells in the differenceMatrix to infinity since none of the cells are reachable
initially.

As we start visiting each cell, all the adjacent cells are now reachable. We update the
absolute difference between the current cell and adjacent cells in the differenceMatrix.
At the same time, we also push all the adjacent cells in a priority queue
(effort, x, y). The priority queue holds all the reachable cells sorted by its value in
differenceMatrix, i.e., the cell with minimum absolute difference with its adjacent
cells would be at the top of the queue.

We begin by adding the source cell (x = 0, y = 0) in the queue. Now, until we have
visited the destination cell or the queue is empty, we visit each cell in the queue
sorted in the order of priority. The less is the difference value (absolute difference
with adjacent cell) of a cell, the higher is its priority.

    - Get the cell from the top of the queue curr and visit the current cell.

    - For each of the 4 cells adjacent to the current cell, calculate the maxDifference
which is the maximum absolute difference to reach the adjacent cell
(adjacentX, adjacentY) from current cell (curr.x, curr.y).

    - If the current value of the adjacent cell (adjacentX, adjacentY) in the
difference matrix is greater than the maxDifference, we must update that value with
maxDifference. In other words, we have found that the path from the current cell to the
adjacent cell takes lesser efforts than the other paths that have reached the adjacent
cell so far. Also, we must add this updated difference value in the queue.

Ideally, for updating the priority queue, we must delete the old value and reinsert with
the new maxDifference value. But, as we know that the updated maximum value is always
lesser than the old value and would be popped from the queue and visited before the old
value, we could save time and avoid removing the old value from the queue.

Complexity
==========

Time
----

minimumEffortPath_bs(heights): O(m * n).
minimumEffortPath_dijkstra(heights): O((m * n) * lg (m * n)).

Space
-----

minimumEffortPath_bs(heights): O(m * n).
minimumEffortPath_dijkstra(heights): O(m * n).
"""


# Standard Library
import heapq

from collections import deque


def sol_bs(heights):
    m, n = len(heights), len(heights[0])

    def bfs(mid):
        queue = deque([(0, 0)])
        while queue:
            row, col = queue.popleft()
            if row == m - 1 and col == n - 1:
                return True
            seen[row][col] = True
            for x, y in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                r, c = row + x, col + y
                if 0 <= r < m and 0 <= c < n and not seen[r][c]:
                    if abs(heights[row][col] - heights[r][c]) <= mid:
                        seen[r][c] = True
                        queue.append((r, c))

    low, high = 0, 10 ** 6
    while low < high:
        mid = low + (high - low) // 2
        seen = [[False] * n for _ in range(m)]
        if not bfs(mid):
            low = mid + 1
        else:
            high = mid
    return low


def sol_dijkstra(heights):
    m, n = len(heights), len(heights[0])
    effort = [[float("inf")] * n for _ in range(m)]
    effort[0][0] = 0
    heap, visited = [(0, 0, 0)], [[False] * n for _ in range(m)]
    while heap:
        _, row, col = heapq.heappop(heap)
        visited[row][col] = True
        for x, y in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            r, c = row + x, col + y
            if 0 <= r < m and 0 <= c < n and not visited[r][c]:
                effort_ = max(abs(heights[row][col] - heights[r][c]), effort[row][col])
                if effort[r][c] > effort_:
                    effort[r][c] = effort_
                    heapq.heappush(heap, (effort_, r, c))
    return effort[-1][-1]
