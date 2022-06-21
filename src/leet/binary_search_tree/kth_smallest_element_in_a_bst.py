"""
Kth Smallest Element in a BST
-----------------------------

Given the root of a binary search tree, and an integer k, return the kth smallest value
(1-indexed) of all the values of the nodes in the tree.

Complexity
==========

Time
----

kthSmallest(root, k): O(H + k), where H is the height of the tree.

Space
-----

kthSmallest(root, k): O(H).
"""


def sol(root, k):
    node, stack = root, []
    while node or stack:
        while node:
            stack.append(node)
            node = node.left
        node = stack.pop()
        k -= 1
        if k == 0:
            return node.val
        node = node.right
