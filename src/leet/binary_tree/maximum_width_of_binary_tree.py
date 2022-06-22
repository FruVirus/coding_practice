"""
Maximum Width of Binary Tree
----------------------------

Given the root of a binary tree, return the maximum width of the given tree.

The maximum width of a tree is the maximum width among all levels.

The width of one level is defined as the length between the end-nodes (the leftmost and
rightmost non-null nodes), where the null nodes between the end-nodes that would be
present in a complete binary tree extending down to that level are also counted into the
length calculation.

It is guaranteed that the answer will in the range of a 32-bit signed integer.

Intuition
---------

The key to solve the problem though lie on how we index the nodes that are on the same
level.

Suppose that the indices for the first and the last nodes of one particular level are
C_1 and C_n respectively, we could then calculate the width of this level as
C_n - C_i + 1.

As we know, for a full binary tree, the number of nodes double at each level, since each
parent node has two child nodes. Naturally, the range of our node index would double as
well.

If the index of a parent node is C_i, accordingly we can define the index of its left
child node as 2 * C_i and the index of its right child node as 2 * C_i + 1.

With the above indexing schema, we manage to assign a unique index for each node on the
same level, and in addition there is no gap among all the indices if it is a full binary
tree.

For a non-full binary tree, the relationship between the indices of a parent and its
child node still holds.

Now that we have an indexing schema, all we need to do is to assign an index for each
node in the tree. Once it is done, we can calculate the width for each level, and
finally we could return the maximal value among them as the solution.

Complexity
==========

Time
----

widthOfBinaryTree_bfs(root) and widthOfBinaryTree_dfs(root): O(n).

Space
-----

widthOfBinaryTree_bfs(root) and widthOfBinaryTree_dfs(root): O(n).
"""

# Standard Library
from collections import deque


def sol_bfs(root):
    max_width = 0
    if root:
        queue = deque([(root, 0)])
        while queue:
            level = queue[0][1]
            for _ in range(len(queue)):
                node, index = queue.popleft()
                if node.left:
                    queue.append((node.left, 2 * index))
                if node.right:
                    queue.append((node.right, 2 * index + 1))
            max_width = max(max_width, index - level + 1)
    return max_width


def sol_dfs(root):
    max_width, table = 0, {}

    def dfs(node, level, index):
        nonlocal max_width
        if node:
            if level not in table:
                table[level] = index
            max_width = max(max_width, index - table[level] + 1)
            dfs(node.left, level + 1, 2 * index)
            dfs(node.right, level + 1, 2 * index + 1)

    dfs(root, 0, 0)
    return max_width
