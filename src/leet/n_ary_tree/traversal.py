"""
N-ary Tree Preorder Traversal
-----------------------------

Given the root of an n-ary tree, return the preorder traversal of its nodes' values.

N-ary Tree Postorder Traversal
------------------------------

Given the root of an n-ary tree, return the postorder traversal of its nodes' values.

N-ary Tree Level Order Traversal
--------------------------------

Given an n-ary tree, return the level order traversal of its nodes' values.

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


class Sol:
    def __init__(self):
        self.order = []

    def levelorder_iterative(self, root):
        if root:
            level, queue = 0, deque([root])
            while queue:
                self.order.append([])
                for _ in range(len(queue)):
                    node = queue.popleft()
                    self.order[level].append(node.val)
                    queue.extend(node.children)
                level += 1
        return self.order

    def levelorder_recursive(self, root):
        def bfs(node, level):
            if node:
                if len(self.order) == level:
                    self.order.append([])
                self.order[level].append(node.val)
                for child in node.children:
                    bfs(child, level + 1)

        bfs(root, 0)
        return self.order

    def postorder_iterative(self, root):
        if root:
            stack = [root]
            while stack:
                node = stack.pop()
                stack.extend(node.children)
                self.order.append(node.val)
        return self.order[::-1]

    def postorder_recursive(self, root):
        if root:
            for node in root.children:
                self.postorder_recursive(node)
            self.order.append(root.val)
        return self.order

    def preorder_iterative(self, root):
        if root:
            stack = [root]
            while stack:
                node = stack.pop()
                self.order.append(node.val)
                stack.extend(node.children[::-1])
        return self.order

    def preorder_recursive(self, root):
        if root:
            self.order.append(root.val)
            for node in root.children:
                self.preorder_recursive(node)
        return self.order
