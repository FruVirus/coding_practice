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
    dp, temp = [1 - i for i in grid[0]], [0] * n
    for i in range(1, len(dp)):
        if dp[i - 1] == 0:
            dp[i] = 0
    for row in range(1, m):
        for col in range(n):
            if grid[row][col] == 0:
                temp[col] = dp[col] if col == 0 else dp[col] + temp[col - 1]
        dp, temp = temp, [0] * n
    return dp[-1]


def sol_td(grid):
    memo, m, n = {}, len(grid), len(grid[0])

    def dp(row, col):
        if row == col == 0:
            return 1 - grid[row][col]
        if (row, col) not in memo:
            num_paths = 0
            if grid[row][col] == 0:
                if row > 0:
                    num_paths += dp(row - 1, col)
                if col > 0:
                    num_paths += dp(row, col - 1)
            memo[(row, col)] = num_paths
        return memo[(row, col)]

    return dp(m - 1, n - 1)
