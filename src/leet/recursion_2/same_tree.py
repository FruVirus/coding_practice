"""
Same Tree
---------

Given two integers n and k, return all possible combinations of k numbers out of the
range [1, n].

You may return the answer in any order.

Complexity
==========

Time
----

isSameTree(p, q): O(n).

Space
-----

isSameTree(p, q): O(n).
"""


def sol(p, q):
    if not (p or q):
        return True
    if not (p and q) or p.val != q.val:
        return False
    return sol(p.right, q.right) and sol(p.left, q.left)
