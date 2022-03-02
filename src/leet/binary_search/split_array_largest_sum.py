"""
Split Array Largest Sum
-----------------------

Given an array nums which consists of non-negative integers and an integer m, you can
split the array into m non-empty continuous subarrays.

Write an algorithm to minimize the largest sum among these m subarrays.

Complexity
==========

Time
----

split_array: O(n * lg(s)), where n is the length of nums and s is the sum of integers in
the nums.

Space
-----

split_array: O(1).
"""


def split_array(nums, m):
    def min_subarrays_required(max_sum_allowed):
        current_sum = splits_required = 0
        for num in nums:
            if current_sum + num <= max_sum_allowed:
                current_sum += num
            else:
                current_sum = num
                splits_required += 1
        return splits_required + 1

    low, high, min_sum = max(nums), sum(nums), None
    while low <= high:
        mid = low + (high - low) // 2
        if min_subarrays_required(mid) <= m:
            high = mid - 1
            min_sum = mid
        else:
            low = mid + 1
    return min_sum
