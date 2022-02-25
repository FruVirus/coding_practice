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

All: O(n).

Space
-----

All: O(n).
"""

# Standard Library
from collections import deque


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def __init__(self):
        self.order = []

    def inorder_iterative(self, root):
        stack, node = [], root
        while node or stack:
            while node:
                stack.append(node)
                node = node.left
            node = stack.pop()
            self.order.append(node.val)
            node = node.right
        return self.order

    def inorder_recursive(self, root):
        if root:
            self.inorder_recursive(root.left)
            self.order.append(root.val)
            self.inorder_recursive(root.right)
        return self.order

    def levelorder_iterative(self, root):
        if not root:
            return self.order
        level, queue = 0, deque([root])
        while queue:
            self.order.append([])
            for _ in range(len(queue)):
                node = queue.popleft()
                self.order[level].append(node.val)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            level += 1
        return self.order

    def levelorder_recursive(self, root):
        def bfs(node, level):
            if node:
                if len(self.order) == level:
                    self.order.append([])
                self.order[level].append(node.val)
                bfs(node.left, level + 1)
                bfs(node.right, level + 1)

        bfs(root, 0)
        return self.order

    def postorder_iterative(self, root):
        if not root:
            return self.order
        stack = [root]
        while stack:
            node = stack.pop()
            if node:
                self.order.append(node.val)
                stack.append(node.left)
                stack.append(node.right)
        return self.order[::-1]

    def postorder_recursive(self, root):
        if not root:
            return self.order
        self.postorder_recursive(root.left)
        self.postorder_recursive(root.right)
        self.order.append(root.val)
        return self.order

    def preorder_iterative(self, root):
        if not root:
            return self.order
        stack = [root]
        while stack:
            node = stack.pop()
            self.order.append(node.val)
            if node.right:
                stack.append(node.right)
            if node.left:
                stack.append(node.left)
        return self.order

    def preorder_recursive(self, root):
        if not root:
            return self.order
        self.order.append(root.val)
        self.preorder_recursive(root.left)
        self.preorder_recursive(root.right)
        return self.order
