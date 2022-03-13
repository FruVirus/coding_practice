"""
Median of Two Sorted Arrays
---------------------------

Given two sorted arrays nums1 and nums2 of size m and n respectively, return the median
of the two sorted arrays.

The overall run time complexity should be O(log (m + n)).

Intuition
---------

A = [1, 2, 3, 4, 5]
B = [1, 2, 3, 4, 5, 6, 7, 8]

total = 13
half = 6

We only need to run binary search on the smaller of the two arrays---A in this example.
The midpoint of A is 3. Knowing the midpoint of A and half, we can determine the size
of the subarray in B to consider; thus, we don't have to run binary search on B.

The left half of A is: [1, 2, 3].
The left half of B is: [1, 2, 3].

The right half of A is: [4, 5].
The right half of B is: [4, 5, 6, 7, 8].

We want to ensure that the rightmost number in both of the left partitions are less than
or equal to all the numbers in both of the right partitions.

We already know that the rightmost number in the left partition of A (i.e., 3) is less
than or equal to all the numbers in the right partition of A since A is sorted. A
similar reasoning applies to B.

However, we need to check if the rightmost number in the left partition of A is less
than or equal to all the numbers in the right partition of B and vice versa. If both of
these conditions are satisfied, then we have done the overall partition correctly. That
is, if we were to merge both of the left partitions together in sorted order, we would
have the lower half of the overall merged array in sorted order.

If we have done the overall partition correctly, then the median is the minimum of the
leftmost numbers in the right partitions of A and B if total is odd. Otherwise, the
median is the average of the max number in the left partitions and the min number in
the right partitions.

If we have NOT done the overall partition correctly, then low or high is updated for A.
If a_left < b_right, this means that we need to decrease the subarray in B by 1 and
increase the subarray in A by 1. We do this by increasing low since increasing low
increases a_left and a_right while also decreasing b_left and b_right at the same time
(since b_mid is calculated from a_mid and a_mid is calculated from low and high). Vice
versa applies if a_left > b_right.

Complexity
==========

Time
----

findMedianSortedArrays(a, b): O(lg(min(m, n))).

Space
-----

findMedianSortedArrays(a, b): O(1).
"""


def sol(a, b):
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
        if a_left < b_right:
            low = a_mid + 1
        else:
            high = a_mid - 1
