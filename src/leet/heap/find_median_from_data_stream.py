"""
Find Median from Data Stream
----------------------------

The median is the middle value in an ordered integer list. If the size of the list is
even, there is no middle value and the median is the mean of the two middle values.

Intuition
---------

We get the median value from the max heap if there are more elements in the max heap
than the min heap. Otherwise, we take the average of the top two values from the max
and min heaps.

Since we move the top value from the min heap to the max heap, this ensures that the
value at the top of the max heap is the median.

Complexity
==========

Time
----

MedianFinder:
    def __init__(self): O(1).
    def add_num(self, val): O(5 * lg n) + O(1) = O(lg n).
    def find_median(self): O(1).

Space
-----

MedianFinder:
    self.max_heap and self.min_heap: O(n).
"""

# Standard Library
import heapq


class Sol:
    def __init__(self):
        self.max_heap, self.min_heap = [], []

    def add_num(self, val):
        heapq.heappush(self.max_heap, -val)
        heapq.heappush(self.min_heap, -heapq.heappop(self.max_heap))
        if len(self.max_heap) < len(self.min_heap):
            heapq.heappush(self.max_heap, -heapq.heappop(self.min_heap))

    def find_median(self):
        if len(self.max_heap) > len(self.min_heap):
            return -self.max_heap[0]
        return (-self.max_heap[0] + self.min_heap[0]) / 2
