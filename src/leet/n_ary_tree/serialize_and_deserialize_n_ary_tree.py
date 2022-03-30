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
    if not root:
        return ""

    def serialize_(root):
        return [[node.val, serialize_(node)] for node in root.children]

    return [root.val, serialize_(root)]


def sol_deserialize(data):
    if not data:
        return None

    def deserialize_(l):
        root = l.pop(0)
        for sub_l in l:
            node = Node(root)
            node.children = [deserialize_(x) for x in sub_l]
            return node

    return deserialize_(data)
