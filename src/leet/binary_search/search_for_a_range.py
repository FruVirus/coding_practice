"""
Search for a Range
------------------

Given an array of integers nums sorted in non-decreasing order, find the starting and
ending position of a given target value.

If target is not found in the array, return [-1, -1].

You must write an algorithm with O(log n) runtime complexity.

Intuition
---------

Instead of using a linear-scan approach to find the boundaries once the target has been
found, let's use two binary searches to find the first and last position of the target.
We can make a small tweak to the checks we perform on the middle element. This tweak
will help us determine the first and the last position of an element.

Normally, we compare nums[mid] == target because we simply need to check if we found our
target or not. But now, apart from checking for equality, we also need to check if mid
is the first or the last index where the target occurs.

There are two situations where an index will be the first occurrence of the target in
the array.

    1. If mid is the same as low which implies our mid element is the first element
in the remaining subarray.

    2. The element to the left of this index is not equal to the target that we are
searching for; i.e. nums[mid - 1] != target. If this condition is not met, we should
keep searching on the left side of the array for the first occurrence of the target.

There are two situations where an index will be the last occurrence of the target in the
array.

    1. If mid is the same as high which implies our mid element is the last element of
the remaining subarray.
    2. If the element to the right of mid is not equal to the target we are searching
for; i.e. nums[mid + 1] != target. If this condition is not met, we should keep
searching on the right side of the array for the last occurrence of the target.

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
    lbound = find_bound(nums, target, True)
    return [-1, -1] if lbound == -1 else [lbound, find_bound(nums, target)]


def find_bound(nums, target, lbound=False):
    low, high = 0, len(nums) - 1
    while low <= high:
        mid = low + (high - low) // 2
        if nums[mid] == target:
            if lbound:
                if mid == low or nums[mid - 1] < target:
                    return mid
                high = mid - 1
            else:
                if mid == high or nums[mid + 1] > target:
                    return mid
                low = mid + 1
        elif nums[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
    return -1
