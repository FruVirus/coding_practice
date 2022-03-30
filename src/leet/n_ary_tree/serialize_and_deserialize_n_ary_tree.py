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


class WrappableInt:
    def __init__(self, x):
        self.value = x

    def get_value(self):
        return self.value

    def increment(self):
        self.value += 1


class Node:
    def __init__(self, val=None, children=None):
        self.val, self.children = val, children


def sol_serialize(root):
    sol = []

    def serialize_(root, sol):
        if not root:
            return
        sol.append(chr(root.val + 36))
        for child in root.children:
            serialize_(child, sol)
        sol.append("#")

    serialize_(root, sol)
    return "".join(sol)


def sol_deserialize(data):
    if not data:
        return None

    def deserialize_(data, index):
        if index.get_value() == len(data):
            return None
        node = Node(ord(data[index.get_value()]) - 36, [])
        index.increment()
        while data[index.get_value()] != "#":
            node.children.append(deserialize_(data, index))
        index.increment()
        return node

    return deserialize_(data, WrappableInt(0))
