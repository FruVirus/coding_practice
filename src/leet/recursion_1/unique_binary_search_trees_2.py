"""
K-th Symbol in Grammar
----------------------

Given an integer n, return all the structurally unique BST's (binary search trees),
which has exactly n nodes of unique values from 1 to n. Return the answer in any order.

Complexity
==========

Time
----

generateTrees(n): O(4^n / n^(1 / 2)).

Space
-----

generateTrees(n): O(4^n / n^(1 / 2)).
"""


class Node:
    def __init__(self, val=0, left=None, right=None):
        self.val, self.left, self.right = val, left, right


def sol(n):
    def generate_trees(start, end):
        if start <= end:
            all_trees = []
            for i in range(start, end + 1):
                left_trees = generate_trees(start, i - 1)
                right_trees = generate_trees(i + 1, end)
                for l in left_trees:
                    for r in right_trees:
                        tree = Node(i)
                        tree.left, tree.right = l, r
                        all_trees.append(tree)
            return all_trees
        return [None]

    return generate_trees(1, n)
