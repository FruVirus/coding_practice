"""
3Sum Closest
------------

Given an integer array nums of length n and an integer target, find three integers in
nums such that the sum is closest to target.

Return the sum of the three integers.

You may assume that each input would have exactly one solution.

Intuition
---------

The two pointers pattern requires the array to be sorted, so we do that first. In the
sorted array, we process each value from left to right. For value v, we need to find a
pair which sum, ideally, is equal to target - v. We will follow the same two pointers
approach as for 3Sum, however, since this 'ideal' pair may not exist, we will track the
smallest absolute difference between the sum and the target. The two pointers approach
naturally enumerates pairs so that the sum moves toward the target.

1. At each step of the for loop, we pick a current number from nums. The while loop then
does binary search and tries out various sums of two numbers.

2. Each combination sum of two numbers will have some difference between its sum and
target. And we keep track of the smallest difference.

3. If diff == 0, then the sum of the three integers is just target.

Complexity
==========

Time
----

threeSumClosest(nums, target): O(n^2).

Space
-----

threeSumClosest(nums, target): O(log n) or O(n), depending on the sorting algorithm.
"""


def sol(nums, target):
    nums.sort()
    diff = float("inf")
    for i in range(len(nums)):
        low, high = i + 1, len(nums) - 1
        while low < high:
            sum_ = nums[i] + nums[low] + nums[high]
            if abs(target - sum_) < abs(diff):
                diff = target - sum_
            if sum_ < target:
                low += 1
            else:
                high -= 1
        if diff == 0:
            break
    return target - diff
