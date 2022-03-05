"""
The K Weakest Rows in a Matrix
------------------------------

You are given an m x n binary matrix mat of 1's (representing soldiers) and 0's
(representing civilians). The soldiers are positioned in front of the civilians. That
is, all the 1's will appear to the left of all the 0's in each row.

A row i is weaker than a row j if one of the following is true:

    The number of soldiers in row i is less than the number of soldiers in row j.
    Both rows have the same number of soldiers and i < j.

Return the indices of the k weakest rows in the matrix ordered from weakest to
strongest.

Complexity
==========

Time
----

kWeakestRows(mat, k): O(m * lg (n * k)).

Space
-----

kWeakestRows(mat, k): O(k).
"""

# Standard Library
import heapq


def kWeakestRows(mat, k):
    heap, rows = [], []

    def get_num_ones(row):
        low, high = 0, len(mat[0])
        while low < high:
            mid = low + (high - low) // 2
            if row[mid] == 1:
                low = mid + 1
            else:
                high = mid
        return low

    for i, row in enumerate(mat):
        entry = (-get_num_ones(row), -i)
        if len(heap) < k or entry > heap[0]:
            heapq.heappush(heap, entry)
        if len(heap) > k:
            heapq.heappop(heap)
    while heap:
        rows.append(-heapq.heappop(heap)[1])
    return rows[::-1]
