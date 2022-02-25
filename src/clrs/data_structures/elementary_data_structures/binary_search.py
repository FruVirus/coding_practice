"""
Overview
========

Binary search searches for the index of an item k in an array by recursively splitting
the array in two. The input array is assumed to be sorted in increasing order.

Complexity
==========

Time
----

bs_iterative() and bs_recursive(): O(lg n).
"""


def bs_iterative(a, low, high, k):
    while low <= high:
        mid = int(low + ((high - low) / 2))
        if a[mid] == k:
            return mid
        if a[mid] > k:
            high = mid - 1
        else:
            low = mid + 1
    return None


def bs_recursive(a, low, high, k):
    if low <= high:
        mid = (low + high) // 2
        if a[mid] == k:
            return mid
        if a[mid] > k:
            return bs_recursive(a, low, mid - 1, k)
        return bs_recursive(a, mid + 1, high, k)
    return None
