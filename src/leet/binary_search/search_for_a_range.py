"""
Search for a Range
------------------

Given an array of integers nums sorted in non-decreasing order, find the starting and
ending position of a given target value.

If target is not found in the array, return [-1, -1].

You must write an algorithm with O(log n) runtime complexity.

Complexity
==========

Time
----

searchRange(nums, target): O(lg n).

Space
-----

searchRange(nums, target): O(1).
"""


def sol(nums, target):
    lower_bound = find_bound(nums, target, True)
    return [-1, -1] if lower_bound == -1 else [lower_bound, find_bound(nums, target)]


def find_bound(nums, target, lower_bound=False):
    low, high = 0, len(nums) - 1
    while low <= high:
        mid = low + (high - low) // 2
        if nums[mid] == target:
            if lower_bound:
                if mid == low or nums[mid - 1] < target:
                    return mid
                high = mid - 1
            else:
                if mid == high or nums[mid + 1] > target:
                    return mid
                low = mid + 1
        elif nums[mid] > target:
            high = mid - 1
        else:
            low = mid + 1
    return -1
