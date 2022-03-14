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

Intuition
---------

Since the input array is sorted, we can use two indices, initially pointing to the first
and the last element, respectively. Compare the sum of these two elements with target.
If the sum is equal to target, we found the exactly only solution. If it is less than
target, we increase the smaller index by one. If it is greater than target, we decrease
the larger index by one. Repeat the comparison until the solution is found.

Complexity
==========

Time
----

twoSum(nums, target): O(n).

Space
-----

twoSum(nums, target): O(1).
"""


def sol(nums, target):
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
