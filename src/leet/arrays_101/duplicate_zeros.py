"""
Duplicate Zeros
---------------

Given a fixed-length integer array arr, duplicate each occurrence of zero, shifting the
remaining elements to the right.

Note that elements beyond the length of the original array are not written. Do the above
modifications to the input array in place and do not return anything.

Complexity
==========

Time
----

duplicateZeros(arr): O(n).

Space
-----

duplicateZeros(arr): O(1).
"""


def sol(arr):
    num_zeros, n = 0, len(arr) - 1
    for i in range(n + 1):
        if i > n - num_zeros:
            break
        if arr[i] == 0:
            if i == n - num_zeros:
                arr[n] = 0
                n -= 1
                break
            num_zeros += 1
    last = n - num_zeros + 1
    for i in reversed(range(last)):
        if arr[i] == 0:
            arr[i + num_zeros] = 0
            num_zeros -= 1
            arr[i + num_zeros] = 0
        else:
            arr[i + num_zeros] = arr[i]
