"""
7 Quicksort
===========

The quicksort algorithm has a worst-case running time of Theta(n^2) on an input array of
n numbers. Despite this slow worst-case running time, quicksort is often the best
practical choice for sorting because it is remarkably efficient on the average: its
expected running time is Theta(n * lg n), and the constant factors hidden in the
Theta(n * lg n) notation are quite small. It also has the advantage of sorting in place.

7.1 Description of quicksort
============================

Quicksort, like merge sort, is a divide and conquer algorithm that sorts in place.

For a typical sub-array A[p...r]:

Divide: Partition (rearrange) the array A[p...r] into two (possibly empty) sub-arrays
A[p...q - 1] and A[q + 1...r] such that each element of A[p...q - 1] is less than or
equal to A[q], which is, in turn, less than or equal to each element of A[q + 1...r].
Compute the index q as part of this partitioning procedure.

Conquer: Sort the two subarrays A[p...q - 1] and A[q + 1...r] by recursive calls to
quicksort.

Combine: Because the subarrays are already sorted, no work is needed to combine them:
the entire array A[p...r] is now sorted.

To sort an entire array A, the initial call is quicksort(A, 0, len(A) - 1).

Partitioning the array
----------------------

partition() always selects an element x = A[r] as a pivot element around which to
partition the sub-array A[p...r]. As the procedure runs, it partitions the array into
four (possible empty) regions. At the start of each iteration of the for-loop, the
regions satisfy certain properties:

For any array index k,

1. If p <= k <= i, then A[k] <= x
2. If i + 1 <= k <= j - 1, then A[k] > x
3. If k = r, then A[k] = x
4. The sub-array A[j...r - 1] can take on any values

The final swap of partition() finishes up by swapping the pivot element with the
leftmost element greater than x, thereby moving the pivot into its correct place in the
partitioned array, and then returning the pivot's new index. The output of partition()
now satisfies the specifications given for the divide step.

7.2 Performance of quicksort
============================

The running time of quicksort depends on whether the partitioning is balanced or
unbalanced, which in turn depends on which elements are used for partitioning. If the
partitioning is balanced, the algorithm runs asymptotically as fast as merge sort. If
the partitioning is unbalanced, however, it can run asymptotically as slowly as
insertion sort.

7.4.2 Expected running time
===========================

The intuition behind why the expected running time of the randomized quicksort is
O(n * lg n) is as follows: if, in each level of recursion, the split induced by the
randomized partition puts any constant fraction of the elements on one side of the
partition, then the recursion tree has depth Theta(lg n) and O(n) work is performed at
each level.

Running time and comparisons
----------------------------

The running time of quicksort is dominated by the time spent in the partition()
procedure. Each time the partition procedure is called, it selects a pivot element, and
this element is never included in any future recursive calls to quicksort() and
partition().

NB: Although quicksort has in-place partition, it is NOT an in-place algorithm due to
the extra stack space required with each recursive call.

Complexity
==========

The worst case time occurs when the partitioning routine produces one sub-problem with
n - 1 elements and one with 0 elements or when the input array is already sorted. The
expected case occurs when we can equally balance the two sides of the partition at every
level of the recursion (only possible when we can choose the median value with each
recursion).

Time
----

partition(): O(n) = O(h - l + 1).
quicksort(): Theta(n^2) worst case, O(n * lg n) expected time.
"""

# Standard Library
import random


def quicksort(a, low, high):
    while low < high:
        pivot = partition(a, low, high)
        quicksort(a, low, pivot - 1)
        low = pivot + 1


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
