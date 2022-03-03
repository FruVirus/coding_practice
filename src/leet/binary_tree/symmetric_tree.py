"""
Symmetric Tree
--------------

Given the root of a binary tree, check whether it is a mirror of itself (i.e., symmetric
around its center).

Complexity
==========

Time
----

is_symmetric: O(n).

Space
-----

is_symmetric: O(n).
"""


def is_symmetric(root):
    stack = [(root.right, root.left)]
    while stack:
        left, right = stack.pop()
        if left and right:
            if left.val != right.val:
                return False
            stack.append((left.left, right.right))
            stack.append((left.right, right.left))
        elif (not left and right) or (left and not right):
            return False
    return True
