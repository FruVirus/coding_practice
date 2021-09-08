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

2. All other operations take O(lg(n)) time.
"""


class RB:
    def __init__(self):
        self.root = None

    def delete(self, k):
        node = self.search(k)
        if node is None:
            return None
        if node is self.root:
            temp_root = RBNode(None, 0)
            temp_root.left = self.root
            self.root.parent = temp_root
            deleted = self.root.delete()
            self.root = temp_root.left
            if self.root is not None:
                self.root.parent = None
            self.delete_fix(deleted)
            return deleted
        deleted, x, orig_c = node.delete()
        if orig_c == 1:
            if x is None:
                x = RBNode(None, None, c=1)
            self.delete_fix(x)
        return deleted

    def delete_fix(self, x):
        while x is not self.root and x.c == 1:
            if x is x.parent.left:
                w = x.parent.right
                if w.c == 0:
                    w.c = 1
                    x.parent.c = 0
                    self.rotate(x.parent.key, left_rotate=True)
                    w = x.parent.right
                if w.left.c == 1 and w.right.c == 1:
                    w.c = 0
                    x = x.parent
                else:
                    if w.right.c == 1:
                        w.left.c = 1
                        w.c = 0
                        self.rotate(w.key, left_rotate=False)
                        w = x.parent.right
                    w.c = x.parent.c
                    x.parent.c = 1
                    w.right.c = 1
                    self.rotate(x.parent.key, left_rotate=True)
                    x = self.root
            else:
                w = x.parent.left
                if w.c == 0:
                    w.c = 1
                    x.parent.c = 0
                    self.rotate(x.parent.key, left_rotate=False)
                    w = x.parent.left
                if w.right.c == 1 and w.left.c == 1:
                    w.c = 0
                    x = x.parent
                else:
                    if w.left.c == 1:
                        w.right.c = 1
                        w.c = 0
                        self.rotate(w.key, left_rotate=True)
                        w = x.parent.left
                    w.c = x.parent.c
                    x.parent.c = 1
                    w.left.c = 1
                    self.rotate(x.parent.key, left_rotate=False)
                    x = self.root
        x.c = 1

    def insert(self, k):
        node = RBNode(None, k, 1 if self.root is None else 0)
        if self.root is None:
            self.root = node
        else:
            self.root.insert(node)
        self.insert_fix(node)

    def insert_fix(self, node):
        while node.parent is not None and node.parent.c == 0:
            if node.parent is node.parent.parent.left:
                uncle = node.parent.parent.right
                if uncle.c == 0:
                    node.parent.c = 1
                    uncle.c = 1
                    node.parent.parent.c = 0
                    node = node.parent.parent
                else:
                    if node is node.parent.right:
                        node = node.parent
                        self.rotate(node.key, left_rotate=True)
                    node.parent.c = 1
                    node.parent.parent.c = 0
                    self.rotate(node.parent.parent.key, left_rotate=False)
            else:
                uncle = node.parent.parent.left
                if uncle.c == 0:
                    node.parent.c = 1
                    uncle.c = 1
                    node.parent.parent.c = 0
                    node = node.parent.parent
                else:
                    if node is node.parent.left:
                        node = node.parent
                        self.rotate(node.key, left_rotate=False)
                    node.parent.c = 1
                    node.parent.parent.c = 0
                    self.rotate(node.parent.parent.key, left_rotate=True)
        self.root.c = 1

    def max(self):
        return self.root and self.root.max()

    def min(self):
        return self.root and self.root.min()

    def predecessor(self, k):
        node = self.search(k)
        return node and node.predecessor()

    def rotate(self, k, left_rotate=True):
        node = self.search(k)
        if node is None:
            return
        parent = node.parent
        y = node.rotate(left_rotate)
        if parent is None:
            self.root = y

    def search(self, k):
        return self.root and self.root.search(k)

    def successor(self, k):
        node = self.search(k)
        return node and node.successor()

    def walk(self):
        if self.root is not None:
            self.root.walk(self.root.left)
            print(self.root.key)
            self.root.walk(self.root.right)


class RBNode:
    def __init__(self, parent, k, c=0):
        self.key, self.parent, self.c = k, parent, c
        self.left = self.right = None

    def delete(self):
        orig_c = self.c
        if self.left is None or self.right is None:
            if self is self.parent.left:
                x = self.left or self.right
                self.parent.left = self.left or self.right
                if self.parent.left is not None:
                    self.parent.left.parent = self.parent
            else:
                x = self.left or self.right
                self.parent.right = self.left or self.right
                if self.parent.right is not None:
                    self.parent.right.parent = self.parent
            return self, x, orig_c
        s = self.successor()
        s_orig_c = s.c
        x = s.right
        if s.parent is self:
            x.parent = s
        else:
            self.key, s.key = s.key, self.key
        self.c, s.c = s.c, self.c
        return s.delete(), x, s_orig_c

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

    def rotate(self, left_rotate=True):
        if left_rotate:
            return self.rotate_left()
        return self.rotate_right()

    def rotate_left(self):
        y = self.right
        self.right = y.left
        if y.left is not None:
            y.left.parent = self
        y.parent = self.parent
        if self.parent is not None:
            if self is self.parent.left:
                self.parent.left = y
            else:
                self.parent.right = y
        y.left = self
        self.parent = y
        return y

    def rotate_right(self):
        x = self.left
        self.left = x.right
        if x.right is not None:
            x.right.parent = self
        x.parent = self.parent
        if self.parent is not None:
            if self is self.parent.right:
                self.parent.right = x
            else:
                self.parent.left = x
        x.right = self
        self.parent = x
        return x

    def search(self, k):
        if k == self.key:
            return self
        if k < self.key:
            return self.left.search(k)
        return self.right.search(k)

    def successor(self):
        if self.right is not None:
            return self.right.min()
        current = self
        while current.parent is not None and current is current.parent.right:
            current = current.parent
        return current.parent

    def walk(self, node):
        if node is not None:
            self.walk(node.left)
            print(node.key)
            self.walk(node.right)


rb = RB()
rb.insert(11)
rb.insert(2)
rb.insert(14)
rb.insert(15)
rb.insert(1)
rb.insert(7)
rb.insert(5)
rb.insert(8)
rb.insert(4)
rb.walk()
print()
print()
print(rb.root.key, rb.root.c)
print(rb.search(7).c)
print(rb.search(2).c)
print(rb.search(11).c)
print(rb.search(1).c)
print(rb.search(5).c)
print(rb.search(8).c)
print(rb.search(14).c)
print(rb.search(4).c)
print(rb.search(15).c)
print()
print()
rb.delete(11)
print(rb.search(14).c)

# rb.insert(26)
# rb.insert(17)
# rb.insert(41)
# rb.insert(14)
# rb.insert(21)
# rb.insert(30)
# rb.insert(47)
# rb.insert(10)
# rb.insert(16)
# rb.insert(19)
# rb.insert(23)
# rb.walk()
# rb.rotate(17)
# print()
# print()
# rb.walk()
# print()
# print()
# node = rb.search(21)
# print(node.key)
# print(node.parent.key)
# print(node.left.key)
# print(node.right.key)
# print()
# print()
# node = rb.search(17)
# print(node.key)
# print(node.parent.key)
# print(node.left.key)
# print(node.right.key)
# print()
# print()
# node = rb.search(14)
# print(node.key)
# print(node.parent.key)
# print(node.left.key)
# print(node.right.key)
# print()
# print()
# rb.rotate(26)
# print(rb.root.key)
# print(rb.root.parent)
# print(rb.root.left.key)
# print(rb.root.right.key)
# print(rb.root.right.parent.key)
# print(rb.root.right.left)
# print(rb.root.right.right)
# print()
# print()
# rb.rotate(41, left_rotate=False)
# rb.rotate(21, left_rotate=False)
# rb.walk()
# print()
# print()
# print(rb.root.key)
# print(rb.root.parent)
# print(rb.root.left.key)
# print(rb.root.right.key)
