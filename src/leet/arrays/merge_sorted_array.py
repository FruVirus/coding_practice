"""
Merge Sorted Array
------------------

You are given two integer arrays nums1 and nums2, sorted in non-decreasing order, and
two integers m and n, representing the number of elements in nums1 and nums2
respectively.

Merge nums1 and nums2 into a single array sorted in non-decreasing order.

The final sorted array should not be returned by the function, but instead be stored
inside the array nums1. To accommodate this, nums1 has a length of m + n, where the
first m elements denote the elements that should be merged, and the last n elements are
set to 0 and should be ignored. nums2 has a length of n.

Complexity
==========

Time
----

merge(): O(n + m).

Space
-----

merge(): O(1).
"""


def merge(nums1, m, nums2, n):
    i, j, k = m - 1, n - 1, m + n - 1
    while j >= 0:
        if i >= 0 and nums1[i] > nums2[j]:
            i, nums1[k] = i - 1, nums1[i]
        else:
            j, nums1[k] = j - 1, nums2[j]
        k -= 1
