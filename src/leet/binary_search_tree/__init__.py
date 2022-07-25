"""
Definition of the Binary Search Tree
====================================

A binary search tree (BST), a special form of a binary tree, satisfies the binary search
property:

1. The value in each node must be greater than (or equal to) any values stored in its
left subtree.
2. The value in each node must be less than (or equal to) any values stored in its right
subtree.

Like a normal binary tree, we can traverse a BST in preorder, inorder, postorder or
level-order. However, it is noteworthy that inorder traversal in BST will be in
ascending order. Therefore, the inorder traversal is the most frequent used traversal
method of a BST.

Search in a BST - Introduction
==============================

BSTs support three main operations: search, insertion and deletion. In this section, we
are going to talk about how to search for a specific value in a BST.

According to the property of BST, for each node:

1. return the node if the target value is equal to the value of the node;
2. continue searching in the left subtree if the target value is less than the value of
the node;
3. continue searching in the right subtree if the target value is larger than the value
of the node.

Search in a BST - Solution
==========================

Let's discuss the time complexity and space complexity of the search operation in a BST
whose height is h. Focus on the recursion solution first. In the worse case, the depth
of our recursion is equal to the height of the tree. Therefore, the time complexity of
the recursion solution is O(h). And taking system stack into consideration, the space
complexity should be O(h) in the worst case as well.

What about the iterative solution? The time complexity will be equal to the loop time
which is also O(h) while the space complexity is O(1) since we do not need system stack
anymore in an iterative solution.

    Question:

    If you do not know the height of the BST h but you are given the total number of
nodes N of the BST, can you express the time complexity and space complexity using N
instead of h?

    Hint:

    What's the difference of the relationship between N and h in the best case and the
relationship in the worst case?

    Answer:

    Best case O(lg N). Worst case O(n).

Insertion in a Binary Search Tree - Introduction
================================================

Another common operation in BST is to insert a new node. There are many different
strategies for insertion. We only talk about a typical insertion strategy which
minimizes the changes. The main idea is to find out a proper leaf position for the
target node and then insert the node as a leaf. Therefore, insertion will begin as a
search.

Similar to our search strategy, for each node, we will:

    1. search the left or right subtrees according to the relation of the value of the
node and the value of our target node;
    2. repeat STEP 1 until reaching an external node;
    3. add the new node as its left or right child depending on the relation of the
value of the node and the value of our target node.

In this way, we add a new node and maintain the property of BST.

Deletion in a BST - Introduction
================================

Deletion is more complicated than the two operations we mentioned before. There are also
many different strategies for deletion. We are going to introduce one of them which
minimizes the changes. Our solution is to replace the target node with a proper child.
According to the number of its children, we should consider three different cases:

1. If the target node has no child, we can simply remove the node.
2. If the target node has one child, we can use its child to replace itself.
3. If the target node has two children, replace the node with its in-order successor or
predecessor node and delete that node.

Introduction to Binary Search Tree - Conclusion
===============================================

The strength of a BST is that you can perform all search, insertion and deletion
operations in O(h) time complexity even in the worst case.

Usually, if you want to store data in order and need several operations, such as search,
insertion or deletion, at the same time, a BST might be a good choice.

Introduction to the Height-Balanced BST
=======================================

In this article, we are going to help you understand the general concept of a balanced
BST.

What is a Height-Balanced BST?
------------------------------

    Terminology used in trees:

        - Depth of node - the number of edges from the tree's root node to the node
        - Height of node - the number of edges on the longest path between that node and
a leaf
        - Height of Tree - the height of its root node

A height-balanced (or self-balancing) binary search tree is a binary search tree that
automatically keeps its height small in the face of arbitrary item insertions and
deletions. That is, the height of a balanced BST with N nodes is always log N. Also, the
height of the two subtrees of every node never differs by more than 1.

Using the definition, we can determine if a BST is height-balanced (Balanced Binary
Tree).

As we mentioned before, the height of a balanced BST with N nodes is always log N. We
can calculate the total number of nodes and the height of the tree to determine if this
BST is a height-balanced BST.

Also, in the definition, we mentioned a property of height-balanced BST: the depth of
the two subtrees of every node never differ by more than 1. We can also validate the
tree recursively according to this rule.

Why Using a Height-Balanced BST?
--------------------------------

We have introduced binary search tree and related operations, including search,
insertion and deletion in the previous article. When we analyze the time complexity of
these operations, it is worth noting that the height of the tree is the most important
factor. Taking search operation as an example, if the height of the BST is h, the time
complexity will be O(h). The height of the BST really matters.

So let's discuss the relationship between the number of nodes N and the height of the
tree h. For a height-balanced BST, as we discussed in the previous section, h >= log N.
But for a normal BST, in the worst case, it can degenerate into a chain.

Therefore, the height of a BST with N nodes can vary from log N to N. That is, the time
complexity of search operation can vary from log N to N. It is a huge difference in the
performance.

Therefore, a height-balanced BST play an important role in improving the performance.

How to Implement a Height-Balanced BST?
---------------------------------------

There are several different implementations for height-balanced BSTs. The details of
these implementations are different but they have similar goals:

1. The data structure should satisfy the binary search property and the height-balanced
property.
2. The data structure should support the basic operations of BST, including search,
insertion and deletion within O(log N) time even in worst case.

We provide a list of popular height-balanced BSTs for your reference:

- Red-black tree
- AVL tree
- Splay tree
- Treap

Practical Application of the Height-balanced BST
------------------------------------------------

The height-balanced BST is widely used in practice since it can provide search,
insertion and deletion operations all in O(log N) time complexity.

The most profound use is in set/map. The principle of set and map are similar. We will
focus on the set in the following discussion.

    Set is another data structure which can store a lot of keys without any particular
order or any duplicate elements. The basic operations it should support are to insert
new elements into the set and to check if an element is in the set or not.

Typically, there are two kinds of sets which are widely used: hash set and tree set.

The tree set, TreeSet in Java or set in C++, is implemented by the height-balanced BST.
Therefore, the time complexity of search, insertion and deletion are all O(log N).

The hash set, HashSet in Java or unordered_set in C++, is implemented by hash, but the
height-balanced BST also plays an important role in hash set. When there are too many
elements with the same hash key, it will cost O(N) time complexity to look up for a
specific element, where N is the number of elements with the same hash key. Typically,
the height-balanced BST will be used here to improve the performance from O(N) to
O(log N).

The essential difference between the hash set and the tree set is that keys in the tree
set are ordered.

Conclusion
----------

A height-balanced BST is a special form of BST which aims at improving the performance.
"""
