"""
Overview
========

HeapQueue is a class that implements a heap-based priority queue.

1. _exchange() is a helper method to exchange two elements in the queue array and runs
in O(1) time.

2. _left(), _parent(), and _right() computes the indices of a node's left child, parent,
and right child, respectively, given the node index i. These methods run in O(1) time.

3. build(), which runs in O(n) time, produces a heap (either maximum or minimum) from an
unordered input array using heapify() and builds the heap in a bottom-up manner. Only
half the length of the input array needs to be iterated over since a heap is a complete
binary tree, which means that approximately half the nodes are leaves that do not need
to be moved at all during the build process. heapify(), which runs in O(lg(n)) time,
maintains the heap (either maximum or minimum) property. Whenever heapify() is called,
the two subtrees of that node are both heaps (either maximum or minimum).

4. extract() extracts the maximum/minimum element from the heap. For max heaps, the
priority is that the largest number will always be maintained at the root node. With
each heap element extraction, the largest number is taken out and removed from the
array, and the rest of the heap is then re-heapified to maintain its max heap state.
Vice versa for min heaps. extract() runs in O(lg(n)) time.

5. get() simply returns the maximum/minimum element from the heap and runs in O(1) time.

6. insert() inserts an element into the key at the correct heap position. change()
changes the value of an element's key to a new value, which is assumed to be at least as
large as the value's current key value. Both insert() and change() runs in O(lg(n))
time.

Complexity
==========

build(): O(n)
change: O(lg(n))
extract(): O(lg(n))
insert(): O(lg(n))
heapify(): O(lg(n))
all others: O(1)

Overall: O(n * lg(n))
"""

# Standard Library
from operator import gt, lt


class HeapQueue:
    def __init__(self, a, is_max):
        self.a = a
        self.is_max = is_max
        self.compare = gt if self.is_max else lt
        self.heap_size = len(self.a)
        self.build()

    def _exchange(self, i, j):
        self.a[i], self.a[j] = self.a[j], self.a[i]

    @staticmethod
    def _left(i):
        return 2 * i + 1

    @staticmethod
    def _parent(i):
        return (i - 1) // 2

    @staticmethod
    def _right(i):
        return 2 * i + 2

    def build(self):
        for i in reversed(range(len(self.a) // 2)):
            self.heapify(i)

    def change(self, i, k):
        assert self.compare(k, self.a[i])
        self.a[i] = k
        while i > 0 and self.compare(self.a[i], self.a[self._parent(i)]):
            self._exchange(i, self._parent(i))
            i = self._parent(i)

    def extract(self):
        assert self.heap_size > 0
        self.heap_size -= 1
        self._exchange(0, self.heap_size)
        self.heapify(0)
        return self.a.pop(-1)

    def get(self):
        return self.a[0]

    def heapify(self, i):
        l, r, index = self._left(i), self._right(i), i
        if l < self.heap_size and self.compare(self.a[l], self.a[i]):
            index = l
        if r < self.heap_size and self.compare(self.a[r], self.a[index]):
            index = r
        if index != i:
            self._exchange(i, index)
            self.heapify(index)

    def insert(self, k):
        self.a.append(-float("inf") if self.is_max else float("inf"))
        self.change(self.heap_size, k)
        self.heap_size += 1
