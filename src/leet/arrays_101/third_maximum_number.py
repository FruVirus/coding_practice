"""
Third Maximum Number
--------------------

Given an integer array nums, return the third distinct maximum number in this array. If
the third maximum does not exist, return the maximum number.

Complexity
==========

Time
----

thirdMax(nums): O(n).

Space
-----

thirdMax(nums): O(1).
"""


def sol(nums):
    max_set = set()
    for num in nums:
        max_set.add(num)
        if len(max_set) > 3:
            max_set.remove(min(max_set))
    return min(max_set) if len(max_set) == 3 else max(max_set)
