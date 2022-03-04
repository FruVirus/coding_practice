"""
Intersection of Two Arrays
--------------------------

Given two integer arrays nums1 and nums2, return an array of their intersection. Each
element in the result must be unique and you may return the result in any order.

Intersection of Two Arrays II
-----------------------------

Given two integer arrays nums1 and nums2, return an array of their intersection. Each
element in the result must appear as many times as it shows in both arrays and you may
return the result in any order.

Complexity
==========

Time
----

intersect(): O(n * lg n).
intersect_two(): O(n + m).

Space
-----

intersect(): O(1).
intersect_two(): O(min(n, m)).
"""

# Standard Library
from collections import Counter


def intersect(nums1, nums2):
    nums1.sort()
    nums2.sort()
    sol = set()
    i = j = 0
    while i < len(nums1) and j < len(nums2):
        if nums1[i] == nums2[j]:
            sol.add(nums1[i])
            i += 1
            j += 1
        elif nums1[i] < nums2[j]:
            i += 1
        else:
            j += 1
    return sol


def intersect_two(nums1, nums2):
    if len(nums1) > len(nums2):
        nums1, nums2 = nums2, nums1
    count, k = Counter(nums1), 0
    for num in nums2:
        if count.get(num, 0) > 0:
            nums1[k] = num
            k += 1
            count[num] -= 1
    return nums1[:k]
