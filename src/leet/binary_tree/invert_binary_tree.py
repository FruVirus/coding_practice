"""
Invert Binary Tree
------------------

Given the root of a binary tree, invert the tree, and return its root.

Complexity
==========

Time
----

invertTree(root): O(n).

Space
-----

invertTree(root): O(n).
"""


def sol(root):
    if not root:
        return None
    stack = [root]
    while stack:
        node = stack.pop()
        node.left, node.right = node.right, node.left
        if node.left:
            stack.append(node.left)
        if node.right:
            stack.append(node.right)
    return root
