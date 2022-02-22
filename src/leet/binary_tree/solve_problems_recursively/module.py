"""
Maximum Depth of a Binary Tree
------------------------------

Given the root of a binary tree, return its maximum depth.

A binary tree's maximum depth is the number of nodes along the longest path from the
root node down to the farthest leaf node.

Symmetric Tree
--------------

Given the root of a binary tree, check whether it is a mirror of itself (i.e., symmetric
around its center).

Path Sum
--------

Given the root of a binary tree and an integer targetSum, return True if the tree has a
root-to-leaf path such that adding up all the values along the path equals targetSum.

A leaf node is a node with no children.

Count Univalue Subtrees
-----------------------

Given the root of a binary tree, return the number of uni-value subtrees.

A uni-value subtree means all nodes of the subtree have the same value.

Complexity
==========

Time
----

hasPathSum(), isSymmetric(), isSymmetric_iterative(), maxDepth(), maxDepth_iterative():
O(n).

Space
-----

hasPathSum(), isSymmetric(), isSymmetric_iterative(), maxDepth(), maxDepth_iterative():
O(n).
"""

# Standard Library
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def countUnivalSubtrees(self, root):
        self.count = 0
        self.is_valid_part(root, 0)
        return self.count

    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        if not root:
            return False
        stack = [(root, targetSum - root.val)]
        while stack:
            node, curr_sum = stack.pop()
            if curr_sum == 0 and node.left is None and node.right is None:
                return True
            if node.right is not None:
                stack.append((node.right, curr_sum - node.right.val))
            if node.left is not None:
                stack.append((node.left, curr_sum - node.left.val))
        return False

    def isMirror(self, left, right):
        if not left and not right:
            return True
        if not left or not right:
            return False
        return (
            left.val == right.val
            and self.isMirror(left.left, right.right)
            and self.isMirror(left.right, right.left)
        )

    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        return self.isMirror(root, root)

    def isSymmetric_iterative(self, root: Optional[TreeNode]) -> bool:
        stack = [(root.left, root.right)]
        while stack:
            right, left = stack.pop()
            if left and right:
                if left.val != right.val:
                    return False
                else:
                    stack.append((left.left, right.right))
                    stack.append((left.right, right.left))
            elif (not left and right) or (left and not right):
                return False
        return True

    def is_valid_part(self, node, val):
        if node is None:
            return True
        if not all(
            [
                self.is_valid_part(node.left, node.val),
                self.is_valid_part(node.right, node.val),
            ]
        ):
            return False
        self.count += 1
        return node.val == val

    def maxDepth(self, root):
        if root is None:
            return 0
        else:
            return max(self.maxDepth(root.left), self.maxDepth(root.right)) + 1

    def maxDepth_iterative(self, root: Optional[TreeNode]) -> int:
        depth, stack = 0, []
        if root is not None:
            stack.append((root, 1))
        while stack:
            root, curr_depth = stack.pop()
            if root is not None:
                depth = max(depth, curr_depth)
                stack.append((root.left, curr_depth + 1))
                stack.append((root.right, curr_depth + 1))
        return depth
