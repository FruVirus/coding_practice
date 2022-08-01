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

In other words, prev is the value of dp[i - 1][j - 1] from the previous iteration of the
inner for-loop, dp[j] is the value of dp[i - 1][j] (before it gets reassigned), and
dp[j - 1] is the value of dp[i][j - 1]. Note that dp[j] gets assigned to temp before
dp[j] gets reassigned (if there is a "1") and then temp gets assigned to prev. Since
dp[j] gets assigned to temp first, this effectively serves to capture the "j - 1"
aspect. Since prev is updated inside the j for-loop, each subsequent iteration of i sees
prev coming from "i - 1".

Complexity
==========

Time
----

maximalSquare_bu(matrix) and maximalSquare_td(matrix): O(m * n).

Space
-----

maximalSquare_bu(matrix): O(n).
maximalSquare_td(matrix): O(m * n).
"""


def sol_bu(matrix):
    m, n = len(matrix), len(matrix[0])
    dp, maxlen, prev = [0] * (n + 1), 0, 0
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            temp = dp[j]
            if matrix[i - 1][j - 1] == "1":
                dp[j] = 1 + min(dp[j], dp[j - 1], prev)
                maxlen = max(maxlen, dp[j])
            else:
                dp[j] = 0
            prev = temp
    return maxlen ** 2


def sol_td(matrix):
    memo, m, n = {}, len(matrix), len(matrix[0])

    def dp(i, j):
        if not (i < m and j < n and matrix[i][j] == "1"):
            return 0
        if (i, j) not in memo:
            memo[(i, j)] = 1 + min(dp(i + 1, j), dp(i, j + 1), dp(i + 1, j + 1))
        return memo[(i, j)]

    return max(dp(i, j) for i in range(m) for j in range(n)) ** 2
