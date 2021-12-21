"""
Overview
========

Quicksort, like merge sort, is a divide and conquer algorithm that sorts in place.

For a typical sub-array A[p...r]:

Divide: Partition (rearrange) the array A[p...r] into two (possibly empty) sub-arrays
A[p...q - 1] and A[q + 1...r] such that each element of A[p...q - 1] is less than or
equal to A[q], which is, in turn, less than or equal to each element of A[q + 1...r].
Compute the index q as part of this partitioning procedure.

partition() selects an element x = A[r] as a pivot element around which to partition the
sub-array A[p...r]. As the procedure runs, it partitions the array into four (possible
empty) regions. At the start of each iteration of the for-loop, the regions satisfy
certain properties:

For any array index k,

1. If p <= k <= i, then A[k] <= x
2. If i + 1 <= k <= j - 1, then A[k] > x
3. If k = r, then A[k] = x
4. The sub-array A[j...r - 1] can take on any values

Conquer: Sort the two sub-arrays A[p...q - 1] and A[q + 1...r] by recursive calls to
quicksort.

Combine: Because the sub-arrays are already sorted, no work is needed to combine them:
the entire array A[p...r] is now sorted.

Note that quicksort has in-place partition but is NOT an in-place algorithm due to the
extra stack space required with each recursive call. The running time of quicksort is
dominated by the time spent in the partition() function.

To sort an entire array A, the initial call is quicksort(A, 0, len(A) - 1).

Complexity
==========

quicksort():
    O(n^2) worst case --> when the partitioning routine produces one sub-problem with
        n - 1 elements and one with 0 elements or when the input array is already sorted
    O(n*lg(n)) expected case --> when we can equally balance the two sides of the
        partition at every level of the recursion (only possible when we can choose the
        median value with each recursion)

partition():
    O(n) = O(h - l + 1)
"""

# Standard Library
import random


def quicksort(a, low, high):
    while low < high:
        pivot = partition(a, low, high)
        if pivot - low < high - pivot:
            quicksort(a, low, pivot - 1)
            low = pivot + 1
        else:
            quicksort(a, pivot + 1, high)
            high = pivot - 1


def partition(a, low, high, pivot_index=None, random_partition=True):
    if random_partition:
        r = random.randrange(low, high + 1)
        a[high], a[r] = a[r], a[high]
    elif pivot_index is not None:
        a[high], a[pivot_index] = a[pivot_index], a[high]
    x, i = a[high], low - 1
    for j in range(low, high):
        if a[j] <= x:
            i += 1
            a[i], a[j] = a[j], a[i]
    a[high], a[i + 1] = a[i + 1], a[high]
    return i + 1
