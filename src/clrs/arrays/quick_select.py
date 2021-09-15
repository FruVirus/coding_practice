"""Quick select returns the i-th smallest element of its input array in worst case O(n).
select.py differs from random_select.py in that the former guarantees a good split upon
partitioning the input array, thus improving the worst case selection time. select.py
uses the deterministic partitioning algorithm from quick sort but modified to take the
element to partition around as an input parameter.

O(n) worst case
"""


# Repository Library
from src.clrs.sorting.comparison_sorting.insertion_sort import insertion_sort
from src.clrs.sorting.comparison_sorting.quick_sort import partition


def _select(a, low, high):
    if low == high:
        return a[low]
    b = []
    for i in range(0, len(a), 5):
        group = a[i : i + 5]
        insertion_sort(group)
        median = (len(group) + 1) // 2 - 1
        b.append(group[median])
    return _select(b, 0, len(b) - 1)


def select(a, low, high, i):
    med_of_med = _select(a, low, high)
    med_index = a.index(med_of_med)
    pivot = partition(a, low, high, random_partition=False, k=med_index)
    k = pivot - low + 1
    if i == k:
        return med_of_med
    if i < k:
        return select(a, low, pivot - 1, i)
    return select(a, pivot + 1, high, i - k)


a = [2, 1, 3, 4, 5, 6, 44, 36, 29, 0, 11, 12]
print(select(a, 0, len(a) - 1, 3))
