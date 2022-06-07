"""
Missing Number
--------------

Given an array nums containing n distinct numbers in the range [0, n], return the only
number in the range that is missing from the array.

Note that you can also use Gauss' formula:

Expected sum = len(nums) * (len(nums) + 1) // 2 - sum(nums)

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
    actual_sum, expected_sum = sum(nums), sum(i for i in range(1, len(nums) + 1))
    return expected_sum - actual_sum
