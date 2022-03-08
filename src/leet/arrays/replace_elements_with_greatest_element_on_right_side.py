"""
Replace Elements with Greatest Element on Right Side
----------------------------------------------------

Given an array arr, replace every element in that array with the greatest element among
the elements to its right, and replace the last element with -1.

After doing so, return the array.

Complexity
==========

Time
----

replaceElements(arr): O(n).

Space
-----

replaceElements(arr): O(1).
"""


def sol(arr):
    max_ = -1
    for i in reversed(range(len(arr))):
        temp, arr[i] = arr[i], max_
        max_ = max(max_, temp)
    return arr
