"""
Array Partition I
-----------------

Given an integer array nums of 2n integers, group these integers into n pairs (a1, b1),
(a2, b2), ..., (an, bn) such that the sum of min(ai, bi) for all i is maximized. Return
the maximized sum.

Complexity
==========

Time
----

arrayPairSum(nums): O(n * lg n).

Space
-----

arrayPairSum(nums): O(1).
"""


def sol(nums):
    nums.sort()
    return sum(nums[::2])
