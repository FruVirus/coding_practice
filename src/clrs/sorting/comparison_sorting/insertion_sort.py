"""
Overview
========

We iterate over each item in the list in the for-loop. In the while-loop, we compare
each previous item in the list with the current item. If the previous item is smaller
than the current item, then we perform a swap of the two items and decrement the index
position of the previous item. By swapping and decrementing the index position of the
previous item, we continuously move the i-th item in a to its correctly sorted position.

NB: Even if we use binary search to find each insertion point, the complexity is still
O(n^2). While binary insertion sorting improves the time it takes to find the right
position for the next element being inserted, it may still take O(n) time to perform the
swaps necessary to shift it into place.

Complexity
==========

Stable
O(n^2)
O(n) if a is already sorted
"""


def insertion_sort(a):
    for i in range(1, len(a)):
        k = a[i]
        j = i - 1
        while j > -1 and a[j] > k:
            a[j + 1] = a[j]
            j -= 1
        a[j + 1] = k
