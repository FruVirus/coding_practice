"""
Overview
========

Random select returns the i-th smallest element of its input array.

Complexity
==========

E[O(n)] time
"""

# Repository Library
from src.clrs.sorting_and_order_statistics.comparison_sorting.quick_sort import (
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
