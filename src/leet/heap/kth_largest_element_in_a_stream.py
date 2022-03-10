"""
Kth Largest Element in a Stream
-------------------------------

Design a class to find the kth largest element in a stream. Note that it is the kth
largest element in the sorted order, not the kth distinct element.

Implement KthLargest class:

    KthLargest(int k, int[] nums) Initializes the object with the integer k and the
stream of integers nums.
    int add(int val) Appends the integer val to the stream and returns the element
representing the kth largest element in the stream.

Complexity
==========

Time
----

KthLargest:
    def __init__(self, k, nums): O(n * lg n).
    def add(self, val): O(m * lg k), where m is the number of calls to add().

Space
-----

KthLargest:
    self.heap: O(n).
"""

# Standard Library
import heapq


class Sol:
    def __init__(self, k, nums):
        self.k, self.heap = k, nums
        heapq.heapify(self.heap)
        while len(self.heap) > self.k:
            heapq.heappop(self.heap)

    def add(self, val):
        heapq.heappush(self.heap, val)
        if len(self.heap) > self.k:
            heapq.heappop(self.heap)
        return self.heap[0]
