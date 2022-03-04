"""
Find the Duplicate Number
-------------------------

Given an array of integers nums containing n + 1 integers where each integer is in the
range [1, n] inclusive.

There is only one repeated number in nums, return this repeated number.

You must solve the problem without modifying the array nums and uses only constant extra
space.

Complexity
==========

Time
----

find_duplicate(): O(n * lg n).
find_duplicate_cycle(): O(n).

Space
-----

find_duplicate() and find_duplicate_cycle: O(1).
"""


def find_duplicate(nums):
    low, high = 1, len(nums) - 1
    while low <= high:
        mid = low + (high - low) // 2
        count = sum(num <= mid for num in nums)
        if count > mid:
            duplicate, high = mid, mid - 1
        else:
            low = mid + 1
    return duplicate


def find_duplicate_cycle(nums):
    tortoise = hare = nums[0]
    while True:
        tortoise, hare = nums[tortoise], nums[nums[hare]]
        if tortoise == hare:
            break
    tortoise = nums[0]
    while tortoise != hare:
        tortoise, hare = nums[tortoise], nums[hare]
    return hare
