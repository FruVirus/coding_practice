"""A red-black tree (RBT) is a binary search tree with one extra bit of storage per
node: its color, which can be either RED (0) or BLACK (1). By constraining the node
colors on any simple path from the root to a leaf, RBTs ensure that no such path is more
than twice as long as any other, so that the tree is approximately balanced.

Each node of the tree now contains the attributes color, key, left, right, and parent.
If a child or the parent of a node does not exist, the corresponding pointer attribute
of the node contains the value None.

A RBT is a binary tree that satisfies the following red-black properties:

1. Every node is either red or black.
2. The root is black.
3. Every leaf (NIL) is black.
4. If a node is red, then both its children are black.
5. For each node, all simple paths from the node to descendant leaves contain the same
number of black nodes.

A RBT tree with n internal nodes has height at most 2* lg(n + 1).

1. walk() takes O(n) time.

2. All other operations take O(lg(n)) or O(1) time.
"""


class RBT:
    def __init__(self, z):
        self.nil = RBTNode(1, None, None)
        self.root = RBTNode(1, z, self.nil)

    def _get_node(self, x):
        if not isinstance(x, RBTNode):
            x = self.search(self.root, x)
        return x

    def delete(self, z):
        z = self._get_node(z)
        y = z
        y_orig_color = y.color
        if z.left is self.nil:
            x = z.right
            self.transplant(z, z.right)
        elif z.right is self.nil:
            x = z.left
            self.transplant(z, z.left)
        else:
            y = self.min(z.right)
            y_orig_color = y.color
            x = y.right
            if y.p is z:
                x.p = y
            else:
                self.transplant(y, y.right)
                y.right = z.right
                y.right.p = y
            self.transplant(z, y)
            y.left = z.left
            y.left.p = y
            y.color = z.color
        if y_orig_color == 1:
            self.delete_fix(x)

    def delete_fix(self, x):
        while x is not self.root and x.color == 1:
            if x is x.p.left:
                w = x.p.right
                if w.color == 0:
                    w.color = 1
                    x.p.color = 0
                    self.rotate(x.p, True)
                    w = x.p.right
                if w.left.color == 1 and w.right.color == 1:
                    w.color = 0
                    x = x.p
                else:
                    if w.right.color == 1:
                        w.left.color = 1
                        w.color = 0
                        self.rotate(w, False)
                        w = x.p.right
                    w.color = x.p.color
                    x.p.color = 1
                    w.right.color = 1
                    self.rotate(x.p, True)
                    x = self.root
            else:
                w = x.p.left
                if w.color == 0:
                    w.color = 1
                    x.p.color = 0
                    self.rotate(x.p, False)
                    w = x.p.left
                if w.left.color == 1 and w.right.color == 1:
                    w.color = 0
                    x = x.p
                else:
                    if w.left.color == 1:
                        w.right.color = 1
                        w.color = 0
                        self.rotate(w, True)
                        w = x.p.left
                    w.color = x.p.color
                    x.p.color = 1
                    w.left.color = 1
                    self.rotate(x.p, False)
                    x = self.root
        x.color = 1

    def insert(self, z):
        z = RBTNode(0, z, None)
        y = self.nil
        x = self.root
        while x is not self.nil:
            y = x
            if z.key < x.key:
                x = x.left or self.nil
            else:
                x = x.right or self.nil
        z.p = y
        if y is self.nil:
            self.root = z
        elif z.key < y.key:
            y.left = z
        else:
            y.right = z
        z.left = self.nil
        z.right = self.nil
        z.color = 0
        self.insert_fix(z)

    def insert_fix(self, z):
        while z.p.color == 0:
            if z.p is z.p.p.left:
                y = z.p.p.right
                if y.color == 0:
                    z.p.color = 1
                    y.color = 1
                    z.p.p.color = 0
                    z = z.p.p
                else:
                    if z is z.p.right:
                        z = z.p
                        self.rotate(z, True)
                    z.p.color = 1
                    z.p.p.color = 0
                    self.rotate(z.p.p, False)
            else:
                y = z.p.p.left
                if y.color == 0:
                    z.p.color = 1
                    y.color = 1
                    z.p.p.color = 0
                    z = z.p.p
                else:
                    if z is z.p.left:
                        z = z.p
                        self.rotate(z, False)
                    z.p.color = 1
                    z.p.p.color = 0
                    self.rotate(z.p.p, True)
        self.root.color = 1

    def max(self, x):
        x = self._get_node(x)
        while x.right is not self.nil:
            x = x.right
        return x

    def min(self, x):
        x = self._get_node(x)
        while x.left is not self.nil:
            x = x.left
        return x

    def predecessor(self, x):
        x = self._get_node(x)
        if x.left is not self.nil:
            return self.min(x.left)
        y = x.p
        while y is not self.nil and x is y.left:
            x = y
            y = y.p
        return y

    def rotate(self, x, left_rotate):
        x = self._get_node(x)
        if left_rotate:
            self.rotate_left(x)
        else:
            self.rotate_right(x)

    def rotate_left(self, x):
        y = x.right
        x.right = y.left
        if y.left is not self.nil:
            y.left.p = x
        y.p = x.p
        if x.p is self.nil:
            self.root = y
        elif x is x.p.left:
            x.p.left = y
        else:
            x.p.right = y
        y.left = x
        x.p = y

    def rotate_right(self, x):
        y = x.left
        x.left = y.right
        if y.right is not self.nil:
            y.right.p = x
        y.p = x.p
        if x.p is self.nil:
            self.root = y
        elif x is x.p.right:
            x.p.right = y
        else:
            x.p.left = y
        y.right = x
        x.p = y

    def search(self, x, k):
        x = self._get_node(x)
        while x is not self.nil and k != x.key:
            if k < x.key:
                x = x.left
            else:
                x = x.right
        return x

    def successor(self, x):
        x = self._get_node(x)
        if x.right is not self.nil:
            return self.min(x.right)
        y = x.p
        while y is not self.nil and x is y.right:
            x = y
            y = y.p
        return y

    def transplant(self, u, v):
        if u.p is self.nil:
            self.root = v
        elif u is u.p.left:
            u.p.left = v
        else:
            u.p.right = v
        v.p = u.p

    def walk(self, x):
        if x is not self.nil:
            x = self._get_node(x)
            self.walk(x.left)
            if x.key is not None:
                print(x.key)
            self.walk(x.right)


class RBTNode:
    def __init__(self, color, key, parent):
        self.color, self.key, self.p = color, key, parent
        self.left = self.right = None
