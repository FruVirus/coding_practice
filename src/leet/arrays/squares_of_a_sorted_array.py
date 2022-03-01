"""
Squares of a Sorted Array
-------------------------

Given an integer array nums sorted in non-decreasing order, return an array of the
squares of each number sorted in non-decreasing order.

Complexity
==========

Time
----

sorted_squares(): O(n).

Space
-----

sorted_squares(): O(n).
"""


def sorted_squares(nums):
    i, j, sol = 0, len(nums) - 1, [0] * len(nums)
    k = j
    while k >= 0:
        if abs(nums[i]) <= abs(nums[j]):
            j, sol[k] = j - 1, nums[j] ** 2
        else:
            i, sol[k] = i + 1, nums[i] ** 2
        k -= 1
    return sol
