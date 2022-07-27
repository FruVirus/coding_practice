"""
Introduction - Singly Linked List
=================================

Each node in a singly-linked list contains not only the value but also a reference field
to link to the next node. By this way, the singly-linked list organizes all the nodes in
a sequence.

Operations
----------

Unlike the array, we are not able to access a random element in a singly-linked list in
constant time. If we want to get the ith element, we have to traverse from the head node
one by one. It takes us O(N) time on average to visit an element by index, where N is
the length of the linked list.

Add Operation - Singly Linked List
==================================

If we want to add a new value after a given node prev, we should:

    1. Initialize a new node cur with the given value;
    2. Link the "next" field of cur to prev's next node next;
    2. Link the "next" field in prev to cur.

Unlike an array, we don’t need to move all elements past the inserted element.
Therefore, you can insert a new node into a linked list in O(1) time complexity, which
is very efficient.

Delete Operation - Singly Linked List
=====================================

If we want to delete an existing node cur from the singly linked list, we can do it in
two steps:

    1. Find cur's previous node prev and its next node next;
    2. Link prev to cur's next node next.

In our first step, we need to find out prev and next. It is easy to find out next using
the reference field of cur. However, we have to traverse the linked list from the head
node to find out prev which will take O(N) time on average, where N is the length of the
linked list. So the time complexity of deleting a node will be O(N).

The space complexity is O(1) because we only need constant space to store our pointers.

Two-Pointer in Linked List
==========================

Let's start with a classic problem:

    Given a linked list, determine if it has a cycle in it.

Imagine there are two runners with different speed. If they are running on a straight
path, the fast runner will first arrive at the destination. However, if they are running
on a circular track, the fast runner will catch up with the slow runner if they keep
running.

That's exactly what we will come across using two pointers with different speed in a
linked list:

    1. If there is no cycle, the fast pointer will stop at the end of the linked list.
    2. If there is a cycle, the fast pointer will eventually meet with the slow pointer.

So the only remaining problem is:

    What should be the proper speed for the two pointers?

It is a safe choice to move the slow pointer one step at a time while moving the fast
pointer two steps at a time. For each iteration, the fast pointer will move one extra
step. If the length of the cycle is M, after M iterations, the fast pointer will
definitely move one more cycle and catch up with the slow pointer.

Introduction - Doubly Linked List
=================================

Definition
----------

The doubly linked list works in a similar way but has one more reference field which is
known as the "prev" field. With this extra field, you are able to know the previous node
of the current node.

Operations
----------

We can access data in the same exact way as in a singly linked list:

    1. We are not able to access a random position in constant time.
    2. We have to traverse from the head to get the i-th node we want.
    3. The time complexity in the worse case will be O(N), where N is the length of the
linked list.

For addition and deletion, it will be a little more complicated since we need to take
care of the "prev" field as well.

Add Operation - Doubly Linked List
----------------------------------

If we want to insert a new node cur after an existing node prev, we can divide this
process into two steps:

    1. Link cur with prev and next, where next is the original next node of prev;
    2. Re-link the prev and next with cur.

Similar to the singly linked list, both the time and the space complexity of the add
operation are O(1).

Delete Operation - Doubly Linked List
-------------------------------------

If we want to delete an existing node cur from the doubly linked list, we can simply
link its previous node prev with its next node next.

    Unlike the singly linked list, it is easy to get the previous node in constant time
with the "prev" field.

Since we no longer need to traverse the linked list to get the previous node, both the
time and space complexity are O(1).

Summary - Linked List
=====================

Review
------

Let's briefly review the performance of the singly linked list and doubly linked list.

They are similar in many operations:

    1. Both of them are not able to access the data at a random position in constant
time.
    2. Both of them can add a new node after given node or at the beginning of the list
in O(1) time.
    3. Both of them can delete the first node in O(1) time.

But it is a little different to delete a given node (including the last node).

    - In a singly linked list, it is not able to get the previous node of a given node
so we have to spend O(N) time to find out the previous node before deleting the given
node.
    - In a doubly-linked list, it will be much easier because we can get the previous
node with the "prev" reference field. So we can delete a given node in O(1) time.

If you need to add or delete a node frequently, a linked list could be a good choice.
If you need to access an element by index often, an array might be a better choice than
a linked list.
"""
