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


def get_median(a):
    if len(a) == 1:
        return a[0]
    b = []
    for i in range(0, len(a), 5):
        group = a[i : i + 5]
        insertion_sort(group)
        median = (len(group) + 1) // 2 - 1
        b.append(group[median])
    return get_median(b)


def quick_select(a, low, high, i):
    med_of_med = get_median(a[low : high + 1])
    med_index = a.index(med_of_med)
    pivot = partition(a, low, high, pivot_index=med_index, random_partition=False)
    k = pivot - low + 1
    if i == k:
        return med_of_med
    if i < k:
        return quick_select(a, low, pivot - 1, i)
    return quick_select(a, pivot + 1, high, i - k)


a = [2, 1, 3, 4, 5, 6, 44, 36, 29, 0, 11, 12]
print(quick_select(a, 0, len(a) - 1, 1))
print(quick_select(a, 0, len(a) - 1, 2))
print(quick_select(a, 0, len(a) - 1, 3))
print(quick_select(a, 0, len(a) - 1, 4))
print(quick_select(a, 0, len(a) - 1, 5))
print(quick_select(a, 0, len(a) - 1, 6))
print(quick_select(a, 0, len(a) - 1, 7))
print(quick_select(a, 0, len(a) - 1, 8))
print(quick_select(a, 0, len(a) - 1, 9))
print(quick_select(a, 0, len(a) - 1, 10))
print(quick_select(a, 0, len(a) - 1, 11))
print(quick_select(a, 0, len(a) - 1, 12))
