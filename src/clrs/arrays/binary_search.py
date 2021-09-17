"""Binary search searches for an item k in an array by recursively splitting the array
in two.

O(lg(n))
"""


def binary_search(a, low, high, k):
    if high >= low:
        mid = (high + low) // 2
        if a[mid] == k:
            return mid
        if a[mid] > k:
            return binary_search(a, low, mid - 1, k)
        return binary_search(a, mid + 1, high, k)
    return None
