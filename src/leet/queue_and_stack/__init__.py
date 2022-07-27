"""
First-in-first-out Data Structure
=================================

In a FIFO data structure, the first element added to the queue will be processed first.

The queue is a typical FIFO data structure. The insert operation is also called enqueue
and the new element is always added at the end of the queue. The delete operation is
called dequeue. You are only allowed to remove the first element.

Circular Queue
==============

Previously, we have provided a straightforward but inefficient implementation of queue.

A more efficient way is to use a circular queue. Specifically, we may use a fixed-size
array and two pointers to indicate the starting position and the ending position. And
the goal is to reuse the wasted storage we mentioned previously.

In a circular queue, we use an array and two pointers, head and tail. head indicates the
start position of the queue while tail indicates the ending position of the queue.

Queue and BFS
=============

One common application of Breadth-first Search (BFS) is to find the shortest path from
the root node to the target node.

Insights
--------

1. What is the processing order of the nodes?

In the first round, we process the root node. In the second round, we process the nodes
next to the root node; in the third round, we process the nodes which are two steps from
the root node; so on and so forth.

Similar to tree's level-order traversal, the nodes closer to the root node will be
traversed earlier.

If a node X is added to the queue in the kth round, the length of the shortest path
between the root node and X is exactly k. That is to say, you are already in the
shortest path the first time you find the target node.

2. What is the enqueue and dequeue order of the queue?

We first enqueue the root node. Then in each round, we process the nodes which are
already in the queue one by one and add all their neighbors to the queue. It is worth
noting that the newly-added nodes will not be traversed immediately but will be
processed in the next round.

The processing order of the nodes is the exact same order as how they were added to the
queue, which is First-in-First-out (FIFO). That's why we use a queue in BFS.

BFS - Template
==============

We have already introduced two main scenarios of using BFS: do traversal or find the
shortest path. Typically, it happens in a tree or a graph. As we mentioned in the
chapter description, BFS can also be used in more abstract scenarios.

    It will be important to determine the nodes and the edges before doing BFS in a
specific question. Typically, the node will be an actual node or a status while the edge
will be an actual edge or a possible transition.

Sometimes, it is important to make sure that we never visit a node twice. Otherwise, we
might get stuck in an infinite loop, e.g. in graph with cycle.

There are some cases where one does not need keep the visited hash set:

    1. You are absolutely sure there is no cycle, for example, in tree traversal;
    2. You do want to add the node to the queue multiple times.

Last-in-first-out Data Structure
================================

In a LIFO data structure, the newest element added to the queue will be processed first.

Different from the queue, the stack is a LIFO data structure. Typically, the insert
operation is called push in a stack. Similar to the queue, a new element is always added
at the end of the stack. However, the delete operation, pop, will always remove the last
element which is opposite from the queue.

Stack and DFS
=============

Similar to BFS, Depth-First Search (DFS) can also be used to find the path from the root
node to the target node.

Insights
--------

1. What is the processing order of the nodes?

We start from the root node A. Firstly, we choose the path to the node B and trace-back
till we reach the node E where we have no way to go deeper. Then we backtrack to A and
choose the second path to the node C. From C, We try the first path to E but E has been
visited. So we go back to C and try another path to F. Finally, we find G.

Overall, we only trace-back and try another path after we reach the deepest node.

As a result, the first path you found in DFS is not always the shortest path. For
instance, in the example above, we successfully found a path A->C->F->G and stop the
DFS. But this is not the shortest path from A to G.

2. What is the push and pop order of the stack?

We first push the root node to the stack; then we try the first neighbor B and push node
B to the stack; so on and so forth. When we reach the deepest node E, we need to trace
back. And when we trace back, we will pop the deepest node from the stack which is
actually the last node pushed to the stack.

The processing order of the nodes is the exact opposite order as how they were added to
the stack, which is Last-in-First-out (LIFO). That's why we use a stack in DFS.

DFS - Template I
================

As we mentioned in the chapter's description, in most cases, we can also use DFS when
using BFS. But there is an important difference: the traversal order.

Different from BFS, the nodes you visit earlier might not be the nodes which are closer
to the root node. As a result, the first path you found in DFS might not be the shortest
path.

DFS - Template II
=================

The advantage of the recursion solution is that it is easier to implement. However,
there is a huge disadvantage: if the depth of recursion is too high, you will suffer
from stack overflow. In that case, you might want to use BFS instead or implement DFS
using an explicit stack.

The logic is exactly the same with the recursion solution. But we use while loop and
stack to simulate the system call stack during recursion.
"""
