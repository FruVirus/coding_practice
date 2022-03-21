"""
House Robber
------------

You are a professional robber planning to rob houses along a street. Each house has a
certain amount of money stashed, the only constraint stopping you from robbing each of
them is that adjacent houses have security systems connected and it will automatically
contact the police if two adjacent houses were broken into on the same night.

Given an integer array nums representing the amount of money of each house, return the
maximum amount of money you can rob tonight without alerting the police.

Complexity
==========

Time
----

rob(nums): O(n).

Space
-----

rob(nums): O(n).
"""


def sol_bu(nums):
    if len(nums) == 1:
        return nums[0]
    dp = [0] * len(nums)
    dp[0] = nums[0]
    dp[1] = max(nums[0], nums[1])
    for i in range(2, len(nums)):
        dp[i] = max(dp[i - 1], dp[i - 2] + nums[i])
    return dp[-1]


def sol_td(nums):
    memo = {}

    def dp(i):
        if i == 0:
            return nums[0]
        if i == 1:
            return max(nums[0], nums[1])
        if i not in memo:
            memo[i] = max(dp(i - 1), dp(i - 2) + nums[i])
        return memo[i]

    return dp(len(nums) - 1)
