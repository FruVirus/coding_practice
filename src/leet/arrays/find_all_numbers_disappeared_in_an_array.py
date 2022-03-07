"""
Find All Numbers Disappeared in an Array
----------------------------------------

Given an array nums of n integers where nums[i] is in the range [1, n], return an array
of all the integers in the range [1, n] that do not appear in nums.

Complexity
==========

Time
----

findDisappearedNumbers(nums): O(n).

Space
-----

findDisappearedNumbers(nums): O(1).
"""


def sol(nums):
    n = [0] * len(nums)
    for num in nums:
        n[num - 1] = num
    return [i for i, x in enumerate(n, 1) if x == 0]
