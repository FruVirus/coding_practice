"""
Squares of a Sorted Array
-------------------------

Given an integer array nums sorted in non-decreasing order, return an array of the
squares of each number sorted in non-decreasing order.

Complexity
==========

Time
----

SortedSquares: O(n).

Space
-----

SortedSquares: O(n).
"""

# pylint: disable=R0201


class SortedSquares:
    def sorted_squares(self, nums):
        i, j, sol = 0, len(nums) - 1, [0] * len(nums)
        for index in reversed(range(len(nums))):
            if abs(nums[i]) <= abs(nums[j]):
                j, sol[index] = j - 1, nums[j] ** 2
            else:
                i, sol[index] = i + 1, nums[i] ** 2
        return sol
