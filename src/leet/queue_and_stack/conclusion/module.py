"""
Implement Queue using Stacks
----------------------------

Implement a first in first out (FIFO) queue using only two stacks. The implemented queue
should support all the functions of a normal queue (push, peek, pop, and empty).

Implement Stack using Queues
----------------------------

Implement a last-in-first-out (LIFO) stack using only two queues. The implemented stack
should support all the functions of a normal stack (push, top, pop, and empty).

Complexity
==========

Time
----

QueueStack:
    self.push(): O(1).
    self.pop(): O(1) amortized.

StackQueue:
    self.push(): O(n).
    self.pop(): O(1).

Space
-----

QueueStack:
    self.s1 and self.s2: O(n).

StackQueue:
    self.q1: O(n).
"""

# Standard Library
from collections import deque


class QueueStack:
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


class StackQueue:
    def __init__(self):
        self.q1 = deque()

    def empty(self):
        return len(self.q1) == 0

    def pop(self):
        return self.q1.popleft()

    def push(self, val):
        self.q1.append(val)
        len_ = len(self.q1)
        while len_ > 1:
            self.q1.append(self.q1.popleft())
            len_ -= 1

    def top(self):
        return self.q1[0]
