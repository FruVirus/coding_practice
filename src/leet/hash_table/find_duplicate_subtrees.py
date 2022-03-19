"""
Find Duplicate Subtrees
-----------------------

Given the root of a binary tree, return all duplicate subtrees.

For each kind of duplicate subtrees, you only need to return the root node of any one of
them.

Two trees are duplicate if they have the same structure with the same node values.

Intuition
---------

As the function recurses, the keys of dups are unique hashes of subtrees and the values
are lists containing roots with those unique hashes. If a given hash has more than one
root, then that is a duplicate subtree in the overall binary tree.

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
    dups = defaultdict(list)

    def helper(root):
        if root:
            lhash = helper(root.left)
            rhash = helper(root.right)
            thash = str(root.val) + "(" + lhash + ")" + "(" + rhash + ")"
            dups[thash].append(root)
            return thash
        return "None"

    helper(root)
    return [l[0] for l in dups.values() if len(l) > 1]
