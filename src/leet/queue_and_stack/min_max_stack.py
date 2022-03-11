"""
Min/Max Stack
----------------------------

Design a stack that supports push, pop, top, and retrieving the minimum element in
constant time.

Implement the MinStack class:

    MinStack() initializes the stack object.
    void push(int val) pushes the element val onto the stack.
    void pop() removes the element on the top of the stack.
    int top() gets the top element of the stack.
    int getMin() retrieves the minimum element in the stack.

Complexity
==========

Time
----

MinStack:
    All: O(1).

Space
-----

MinStack:
    self.stack and self.min_stack: O(n).
"""


class Sol:
    def __init__(self):
        self.stack, self.min_stack = [], []

    def get_min(self):
        return self.min_stack[-1][0]

    def pop(self):
        if self.min_stack[-1][0] == self.stack[-1]:
            self.min_stack[-1][1] -= 1
        if self.min_stack[-1][1] == 0:
            self.min_stack.pop()
        return self.stack.pop()

    def push(self, val):
        self.stack.append(val)
        if not self.min_stack or val < self.min_stack[-1][0]:
            self.min_stack.append([val, 1])
        elif val == self.min_stack[-1][0]:
            self.min_stack[-1][1] += 1

    def top(self):
        return self.stack[-1]
