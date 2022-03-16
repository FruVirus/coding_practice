"""
Combinations
------------

Given two integers n and k, return all possible combinations of k numbers out of the
range [1, n].

You may return the answer in any order.

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
    sol, curr = [], []

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

    backtrack(1, curr)
    return sol
