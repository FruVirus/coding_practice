"""
Kth Smallest Element in a Sorted Matrix
---------------------------------------

Given an n x n matrix where each of the rows and columns is sorted in ascending order,
return the kth smallest element in the matrix.

Note that it is the kth smallest element in the sorted order, not the kth distinct
element.

You must find a solution with a memory complexity better than O(n^2).

Intuition
---------

Since the matrix rows and columns are already sorted, we only need to consider min(n, k)
rows since numbers in rows greater than k cannot contain the kth smallest element by
definition. As such, we add the numbers in the first columns for those rows to the heap.
Once we heapify the heap, the smallest element will be at the top of the heap.

As we iterate through k, we add numbers from the popped off row and next column into
the heap. The heap will keep the smallest element on top.

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
