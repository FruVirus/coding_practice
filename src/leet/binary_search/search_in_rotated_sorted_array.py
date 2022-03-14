"""
Search in Rotated Sorted Array
------------------------------

There is an integer array nums sorted in ascending order (with distinct values).

Prior to being passed to your function, nums is possibly rotated at an unknown pivot
index k (1 <= k < nums.length) such that the resulting array is
[nums[k], nums[k+1], ..., nums[n-1], nums[0], nums[1], ..., nums[k-1]] (0-indexed). For
example, [0,1,2,4,5,6,7] might be rotated at pivot index 3 and become [4,5,6,7,0,1,2].

Given the array nums after the possible rotation and an integer target, return the index
of target if it is in nums, or -1 if it is not in nums.

You must write an algorithm with O(log n) runtime complexity.

Intuition
---------

The idea is that we add some additional condition checks in the normal binary search in
order to better narrow down the scope of the search.

If nums[mid] == target, then the job is done and we return mid.

Otherwise, there can be two situations:

    1. Mid element is larger than the first element in the array, i.e. the subarray from
the first element to the mid element is non-rotated. If the target is located in the
non-rotated subarray, then we decrease high. Otherwise, we increase low.

    2. Mid element is smaller than the first element of the array, i.e. the rotation
index is somewhere between 0 and mid. It implies that the sub-array from the mid element
to the last one is non-rotated. If the target is located in the non-rotated subarray,
then we increase low. Otherwise, we decrease high.

Complexity
==========

Time
----

search(nums, target): O(lg n).

Space
-----

search(nums, target): O(1).
"""


def sol(nums, target):
    low, high = 0, len(nums) - 1
    while low <= high:
        mid = low + (high - low) // 2
        if nums[mid] == target:
            return mid
        if nums[mid] >= nums[low]:
            if nums[low] <= target < nums[mid]:
                high = mid - 1
            else:
                low = mid + 1
        elif nums[mid] < target <= nums[high]:
            low = mid + 1
        else:
            high = mid - 1
    return -1
