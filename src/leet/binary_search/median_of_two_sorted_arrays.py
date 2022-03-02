"""
Median of Two Sorted Arrays
---------------------------

Given two sorted arrays nums1 and nums2 of size m and n respectively, return the median
of the two sorted arrays.

The overall run time complexity should be O(log (m + n)).

Complexity
==========

Time
----

find_median_sorted_arrays(): O(lg(min(m, n))).

Space
-----

find_median_sorted_arrays(): O(1).
"""


def find_median_sorted_arrays(nums1, nums2):
    a, b = nums1, nums2
    if len(a) > len(b):
        a, b = b, a
    m, n = len(a), len(b)
    low, high, total = 0, m - 1, m + n
    half = total // 2
    while True:
        a_mid = low + (high - low) // 2
        b_mid = half - a_mid - 2
        a_left = a[a_mid] if a_mid >= 0 else -float("inf")
        a_right = a[a_mid + 1] if a_mid + 1 < m else float("inf")
        b_left = b[b_mid] if b_mid >= 0 else -float("inf")
        b_right = b[b_mid + 1] if b_mid + 1 < n else float("inf")
        if a_left <= b_right and b_left <= a_right:
            if total % 2 == 1:
                return min(a_right, b_right)
            return (max(a_left, b_left) + min(a_right, b_right)) / 2
        if a_left > b_right:
            high = a_mid - 1
        else:
            low = a_mid + 1
