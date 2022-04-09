"""
Unique Paths II
---------------

A robot is located at the top-left corner of a m x n grid.

The robot can only move either down or right at any point in time. The robot is trying
to reach the bottom-right corner of the grid.

Now consider if some obstacles are added to the grids. How many unique paths would there
be?

An obstacle and space is marked as 1 and 0 respectively in the grid.

Complexity
==========

Time
----

uniquePathsWithObstacles(grid): O(m * n).

Space
-----

uniquePathsWithObstacles_bu(grid): O(n).
uniquePathsWithObstacles_td(grid): O(m * n).
"""


def sol_bu(grid):
    m, n = len(grid), len(grid[0])
    dp = [1 - i for i in grid[0]]
    for i in range(1, n):
        if dp[i - 1] == 0:
            dp[i] = 0
    for i in range(1, m):
        curr = [0] * n
        for j in range(n):
            if grid[i][j] == 0:
                curr[j] = dp[j] if j == 0 else dp[j] + curr[j - 1]
        dp = curr
    return dp[-1]


def sol_td(grid):
    memo, m, n = {}, len(grid), len(grid[0])

    def dp(i, j):
        if i == j == 0:
            return 1 if grid[i][j] == 0 else 0
        if i < 0 or j < 0:
            return 0
        if (i, j) not in memo:
            memo[(i, j)] = dp(i - 1, j) + dp(i, j - 1) if grid[i][j] == 0 else 0
        return memo[(i, j)]

    return dp(m - 1, n - 1)
