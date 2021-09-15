"""Random select returns the i-th smallest element of its input array.

E[O(n)] time
"""


# Repository Library
from src.clrs.sorting.comparison_sorting.quick_sort import partition


def random_select(a, low, high, i):
    if low == high:
        return a[low]
    pivot = partition(a, low, high)
    k = pivot - low + 1
    if i == k:
        return a[pivot]
    if i < k:
        return random_select(a, low, pivot - 1, i)
    return random_select(a, pivot + 1, high, i - k)


a = [2, 1, 3, 4, 5, 6, 44, 46, 29, 0, 11, 12]
print(random_select(a, 0, len(a) - 1, 1))
