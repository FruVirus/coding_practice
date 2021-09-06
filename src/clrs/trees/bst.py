"""A binary search tree (BST) is organized as a binary tree. We can recognize such a
tree by a linked data structure in which each node is an object. In addition to a key
and satellite data, each node contains attributes, left, right, and p that point to the
nodes corresponding to its left child, its right child, and its parent, respectively. If
a child or parent is missing, the appropriate attribute contains the value None. The
root node is the only node in the tree whose parent is None.

The keys in a binary search tree are always stored in such a way as to satisfy the
binary-search-tree property:

    Let x be a node in a binary search tree. If y is a node in the left subtree of x,
    then y.key <= x.key. If y is a node in the right subtree of x, then y.key >= x.key.

1. inorder_walk() takes O(n) time.

2. insert(), delete(), search(), min(), max(), successor(), and predecessor() all take
O(h) = O(lg(n)) time on a bst of height h.
"""


class BST:
    def __init__(self):
        self.root = None

    def delete(self, k):
        node = self.search(k)
        if node is None:
            return None
        if node is self.root:
            temp_root = BSTNode(None, 0)
            temp_root.left = self.root
            self.root.parent = temp_root
            deleted = self.root.delete()
            self.root = temp_root.left
            if self.root is not None:
                self.root.parent = None
            return deleted
        return node.delete()

    def insert(self, k):
        node = BSTNode(None, k)
        if self.root is None:
            self.root = node
        else:
            self.root.insert(node)

    def min(self):
        return self.root and self.root.min()

    def search(self, k):
        return self.root and self.root.search(k)

    def successor(self, k):
        node = self.search(k)
        return node and node.successor()


class BSTNode:
    def __init__(self, parent, k):
        self.key = k
        self.parent = parent
        self.left = self.right = None

    def delete(self):
        if self.left is None or self.right is None:
            if self is self.parent.left:
                self.parent.left = self.left or self.right
                if self.parent.left is not None:
                    self.parent.left.parent = self.parent
            else:
                self.parent.right = self.left or self.right
                if self.parent.right is not None:
                    self.parent.right.parent = self.parent
            return self
        s = self.successor()
        self.key, s.key = s.key, self.key
        return s.delete()

    def insert(self, node):
        if node is None:
            return
        if node.key < self.key:
            if self.left is None:
                node.parent = self
                self.left = node
            else:
                self.left.insert(node)
        elif self.right is None:
            node.parent = self
            self.right = node
        else:
            self.right.insert(node)

    def max(self):
        current = self
        while current.right is not None:
            current = current.right
        return current

    def min(self):
        current = self
        while current.left is not None:
            current = current.left
        return current

    def predecessor(self):
        if self.left is not None:
            return self.left.max()
        current = self
        while current.parent is not None and current is current.parent.left:
            current = current.parent
        return current.parent

    def search(self, k):
        if k == self.key:
            return self
        if k < self.key:
            return None if self.left is None else self.left.search(k)
        return None if self.right is None else self.right.search(k)

    def successor(self):
        if self.right is not None:
            return self.right.min()
        current = self
        while current.parent is not None and current is current.parent.right:
            current = current.parent
        return current.parent


class MinBSTNode(BSTNode):
    def __init__(self, parent, key):
        super().__init__(parent, key)
        self.min = self
