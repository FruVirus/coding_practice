"""
Sort Array By Parity
--------------------

Given an integer array nums, move all the even integers at the beginning of the array
followed by all the odd integers.

Return any array that satisfies this condition.

Complexity
==========

Time
----

sortArrayByParity(nums): O(n).

Space
-----

sortArrayByParity(nums): O(1).
"""


def sol(nums):
    i, j = 0, len(nums) - 1
    while i != j:
        if nums[i] % 2 != 0:
            nums[i], nums[j] = nums[j], nums[i]
            j -= 1
        else:
            i += 1
    return nums
