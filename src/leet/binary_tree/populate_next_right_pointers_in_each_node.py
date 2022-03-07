"""
Populating Next Right Pointers in Each Node II
----------------------------------------------

Given a binary tree, populate each next pointer to point to its next right node. If
there is no next right node, the next pointer should be set to NULL.

Initially, all next pointers are set to NULL.

Complexity
==========

Time
----

connect(root): O(n).

Space
-----

connect(root): O(1).
"""


def sol(root):
    leftmost = root
    while leftmost:
        prev, node, leftmost = None, leftmost, None
        while node:
            if node.left:
                prev, leftmost = update(prev, node.left, leftmost)
            if node.right:
                prev, leftmost = update(prev, node.right, leftmost)
            node = node.next
    return root


def update(prev, node, leftmost):
    if prev:
        prev.next = node
    else:
        leftmost = node
    prev = node
    return prev, leftmost
