"""
Unique Binary Search Trees II
-----------------------------

Given an integer n, return all the structurally unique BST's (binary search trees),
which has exactly n nodes of unique values from 1 to n. Return the answer in any order.

Complexity
==========

Time
----

generateTrees(n): O(4^n / sqrt(n)).

Space
-----

generateTrees(n): O(4^n / sqrt(n)).
"""


class Node:
    def __init__(self, val=0, left=None, right=None):
        self.val, self.left, self.right = val, left, right


def sol(n):
    memo = {}

    def generate_trees(start, end):
        if start <= end:
            if (start, end) in memo:
                return memo[(start, end)]
            all_trees = []
            for i in range(start, end + 1):
                for l in generate_trees(start, i - 1):
                    for r in generate_trees(i + 1, end):
                        tree = Node(i)
                        tree.left, tree.right = l, r
                        all_trees.append(tree)
            memo[(start, end)] = all_trees
            return all_trees
        return [None]

    return generate_trees(1, n)
