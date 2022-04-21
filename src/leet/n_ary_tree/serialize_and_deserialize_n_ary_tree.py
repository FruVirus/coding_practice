"""
Serialize and Deserialize N-ary Tree
------------------------------------

Serialization is the process of converting a data structure or object into a sequence of
bits so that it can be stored in a file or memory buffer, or transmitted across a
network connection link to be reconstructed later in the same or another computer
environment.

Design an algorithm to serialize and deserialize an N-ary tree. An N-ary tree is a
rooted tree in which each node has no more than N children. There is no restriction on
how your serialization/deserialization algorithm should work. You just need to ensure
that an N-ary tree can be serialized to a string and this string can be deserialized to
the original tree structure.

Intuition
---------

We add a sentinel value when all the children have been added to the final string.

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
    def __init__(self, val=None, children=None):
        self.val, self.children = val, children


def sol_serialize(root):
    sol = []

    def serialize(root):
        if root:
            sol.append(chr(root.val + 36))
            for child in root.children:
                serialize(child)
            sol.append("#")

    serialize(root)
    return "".join(sol)


def sol_deserialize(data):
    if not data:
        return None
    index = 0

    def deserialize():
        nonlocal index
        if index != len(data):
            node = Node(ord(data[index]) - 36, [])
            index += 1
            while data[index] != "#":
                node.children.append(deserialize())
            index += 1
            return node
        return None

    return deserialize()
