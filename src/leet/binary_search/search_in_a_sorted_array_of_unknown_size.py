"""
Search in a Sorted Array of Unknown Size
----------------------------------------

This is an interactive problem.

You have a sorted array of unique elements and an unknown size. You do not have access
to the array but you can use the ArrayReader interface to access it. You can call
ArrayReader.get(i) that:

    1. returns the value at the ith index (0-indexed) of the secret array (i.e.,
secret[i]), or

    2. returns 2^31 - 1 if the i is out of the boundary of the array.

You are also given an integer target.

Return the index k of the hidden array where secret[k] == target or return -1 otherwise.

You must write an algorithm with O(log n) runtime complexity.

Intuition
---------

The idea is quite simple. Let's take two first indexes, 0 and 1, as left and right
boundaries. If the target value is not among these zeroth and the first element, then
it's outside the boundaries, on the right.

That means that the left boundary could moved to the right, and the right boundary
should be extended. To keep logarithmic time complexity, let's extend it twice as far:
right = right * 2.

If the target now is less than the right element, we're done, the boundaries are set. If
not, repeat these two steps till the boundaries are established.

Complexity
==========

Time
----

search(reader, target): O(lg n).

Space
-----

search(reader, target): O(1).
"""


def sol(reader, target):
    low, high = 0, 1
    while target > reader.get(high):
        low, high = high, high << 1
    while low <= high:
        mid = low + ((high - low) >> 1)
        if reader.get(mid) == target:
            return mid
        if reader.get(mid) < target:
            low = mid + 1
        else:
            high = mid - 1
    return -1
