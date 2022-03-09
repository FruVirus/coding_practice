"""
Binary Search Tree Iterator
---------------------------

Implement the BSTIterator class that represents an iterator over the in-order traversal
of a binary search tree (BST):

    BSTIterator(TreeNode root) Initializes an object of the BSTIterator class. The root
of the BST is given as part of the constructor. The pointer should be initialized to a
non-existent number smaller than any element in the BST.
    boolean hasNext() Returns true if there exists a number in the traversal to the
right of the pointer, otherwise returns false.
    int next() Moves the pointer to the right, then returns the number at the pointer.

Notice that by initializing the pointer to a non-existent smallest number, the first
call to next() will return the smallest element in the BST.

You may assume that next() calls will always be valid. That is, there will be at least a
next number in the in-order traversal when next() is called.

Complexity
==========

Time
----

BSTIterator:
    def __init__(self, root): O(n).
    def inorder_leftmost(self, root): O(n).
    def next(self): O(1) amortized.
    def has_next(self): O(1).

Space
-----

BSTIterator:
    All: O(n).
"""


class Sol:
    def __init__(self, root):
        self.stack = []
        self.inorder_leftmost(root)

    def has_next(self):
        return len(self.stack) > 0

    def inorder_leftmost(self, root):
        while root:
            self.stack.append(root)
            root = root.left

    def next(self):
        node = self.stack.pop()
        self.inorder_leftmost(node.right)
        return node.val
