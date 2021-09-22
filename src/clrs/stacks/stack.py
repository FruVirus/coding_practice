"""In a stack, the element deleted from the set is the one most recently inserted: the
stack implements a last-in, first-out, or LIFO, policy.

We can implement a stack of at most n elements with an array, S, of size n. The array
has an attribute S.top that indexes the most recently inserted element. When S.top = -1,
the stack contains no elements and is empty. When S.top == n, then the stack overflows.

NB: Stack mimics table doubling for practice even though it's redundant in Python.

Each of the stack operations take O(1).
"""


class Stack:
    def __init__(self, size, table_double=False):
        self.size = size
        self.table_double = table_double
        self.a = [None] * self.size
        self.top = -1

    def _grow(self):
        if self.top + 1 == self.size:
            self.a = self.a + [None] * self.size
            self.size *= 2

    def _reduce(self):
        if self.top + 1 == self.size // 4:
            self.a = [self.a[i] for i in range(self.size // 2)]
            self.size = int(self.size / 2)

    def empty(self):
        return self.top == -1

    def full(self):
        return self.top + 1 == self.size

    def pop(self):
        assert not self.empty()
        self.top -= 1
        if self.table_double:
            self._reduce()
        return self.a[self.top + 1]

    def push(self, x):
        if self.table_double:
            self._grow()
        else:
            assert not self.full()
        self.top += 1
        self.a[self.top] = x
