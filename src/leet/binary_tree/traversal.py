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

Binary Tree Zigzag Level Order Traversal
----------------------------------------

Given the root of a binary tree, return the zigzag level order traversal of its nodes'
values. (i.e., from left to right, then right to left for the next level and alternate
between).

Intuition
---------

We want to use a deque() since appendleft is an O(1) operation.

One can start with the normal BFS algorithm, upon which we add a touch of zigzag order
with the help of deque. For each level, we start from an empty deque container to hold
all the values of the same level. Depending on the ordering of each level, i.e. either
from-left-to-right or from-right-to-left, we decide at which end of the deque to add the
new element:

    - from left-to-right: insert at tail
    - from right-to-left: insert at head

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

    def inorder_iterative(self, root):
        node, stack = root, []
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
        if root:
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
        def dfs(node, level):
            if node:
                if len(self.order) == level:
                    self.order.append([])
                self.order[level].append(node.val)
                dfs(node.left, level + 1)
                dfs(node.right, level + 1)

        dfs(root, 0)
        return self.order

    def postorder_iterative(self, root):
        if root:
            stack = [root]
            while stack:
                node = stack.pop()
                if node.left:
                    stack.append(node.left)
                if node.right:
                    stack.append(node.right)
                self.order.append(node.val)
        return self.order[::-1]

    def postorder_recursive(self, root):
        if root:
            self.postorder_recursive(root.left)
            self.postorder_recursive(root.right)
            self.order.append(root.val)
        return self.order

    def preorder_iterative(self, root):
        if root:
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
        if root:
            self.order.append(root.val)
            self.preorder_recursive(root.left)
            self.preorder_recursive(root.right)
        return self.order

    def zigzag_iterative(self, root):
        level_queue = deque()
        if root:
            level, queue, ltr = 0, deque([root]), True
            while queue:
                for _ in range(len(queue)):
                    node = queue.popleft()
                    if ltr:
                        level_queue.append(node.val)
                    else:
                        level_queue.appendleft(node.val)
                    if node.left:
                        queue.append(node.left)
                    if node.right:
                        queue.append(node.right)
                level += 1
                self.order.append(level_queue)
                level_queue = deque()
                ltr = not ltr
        return self.order

    def zigzag_recursive(self, root):
        def dfs(node, level):
            if node:
                if len(self.order) == level:
                    self.order.append(deque())
                if level % 2 == 0:
                    self.order[level].append(node.val)
                else:
                    self.order[level].appendleft(node.val)
                dfs(node.left, level + 1)
                dfs(node.right, level + 1)

        dfs(root, 0)
        return self.order
