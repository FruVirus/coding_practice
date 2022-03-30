"""
Maximum Depth of N-ary Tree
---------------------------

Given a n-ary tree, find its maximum depth.

The maximum depth is the number of nodes along the longest path from the root node down
to the farthest leaf node.

Complexity
==========

Time
----

maxDepth(root): O(n).

Space
-----

maxDepth(root): O(n) or O(lg n) if the tree is balanced.
"""


def sol(root):
    depth, stack = 0, [(root, 1)]
    while stack:
        node, curr_depth = stack.pop()
        if node:
            depth = max(depth, curr_depth)
            for child in node.children:
                stack.append((child, curr_depth + 1))
    return depth
