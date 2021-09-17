"""An AVL tree is a BST that balances itself every time an element is inserted or
deleted. In addition to the invariants of a BST, each node of an AVL tree has the
invariant property that the heights of the sub-tree rooted at its children differ by at
most one: |height(node.left) - height(node.right)| <= 1.

EVery time we insert or delete a node, we need to update the height all the way up the
ancestry until the height of a node doesn't change.

1. walk() takes O(n) time.

2. insert(), delete(), search(), min(), max(), successor(), and predecessor() all take
O(lg(n)) time.
"""


# Repository Library
from src.clrs.trees.bst import BST, BSTNode


class AVL(BST):
    def __init__(self, z):
        self.root = AVLNode(z, None, 0)

    def balance(self, x):
        while x is not None:
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

    def count(self, l, h):
        assert l < h
        count = self.rank(h) - self.rank(l)
        has_l = self.search(self.root, l)
        if has_l is None or (has_l is None and self.search(self.root, h) is None):
            return count
        return count + 1

    def delete(self, z):
        z = super().delete(z)
        self.balance(z.p)

    def height(self, x):
        if x is None:
            return 0
        if not isinstance(x, AVLNode):
            x = self.search(self.root, x)
        return x.h

    def insert(self, z):
        z = super().insert(AVLNode(z, None, 0))
        self.balance(z)

    def rank(self, k):
        r, x = 0, self.root
        while x is not None:
            if k < x.key:
                x = x.left
            else:
                if x.left is not None:
                    r = r + 1 + x.left.size
                else:
                    r = r + 1
                if x.key == k:
                    return r
                x = x.right
        return r

    def rotate(self, x, left_rotate):
        x = self._get_node(x)
        if left_rotate:
            self.rotate_left(x)
        else:
            self.rotate_right(x)

    def rotate_left(self, x):
        y = x.right
        x.right = y.left
        if y.left is not None:
            y.left.p = x
        y.p = x.p
        if x.p is None:
            self.root = y
        elif x is x.p.left:
            x.p.left = y
        else:
            x.p.right = y
        y.left = x
        x.p = y
        self.update_height(x)
        self.update_height(y)
        self.update_size(x)
        self.update_size(y)

    def rotate_right(self, x):
        y = x.left
        x.left = y.right
        if y.right is not None:
            y.right.p = x
        y.p = x.p
        if x.p is None:
            self.root = y
        elif x is x.p.right:
            x.p.right = y
        else:
            x.p.left = y
        y.right = x
        x.p = y
        self.update_height(x)
        self.update_height(y)
        self.update_size(x)
        self.update_size(y)

    def update_height(self, x):
        x.h = max(self.height(x.left), self.height(x.right)) + 1

    @staticmethod
    def update_size(x):
        x.size = 1 + ((x.left and x.left.size) or 0) + ((x.right and x.right.size) or 0)


class AVLNode(BSTNode):
    def __init__(self, key, parent, height):
        super().__init__(key, parent)
        self.h, self.size = height, 1
