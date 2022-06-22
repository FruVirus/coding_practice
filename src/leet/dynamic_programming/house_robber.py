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

rob_bu(nums) and rob_td(nums): O(n).

Space
-----

rob_bu(nums): O(1).
rob_td(nums): O(n).
"""


def sol_bu(nums):
    if len(nums) == 1:
        return nums[0]
    rob_first, rob_next = nums[0], max(nums[0], nums[1])
    for num in nums[2:]:
        rob_first, rob_next = rob_next, max(rob_next, rob_first + num)
    return rob_next


def sol_td(nums):
    memo = {}

    def dp(i):
        if i < 2:
            return nums[0] if i == 0 else max(nums[0], nums[1])
        if i not in memo:
            memo[i] = max(dp(i - 1), dp(i - 2) + nums[i])
        return memo[i]

    return dp(len(nums) - 1)
