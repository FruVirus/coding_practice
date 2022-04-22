"""
Permutations
------------

Given an array nums of distinct integers, return all the possible permutations. You can
return the answer in any order.

Intuition
---------

Here is a backtrack function which takes the index of the first integer to consider as
an argument backtrack(first).

    1. If the first integer to consider has index n that means that the current
permutation is done.

    2. Iterate over the integers from index first to index n - 1.
        - Place i-th integer first in the permutation, i.e. swap(nums[first], nums[i]).
        - Proceed to create all permutations which starts from i-th integer:
backtrack(first + 1).
        - Backtrack; i.e. swap(nums[first], nums[i]) back.

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
    sol = []

    def backtrack(first):
        if first == len(nums):
            sol.append(nums[:])
            return
        for i in range(first, len(nums)):
            nums[first], nums[i] = nums[i], nums[first]
            backtrack(first + 1)
            nums[first], nums[i] = nums[i], nums[first]

    backtrack(0)
    return sol
