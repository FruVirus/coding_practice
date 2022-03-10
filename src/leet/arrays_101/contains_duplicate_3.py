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

containsNearbyAlmostDuplicate(nums, k, t): O().

Space
-----

containsNearbyAlmostDuplicate(nums, k, t): O().
"""

# pylint: disable=C0200


def sol(nums, k, t):
    buckets, w = {}, t + 1
    for i in range(len(nums)):
        j = nums[i] // w
        if j in buckets:
            return True
        if j - 1 in buckets and abs(nums[i] - buckets[j - 1]) < w:
            return True
        if j + 1 in buckets and abs(nums[i] - buckets[j + 1]) < w:
            return True
        buckets[j] = nums[i]
        if i >= k:
            del buckets[nums[i - k] // w]
    return False
