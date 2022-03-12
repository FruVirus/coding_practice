"""
Symmetric Tree
--------------

Given the root of a binary tree, check whether it is a mirror of itself (i.e., symmetric
around its center).

Complexity
==========

Time
----

isSymmetric(root): O(n).

Space
-----

isSymmetric(root): O(n).
"""


def sol(root):
    stack = [(root.left, root.right)]
    while stack:
        left, right = stack.pop()
        if left and right:
            if left.val != right.val:
                return False
            stack.append((left.left, right.right))
            stack.append((left.right, right.left))
        elif left or right:
            return False
    return True
