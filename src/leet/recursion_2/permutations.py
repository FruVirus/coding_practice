"""
Permutations
------------

Given an array nums of distinct integers, return all the possible permutations. You can
return the answer in any order.

Complexity
==========

Time
----

permute(nums): O(n!) < O() < O(n * n!).

Space
-----

permute(nums): O(n!).
"""


def sol(nums):
    n, sol = len(nums), []

    def backtrack(first=0):
        if first == n:
            sol.append(nums[:])
        for i in range(first, n):
            nums[first], nums[i] = nums[i], nums[first]
            backtrack(first + 1)
            nums[first], nums[i] = nums[i], nums[first]

    backtrack()
    return sol
