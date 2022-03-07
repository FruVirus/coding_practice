"""
Construct Binary Tree from Inorder and Postorder Traversal
----------------------------------------------------------

Given two integer arrays inorder and postorder where inorder is the inorder traversal of
a binary tree and postorder is the postorder traversal of the same tree, construct and
return the binary tree.

Construct Binary Tree from Preorder and Inorder Traversal
---------------------------------------------------------

Given two integer arrays preorder and inorder where preorder is the preorder traversal
of a binary tree and inorder is the inorder traversal of the same tree, construct and
return the binary tree.

Complexity
==========

Time
----

buildTree() and buildTree(): O(n).

Space
-----

buildTree() and buildTree(): O(n).
"""


class Node:
    def __init__(self, val=0, left=None, right=None):
        self.left, self.right, self.val = left, right, val


def sol_postorder(inorder, postorder):
    def helper(in_left, in_right):
        if in_left <= in_right:
            val = postorder.pop()
            root, index = Node(val), idx_map[val]
            root.right = helper(index + 1, in_right)
            root.left = helper(in_left, index - 1)
            return root
        return None

    idx_map = {val: idx for idx, val in enumerate(inorder)}
    return helper(0, len(inorder) - 1)


def sol_preorder(inorder, preorder):
    def helper(in_left, in_right):
        if in_left <= in_right:
            val = preorder.pop(0)
            root, index = Node(val), idx_map[val]
            root.left = helper(in_left, index - 1)
            root.right = helper(index + 1, in_right)
            return root
        return None

    idx_map = {val: idx for idx, val in enumerate(inorder)}
    return helper(0, len(inorder) - 1)
