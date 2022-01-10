"""
12 Binary Search Trees
======================

The search tree data structure supports many dynamic-set operations, including search,
minimum, maximum, predecessor, successor, insert, and delete. Thus, we can use a search
tree both as a dictionary and as a priority queue.

Basic operations on a binary search tree take time proportional to the height of the
tree. For a complete binary tree with n nodes, such operations run in Theta(lg n) worst
case time. If the tree is a linear chain of n nodes, however, the same operations take
Theta(n) worst case time. The expected height of a randomly built binary search tree is
O(lg n), so that basic dynamic-set operations on such a tree take Theta(lg n) time on
average.

12.1 What is a binary search tree?
==================================

A binary search tree is organized, as the name suggests, in a binary tree. We can
represent such a tree by a linked data structure in which each node is an object. In
addition to a key and satellite data, each node contains attributes left, right, and p
that point to the nodes corresponding to its left child, its right child, and its
parent, respectively. If a child or the parent is missing, the appropriate attribute
contains the value NIL. The root node is the only node in the tree whose parent is NIL.

The keys in a binary search tree are always stored in such a way as to satisfy the
binary-search-tree property:

    Let x be a node in a binary search tree. If y is a node in the left subtree of x,
    then y.key <= x.key. If y is a node in the right subtree of x, then y.key >= x.key.

count(l, h) returns the number of keys in the range [l, h].

lca(l, h) produces the root of the smallest subtree (i.e., the lowest common ancestor)
that contains keys between [l, h]. If l and h do not exist in the tree, lca() returns
the lowest-common ancestor of the two nodes that would be created by inserting l and h.

list(l, h) produces a list of all the keys between [l, h].

rank(x) returns the rank of node x. rank() does NOT assume that the keys of the tree are
distinct. We can think of node x's rank as the number of nodes preceding x in an inorder
tree walk, plus 1 for x itself.

rank_key(k) returns the number of keys in the tree that are less than or equal to k.
Informally, if the keys were listed in ascending order, x's key rank would indicate its
position in the sorted array. rank_key() assumes that the keys of the tree are distinct!

select() finds the node with the i-th smallest key the tree.

update_size() updates the size attribute of a node in the BST. The size attribute of a
node indicates how many nodes are rooted at that subtree including the subtree root node
itself. Thus, the root of the overall BST would contain the highest number for its size
attribute since every single node is rooted at the root.

Complexity
==========

Time
----

If the BST is balanced, then O(h) = O(lg n).

count(), delete(), insert(), lca(), min(), max(), predecessor(), rank(), rank_key(),
search(), select(), successor(), and update_size(): O(h).

list(): O(h) + O(L) where L is the number of keys returned. O(L) is for the append
operation.

walk(): O(n).
"""


class BST:
    def __init__(self, z, sentinel=None):
        self.root = BSTNode(z) if isinstance(z, (int, float)) else z
        self.sentinel = sentinel

    def _get_node(self, x):
        return self.search(self.root, x) if isinstance(x, (int, float)) else x

    def count(self, l, h):
        assert l < h
        count = self.rank_key(h) - self.rank_key(l)
        return count if self.search(self.root, l) is self.sentinel else count + 1

    def delete(self, z):
        z = self._get_node(z)
        if z.left is self.sentinel:
            self.transplant(z, z.right)
        elif z.right is self.sentinel:
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
        x, y = self.root, self.sentinel
        if isinstance(z, (int, float)):
            z = BSTNode(z)
        while x is not self.sentinel:
            x, y = x.left if z.key < x.key else x.right, x
        z.p = y
        if y is self.sentinel:
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
        while x is not self.sentinel and not l <= x.key <= h:
            x = x.left if l < x.key else x.right
        return x

    def list(self, l, h):
        result, node = [l], self.successor(l)
        while node is not self.sentinel and node.key <= h:
            result.append(node.key)
            node = self.successor(node)
        return result

    def max(self, x):
        x = self._get_node(x)
        while x.right is not self.sentinel:
            x = x.right
        return x

    def min(self, x):
        x = self._get_node(x)
        while x.left is not self.sentinel:
            x = x.left
        return x

    def predecessor(self, x):
        x = self._get_node(x)
        if x.left is not self.sentinel:
            return self.max(x.left)
        y = x.p
        while y is not self.sentinel and x is y.left:
            x, y = y, y.p
        return y

    def rank(self, x):
        r, y = 1 + ((x.left and x.left.size) or 0), x
        while y is not self.root:
            if y is y.p.right:
                r += 1 + ((y.p.left and y.p.left.size) or 0)
            y = y.p
        return r

    def rank_key(self, k):
        r, x = 0, self.root
        while x is not self.sentinel:
            if k < x.key:
                x = x.left
            else:
                r += 1 + ((x.left and x.left.size) or 0)
                if k == x.key:
                    return r
                x = x.right
        return r

    def search(self, x, k):
        x = self._get_node(x)
        while x is not self.sentinel and k != x.key:
            x = x.left if k < x.key else x.right
        return x

    def select(self, i, x=None):
        x = x or self.root
        r = 1 + ((x.left and x.left.size) or 0)
        if i == r:
            return x
        return self.select(i, x.left) if i < r else self.select(i - r, x.right)

    def successor(self, x):
        x = self._get_node(x)
        if x.right is not self.sentinel:
            return self.min(x.right)
        y = x.p
        while y is not self.sentinel and x is y.right:
            x, y = y, y.p
        return y

    def transplant(self, u, v):
        if u.p is self.sentinel:
            self.root = v
        elif u is u.p.left:
            u.p.left = v
        else:
            u.p.right = v
        if v is not self.sentinel or self.sentinel is not None:
            v.p = u.p

    def update_size(self, x):
        if x is self.sentinel:
            return
        x.size = 1 + ((x.left and x.left.size) or 0) + ((x.right and x.right.size) or 0)
        self.update_size(x.left)
        self.update_size(x.right)

    def walk(self, x):
        node = self.min(x)
        while node is not self.sentinel:
            print(node.key)
            node = self.successor(node)


class BSTNode:
    def __init__(self, key, parent=None, size=1):
        self.key, self.p, self.size = key, parent, size
        self.left = self.right = None
