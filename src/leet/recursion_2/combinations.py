"""
Combinations
------------

Given two integers n and k, return all possible combinations of k numbers out of the
range [1, n].

You may return the answer in any order.

Intuition
---------

Here is a backtrack function which takes a first integer to add and a current
combination as arguments backtrack(first, curr).

    1. If the current combination is done - add it to output.

    2. Iterate over the integers from first to n.
        - Add integer i into the current combination curr.
        - Proceed to add more integers into the combination : backtrack(i + 1, curr).
        - Backtrack by removing i from curr.

Complexity
==========

Time
----

combine(n, k): O(k * nCk).

Space
-----

combine(n, k): O(nCk).
"""


def sol(n, k):
    sol = []

    def backtrack(first, curr):
        if len(curr) == k:
            sol.append(curr[:])
            return
        if k - len(curr) > n - first + 1:
            return
        for i in range(first, n + 1):
            curr.append(i)
            backtrack(i + 1, curr)
            curr.pop()

    backtrack(1, [])
    return sol
