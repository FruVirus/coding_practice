"""
Subsets
-------

Given an integer array nums of unique elements, return all possible subsets (the power
set).

The solution set must not contain duplicate subsets. Return the solution in any order.

Intuition
---------

Power set is all possible combinations of all possible lengths, from 0 to n.

Given the definition, the problem can also be interpreted as finding the power set from
a sequence.

So, this time let us loop over the length of combination, rather than the candidate
numbers, and generate all combinations for a given length with the help of backtracking
technique.

Complexity
==========

Time
----

subsets(nums) O(n * 2 ^ n).

Space
-----

subsets(nums): O(n).
"""


def sol(nums):
    sol = []

    def backtrack(first, curr):
        if len(curr) == k:
            sol.append(curr[:])
            return
        for i in range(first, len(nums)):
            curr.append(nums[i])
            backtrack(i + 1, curr)
            curr.pop()

    for k in range(len(nums) + 1):
        backtrack(0, [])
    return sol
