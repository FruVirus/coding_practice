"""
Minimum Size Subarray Sum
-------------------------

Given an array of positive integers nums and a positive integer target, return the
minimal length of a contiguous subarray [numsl, numsl+1, ..., numsr-1, numsr] of which
the sum is greater than or equal to target. If there is no such subarray, return 0
instead.

Complexity
==========

Time
----

minSubArrayLen(nums, target): O(n).

Space
-----

minSubArrayLen(nums, target): O(1).
"""


def sol(nums, target):
    min_len, left, sum_ = float("inf"), 0, 0
    for i, num in enumerate(nums):
        sum_ += num
        while sum_ >= target:
            min_len = min(min_len, i + 1 - left)
            sum_ -= nums[left]
            left += 1
    return 0 if min_len == float("inf") else min_len
