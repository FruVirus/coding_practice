"""
13 Red-Black Trees
==================

Red-black trees are one of many search-tree schemes that are "balanced" in order to
guarantee that basic dynamic-set operations take O(lg n) time in the worst case.

13.1 Properties of red-black trees
==================================

A red-black tree (RBT) is a binary search tree with one extra bit of storage per node:
its color, which can be either RED (0) or BLACK (1). By constraining the node colors on
any simple path from the root to a leaf, RBTs ensure that no such path is more than
twice as long as any other, so that the tree is approximately balanced.

Each node of the tree now contains the attributes color, key, left, right, and parent.
If a child or the parent of a node does not exist, the corresponding pointer attribute
of the node contains the value NIL. We shall regard these NILs as being pointers to
leaves (external nodes) of the binary search tree and the normal, key-bearing nodes as
being internal nodes of the tree.

A RBT is a binary tree that satisfies the following red-black properties:

1. Every node is either red or black.
2. The root is black.
3. Every leaf (NIL) is black.
4. If a node is red, then both its children are black.
5. For each node, all simple paths from the node to descendant leaves contain the same
number of black nodes.

As a matter of convenience in dealing with boundary conditions in red-black tree code,
we use a single sentinel to represent NIL. For a RBT T, the sentinel T.nil is an object
with the same attributes as an ordinary node in the tree. Its color attribute is BLACK,
and its other attributes---p, left, right, and key---can take on arbitrary values.

We use the sentinel so that we can treat a NIL child of a node x as an ordinary node
whose parent is x. Although we instead could add a distinct sentinel node for each NIL
in the tree, so that the parent of each NIL is well defined, that approach would waste
space. Instead, we use the one sentinel T.nil to represent all the NILs---all leaves and
the root's parent. The values of the attributes p, left, right, and key of the sentinel
are immaterial, although we may set them during the course of a procedure for our
convenience.

We call the number of black nodes on any simple path from, but not including, a node x
down to a leaf the black-height of the node, denoted bh(x). By property 5, the notion of
black-height is well defined, since all descending simple paths from the node have the
same number of black nodes. We define the black-height of a RBT to be the black-height
of its root.

A RBT tree with n internal nodes has height at most 2 * lg(n + 1).

13.2 Rotations
==============

The search-tree operations insert() and delete(), when run on a RBT with n keys, take
O(lg n) time. Because they modify the tree, the result may violate the red-black
properties. To restore these properties, we must change the colors of some of the nodes
in the tree and also change the pointer structure.

We change the pointer structure through rotation, which is a local operation in a search
tree that p[reserves the BST property. When we do a left rotation on a node x, we assume
that its right child y is not T.nil; x may be any node in the tree whose right child is
not T.nil (and vice versa for right rotation).

13.3 Insertion
==============

We can insert a node into an n-node RBT in O(lg n) time. To do so, we use a slightly
modified version of the insert() procedure for BST to insert node z into the tree T as
if it were an ordinary BST, and then we color z red. We color z red instead of black
because if we chose to set the color of z to black, then we would be violating property
5 since any path from the root to a leaf under z would have one more black node than the
paths to the other leaves. To guarantee that the red-black properties are preserved, we
then call an auxiliary procedure insert_fix() to recolor nodes and perform rotations.

Which of the red-black properties might be violated upon the call to insert_fix()?
Property 1 certainly continues to hold, as does property 3, since both children of the
newly inserted red node are the sentinel T.nil. Property 5 is satisfied as well, because
node z replaces the (black) sentinel, and node z is red with sentinel children. Thus,
the only properties that might be violated are properties 2 and 4. Both possible
violations are due to z being colored red. Property 2 is violated if z is the root, and
property 4 is violated if z's parent is red.

13.4 Deletion
=============

Like the other basic operations on an n-node red-black tree, deletion of a node takes
time O(lg n).

The RBT procedure delete() is like the BST deleted() procedure, but with additional
lines of pseudocode. Some of the additional lines keep track of a node y that might
cause violations of the red-black properties. When we want to delete node z and z has
fewer than two children, then z is removed from the tree, and we want y to be z. When z
has two children, then y should be z's successor, and y moves into z's position in the
tree. We also remember y's color before it is removed from or moved within the tree, and
we keep track of the node x that moves into y's original position in the tree, because
node x might also cause violations of the red-black properties. After deleting node z,
delete_fix() is called, which changes colors and performs rotations to restore the
red-black properties.

Complexity
==========

Time
----

insert(), insert_fix(), delete(), delete_fix(), search(), min(), max(), successor(), and
predecessor(): O(lg n).

list(): O(lg n) + O(L) where L is the number of keys returned. O(L) is for the append
operation.

count(), rank(), and update_size(): O(lg n).

rotate_left() and rotate_right(): O(1).

walk(): O(n).
"""


