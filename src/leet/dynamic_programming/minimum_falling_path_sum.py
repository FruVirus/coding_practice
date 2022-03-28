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

minFallingPathSum(matrix): O(m * n).

Space
-----

minFallingPathSum(matrix): O(n).
"""


def sol_bu(matrix):
    m, n = len(matrix), len(matrix[0])
    dp, temp = matrix[0][:], [0] * n
    for i in range(1, m):
        for j in range(n):
            above = dp[j]
            above_left = float("inf") if j == 0 else dp[j - 1]
            above_right = float("inf") if j == n - 1 else dp[j + 1]
            temp[j] = matrix[i][j] + min(above, above_left, above_right)
        dp, temp = temp, dp
    return min(dp)


def sol_td(matrix):
    memo, n = {}, len(matrix)

    def dp(row, col):
        if row == n:
            return 0
        if col < 0 or col > n - 1:
            return float("inf")
        if (row, col) not in memo:
            above = dp(row + 1, col)
            above_left = dp(row + 1, col - 1)
            above_right = dp(row + 1, col + 1)
            memo[(row, col)] = matrix[row][col] + min(above, above_left, above_right)
        return memo[(row, col)]

    return min(dp(0, col) for col in range(n))
