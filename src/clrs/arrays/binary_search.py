"""Binary search searches for an item k in an array by recursively splitting the array
in two.

O(lg(n))
"""


def binary_search(arr, low, high, k):
    if high >= low:
        mid = (high + low) // 2
        if arr[mid] == k:
            return mid
        if arr[mid] > k:
            return binary_search(arr, low, mid - 1, k)
        return binary_search(arr, mid + 1, high, k)
    return None
