"""
Find Median from Data Stream
----------------------------

The median is the middle value in an ordered integer list. If the size of the list is
even, there is no middle value and the median is the mean of the two middle values.

Complexity
==========

Time
----

MedianFinder: O(5 * lg n) + O(1) = O(lg n).

Space
-----

MedianFinder: O(n).
"""

# Standard Library
import heapq


class MedianFinder:
    def __init__(self):
        self.max_heap, self.min_heap = [], []

    def add_num(self, num):
        heapq.heappush(self.max_heap, -num)
        heapq.heappush(self.min_heap, -self.max_heap[0])
        heapq.heappop(self.max_heap)
        if len(self.max_heap) < len(self.min_heap):
            heapq.heappush(self.max_heap, -self.min_heap[0])
            heapq.heappop(self.min_heap)

    def find_median(self):
        if len(self.max_heap) > len(self.min_heap):
            return -self.max_heap[0]
        return (-self.max_heap[0] + self.min_heap[0]) / 2
