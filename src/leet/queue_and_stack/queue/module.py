"""
Design Circular Queue
---------------------

Design your implementation of the circular queue. The circular queue is a linear data
structure in which the operations are performed based on FIFO (First In First Out)
principle and the last position is connected back to the first position to make a
circle. It is also called "Ring Buffer".

One of the benefits of the circular queue is that we can make use of the spaces in front
of the queue. In a normal queue, once the queue becomes full, we cannot insert the next
element even if there is a space in front of the queue. But using the circular queue, we
can use the space to store new values.

Complexity
==========

Time
----

All: O(1).

Space
-----

self.queue: O(n).
"""


class MyCircularQueue:
    def __init__(self, k):
        self.capacity, self.count, self.head_index, self.queue = k, 0, 0, [0] * k

    def dequeue(self):
        if self.is_empty():
            return False
        self.head_index = (self.head_index + 1) % self.capacity
        self.count -= 1
        return True

    def enqueue(self, value):
        if self.is_full():
            return False
        self.queue[(self.head_index + self.count) % self.capacity] = value
        self.count += 1
        return True

    def front(self):
        return -1 if self.is_empty() else self.queue[self.head_index]

    def is_empty(self):
        return self.count == 0

    def is_full(self):
        return self.count == self.capacity

    def rear(self):
        if self.is_empty():
            return -1
        return self.queue[(self.head_index + self.count - 1) % self.capacity]