class RBT:
    def __init__(self, z):
        self.nil = RBTNode(1, None, None, 0)
        self.root = RBTNode(1, z, self.nil)
        self.root.left, self.root.right = self.nil, self.nil

    def _get_node(self, x):
        return self.search(self.root, x) if isinstance(x, (int, float)) else x

    def count(self, l, h):
        assert l < h
        count, has_l = self.rank(h) - self.rank(l), self.search(self.root, l)
        if has_l is self.nil or not (has_l or self.search(self.root, h) is self.nil):
            return count
        return count + 1

    def delete(self, z):
        z = self._get_node(z)
        y, y_c = z, z.c
        if z.left is self.nil:
            x = z.right
            self.transplant(z, z.right)
        elif z.right is self.nil:
            x = z.left
            self.transplant(z, z.left)
        else:
            y = self.min(z.right)
            y_c, x = y.c, y.right
            if y.p is not z:
                self.transplant(y, y.right)
                y.right = z.right
                y.right.p = y
            else:
                x.p = y
            self.transplant(z, y)
            y.left = z.left
            y.left.p = y
            y.c = z.c
        if y_c == 1:
            self.delete_fix(x)

    def delete_fix(self, x):
        while x is not self.root and x.c == 1:
            if x is x.p.left:
                w = x.p.right
                if w.c == 0:
                    w.c, x.p.c = 1, 0
                    self.rotate(x.p, True)
                    w = x.p.right
                if w.left.c == 1 and w.right.c == 1:
                    w.c, x = 0, x.p
                else:
                    if w.right.c == 1:
                        w.left.c, w.c = 1, 0
                        self.rotate(w, False)
                        w = x.p.right
                    w.c, x.p.c, w.right.c = x.p.c, 1, 1
                    self.rotate(x.p, True)
                    x = self.root
            else:
                w = x.p.left
                if w.c == 0:
                    w.c, x.p.c = 1, 0
                    self.rotate(x.p, False)
                    w = x.p.left
                if w.right.c == 1 and w.left.c == 1:
                    w.c, x = 0, x.p
                else:
                    if w.left.c == 1:
                        w.right.c, w.c = 1, 0
                        self.rotate(w, True)
                        w = x.p.left
                    w.c, x.p.c, w.left.c = x.p.c, 1, 1
                    self.rotate(x.p, False)
                    x = self.root
        x.c = 1

    def insert(self, z):
        x, y, z = self.root, self.nil, RBTNode(0, z, None)
        while x is not self.nil:
            x.size, x, y = x.size + 1, x.left if z.key < x.key else x.right, x
        z.p = y
        if y is self.nil:
            self.root = z
        elif z.key < y.key:
            y.left = z
        else:
            y.right = z
        z.left, z.right, z.c = self.nil, self.nil, 0
        self.insert_fix(z)
        return z

    def insert_fix(self, z):
        while z.p.c == 0:
            if z.p is z.p.p.left:
                y = z.p.p.right
                if y.c == 0:
                    y.c, z.p.c, z.p.p.c, z = 1, 1, 0, z.p.p
                else:
                    if z is z.p.right:
                        z = z.p
                        self.rotate(z, True)
                    z.p.c, z.p.p.c = 1, 0
                    self.rotate(z.p.p, False)
            else:
                y = z.p.p.left
                if y.c == 0:
                    y.c, z.p.c, z.p.p.c, z = 1, 1, 0, z.p.p
                else:
                    if z is z.p.left:
                        z = z.p
                        self.rotate(z, False)
                    z.p.c, z.p.p.c = 1, 0
                    self.rotate(z.p.p, True)
        self.root.c = 1

    def lca(self, l, h):
        x = self.root
        while x is not self.nil and not l <= x.key <= h:
            x = x.left if l < x.key else x.right
        return x

    def list(self, l, h):
        result, node = [l], self.successor(l)
        while node is not self.nil and node.key <= h:
            result.append(node.key)
            node = self.successor(node)
        return result

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
            return self.max(x.left)
        y = x.p
        while y is not self.nil and x is y.left:
            x, y = y, y.p
        return y

    def rank(self, k):
        r, x = 0, self.root
        while x is not self.nil:
            if k < x.key:
                x = x.left
            else:
                r += 1 + ((x.left and x.left.size) or 0)
                if k == x.key:
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
        if y.left is not self.nil:
            y.left.p = x
        y.p = x.p
        if x.p is self.nil:
            self.root = y
        elif x is x.p.left:
            x.p.left = y
        else:
            x.p.right = y
        y.left, x.p = x, y
        y.size, x.size = x.size, 1 + x.left.size + x.right.size

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
        y.right, x.p = x, y
        y.size, x.size = x.size, 1 + x.left.size + x.right.size

    def search(self, x, k):
        x = self._get_node(x)
        while x is not self.nil and k != x.key:
            x = x.left if k < x.key else x.right
        return x

    def successor(self, x):
        x = self._get_node(x)
        if x.right is not self.nil:
            return self.min(x.right)
        y = x.p
        while y is not self.nil and x is y.right:
            x, y = y, y.p
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
        node = self.min(x)
        while node is not self.nil:
            print(node.key)
            node = self.successor(node)


