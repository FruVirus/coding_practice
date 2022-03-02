"""
Intersection of Two Arrays II
-----------------------------

Given two integer arrays nums1 and nums2, return an array of their intersection. Each
element in the result must appear as many times as it shows in both arrays and you may
return the result in any order.

Complexity
==========

Time
----

intersect(): O(n + m).

Space
-----

intersect(): O(min(n, m)).
"""

# Standard Library
from collections import Counter


def intersect(nums1, nums2):
    if len(nums1) > len(nums2):
        nums1, nums2 = nums2, nums1
    count, k = Counter(nums1), 0
    for num in nums2:
        if count.get(num, 0) > 0:
            nums1[k] = num
            k += 1
            count[num] -= 1
    return nums1[:k]
