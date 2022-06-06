"""
Diameter of Binary Tree
-----------------------

Given the root of a binary tree, return the length of the diameter of the tree.

The diameter of a binary tree is the length of the longest path between any two nodes in
a tree. This path may or may not pass through the root.

The length of a path between two nodes is represented by the number of edges between
them.

Intuition
---------

The key observation to make is: the longest path has to be between two leaf nodes. We
can prove this with contradiction. Imagine that we have found the longest path, and it
is not between two leaf nodes. We can extend that path by 1, by adding the child node of
one of the end nodes (as at least one must have a child, given that they aren't both
leaves). This contradicts the fact that our path is the longest path. Therefore, the
longest path must be between two leaf nodes.

Moreover, we know that in a tree, nodes are only connected with their parent node and 2
children. Therefore we know that the longest path in the tree would consist of a node,
its longest left branch, and its longest right branch. So, our algorithm to solve this
problem will find the node where the sum of its longest left and right branches is
maximized. This would hint at us to apply Depth-first search (DFS) to count each node's
branch lengths, because it would allow us to dive deep into the leaves first, and then
start counting the edges upwards.

In the midst of DFS, we also need to take the following two cases into account:

    1. the current node's both left and right branches might be a part of the longest
path;
    2. one of the current node's left/right branches might be a part of the longest
path.

Complexity
==========

Time
----

diameterOfBinaryTree(root): O(n).

Space
-----

diameterOfBinaryTree(root): O(n).
"""


def sol(root):
    diameter = 0

    def helper(node):
        nonlocal diameter
        if not node:
            return 0
        left, right = helper(node.left), helper(node.right)
        diameter = max(diameter, left + right)
        return 1 + max(left, right)

    helper(root)
    return diameter
