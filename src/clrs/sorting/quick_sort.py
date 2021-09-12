"""Quicksort, like merge sort, is a divide and conquer algorithm that sorts in place.

For a typical subarray A[p...r]:

Divide: Partition (rearrange) the array A[p...r] into two (possibly empty) sub-arrays
A[p...q - 1] and A[q + 1...r] such that each element of A[p...q - 1] is less than or
equal to A[q], which is, in turn, less than or equal to each element of A[q + 1...r].
Compute the index q as part of this partitioning procedure.

partition() selects an element x = A[r] as a pivot element around which to partition the
subarray A[p...r]. As the procedure runs, it partitions the array into four (possible
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

To sort an entire array A, the initial call is quicksort(A, 0, len(A) - 1).

O(n^2) worst case
O(n*lg(n)) expect case.
"""


def quicksort(a, p, r):
    if p < r:
        q = partition(a, p, r)
        quicksort(a, p, q - 1)
        quicksort(a, q + 1, r)
    return a


def partition(a, p, r):
    x, i = a[r], p - 1
    for j in range(p, r):
        if a[j] <= x:
            i += 1
            a[i], a[j] = a[j], a[i]
    a[i + 1], a[r] = a[r], a[i + 1]
    return i + 1
