"""
Find K Closest Elements
-----------------------

Given a sorted integer array arr, two integers k and x, return the k closest integers to
x in the array. The result should also be sorted in ascending order.

Intuition
---------

We need to find the leftmost index of a number that will be in the final answer. The
farthest right it could possibly be is the length of the array - k. Otherwise, there
wouldn't be enough elements to its right.

arr = [1, 2, 3, 4, 5, 6, 7, 8], k = 3, x = 4

low = 0, high = 5, mid = 2, mid + k = 5

Since arr[mid] (3) is closer to x than arr[mid + k] (6), this means that arr[mid + k:]
(6, 7, 8) can never be in the final answer, since that would imply 3 is not in the final
answer but we know that 3 is closer to x than 6, 7, and 8. Thus, we move the high
pointer.

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
