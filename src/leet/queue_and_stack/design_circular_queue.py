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

Sol:
    All: O(1).

Space
-----

Sol:
    self.queue: O(n).
"""


class Sol:
    def __init__(self, k):
        self.capacity, self.count, self.head_index, self.queue = k, 0, 0, [0] * k

    def dequeue(self):
        if self.empty():
            return False
        self.count -= 1
        self.head_index = (self.head_index + 1) % self.capacity
        return True

    def empty(self):
        return self.count == 0

    def enqueue(self, val):
        if self.full():
            return False
        self.count += 1
        self.queue[self.tail_index()] = val
        return True

    def full(self):
        return self.count == self.capacity

    def head(self):
        return -1 if self.empty() else self.queue[self.head_index]

    def tail(self):
        return -1 if self.empty() else self.queue[self.tail_index()]

    def tail_index(self):
        return (self.head_index + self.count - 1) % self.capacity
