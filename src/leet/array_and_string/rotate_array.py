"""
Rotate Array
------------

Given an array, rotate the array to the right by k steps, where k is non-negative.

Complexity
==========

Time
----

rotate(nums, k): O(n).

Space
-----

rotate(nums, k): O(1).
"""


def sol(nums, k):
    n = len(nums)
    k %= n
    reverse(nums, 0, n - 1)
    reverse(nums, 0, k - 1)
    reverse(nums, k, n - 1)


def reverse(nums, start, end):
    while start < end:
        nums[start], nums[end] = nums[end], nums[start]
        start, end = start + 1, end - 1
