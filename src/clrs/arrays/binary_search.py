"""
Overview
========

Binary search searches for an item k in an array by recursively splitting the array in
two. The input array is assumed to be sorted in increasing order.

Complexity
==========

bs_iterative(): O(lg n)
bs_recursive(): O(lg n)
"""


def bs_iterative(a, low, high, k):
    while high >= low:
        mid = (low + high) // 2
        if a[mid] == k:
            return mid
        if a[mid] > k:
            high = mid - 1
        else:
            low = mid + 1
    return None


def bs_recursive(a, low, high, k):
    if high >= low:
        mid = (low + high) // 2
        if a[mid] == k:
            return mid
        if a[mid] > k:
            return bs_recursive(a, low, mid - 1, k)
        return bs_recursive(a, mid + 1, high, k)
    return None
