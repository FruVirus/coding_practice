"""
Maximal Square
--------------

Given an m x n binary matrix filled with 0's and 1's, find the largest square containing
only 1's and return its area.

Intuition
---------

We initialize another matrix (dp) with the same dimensions as the original one
initialized with all 0’s.

dp(i, j) represents the side length of the maximum square whose bottom right corner is
the cell with index (i, j) in the original matrix.

Starting from index (0, 0), for every 1 found in the original matrix, we update the
value of the current element as

    - dp(i, j) = min(dp(i − 1, j), dp(i − 1, j − 1), dp(i, j − 1)) + 1

We also remember the size of the largest square found so far. In this way, we traverse
the original matrix once and find out the required maximum size. This gives the side
length of the square. The required result is the area.

Square ending at (i, j) is the intersection of:

    1. Square ending at (i - 1, j - 1)
    2. Square ending at (i - 1, j)
    3. Square ending at (i, j - 1)

So maximum size of square ending at (i, j) will be minimum of the above three squares
plus 1 (if the square at (i, j) has a value of 1).

In the bottom up approach for calculating dp of i-th row we are using only the previous
element and the (i - 1)-th row. Therefore, we don't need 2D dp matrix as 1D dp array
will be sufficient for this. In the memory optimized approach, the dp array initially
contains all 0's. As we scan the elements of the original matrix across a row, we keep
on updating the dp array as per the equation dp[j] = min(dp[j - 1], dp[j], prev), where
prev refers to the old dp[j - 1]. For every row, we repeat the same process and update
in the same dp array.

Complexity
==========

Time
----

maximalSquare_bu(matrix) and maximalSquare_opt(matrix): O(m * n).

Space
-----

maximalSquare_bu(matrix): O(m * n).
maximalSquare_opt(matrix): O(n).
"""


def sol_bu(matrix):
    rows, cols = len(matrix), len(matrix[0])
    dp, maxsqlen = [[0] * (cols + 1) for _ in range(rows + 1)], 0
    for i in range(1, rows + 1):
        for j in range(1, cols + 1):
            if matrix[i - 1][j - 1] == "1":
                dp[i][j] = min(dp[i - 1][j], dp[i][j - 1], dp[i - 1][j - 1]) + 1
                maxsqlen = max(maxsqlen, dp[i][j])
    return maxsqlen ** 2


def sol_opt(matrix):
    rows, cols = len(matrix), len(matrix[0])
    dp, maxsqlen, prev = [0] * (cols + 1), 0, 0
    for i in range(1, rows + 1):
        for j in range(1, cols + 1):
            temp = dp[j]
            if matrix[i - 1][j - 1] == "1":
                dp[j] = min(dp[j], dp[j - 1], prev) + 1
                maxsqlen = max(maxsqlen, dp[j])
            else:
                dp[j] = 0
            prev = temp
    return maxsqlen ** 2
