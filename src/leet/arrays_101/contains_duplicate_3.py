"""
Contains Duplicate III
----------------------

Given an integer array nums and two integers k and t, return true if there are two
distinct indices i and j in the array such that abs(nums[i] - nums[j]) <= t and
abs(i - j) <= k.

Complexity
==========

Time
----

containsNearbyAlmostDuplicate(nums, k, t): O(n).

Space
-----

containsNearbyAlmostDuplicate(nums, k, t): O(min(n, k)).
"""

# pylint: disable=C0200


def sol(nums, k, t):
    b, w = {}, t + 1
    for i in range(len(nums)):
        b_index = nums[i] // w
        if b_index in b:
            return True
        if b_index - 1 in b and abs(nums[i] - b[b_index - 1]) < w:
            return True
        if b_index + 1 in b and abs(nums[i] - b[b_index + 1]) < w:
            return True
        b[b_index] = nums[i]
        if i >= k:
            del b[nums[i - k] // w]
    return False
