"""
Serialize and Deserialize Binary Tree
-------------------------------------

Serialization is the process of converting a data structure or object into a sequence of
bits so that it can be stored in a file or memory buffer, or transmitted across a
network connection link to be reconstructed later in the same or another computer
environment.

Design an algorithm to serialize and deserialize a binary tree. There is no restriction
on how your serialization/deserialization algorithm should work. You just need to ensure
that a binary tree can be serialized to a string and this string can be deserialized to
the original tree structure.

Complexity
==========

Time
----

serialize(root) and deserialize(data): O(n), where n is the number of nodes in the tree.

Space
-----

serialize(root) and deserialize(data): O(n).
"""


class Node:
    def __init__(self, x):
        self.val, self.left, self.right = x, None, None


def sol_serialize(root):
    def serialize(root, s):
        if not root:
            s += "None,"
        else:
            s += str(root.val) + ","
            s = serialize(root.left, s)
            s = serialize(root.right, s)
        return s

    return serialize(root, "")


def sol_deserialize(data):
    def deserialize(l):
        root = l.pop(0)
        if root == "None":
            return None
        root = Node(root)
        root.left, root.right = deserialize(l), deserialize(l)
        return root

    return deserialize(data.split(","))
