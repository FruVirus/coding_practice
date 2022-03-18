"""
Find Duplicate Subtrees
-----------------------

Given the root of a binary tree, return all duplicate subtrees.

For each kind of duplicate subtrees, you only need to return the root node of any one of
them.

Two trees are duplicate if they have the same structure with the same node values.

Complexity
==========

Time
----

findDuplicateSubtrees(root): O(n^2).

Space
-----

findDuplicateSubtrees(root): O(n^2).
"""

# Standard Library
from collections import defaultdict


def sol(root):
    def helper(root):
        if root:
            l_hash = helper(root.left)
            r_hash = helper(root.right)
            c_hash = str(root.val) + "(" + l_hash + ")" + "(" + r_hash + ")"
            dups[c_hash].append(root)
            return c_hash
        return "None"

    dups = defaultdict(list)
    helper(root)
    return [l[0] for l in dups.values() if len(l) > 1]
