"""
8.3 Radix sort
==============

Radix sort sorts numbers from the least to most significant digit. Only d passes through
the array is required for an array of n numbers where each number has d digits.

Radix sort is stable if the counting sort is used as the underlying sorting procedure.

Complexity
==========

radix_sort(): O(d * (n + k)).
"""

# Repository Library
from src.clrs.sorting_and_order_statistics.sorting.linear_sorting.counting_sort import (
    counting_sort,
)


def radix_sort(a, base=10, exp=1):
    while max(a) / exp > 1:
        a = counting_sort(a, base, exp)
        exp *= base
    return a
