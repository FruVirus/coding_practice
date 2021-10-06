"""
Overview
========

Quick select returns the i-th smallest element of its input array in worst case O(n).
quick_select.py differs from random_select.py in that the former guarantees a good split
upon partitioning the input array, thus improving the worst case selection time.
quick_select.py uses the deterministic partitioning algorithm from quick sort but
modified to take the element to partition around as an input parameter.

Complexity
==========

O(n) worst case
"""

# Repository Library
from src.clrs.sorting.comparison_sorting.insertion_sort import insertion_sort
from src.clrs.sorting.comparison_sorting.quick_sort import partition


def get_median(a):
    b = []
    for i in range(0, len(a), 5):
        group = a[i : i + 5]
        insertion_sort(group)
        med_index = (len(group) + 1) // 2 - 1
        b.append(group[med_index])
    return b


def quick_select(a, low, high, i):
    med = a
    while isinstance(med, list) and len(med) > 1:
        med = get_median(med[low : high + 1])
    pivot = partition(a, low, high, a.index(med[0]), False)
    k = pivot - low + 1
    if i == k:
        return a[pivot]
    if i < k:
        return quick_select(a, low, pivot - 1, i)
    return quick_select(a, pivot + 1, high, i - k)
