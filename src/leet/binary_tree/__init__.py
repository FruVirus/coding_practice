"""
Traverse a Tree - Introduction
==============================

Pre-order Traversal
-------------------

Pre-order traversal is to visit the root first. Then traverse the left subtree. Finally,
traverse the right subtree. Here is an example:

In-order Traversal
------------------

In-order traversal is to traverse the left subtree first. Then visit the root. Finally,
traverse the right subtree.

Post-order Traversal
--------------------

Post-order traversal is to traverse the left subtree first. Then traverse the right
subtree. Finally, visit the root.

It is worth noting that when you delete nodes in a tree, deletion process will be in
post-order. That is to say, when you delete a node, you will delete its left child and
its right child before you delete the node itself.

Also, post-order is widely use in mathematical expression. It is easier to write a
program to parse a post-order expression.

Binary Tree Traversal - Solution
================================

Iterative Solution
------------------

There are several iterative solutions for tree traversal. One of the solutions is to use
a stack to simulate the recursion process.

Taking pre-order traversal as an example, in each iteration, we pop one node from the
stack and visit this node. Then if this node has a right child, push its right child
into the stack. If this node has a left child, push its left child into the stack. It is
noteworthy that we push the right child first so that we can visit the left child first
since the nature of the stack is LIFO (last in first out). After that, we can continue
to the next iteration until the stack is empty.

Complexity Analysis
-------------------

As we mentioned before, we can traverse a tree recursively to retrieve all the data in
pre-order, in-order or post-order. The time complexity is O(N) because we visit each
node exactly once. And the depth of the tree might be N in the worst case. That is to
say, the level of recursion might be at most N in the worst case. Therefore, taking
system stack into consideration, the space complexity is O(N) as well.

To be cautious, the complexity might be different due to a different implementation. It
is comparatively easy to do traversal recursively but when the depth of the tree is too
large, we might suffer from stack overflow problem. That's one of the main reasons why
we want to solve this problem iteratively sometimes.

For the iterative solution, the time complexity is apparently the same with recursion
solution which is O(N). The space complexity is also O(N) since in the worst case, we
will have all the nodes in the stack. There are some other solutions for iterative
traversal which can reduce the space complexity to O(1).

Level-order Traversal - Introduction
====================================

Level-order traversal is to traverse the tree level by level.

Breadth-First Search is an algorithm to traverse or search in data structures like a
tree or a graph. The algorithm starts with a root node and visit the node itself first.
Then traverse its neighbors, traverse its second level neighbors, traverse its third
level neighbors, so on and so forth.

When we do breadth-first search in a tree, the order of the nodes we visited is in level
order.

Typically, we use a queue to help us to do BFS.

Solve Tree Problems Recursively
===============================

As we know, a tree can be defined recursively as a node (the root node) that includes a
value and a list of references to children nodes. Recursion is one of the natural
features of a tree. Therefore, many tree problems can be solved recursively. For each
recursive function call, we only focus on the problem for the current node and call the
function recursively to solve its children.

Typically, we can solve a tree problem recursively using a top-down approach or using a
bottom-up approach.

"Top-down" Solution
-------------------

"Top-down" means that in each recursive call, we will visit the node first to come up
with some values, and pass these values to its children when calling the function
recursively. So the "top-down" solution can be considered as a kind of preorder
traversal.

"Bottom-up" Solution
--------------------

"Bottom-up" is another recursive solution. In each recursive call, we will firstly call
the function recursively for all the children nodes and then come up with the answer
according to the returned values and the value of the current node itself. This process
can be regarded as a kind of postorder traversal.


"""
