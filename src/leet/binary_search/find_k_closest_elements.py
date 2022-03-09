"""
Find K Closest Elements
-----------------------

Given a sorted integer array arr, two integers k and x, return the k closest integers to
x in the array. The result should also be sorted in ascending order.

Complexity
==========

Time
----

findClosestElements(arr, k, x): O(lg(n - k) + k), where O(k) is the time taken to build
the final output.

Space
-----

findClosestElements(arr, k, x): O(1).
"""


def sol(arr, k, x):
    low, high = 0, len(arr) - k
    while low < high:
        mid = low + (high - low) // 2
        if x - arr[mid] > arr[mid + k] - x:
            low = mid + 1
        else:
            high = mid
    return arr[low : low + k]
