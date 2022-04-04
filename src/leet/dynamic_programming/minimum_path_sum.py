"""
Minimum Path Sum
----------------

Given a m x n grid filled with non-negative numbers, find a path from top left to bottom
right, which minimizes the sum of all numbers along its path.

Note: You can only move either down or right at any point in time.

Intuition
---------

We can do the same work using a dp array of the row size, since for making the current
entry all we need is the dp entry for the bottom and the right element. Thus, we start
by initializing only the last element of the array as the last element of the given
matrix. The last entry is the bottom rightmost element of the given matrix. Then, we
start moving towards the left and update the entry dp(j) as:

    - dp(j) = grid(i,j) + min(dp(j), dp(j + 1))

We repeat the same process for every row as we move upwards. At the end dp(0) gives the
required minimum sum.

Complexity
==========

Time
----

minPathSum(grid): O(m * n).

Space
-----

minPathSum_bu(grid): O(n).
minPathSum_td(grid): O(n).
"""


def sol_bu(grid):
    m, n = len(grid), len(grid[0])
    dp = [0] * (n - 1) + [grid[-1][-1]]
    for i in reversed(range(m)):
        for j in reversed(range(n)):
            if i == m - 1 and j != n - 1:
                dp[j] = grid[i][j] + dp[j + 1]
            elif i != m - 1 and j == n - 1:
                dp[j] += grid[i][j]
            elif i != m - 1 and j != n - 1:
                dp[j] = grid[i][j] + min(dp[j], dp[j + 1])
    return dp[0]


def sol_td(grid):
    memo, m, n = {}, len(grid), len(grid[0])

    def dp(i, j):
        val = grid[i][j]
        if i == m - 1 and j == n - 1:
            return val
        if (i, j) not in memo:
            if i == m - 1 and j != n - 1:
                val += dp(i, j + 1)
            elif i != m - 1 and j == n - 1:
                val += dp(i + 1, j)
            else:
                val += min(dp(i + 1, j), dp(i, j + 1))
            memo[(i, j)] = val
        return memo[(i, j)]

    return dp(0, 0)
