"""In a queue, the element deleted is always the one that has been set for the longest
time: queue implements a first-in, first-out, or FIFO, policy.

The queue has a head and a tail. When an element is enqueued, it takes its place at the
tail of the queue. The element dequeued is always the one at the head of the queue.

An array, Q, of size n can implement a queue of at almost n - 1 elements. The queue has
an attribute Q.head that indexes, or points to, its head. The attribute Q.tail indexes
the next location at which a newly arriving element will be inserted into the queue.

The elements in the queue reside in locations Q.head, Q.head + 1, ..., Q.tail - 1, where
we "wrap around" in the sense that location 1 immediately follows location n in a
circular order. When Q.head == Q.tail, the queue is empty. Initially,
Q.head = Q.tail = 1. If we attempt to dequeue an element from an empty queue, the queue
underflows. When Q.head = Q.tail + 1 or both Q.head = 1 and Q.tail = Q.length, the queue
is full, and if we attempt to enqueue an element, then the queue underflows.

NB: Queue mimics table doubling for practice even though it's redundant in Python.

enqueue() and dequeue() each take O(1) time.
"""


class Queue:
    def __init__(self, size, table_double=False):
        self.size = size
        self.table_double = table_double
        self.a = [None] * self.size
        self.head = self.tail = 0

    def _grow(self):
        if self.tail == self.size - 1:
            self.a = self.a + [None] * self.size
            self.size *= 2

    def _reduce(self):
        x = self.a[self.head]
        if self.tail - self.head + 1 == self.size // 4 or self.size // 4 <= 1:
            start = self.head + 1
            end = start + self.size // 2
            self.a = [self.a[i] for i in range(start, end)]
            self.size = int(self.size / 2)
            self.tail = self.tail - self.head - 1
            self.head = 0
        else:
            self.head += 1
        return x

    def dequeue(self):
        if not self.table_double:
            assert self.head != self.tail
            x = self.a[self.head]
            if self.head == self.size - 1:
                self.head = 0
            else:
                self.head += 1
            return x
        return self._reduce()

    def enqueue(self, x):
        if not self.table_double:
            assert self.head != self.tail + 1
            assert not (self.head == 0 and self.tail == self.size - 1)
            self.a[self.tail] = x
            if self.tail == self.size - 1:
                self.tail = 0
            else:
                self.tail += 1
        else:
            self._grow()
            self.a[self.tail] = x
            self.tail += 1
