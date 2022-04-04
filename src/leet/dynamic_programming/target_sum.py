"""
Target Sum
----------

You are given an integer array nums and an integer target.

You want to build an expression out of nums by adding one of the symbols '+' and '-'
before each integer in nums and then concatenate all the integers.

    - For example, if nums = [2, 1], you can add a '+' before 2 and a '-' before 1 and
concatenate them to build the expression "+2-1".

Return the number of different expressions that you can build, which evaluates to
target.

Intuition
---------

The brute force approach is based on recursion. We need to try to put both the + and -
symbols at every location in the given nums array and find out the assignments which
lead to the required result S.

For this, we make use of a recursive function calculate(nums, i, sum, S), which returns
the assignments leading to the sum S, starting from the i-th index onwards, provided the
sum of elements up to the i-th element is sum. This function appends a + sign and a -
sign both to the element at the current index and calls itself with the updated sum as
sum + nums[i] and sum - nums[i] respectively along with the updated current index as
i + 1. Whenever we reach the end of the array, we compare the sum obtained with S. If
they are equal, we increment the count value to be returned.

Complexity
==========

Time
----

findTargetSumWays(nums, target): O(n * t), where n is the length of nums and t refers to
the sum of the nums array.

Space
-----

findTargetSumWays_bu(nums, target): O(t).
findTargetSumWays_td(nums, target): O(n * t).
"""


def sol_bu(nums, target):
    sum_ = sum(nums)
    dp = [0] * (2 * sum_ + 1)
    dp[nums[0] + sum_] = 1
    dp[-nums[0] + sum_] += 1
    for i in range(1, len(nums)):
        curr = [0] * (2 * sum_ + 1)
        for j in range(-sum_, sum_ + 1):
            if dp[j + sum_] > 0:
                curr[j + sum_ + nums[i]] += dp[j + sum_]
                curr[j + sum_ - nums[i]] += dp[j + sum_]
        dp = curr
    return 0 if abs(target) > sum_ else dp[target + sum_]


def sol_td(nums, target):
    memo = {}

    def dp(i, sum_):
        if i == len(nums):
            return 1 if sum_ == target else 0
        if (i, sum_) not in memo:
            add = dp(i + 1, sum_ + nums[i])
            sub = dp(i + 1, sum_ - nums[i])
            memo[(i, sum_)] = add + sub
        return memo[(i, sum_)]

    return dp(0, 0)
