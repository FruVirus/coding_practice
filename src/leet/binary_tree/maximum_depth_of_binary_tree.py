"""
Maximum Depth of Binary Tree
----------------------------

Given the root of a binary tree, return its maximum depth.

A binary tree's maximum depth is the number of nodes along the longest path from the
root node down to the farthest leaf node.

Complexity
==========

Time
----

max_depth: O(n).

Space
-----

max_depth: O(n) or O(lg n) if the tree is balanced.
"""


def max_depth(root):
    if not root:
        return 0
    depth, stack = 0, [(root, 1)]
    while stack:
        node, curr_depth = stack.pop()
        if node:
            depth = max(depth, curr_depth)
            stack.append((node.left, curr_depth + 1))
            stack.append((node.right, curr_depth + 1))
    return depth
