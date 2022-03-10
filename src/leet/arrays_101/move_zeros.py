"""
Move Zeroes
-----------

Given an integer array nums, move all 0's to the end of it while maintaining the
relative order of the non-zero elements.

Note that you must do this in-place without making a copy of the array.

Complexity
==========

Time
----

moveZeroes(nums): O(n).

Space
-----

moveZeroes(nums): O(1).
"""


# pylint: disable = C0200


def sol(nums):
    last_non_zero = 0
    for i in range(len(nums)):
        if nums[i] != 0:
            nums[last_non_zero] = nums[i]
            last_non_zero += 1
    for i in range(last_non_zero, len(nums)):
        nums[i] = 0
