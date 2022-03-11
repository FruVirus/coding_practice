"""
Kth Smallest Element in a Sorted Matrix
---------------------------------------

Given an n x n matrix where each of the rows and columns is sorted in ascending order,
return the kth smallest element in the matrix.

Note that it is the kth smallest element in the sorted order, not the kth distinct
element.

You must find a solution with a memory complexity better than O(n^2).

Complexity
==========

Time
----

kthSmallest(matrix, k): O(min(n, k) + k * lg(min(n, k))).

Space
-----

kthSmallest(matrix, k): O(min(n, k)).
"""

# Standard Library
import heapq


def sol(matrix, k):
    heap = [(matrix[r][0], r, 0) for r in range(min(len(matrix), k))]
    heapq.heapify(heap)
    while k > 0:
        val, r, c = heapq.heappop(heap)
        if c < len(matrix[0]) - 1:
            heapq.heappush(heap, (matrix[r][c + 1], r, c + 1))
        k -= 1
    return val
