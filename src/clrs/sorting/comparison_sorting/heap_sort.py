"""
Overview
========

HeapSort is a class that implements heap sorting on an unordered input array.

1. _exchange() is a helper method to exchange two elements in the queue array.

2. _left() and _right() computes the indices of a node's left child and right child,
respectively, given the node index i.

3. build(), which runs in O(n) time, produces a heap (either maximum or minimum) from an
unordered input array using heapify() and builds the heap in a bottom-up manner.
heapify(), which runs in O(lg(n)) time, maintains the heap (either maximum or minimum)
property. Whenever heapify() is called, the two subtrees of that node are both heaps
(either maximum or minimum).

4. sort(), which which runs in O(n * lg(n)) time, sorts an unordered array in place. It
sorts the unordered input array by first building an initial heap, then moving the 0-th
item in the heap array to the i-th element. Each time the movement is conducted, the
heap array is rebuilt with a smaller heap size.

Heap sort is an asymptotically optimal comparison sort.

Complexity
==========

Not stable
O(n * lg(n))
"""

# Repository Library
from src.clrs.queues.heap_queue import HeapQueue


class HeapSort(HeapQueue):
    def sort(self):
        assert self.heap_size > 0
        for i in range(len(self.a) - 1, 0, -1):
            self._exchange(0, i)
            self.heap_size -= 1
            self.heapify(0)
