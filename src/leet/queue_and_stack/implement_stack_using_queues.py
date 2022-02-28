"""
Implement Stack using Queues
----------------------------

Implement a last-in-first-out (LIFO) stack using only two queues. The implemented stack
should support all the functions of a normal stack (push, top, pop, and empty).

Complexity
==========

Time
----

StackQueue:
    self.push(): O(n).
    self.pop(): O(1).

Space
-----

StackQueue:
    self.q1: O(n).
"""

# Standard Library
from collections import deque


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
