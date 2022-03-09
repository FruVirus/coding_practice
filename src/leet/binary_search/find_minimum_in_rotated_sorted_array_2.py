"""
Find Minimum in Rotated Sorted Array II
---------------------------------------

Suppose an array of length n sorted in ascending order is rotated between 1 and n times.
For example, the array nums = [0,1,4,4,5,6,7] might become:

    [4,5,6,7,0,1,4] if it was rotated 4 times.
    [0,1,4,4,5,6,7] if it was rotated 7 times.

Notice that rotating an array [a[0], a[1], a[2], ..., a[n-1]] 1 time results in the
array [a[n-1], a[0], a[1], a[2], ..., a[n-2]].

Given the sorted rotated array nums that may contain duplicates, return the minimum
element of this array.

You must decrease the overall operation steps as much as possible.

Complexity
==========

Time
----

findMin(nums): O(lg n)/O(n) expected/worse case. Worst case occurs when the array
contains all identical elements.

Space
-----

findMin(nums): O(1).
"""


def sol(nums):
    low, high = 0, len(nums) - 1
    while low < high:
        mid = low + (high - low) // 2
        if nums[low] == nums[mid] == nums[high]:
            low += 1
            high -= 1
        elif nums[mid] <= nums[high]:
            high = mid
        else:
            low = mid + 1
    return nums[low]
