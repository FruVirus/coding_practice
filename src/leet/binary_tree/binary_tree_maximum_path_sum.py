"""
Binary Tree Maximum Path Sum
----------------------------

A path in a binary tree is a sequence of nodes where each pair of adjacent nodes in the
sequence has an edge connecting them. A node can only appear in the sequence at most
once. Note that the path does not need to pass through the root.

The path sum of a path is the sum of the node's values in the path.

Given the root of a binary tree, return the maximum path sum of any non-empty path.

Intuition
---------

First of all, let's simplify the problem and implement a function max_gain(node) which
takes a node as an argument and computes a maximum contribution that this node and
one/zero of its subtrees could add.

    In other words, it's a maximum gain one could have including the node (and maybe one
of its subtrees) into the path.

Hence if one would know for sure that the max path contains root, the problem would be
solved as max_gain(root). Unfortunately, the max path does not need to go through the
root.

That means one needs to modify the above function and to check at each step what is
better: to continue the current path or to start a new path with the current node as a
highest node in this new path.

When we are looking at the maximum path that we can form involving the left and right
branches of a node, we only care about the gains we can make. This means, if the sum of
all the nodes on either of the branches is less than 0, then the branch is not worth
exploring at all and we just clamp the max gain at 0.

When we are looking at the maximum path that we can form involving a particular node,
two sub questions arise:
    - What is the maximum gain we can get from its left branch?
    - What is the maximum gain we can get from its right branch?

The maximum path that we can form involving a particular node is node.val + left_gain +
right_gain. If this value is greater than the current max value, then we update the max
value.

When we return from the recursion, we can only form a path involving the node and one of
the two branches of the node (i.e., we can't take the gain from both branches).
Otherwise, this wouldn't form a valid path down the tree.

Complexity
==========

Time
----

maxPathSum(root): O(n).

Space
-----

maxPathSum(root): O(h).
"""


def sol(root):
    def max_gain(node):
        nonlocal max_sum
        if not node:
            return 0
        left_gain = max(max_gain(node.left), 0)
        right_gain = max(max_gain(node.right), 0)
        max_sum = max(max_sum, node.val + left_gain + right_gain)
        return node.val + max(left_gain, right_gain)

    max_sum = -float("inf")
    max_gain(root)
    return max_sum
