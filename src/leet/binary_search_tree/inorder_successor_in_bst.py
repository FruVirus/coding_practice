"""
Inorder Successor in BST
------------------------

Given the root of a binary search tree and a node p in it, return the in-order successor
of that node in the BST. If the given node has no in-order successor in the tree, return
null.

The successor of a node p is the node with the smallest key greater than p.val.

Complexity
==========

Time
----

inorderSuccessor(root, p): O(n).

Space
-----

inorderSuccessor(root, p): O(1).
"""


def sol(root, p):
    successor = None
    while root:
        if p.val >= root.val:
            root = root.right
        else:
            successor = root
            root = root.left
    return successor
