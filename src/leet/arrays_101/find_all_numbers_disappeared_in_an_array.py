"""
Find All Numbers Disappeared in an Array
----------------------------------------

Given an array nums of n integers where nums[i] is in the range [1, n], return an array
of all the integers in the range [1, n] that do not appear in nums.

Intuition
---------

We will be negating the numbers seen in the array and use the sign of each of the
numbers for finding our missing numbers. We will be treating numbers in the array as
indices and mark corresponding locations in the array as negative.

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
    for num in nums:
        new_index = abs(num) - 1
        if nums[new_index] > 0:
            nums[new_index] *= -1
    return [i for i in range(1, len(nums) + 1) if nums[i - 1] > 0]
