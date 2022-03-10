"""
Balanced Binary Tree
--------------------

Given a binary tree, determine if it is height-balanced.

Complexity
==========

Time
----

isBalanced(root): O(n).

Space
-----

isBalanced(root): O(n).
"""


def sol(root):
    def helper(root):
        if not root:
            return True, -1
        left_balanced, left_height = helper(root.left)
        if not left_balanced:
            return False, 0
        right_balanced, right_height = helper(root.right)
        if not right_balanced:
            return False, 0
        return abs(left_height - right_height) < 2, 1 + max(left_height, right_height)

    return helper(root)[0]
