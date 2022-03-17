"""
Two Sum
-------

Given an array of integers nums and an integer target, return indices of the two numbers
such that they add up to target.

You may assume that each input would have exactly one solution, and you may not use the
same element twice.

You can return the answer in any order.

Complexity
==========

Time
----

twoSum(nums, target): O(n).

Space
-----

twoSum(nums, target): O(n).
"""


def sol(nums, target):
    com = {}
    for i, num in enumerate(nums):
        if target - num in com:
            return [com[target - num], i]
        com[num] = i
    return [-1, -1]
