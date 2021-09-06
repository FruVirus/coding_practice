"""In a stack, the element deleted from the set is the one most recently inserted: the
stack implements a last-in, first-out, or LIFO, policy.

We can implement a stack of at most n elements with an array, S, of size n. The array
has an attribute S.top that indexes the most recently inserted element. When S.top = -1,
the stack contains no elements and is empty. When S.top == n, then the stack overflows.

Each of the stack operations take O(1).
"""


class Stack:
    def __init__(self, size):
        self.size = size
        self.a = [None] * self.size
        self.top = -1

    def empty(self):
        return True if self.top == -1 else False

    def pop(self):
        assert self.top != -1
        self.top -= 1
        return self.a[self.top + 1]

    def push(self, x):
        assert self.top + 1 != self.size
        self.top += 1
        self.a[self.top] = x


size = 10
item = list(range(size))
stack = Stack(size)
for i in range(size):
    stack.push(i)
assert stack.a == item
for i in range(size):
    assert stack.pop() == item[size - i - 1]
assert stack.empty()
