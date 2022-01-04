"""
9.2 Selection in expected linear time
=====================================

As in quicksort, we partition the input array recursively. But unlike quicksort, which
recursively processes both sides of the partition, random_select() works on only one
side of the partition.

The base case of the recursion occurs when the the subarray A[p...r] consists of just
one element. In this case, i must equal 1, and we simply return A[p] as the i-th
smallest element. Otherwise, we partition the array A[p...r] into two (possibly empty)
subarrays A[p...q - 1] and A[q + 1...r] such that each element of A[p...q - 1] is less
than or equal to A[q], which in turn is less than each element of A[q + 1...r]. As in
quicksort, we refer to A[q] as the pivot element. k is the number of elements in the
subarray A[p...q], that is, the number of elements in the low side of the partition,
plus one for the pivot element. If i == k, then A[q] is the i-th smallest element.
Otherwise, the algorithm determines in which of the two subarrays A[p...q - 1] and
A[q + 1...r] the i-th smallest element lies. If i < k, then the desired element lies on
the low side of the partition. If i > k, however, then the desired element lies on the
high side of the partition. Since we already know k values that are smaller than the
i-th smallest element of A[p...r]---namely, the elements of A[p...q]---the desired
element is the (i - k)-th smallest element of A[q + 1...r].

Complexity
==========

Time
----

random_select(): E[O(n)], Theta(n^2) worst case.
"""

# Repository Library
from src.clrs.sorting_and_order_statistics.sorting.comparison_sorting.quicksort import (
    partition,
)


def random_select(a, low, high, i):
    if low == high:
        return a[low]
    pivot = partition(a, low, high)
    k = pivot - low + 1
    if i == k:
        return a[pivot]
    if i < k:
        return random_select(a, low, pivot - 1, i)
    return random_select(a, pivot + 1, high, i - k)
