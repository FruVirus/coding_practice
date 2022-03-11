"""
Validate Binary Search Tree
---------------------------

Given the root of a binary tree, determine if it is a valid binary search tree (BST).

A valid BST is defined as follows:

    The left subtree of a node contains only nodes with keys less than the node's key.
    The right subtree of a node contains only nodes with keys greater than the node's
key.
    Both the left and right subtrees must also be binary search trees.

Complexity
==========

Time
----

isValidBST(root): O(n).

Space
-----

isValidBST(root): O(n).
"""


def sol(root):
    node, prev, stack = root, -float("inf"), []
    while node or stack:
        while node:
            stack.append(node)
            node = node.left
        node = stack.pop()
        if node.val <= prev:
            return False
        prev, node = node.val, node.right
    return True
