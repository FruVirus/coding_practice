"""
Implement Queue using Stacks
----------------------------

Implement a first in first out (FIFO) queue using only two stacks. The implemented queue
should support all the functions of a normal queue (push, peek, pop, and empty).

Complexity
==========

Time
----

MyQueue:
    def push(self, val): O(1).
    def pop(self): O(1) amortized.

Space
-----

MyQueue:
    self.s1 and self.s2: O(n).
"""


class Sol:
    def __init__(self):
        self.s1, self.s2 = [], []

    def empty(self):
        return not (self.s1 or self.s2)

    def peek(self):
        if not self.s2:
            while self.s1:
                self.s2.append(self.s1.pop())
        return self.s2[-1]

    def pop(self):
        self.peek()
        return self.s2.pop()

    def push(self, val):
        self.s1.append(val)
