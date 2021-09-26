"""
Overview
========

Radix sort sorts numbers based on least significant digits first. Only d passes through
the array is required for an array whose numbers have d digits. If radix sort uses
counting sort, then radix sort is also stable.

Complexity
==========

Stable
O(d * (n + k))
"""

# Repository Library
from src.clrs.sorting.linear_sorting.counting_sort import counting_sort


def radix_sort(a, base=10):
    exp = 1
    while max(a) / exp > 1:
        a = counting_sort(a, exp=exp, base=base)
        exp *= base
    return a
