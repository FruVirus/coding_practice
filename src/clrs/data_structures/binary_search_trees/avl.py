"""
Overview
========

In a BST, the height of the tree dictates the running time of the various tree
operations. The height of the tree can range from O(lg n) at a minimum to O(n) at a
maximum depending on how the keys are inserted/deleted.

For n keys, there are n! possible BSTs. To get a balanced BST, we can perform rotations
until we get a tree with a minimum height.

An AVL tree is a BST that balances itself every time an element is inserted or deleted
via rotations. In addition to the invariants of a BST, each node of an AVL tree has the
invariant property that the heights of the sub-tree rooted at its children differ by at
most one: balance factor = |height(node.left) - height(node.right)| <= 1.

Every time we insert or delete a node, we need to update the height all the way up the
ancestry until the height of a node doesn't change.

Rotation starts from the newly inserted node and finds the first ancestor that is
unbalanced. If an ancestor is unbalanced, then rotations are performed around that
ancestor.

Rotations are always done on three nodes at a time regardless of the size of the overall
tree since we want our balance factor to be <= 1. Hence, we consider x, x's children,
and x's grand-children only. If x's grand-children are not unbalanced, then we only need
to rotate x. Otherwise, we have to rotate x's grand-children first before rotating x.

AVL trees are fast for searching but can be slow for insertion and deletion due to the
number of rotations performed. If insertion/deletion is more common than searching, then
RBTs are a better data structure.

Complexity
==========

Time
----

balance(), delete(), insert(), and rotate(): O(lg n).

rotate_left() and rotate_right(): O(1).
"""

# Repository Library
from src.clrs.data_structures.binary_search_trees.bst import BST, BSTNode


class AVL(BST):
    def __init__(self, z, sentinel=None):
        super().__init__(AVLNode(z) if isinstance(z, (int, float)) else z, sentinel)

    def balance(self, x):
        while x is not self.sentinel:
            self.update_height(x)
            self.update_size(x)
            if self.height(x.left) >= self.height(x.right) + 2:
                if self.height(x.left.left) < self.height(x.left.right):
                    self.rotate(x.left, True)
                self.rotate(x, False)
            elif self.height(x.right) >= self.height(x.left) + 2:
                if self.height(x.right.right) < self.height(x.right.left):
                    self.rotate(x.right, False)
                self.rotate(x, True)
            x = x.p

    def delete(self, z):
        self.balance(super().delete(z).p)

    def height(self, x):
        return 0 if x is self.sentinel else self._get_node(x).h

    def insert(self, z):
        self.balance(super().insert(AVLNode(z)))

    def rotate(self, x, left_rotate):
        x = self._get_node(x)
        if left_rotate:
            self.rotate_left(x)
        else:
            self.rotate_right(x)

    def rotate_left(self, x):
        y = x.right
        x.right = y.left
        if y.left is not self.sentinel:
            y.left.p = x
        y.p = x.p
        if x.p is self.sentinel:
            self.root = y
        elif x is x.p.left:
            x.p.left = y
        else:
            x.p.right = y
        y.left, x.p = x, y
        if isinstance(x, AVLNode):
            self.update_height(x)
            self.update_height(y)
        self.update_size(x)
        self.update_size(y)

    def rotate_right(self, x):
        y = x.left
        x.left = y.right
        if y.right is not self.sentinel:
            y.right.p = x
        y.p = x.p
        if x.p is self.sentinel:
            self.root = y
        elif x is x.p.right:
            x.p.right = y
        else:
            x.p.left = y
        y.right, x.p = x, y
        if isinstance(x, AVLNode):
            self.update_height(x)
            self.update_height(y)
        self.update_size(x)
        self.update_size(y)

    def update_height(self, x):
        x.h = max(self.height(x.left), self.height(x.right)) + 1


class AVLNode(BSTNode):
    def __init__(self, key, parent=None, height=0):
        super().__init__(key, parent)
        self.h = height
