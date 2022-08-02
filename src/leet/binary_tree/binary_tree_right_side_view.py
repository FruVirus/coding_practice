"""
Binary Tree Right Side View
---------------------------

Given the root of a binary tree, imagine yourself standing on the right side of it,
return the values of the nodes you can see ordered from top to bottom.

Complexity
==========

Time
----

rightSideView_bfs(root) and rightSideView_dfs(root): O(n).

Space
-----

rightSideView_bfs(root): O(d), where d is the tree diameter. For the last tree level, it
could contain up to n / 2 nodes in the case of a complete binary tree.
rightSideView_dfs(root): O(h), where h is the tree height.
"""

# Standard Library
from collections import deque


def sol_bfs(root):
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


def sol_dfs(root):
    sol = []
    if not root:
        return sol

    def dfs(node, level):
        if node:
            if len(sol) == level:
                sol.append(node.val)
            dfs(node.right, level + 1)
            dfs(node.left, level + 1)

    dfs(root, 0)
    return sol
