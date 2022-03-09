"""
Two Sum II - Input array is sorted
----------------------------------

Given a 1-indexed array of integers numbers that is already sorted in non-decreasing
order, find two numbers such that they add up to a specific target number. Let these two
numbers be numbers[index1] and numbers[index2] where
1 <= index1 < index2 <= numbers.length.

Return the indices of the two numbers, index1 and index2, added by one as an integer
array [index1, index2] of length 2.

The tests are generated such that there is exactly one solution. You may not use the
same element twice.

Your solution must use only constant extra space.

Complexity
==========

Time
----

two_sum(nums, target): O(n).

Space
-----

two_sum(nums, target): O(1).
"""


def two_sum(nums, target):
    low, high = 0, len(nums) - 1
    while low < high:
        num = nums[low] + nums[high]
        if num == target:
            return [low + 1, high + 1]
        if num < target:
            low += 1
        else:
            high -= 1
    return [-1, -1]
