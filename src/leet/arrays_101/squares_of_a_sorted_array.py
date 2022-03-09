"""
Squares of a Sorted Array
-------------------------

Given an integer array nums sorted in non-decreasing order, return an array of the
squares of each number sorted in non-decreasing order.

Complexity
==========

Time
----

sortedSquares(nums): O(n).

Space
-----

sortedSquares(nums): O(n).
"""


def sol(nums):
    i, j, sol = 0, len(nums) - 1, [0] * len(nums)
    k = j
    while k >= 0:
        if abs(nums[i]) > abs(nums[j]):
            i, sol[k] = i + 1, nums[i] ** 2
        else:
            j, sol[k] = j - 1, nums[j] ** 2
        k -= 1
    return sol
