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

findDuplicate(nums): O(n * lg n).
findDuplicate_cycle(nums): O(n).

Space
-----

findDuplicate(nums) and findDuplicate_cycle(nums): O(1).
"""


def sol(nums):
    low, high = 1, len(nums) - 1
    while low <= high:
        mid = low + (high - low) // 2
        count = sum(num <= mid for num in nums)
        if count > mid:
            duplicate, high = mid, mid - 1
        else:
            low = mid + 1
    return duplicate


def sol_cycle(nums):
    tortoise = hare = nums[0]
    while True:
        tortoise, hare = nums[tortoise], nums[nums[hare]]
        if tortoise == hare:
            break
    tortoise = nums[0]
    while tortoise != hare:
        tortoise, hare = nums[tortoise], nums[hare]
    return hare
