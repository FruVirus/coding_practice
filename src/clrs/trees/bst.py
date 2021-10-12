"""
Overview
========

A binary search tree (BST) is organized as a binary tree. We can recognize such a tree
by a linked data structure in which each node is an object. In addition to a key and
satellite data, each node contains attributes, left, right, and p that point to the
nodes corresponding to its left child, its right child, and its parent, respectively. If
a child or parent is missing, the appropriate attribute contains the value None. The
root node is the only node in the tree whose parent is None.

The keys in a binary search tree are always stored in such a way as to satisfy the
binary-search-tree property:

    Let x be a node in a binary search tree. If y is a node in the left subtree of x,
    then y.key <= x.key. If y is a node in the right subtree of x, then y.key >= x.key.

Complexity
==========

1. walk() takes O(n) time.

2. insert(), delete(), search(), min(), max(), successor(), and predecessor() all take
O(h) time on a BST of height h. If the BST is balanced, then O(h) = O(lg(n)).

3. list() takes O(lg(n)) + O(L) time where L is the number of keys returned.

4. rank() and count() both take O(lg(n)) time.
"""


class BST:
    def __init__(self, z):
        self.root = BSTNode(z)

    def _get_node(self, x):
        if isinstance(x, (int, float)):
            x = self.search(self.root, x)
        return x

    def count(self, l, h):
        assert l < h
        count = self.rank(h) - self.rank(l)
        has_l = self.search(self.root, l)
        if has_l is None or (has_l is None and self.search(self.root, h) is None):
            return count
        return count + 1

    def delete(self, z):
        z = self._get_node(z)
        if z.left is None:
            self.transplant(z, z.right)
        elif z.right is None:
            self.transplant(z, z.left)
        else:
            y = self.min(z.right)
            if y.p is not z:
                self.transplant(y, y.right)
                y.right = z.right
                y.right.p = y
            self.transplant(z, y)
            y.left = z.left
            y.left.p = y
        if isinstance(z.p, BSTNode):
            self.update_size(z.p)
        return z

    def insert(self, z):
        x, y = self.root, None
        if isinstance(z, (int, float)):
            z = BSTNode(z)
        while x is not None:
            y = x
            x = x.left if z.key < x.key else x.right
        z.p = y
        if y is None:
            self.root = z
        elif z.key < y.key:
            y.left = z
        else:
            y.right = z
        if isinstance(z.p, BSTNode):
            self.update_size(z.p)
        return z

    def lca(self, l, h):
        x = self.root
        while x is not None and not l <= x.key <= h:
            x = x.left if l < x.key else x.right
        return x

    def list(self, l, h):
        result = [l]
        node = self.successor(l)
        while node is not None and node.key <= h:
            result.append(node.key)
            node = self.successor(node)
        return result

    def max(self, x):
        x = self._get_node(x)
        while x.right is not None:
            x = x.right
        return x

    def min(self, x):
        x = self._get_node(x)
        while x.left is not None:
            x = x.left
        return x

    def predecessor(self, x):
        x = self._get_node(x)
        if x.left is not None:
            return self.max(x.left)
        y = x.p
        while y is not None and x is y.left:
            x, y = y, y.p
        return y

    def rank(self, k):
        r, x = 0, self.root
        while x is not None:
            if k < x.key:
                x = x.left
            else:
                r += 1 + (x.left and x.left.size or 0)
                if k == x.key:
                    return r
                x = x.right
        return r

    def search(self, x, k):
        x = self._get_node(x)
        while x is not None and k != x.key:
            x = x.left if k < x.key else x.right
        return x

    def successor(self, x):
        x = self._get_node(x)
        if x.right is not None:
            return self.min(x.right)
        y = x.p
        while y is not None and x is y.right:
            x, y = y, y.p
        return y

    def transplant(self, u, v):
        if u.p is None:
            self.root = v
        elif u is u.p.left:
            u.p.left = v
        else:
            u.p.right = v
        if v is not None:
            v.p = u.p

    def update_size(self, x):
        if x is None:
            return
        x.size = 1 + ((x.left and x.left.size) or 0) + ((x.right and x.right.size) or 0)
        self.update_size(x.left)
        self.update_size(x.right)

    def walk(self, x):
        if x is not None:
            node = self.min(x)
            while node is not None:
                print(node.key)
                node = self.successor(node)


class BSTNode:
    def __init__(self, key, parent=None):
        self.key, self.p, self.size = key, parent, 1
        self.left = self.right = None
