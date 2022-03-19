"""
Same Tree
---------

Given the roots of two binary trees p and q, write a function to check if they are the
same or not.

Two binary trees are considered the same if they are structurally identical, and the
nodes have the same value.

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
    return sol(p.left, q.left) and sol(p.right, q.right)
