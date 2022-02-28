"""
Third Maximum Number
--------------------

Given an integer array nums, return the third distinct maximum number in this array. If
the third maximum does not exist, return the maximum number.

Complexity
==========

Time
----

third_max(): O(n).

Space
-----

third_max(): O(1).
"""


def third_max(nums):
    max_set = set()
    for i in nums:
        max_set.add(i)
        if len(max_set) == 3:
            max_set.remove(min(max_set))
    return min(max_set) if len(max_set) == 3 else max(max_set)
