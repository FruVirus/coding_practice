"""
Unique Paths
------------

There is a robot on an m x n grid. The robot is initially located at the top-left corner
(i.e., grid[0][0]). The robot tries to move to the bottom-right corner (i.e.,
grid[m - 1][n - 1]). The robot can only move either down or right at any point in time.

Given the two integers m and n, return the number of possible unique paths that the
robot can take to reach the bottom-right corner.

Intuition
---------

1. An array that answers the problem for a given state

State variables are usually easy to find in pathing problems. Similar to how we need one
index (i) for 1D array inputs, with pathing problems on a 2D matrix, we need two indices
(row and col) to denote position. Some problems have added constraints that will require
additional state variables, but there doesn't seem to be anything of the sort in this
problem. Therefore, we will just use two state variables row which represents the
current row, and col which represents the current column.

The problem is asking for the number of paths to the final square, so let's have
dp[row][col] represent how many paths there are from the start (top-left corner) to the
square at (row, col). We will return dp[m - 1][n - 1] where m and n are the number of
rows and columns respectively.

2. A recurrence relation to transition between states

The problem says that we are allowed to move down or right. That means, if we are at
some square, we arrived from either the square above or the square to the left. These
two squares are (row - 1, col) and (row, col - 1). Since we can arrive at the current
square from either of these squares, the number of ways to get to the current square is
the sum of the number of ways to get to these two squares. Either of these may be out of
the grid bounds, so we should make sure to check for that. This gives us our simple
recurrence relation:

    - dp[row][col] = dp[row - 1][col] + dp[row][col - 1], where
dp[row - 1][col] and dp[row][col - 1] is equal to 0 if out of bounds.

3. Base cases

In the previous chapter, when talking about counting DP problems, we said that the base
cases need to be set to nonzero values so that the terms in the recurrence relation
don't just stay stuck at zero. In this problem, we start in the top-left corner. How
many ways are there for us to get to the first square? Only 1 - we start on it.
Therefore, our base case is dp[0][0] = 1.

Complexity
==========

Time
----

uniquePaths_bu(m, n) and uniquePaths_td(m, n): O(m * n).

Space
-----

uniquePaths_bu(m, n): O(n).
uniquePaths_td(m, n): O(m * n).
"""


def sol_bu(m, n):
    if m > n:
        m, n = n, m
    dp = [1] * m
    for _ in range(1, n):
        for j in range(1, m):
            dp[j] += dp[j - 1]
    return dp[-1]


def sol_td(m, n):
    memo = {}

    def dp(i, j):
        if i == j == 0:
            return 1
        if i < 0 or j < 0:
            return 0
        if (i, j) not in memo:
            memo[(i, j)] = dp(i - 1, j) + dp(i, j - 1)
        return memo[(i, j)]

    return dp(m - 1, n - 1)