class RBTNode:
    def __init__(self, color, key, parent=None, size=1):
        self.c, self.key, self.p, self.size = color, key, parent, size
        self.left = self.right = None


rbt = RBT(11)
rbt.insert(2)
rbt.insert(14)
rbt.insert(1)
rbt.insert(7)
rbt.insert(15)
rbt.insert(5)
rbt.insert(8)
assert rbt.root.key == 11
assert rbt.root.c == 1
assert rbt.root.left.key == 2
assert rbt.root.left.c == 0
assert rbt.root.right.key == 14
assert rbt.root.right.c == 1
assert rbt.root.left.left.key == 1
assert rbt.root.left.left.c == 1
assert rbt.root.right.right.key == 15
assert rbt.root.right.right.c == 0
assert rbt.root.left.right.key == 7
assert rbt.root.left.right.c == 1
assert rbt.root.left.right.left.key == 5
assert rbt.root.left.right.left.c == 0
assert rbt.root.left.right.right.key == 8
assert rbt.root.left.right.right.c == 0
rbt.insert(4)
assert rbt.root.key == 7
assert rbt.root.c == 1
assert rbt.root.left.key == 2
assert rbt.root.left.c == 0
assert rbt.root.right.key == 11
assert rbt.root.right.c == 0
assert rbt.root.left.left.key == 1
assert rbt.root.left.left.c == 1
assert rbt.root.right.right.key == 14
assert rbt.root.right.right.c == 1
assert rbt.root.left.right.key == 5
assert rbt.root.left.right.c == 1
assert rbt.root.left.right.left.key == 4
assert rbt.root.left.right.left.c == 0
assert rbt.root.right.left.key == 8
assert rbt.root.right.left.c == 1
assert rbt.root.right.right.right.key == 15
assert rbt.root.right.right.right.c == 0
assert rbt.predecessor(7).key == 5
assert rbt.successor(7).key == 8
assert rbt.predecessor(14).key == 11
assert rbt.successor(14).key == 15
assert rbt.min(7).key == 1
assert rbt.max(7).key == 15
assert rbt.lca(1, 15).key == 7
assert rbt.lca(1, 5).key == 2
assert rbt.lca(14, 15).key == 14
assert rbt.lca(8, 15).key == 11
assert rbt.list(1, 15) == [1, 2, 4, 5, 7, 8, 11, 14, 15]
assert rbt.list(8, 15) == [8, 11, 14, 15]
assert rbt.search(7, 15).key == 15
assert rbt.root.size == 9
assert rbt.root.left.size == 4
assert rbt.root.right.size == 4
assert rbt.root.left.right.size == 2
assert rbt.root.right.right.size == 2
assert rbt.rank(1) == 1
assert rbt.rank(7) == 5
assert rbt.rank(15) == 9
assert rbt.count(1, 15) == 9
assert rbt.count(2, 15) == 8
assert rbt.count(3, 15) == 7
assert rbt.count(4, 15) == 7
assert rbt.count(4, 16) == 7
assert rbt.count(3, 12) == 5
assert rbt.count(4, 11) == 5
rbt.delete(11)
assert rbt.root.key == 7
assert rbt.root.c == 1
assert rbt.root.left.key == 2
assert rbt.root.left.c == 0
assert rbt.root.left.left.key == 1
assert rbt.root.left.left.c == 1
assert rbt.root.left.right.key == 5
assert rbt.root.left.right.c == 1
assert rbt.root.left.right.left.key == 4
assert rbt.root.left.right.left.c == 0
assert rbt.root.right.key == 14
assert rbt.root.right.c == 0
assert rbt.root.right.left.key == 8
assert rbt.root.right.left.c == 1
assert rbt.root.right.right.key == 15
assert rbt.root.right.right.c == 1
rbt.delete(2)
assert rbt.root.key == 7
assert rbt.root.c == 1
assert rbt.root.left.key == 4
assert rbt.root.left.c == 0
assert rbt.root.left.left.key == 1
assert rbt.root.left.left.c == 1
assert rbt.root.left.right.key == 5
assert rbt.root.left.right.c == 1
assert rbt.root.right.key == 14
assert rbt.root.right.c == 0
assert rbt.root.right.left.key == 8
assert rbt.root.right.left.c == 1
assert rbt.root.right.right.key == 15
assert rbt.root.right.right.c == 1
