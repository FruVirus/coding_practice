"""
Missing Number
--------------

Given an array nums containing n distinct numbers in the range [0, n], return the only
number in the range that is missing from the array.

Complexity
==========

Time
----

missingNumber(nums): O(m + n).

Space
-----

missingNumber(nums): O(1).
"""


def sol(nums):
    return len(nums) * (len(nums) + 1) // 2 - sum(nums)
