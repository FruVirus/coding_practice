"""
Path Sum
--------

Given the root of a binary tree and an integer targetSum, return true if the tree has a
root-to-leaf path such that adding up all the values along the path equals targetSum.

A leaf is a node with no children.

Complexity
==========

Time
----

hasPathSum(root, target_sum): O(n).

Space
-----

hasPathSum(root, target_sum): O(n).
"""


def sol(root, target_sum):
    if not root:
        return False
    stack = [(root, target_sum - root.val)]
    while stack:
        node, sum_ = stack.pop()
        if sum_ == 0 and not (node.left or node.right):
            return True
        if node.left:
            stack.append((node.left, sum_ - node.left.val))
        if node.right:
            stack.append((node.right, sum_ - node.right.val))
    return False
