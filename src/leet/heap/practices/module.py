"""
Top K Frequent Elements
-----------------------

Given an integer array nums and an integer k, return the k most frequent elements. You
may return the answer in any order.

Kth Smallest Element in a Sorted Matrix
---------------------------------------

Given an n x n matrix where each of the rows and columns is sorted in ascending order,
return the kth smallest element in the matrix.

Note that it is the kth smallest element in the sorted order, not the kth distinct
element.

You must find a solution with a memory complexity better than O(n^2).

Find Median from Data Stream
----------------------------

The median is the middle value in an ordered integer list. If the size of the list is
even, there is no middle value and the median is the mean of the two middle values.

Complexity
==========

Time
----

KthSmallest: min(n, k) + k * lg(min(n, k)).

MedianFinder: O(5 * lg n) + O(1) = O(lg n).

TopKFrequent: O(n).

Space
-----

KthSmallest: O(min(n, k)).

MedianFinder: O(n).

TopKFrequent: O(n).
"""

# pylint: disable=R0201

# Standard Library
import heapq

from collections import Counter


class KthSmallest:
    def kth_smallest(self, matrix, k):
        min_heap = [(matrix[r][0], r, 0) for r in range(min(len(matrix), k))]
        heapq.heapify(min_heap)
        while k > 0:
            val, r, c = heapq.heappop(min_heap)
            if c < len(matrix[0]) - 1:
                heapq.heappush(min_heap, (matrix[r][c + 1], r, c + 1))
            k -= 1
        return val


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


class TopKFrequent:
    def topk_frequent(self, nums, k):
        b = [[] for _ in range(len(nums) + 1)]
        for num, freq in Counter(nums).items():
            b[freq].append(num)
        flat = [item for sublist in b for item in sublist]
        return flat[len(flat) - k :]
