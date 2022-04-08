"""
Minimum Falling Path Sum
------------------------

Given an n x n array of integers matrix, return the minimum sum of any falling path
through matrix.

A falling path starts at any element in the first row and chooses the element in the
next row that is either directly below or diagonally left/right. Specifically, the next
element from position (row, col) will be (row + 1, col - 1), (row + 1, col), or
(row + 1, col + 1).

Complexity
==========

Time
----

minFallingPathSum(matrix): O(n^2).

Space
-----

minFallingPathSum_bu(matrix): O(n).
minFallingPathSum_td(matrix): O(n^2).
"""


def sol_bu(matrix):
    n = len(matrix)
    dp, curr = matrix[0][:], [0] * n
    for i in range(1, n):
        for j in range(n):
            above = dp[j]
            above_left = float("inf") if j == 0 else dp[j - 1]
            above_right = float("inf") if j == n - 1 else dp[j + 1]
            curr[j] = matrix[i][j] + min(above, above_left, above_right)
        dp, curr = curr, dp
    return min(dp)


def sol_td(matrix):
    memo, n = {}, len(matrix)

    def dp(i, j):
        if i == n:
            return 0
        if (i, j) not in memo:
            above = dp(i + 1, j)
            above_left = float("inf") if j == 0 else dp(i + 1, j - 1)
            above_right = float("inf") if j == n - 1 else dp(i + 1, j + 1)
            memo[(i, j)] = matrix[i][j] + min(above, above_left, above_right)
        return memo[(i, j)]

    return min(dp(0, j) for j in range(n))
