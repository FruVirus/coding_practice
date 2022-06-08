"""
Subtree of Another Tree
-----------------------

Given the roots of two binary trees root and subRoot, return true if there is a subtree
of root with the same structure and node values of subRoot and false otherwise.

A subtree of a binary tree is a tree that consists of a node in tree and all of this
node's descendants. The tree could also be considered as a subtree of itself.

Complexity
==========

Time
----

isSubtree(root, sub_root) O(n).

Space
-----

isSubtree(root, sub_root): O(1).
"""


def sol(root, sub_root):
    if not (root and sub_root):
        return False

    def helper(left, right):
        if not left:
            return right is None
        if not right:
            return left is None
        if left.val != right.val:
            return False
        return helper(left.left, right.left) and helper(left.right, right.right)

    if helper(root, sub_root):
        return True
    return sol(root.left, sub_root) or sol(root.right, sub_root)
