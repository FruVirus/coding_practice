"""
Valid Mountain Array
--------------------

Given an array of integers arr, return true if and only if it is a valid mountain array.

Complexity
==========

Time
----

validMountainArray(arr): O(n).

Space
-----

validMountainArray(arr): O(1).
"""


def sol(arr):
    i, j = 0, len(arr) - 1
    while i < j and arr[i] < arr[i + 1]:
        i += 1
    if i in [0, j]:
        return False
    while i < j and arr[i] > arr[i + 1]:
        i += 1
    return i == j
