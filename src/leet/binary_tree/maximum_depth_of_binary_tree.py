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
        root, curr_depth = stack.pop()
        if root:
            depth = max(depth, curr_depth)
            stack.append((root.left, curr_depth + 1))
            stack.append((root.right, curr_depth + 1))
    return depth
