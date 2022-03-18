"""
Contains Duplicate II
---------------------

Given an integer array nums and an integer k, return true if there are two distinct
indices i and j in the array such that nums[i] == nums[j] and abs(i - j) <= k.

Complexity
==========

Time
----

containsNearbyDuplicate(nums, k): O(n).

Space
-----

containsNearbyDuplicate(nums, k): O(min(n, k)).
"""


def sol(nums, k):
    seen = {}
    for i, num in enumerate(nums):
        if num in seen and i - seen[num] <= k:
            return True
        seen[num] = i
    return False
