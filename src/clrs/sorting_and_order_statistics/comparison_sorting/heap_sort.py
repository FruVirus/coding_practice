"""
6 Heapsort
==========

Like merge sort, but unlike insertion sort, heapsort's running time is O(n * lg n). Like
insertion sort, but unlike merge sort, heapsort sorts in place: only a constant number
of array elements are stored outside the input array at any time.

Heapsort uses a data structure called a "heap" to manage information. Not only is the
heap data structure useful for heapsort, but it also makes an efficient priority queue.

6.3 The heapsort algorithm
==========================

The heapsort algorithm starts by using build() to build a max-heap on the input array
A[1...n], where n = A.length. Since the maximum element of the array is stored at the
root A[1], we can put it into its correct final position by exchanging it with A[n]. If
we now discard node n from the heap---and we can do so by simply decrementing
A.heap-size---we observe that the children of the root remain max-heaps, but the new
root element might violate the max-heap property. All we need to do to restore the
max-heap property, however, is call heapify(), which leaves a max-heap in A[1...n - 1].
The heapsort algorithm then repeats this process for the max-heap of size n - 1 down to
a heap of size 2.

sort() sorts the unordered input array by first building an initial heap, then moving
the 0-th item in the heap array to the i-th element of the for-loop. Each time the
movement is conducted, the heap array is rebuilt with a smaller heap size.

Heapsort is an asymptotically optimal comparison sort.

Heapsort is not stable.

Complexity
==========

Time
----

sort(): O(n * lg n).
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
