"""
Overview
========

Binary search searches for the index of an item k in an array by recursively splitting
the array in two. The input array is assumed to be sorted in increasing order.

Intuition
---------

bs_iterative_one() is used to search for an element or condition which can be determined
by accessing a single index in the array.

bs_iterative_two() is used to search for an element or condition which requires
accessing the current index and its immediate right neighbor's index in the array.
Post-processing is required since the loop/recursion ends when you have 1 element left.
Thus, we need to assess if the remaining element meets the condition. This guarantees
that the search space is at least 2 in size at each step.

bs_iterative_three() is used to search for an element or condition which requires
accessing the current index and its immediate left and right neighbor's index in the
array. Post-processing is required since the loop/recursion ends when you have 2
elements left. Thus, we need to assess if the remaining elements meet the condition.
This guarantees that th search space is at least 3 in size at each step.

Complexity
==========

Time
----

bs_iterative_one(), bs_iterative_two(), bs_iterative_three(), and bs_recursive():
O(lg n).

Space
-----

bs_recursive(): O(lg n) stack space.
"""


def bs_iterative_one(a, k):
    low, high = 0, len(a) - 1
    while low <= high:
        mid = low + ((high - low) // 2)
        if a[mid] == k:
            return mid
        if a[mid] > k:
            high = mid - 1
        else:
            low = mid + 1
    return None


def bs_iterative_two(a, k):
    low, high = 0, len(a)
    while low < high:
        mid = low + ((high - low) // 2)
        if a[mid] == k:
            return mid
        if a[mid] > k:
            high = mid
        else:
            low = mid + 1
    return low if low != len(a) and a[low] == k else None


def bs_iterative_three(a, k):
    low, high = 0, len(a) - 1
    while low + 1 < high:
        mid = low + ((high - low) // 2)
        if a[mid] == k:
            return mid
        if a[mid] > k:
            high = mid
        else:
            low = mid
    if a[low] == k:
        return low
    if a[high] == k:
        return high
    return None


def bs_recursive(a, low, high, k):
    if low <= high:
        mid = low + ((high - low) // 2)
        if a[mid] == k:
            return mid
        if a[mid] > k:
            return bs_recursive(a, low, mid - 1, k)
        return bs_recursive(a, mid + 1, high, k)
    return None
