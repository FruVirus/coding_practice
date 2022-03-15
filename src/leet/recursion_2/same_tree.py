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
    stack = [(p, q)]
    while stack:
        p, q = stack.pop()
        if p and q and p.val == q.val:
            stack.append((p.left, q.left))
            stack.append((p.right, q.right))
        elif p or q:
            return False
    return True
