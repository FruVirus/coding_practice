"""
Lowest Common Ancestor of a Binary Tree
---------------------------------------

Given a binary tree, find the lowest common ancestor (LCA) of two given nodes in the
tree.

According to the definition of LCA on Wikipedia: “The lowest common ancestor is defined
between two nodes p and q as the lowest node in T that has both p and q as descendants
(where we allow a node to be a descendant of itself).”

Complexity
==========

Time
----

lca: O(n).

Space
-----

lca: O(n).
"""


def lca(root, p, q):
    ancestors, node, parent, stack = set(), root, {root: None}, [root]
    while not (p in parent and q in parent):
        node = stack.pop()
        if node.left:
            parent[node.left] = node
            stack.append(node.left)
        if node.right:
            parent[node.right] = node
            stack.append(node.right)
    while p:
        ancestors.add(p)
        p = parent[p]
    while q not in ancestors:
        q = parent[q]
    return q
