"""
Maximum Score from Performing Multiplication Operations
-------------------------------------------------------

You are given two integer arrays nums and multipliers of size n and m respectively,
where n >= m. The arrays are 1-indexed.

You begin with a score of 0. You want to perform exactly m operations. On the i-th
operation (1-indexed), you will:

    - Choose one integer x from either the start or the end of the array nums.
    - Add multipliers[i] * x to your score.
    - Remove x from the array nums.

Return the maximum score after performing m operations.

Complexity
==========

Time
----

maximumScore(nums, multipliers): O(m^2), where m is the length of multipliers.

Space
-----

maximumScore(nums, multipliers): O(m^2).
"""


# Standard Library
from functools import lru_cache


def sol_bu(nums, mults):
    n, m = len(nums), len(mults)
    dp = [[0] * (m + 1) for _ in range(m + 1)]
    for i in reversed(range(m)):
        for left in range(i, -1, -1):
            mult, right = mults[i], n - (i - left) - 1
            dp[i][left] = max(
                mult * nums[left] + dp[i + 1][left + 1],
                mult * nums[right] + dp[i + 1][left],
            )
    return dp[0][0]


def sol_td(nums, mults):
    n, m = len(nums), len(mults)

    @lru_cache(2000)
    def dp(i, left):
        if i == m:
            return 0
        mult, right = mults[i], n - (i - left) - 1
        return max(
            mult * nums[left] + dp(i + 1, left + 1),
            mult * nums[right] + dp(i + 1, left),
        )

    return dp(0, 0)
