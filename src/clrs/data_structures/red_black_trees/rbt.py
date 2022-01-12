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

Intuition
---------

Insertion into a RBT consists of two phases. The first phase goes down the tree from the
root, inserting the new node as a child of an existing node. The second phase goes up
the tree, changing colors and performing rotations to maintain the red-black properties.

In the second phase, the only structural changes to the underlying RBT are caused by
rotations, of which there are at most two.

When we insert, we color the inserted node RED. As a result, we can potentially violate
properties 2 and 4. Thus, we need to fix it. If the inserted node is the root, the fix
is to simply color the inserted node BLACK. Otherwise, during the fix, we care about the
color of the inserted node's uncle (i.e., the sibling of the inserted node's parent)
and whether the inserted node is a left or right child of its parent. The three cases
are then:

1. z's uncle y is red.
2. z's uncle y is black and z is a right child (we transform this to case 3)
3. z's uncle y is black and z is a left child

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

We maintain node y as the node either removed from the tree or moved within the tree.
When z has fewer than two children, y points to z and z is removed. When z has two
children, y points to z's successor and y will move into z's position in the tree.

Because node y's color might change, the variable y_c stores y's color before any
changes occur. We need to save y's original color in order to test it at the end of
delete(); if it was black, then removing or moving y could cause violations of the
red-black properties.

We keep track of the node x that moves into node y's original position. x points to
either y's only child or, if y has no children, the sentinel T.nil (recall that y has no
left child).

Since node x moves into node y's original position, the attribute x.p is always set to
point to the original position in the tree of y's parent, even if x is, in fact, the
sentinel T.nil. Unless z is y's original parent, the assigment to x.p takes place in the
transplant() procedure.

When y's original parent is z, however, we do not want x.p to point to y's original
parent, z, since we are removing that node from the tree. Because node y will move up to
take z's position in the tree, setting x.p to y causes x.p to point to the original
position of y's parent, even if x = T.nil.

Finally, if node y was black, we might have introduced one or more violations of the
red-black properties, and so we call delete_fix() to restore the red-black properties.
If y was red, the red-black properties still hold when y is removed or moved, for the
following reasons:

    1. No black-heights in the tree have changed.
    2. No red nodes have been made adjacent. Because y takes z's place in the tree,
    along with z's color, we cannot have two adjacent red nodes at y's new position in
    the tree. In addition, if y was not z's right child, then y's original right child x
    replaces y in the tree. If y is red, then x must be black, and so replacing y by x
    cannot cause two red nodes to become adjacent.
    3. Since y could not have been the root if it was red, the root remains black.

If node y was black, three problems may arise, which the call of delete_fix() will
remedy. First, if y had been the root and a red child of y becomes the new root, we have
violated property 2. Second, if both x and x.p are red, then we have violated property
4. Third, moving y within the tree causes any simple path that previously contained y
to have one fewer black node. Thus, property 5 is now violated by any ancestor of y in
the tree. We can correct the violation of property 5 by saying that node x, now
occupying y's original position, has an "extra" black. That is, if we add 1 to the count
of black nodes on any simple path that contains x, then under this interpretation,
property 5 holds. When we remove or move the black node y, we "push" its blackness onto
node x. The problem is that now node x is neither red nor black, thereby violating
property 1. Instead, node x is either "doubly" black or "red-and-black," and it
contributes either 2 or 1, respectively, to the count of black nodes on simple paths
containing x. The color attribute of x will still be either RED (if x is red-and-black)
or BLACK (if x is doubly black). In other words, the extra black on a node is reflected
in x's pointing to the node rather than in the color attribute.

Intuition
---------

Deletion from a RBT also consists of two phases: the first operates on the underlying
search tree, and the second causes at most three rotations and otherwise performs no
structural changes. The first phase removes one node z from the tree and could move up
to two other nodes within the tree (nodes y and x).

When we delete, we can violate property 5 if the color of the deleted node is BLACK. If
the color of the deleted node is RED, then we just perform a normal (more or less) BST
delete. WHen a fix is required, we care about the color of the sibling (w) of the node
(x) that moves into the deleted node's (y) position. The four cases are then:

1. x's sibling w is red.
2. x's sibling w is black, and both of w's children are black.
3. x's sibling w is black, w's left child is red, and w's right child is black (we
transform this to case 4).
4. x's sibling w is black, and w's right child is red.

In all cases, we essentially perform rotations and/or re-colorings in order to maintain
property 5 in some form or fashion.

Complexity
==========

Time
----

delete(), delete_fix(), insert(), and insert_fix(): O(lg n).
"""

# Repository Library
from src.clrs.data_structures.binary_search_trees.avl import AVL
from src.clrs.data_structures.binary_search_trees.bst import BSTNode


class RBT(AVL):
    def __init__(self, z):
        sentinel = RBTNode(1, None, None, 0)
        super().__init__(RBTNode(1, z, sentinel), sentinel)
        self.root.left = self.root.right = self.sentinel

    def delete(self, z):
        z = self._get_node(z)
        y_c = z.c
        if z.left is self.sentinel:
            x = z.right
            self.transplant(z, z.right)
        elif z.right is self.sentinel:
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
        while x is not self.sentinel:
            self.update_size(x)
            x = x.p

    def delete_fix(self, x):
        while x is not self.root and x.c == 1:
            if x is x.p.left:
                w = x.p.right
                if w.c == 0:
                    w.c, x.p.c = 1, 0
                    self.rotate(x.p, True)
                    w = x.p.right
                if w.left.c == w.right.c == 1:
                    w.c, x = 0, x.p
                else:
                    if w.right.c == 1:
                        w.left.c, w.c = 1, 0
                        self.rotate(w, False)
                        w = x.p.right
                    w.c, w.right.c, x.p.c = x.p.c, 1, 1
                    self.rotate(x.p, True)
                    x = self.root
            else:
                w = x.p.left
                if w.c == 0:
                    w.c, x.p.c = 1, 0
                    self.rotate(x.p, False)
                    w = x.p.left
                if w.left.c == w.right.c == 1:
                    w.c, x = 0, x.p
                else:
                    if w.left.c == 1:
                        w.right.c, w.c = 1, 0
                        self.rotate(w, True)
                        w = x.p.left
                    w.c, w.left.c, x.p.c = x.p.c, 1, 1
                    self.rotate(x.p, False)
                    x = self.root
        x.c = 1

    def insert(self, z):
        x, y, z = self.root, self.sentinel, RBTNode(0, z, self.sentinel)
        while x is not self.sentinel:
            x.size, x, y = x.size + 1, x.left if z.key < x.key else x.right, x
        z.p = y
        if y is self.sentinel:
            self.root = z
        elif z.key < y.key:
            y.left = z
        else:
            y.right = z
        z.left, z.right, z.c = self.sentinel, self.sentinel, 0
        self.insert_fix(z)

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


class RBTNode(BSTNode):
    def __init__(self, color, key, parent=None, size=1):
        super().__init__(key, parent, size)
        self.c = color
