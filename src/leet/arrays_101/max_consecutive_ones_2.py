"""
Max Consecutive Ones II
-----------------------

Given a binary array nums, return the maximum number of consecutive 1's in the array if
you can flip at most one 0.

Complexity
==========

Time
----

findMaxConsecutiveOnes(nums): O(n).

Space
-----

findMaxConsecutiveOnes(nums): O(1).
"""

# pylint: disable=C0200


def sol(nums):
    last_zero, longest_ones, num_ones = -1, 0, 0
    for i in range(len(nums)):
        if nums[i] == 0:
            num_ones, last_zero = i - last_zero, i
        else:
            num_ones += 1
        longest_ones = max(longest_ones, num_ones)
    return longest_ones
