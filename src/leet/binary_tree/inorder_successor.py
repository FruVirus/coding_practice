"""
Inorder Successor
-----------------

Given the root of a binary tree and a node p in it, return the in-order successor of
that node in the binary tree. If the given node has no in-order successor in the tree,
return null.

The successor of a node p is the node with the smallest key greater than p.val.

Complexity
==========

Time
----

inorderSuccessor(root, p): O(n).

Space
-----

inorderSuccessor(root, p): O(n).
"""


def sol(root, p):
    if p.right:
        leftmost = p.right
        while leftmost.left:
            leftmost = leftmost.left
        return leftmost
    return inorder(root, p)[1]


def inorder(node, p, prev=None, successor=None):
    if node:
        prev, successor = inorder(node.left, p, prev, successor)
        if prev is p and not successor:
            successor = node
        else:
            prev, successor = inorder(node.right, p, node, successor)
    return prev, successor
