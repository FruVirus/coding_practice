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

For every call to calculate(nums, i, sum, S), we store the result obtained in
memo[i][sum + total], where total stands for the sum of all the elements from the input
array. The factor of total has been added as an offset to the sum value to map all the
sums possible to positive integer range. By making use of memoization, we can get the
result of each redundant function call in constant time.

Complexity
==========

Time
----

findTargetSumWays_td(nums, target): O(n * t), where n is the length of nums and t refers
to the sum of the nums array.

Space
-----

findTargetSumWays_td(nums, target): O(n * t).
"""


def sol_td(nums, target):
    total = sum(nums)
    memo = [[-float("inf")] * (2 * total + 1) for _ in range(len(nums))]

    def dp(i, sum_):
        if i == len(nums):
            return int(sum_ == target)
        if memo[i][sum_ + total] == -float("inf"):
            add = dp(i + 1, sum_ + nums[i])
            subtract = dp(i + 1, sum_ - nums[i])
            memo[i][sum_ + total] = add + subtract
        return memo[i][sum_ + total]

    return dp(0, 0)
