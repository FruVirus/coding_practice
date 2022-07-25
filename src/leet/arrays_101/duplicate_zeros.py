"""
Duplicate Zeros
---------------

Given a fixed-length integer array arr, duplicate each occurrence of zero, shifting the
remaining elements to the right.

Note that elements beyond the length of the original array are not written. Do the above
modifications to the input array in place and do not return anything.

Intuition
---------

1. Find the number of zeros which would be duplicated. We do need to make sure we are
not counting the zeros which would be trimmed off since the discarded zeros won't be
part of the final array. The number of zeros would give us the number of elements to be
trimmed off the original array.

2. Handle the edge case for a zero present on the boundary of the leftover elements.

An example of the edge case is - [8,4,5,0,0,0,0,7]. In this array there is space to
accommodate the duplicates of first and second occurrences of zero. But we don't have
enough space for the duplicate of the third occurrence of zero. Hence when we are
copying we need to make sure for the third occurrence we don't copy twice. Result =
[8,4,5,0,0,0,0,0]

3. Iterate the array from the end and copy a non-zero element once and zero element
twice. When we say we discard the extraneous elements, it simply means we start from the
left of the extraneous elements and start overwriting them with new values, eventually
right shifting the left over elements and creating space for all the duplicated elements
in the array.

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
