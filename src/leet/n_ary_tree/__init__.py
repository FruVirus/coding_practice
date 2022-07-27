"""
N-ary Tree Definition
=====================

If a tree is a rooted tree in which each node has no more than N children, it is called
N-ary tree.

Traversal of N-ary Tree
=======================

Tree Traversal
--------------

A binary tree can be traversed in preorder, inorder, postorder or level-order. Among
these traversal methods, preorder, postorder and level-order traversal are suitable to
be extended to an N-ary tree.

To generalize the above to n-ary trees, you simply replace the steps:

    Traverse the left subtree.... Traverse the right subtree....

in the above by:

    For each child:
        Traverse the subtree rooted at that child by recursively calling the traversal
function

We assume that the for-loop will iterate through the children in the order they are
found in the data-structure: typically, in left-to-right order.
"""
