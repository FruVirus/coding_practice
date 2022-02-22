"""
Binary Tree Preorder Traversal
------------------------------

Given the root of a binary tree, return the preorder traversal of its nodes' values.

Binary Tree Inorder Traversal
-----------------------------

Given the root of a binary tree, return the inorder traversal of its nodes' values.

Binary Tree Postorder Traversal
-------------------------------

Given the root of a binary tree, return the postorder traversal of its nodes' values.

Binary Tree Level Order Traversal
---------------------------------

Given the root of a binary tree, return the level order traversal of its nodes' values
(i.e., from left to right, level by level).

Complexity
==========

Time
----

inorderTraversal(), levelOrder(), postorderTraversal(), and preorderTraversal(): O(n).

Space
-----

inorderTraversal(), levelOrder(), postorderTraversal(), and preorderTraversal(): O(n).
"""

# Standard Library
from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        inorder, stack, curr = [], [], root
        while curr is not None or stack:
            while curr is not None:
                stack.append(curr)
                curr = curr.left
            curr = stack.pop()
            inorder.append(curr.val)
            curr = curr.right
        return inorder

    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        levelorder = []
        if not root:
            return levelorder
        stack = [(root, 0)]
        while stack:
            curr_node, level = stack.pop()
            if len(levelorder) == level:
                levelorder.append([])
            levelorder[level].append(curr_node.val)
            if curr_node.right:
                stack.append((curr_node.right, level + 1))
            if curr_node.left:
                stack.append((curr_node.left, level + 1))
        return levelorder

    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        postorder, stack, curr = [], [], root
        while curr is not None or stack:
            if curr is None:
                curr = stack.pop()
                curr = curr.left
            else:
                stack.append(curr)
                postorder.append(curr.val)
                curr = curr.right
        return list(reversed(postorder))

    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        preorder, stack = [], [root]
        while stack:
            node = stack.pop()
            preorder.append(node.val)
            if node.right:
                stack.append(node.right)
            if node.left:
                stack.append(node.left)
        return preorder
