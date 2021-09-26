"""
Overview
========

We iterate over each item in the list in the for-loop. In the while-loop, we compare
each previous item in the list with the current item. If the previous item is smaller
than the current item, then we perform a swap of the two items and decrement the index
position of the previous item. By swapping and decrementing the index position of the
previous item, we continuously move the i-th item in a to its correctly sorted position.

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
