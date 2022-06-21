"""
Binary Tree Right Side View
---------------------------

Given the root of a binary tree, imagine yourself standing on the right side of it,
return the values of the nodes you can see ordered from top to bottom.

Complexity
==========

Time
----

rightSideView(root): O(n).

Space
-----

rightSideView(root): O(d), where d is the tree diameter. For the last tree level, it
could contain up to n / 2 nodes in the case of a complete binary tree.
"""

# Standard Library
from collections import deque


def sol(root):
    sol = []
    if not root:
        return sol
    queue = deque([root])
    while queue:
        for _ in range(len(queue)):
            node = queue.popleft()
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        sol.append(node.val)
    return sol
