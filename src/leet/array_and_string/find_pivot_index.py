"""
Find Pivot Index
----------------

Given an array of integers nums, calculate the pivot index of this array.

The pivot index is the index where the sum of all the numbers strictly to the left of
the index is equal to the sum of all the numbers strictly to the index's right.

If the index is on the left edge of the array, then the left sum is 0 because there are
no elements to the left. This also applies to the right edge of the array.

Return the leftmost pivot index. If no such index exists, return -1.

Complexity
==========

Time
----

pivotIndex(nums): O(n).

Space
-----

pivotIndex(nums): O(1).
"""


def sol(nums):
    sum_, left_sum = sum(nums), 0
    for i, num in enumerate(nums):
        if left_sum == (sum_ - left_sum - num):
            return i
        left_sum += num
    return -1
