"""
Find Peak Element
-----------------

A peak element is an element that is strictly greater than its neighbors.

Given an integer array nums, find a peak element, and return its index. If the array
contains multiple peaks, return the index to any of the peaks.

You may imagine that nums[-1] = nums[n] = -∞.

You must write an algorithm that runs in O(log n) time.

Intuition
---------

We start off by finding the mid element from the given nums array. If this element
happens to be lying in a descending sequence of numbers (i.e.,
nums[mid] > nums[mid + 1]), it means that the peak will always lie towards the left of
this element. Thus, we reduce the search space to the right of mid and perform the same
process on the right subarray.

In this way, we keep on reducing hte search space until we eventually reach a state
where only one element is remaining in the search space. This single element is the peak
element.

Complexity
==========

Time
----

findPeakElement(nums): O(lg n).

Space
-----

findPeakElement(nums): O(1).
"""


def sol(nums):
    low, high = 0, len(nums) - 1
    while low < high:
        mid = low + (high - low) // 2
        if nums[mid] < nums[mid + 1]:
            low = mid + 1
        else:
            high = mid
    return low
