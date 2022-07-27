"""
Definition and Classification of Heap
=====================================

Priority Queues
---------------

Before introducing a Heap, let's first talk about a Priority Queue.

Wikipedia: a priority queue is an abstract data type similar to a regular queue or stack
data structure in which each element additionally has a "priority" associated with it.
In a priority queue, an element with high priority is served before an element with low
priority.

In daily life, we would assign different priorities to tasks, start working on the task
with the highest priority and then proceed to the task with the second highest priority.
This is an example of a Priority Queue.

A common misconception is that a Heap is the same as a Priority Queue, which is not
true. A priority queue is an abstract data type, while a Heap is a data structure.
Therefore, a Heap is not a Priority Queue, but a way to implement a Priority Queue.

There are multiple ways to implement a Priority Queue, such as array and linked list.
However, these implementations only guarantee O(1) time complexity for either insertion
or deletion, while the other operation will have a time complexity of O(N). On the other
hand, implementing the priority queue with Heap will allow both insertion and deletion
to have a time complexity of O(log N). So, what is a Heap?

Definition of Heap
------------------

According to Wikipedia, a Heap is a special type of binary tree. A heap is a binary tree
that meets the following criteria:

    - Is a complete binary tree;
    - The value of each node must be no greater than (or no less than) the value of its
child nodes.

A Heap has the following properties:

    - Insertion of an element into the Heap has a time complexity of O(log N);
    - Deletion of an element from the Heap has a time complexity of O(log N);
    - The maximum/minimum value in the Heap can be obtained with O(1) time complexity.

Classification of Heap
----------------------

There are two kinds of heaps: Max Heap and Min Heap.

    - Max Heap: Each node in the Heap has a value no less than its child nodes.
Therefore, the top element (root node) has the largest value in the Heap.
    - Min Heap: Each node in the Heap has a value no larger than its child nodes.
Therefore, the top element (root node) has the smallest value in the Heap.

Heap Insertion
==============

Insertion means adding an element to the Heap. After inserting the element, the
properties of the Heap should remain unchanged.

Heap Deletion
=============

Deletion means removing the “top” element from the Heap. After deleting the element, the
property of Heap should remain unchanged.

Implementation of a Heap
========================

We often perform insertion, deletion, and getting the top element with a Heap data
structure.

We can implement a Heap using an array. Elements in the Heap can be stored in the array
in the form of a binary tree. The code below will implement “Max Heap” and “Min Heap”
for integers.

Construct a Heap
================

Constructing a Heap means initializing an instance of a Heap. All methods of Heap need
to be performed on an instance. Therefore, we need to initialize an instance before
applying the methods. When creating a Heap, we can simultaneously perform the heapify
operation. Heapify means converting a group of data into a Heap.

Time complexity: O(N).
Space complexity: O(N).

Python Max Heap Video
---------------------

Python's built-in heap module, heapq, differs from the standard implementation of a heap
in two ways. Firstly, it uses zero-based indexing, and this means that it stores the
root node at index zero instead of the size of the heap. As a result, the relationship
between the index of the children and parent nodes is slightly different. Secondly, the
built-in heapq module does not offer a direct way to create a max heap. Instead, we must
modify the value(s) of each element when inserting it into the heap and when removing it
from the heap.

Inserting an Element
====================

Insertion means inserting a new element into the Heap. Note that, after the new element
is inserted, properties of the Heap are still maintained.

Time complexity: O(log N).
Space complexity: O(1).

Getting the Top Element of the Heap
===================================

The top element of a Max heap is the maximum value in the Heap, while the top element of
a Min Heap is the smallest value in the Heap. The top element of the Heap is the most
important element in the Heap.

Time complexity: O(1).
Space complexity: O(1).

Deleting the top element
========================

Note that, after deleting the top element, the properties of the Heap will still hold.
Therefore, the new top element in the Heap will be the maximum (for Max Heap) or minimum
(for Min Heap) of the current Heap.

Time complexity: O(log N).
Space complexity: O(1).

Getting the Length of a Heap
============================

The length of the Heap can be used to determine the size of the current heap, and it can
also be used to determine if the current Heap is empty. If there are no elements in the
current Heap, the length of the Heap is zero.

Time complexity: O(1).
Space complexity: O(1).


"""
