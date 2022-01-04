"""
2.3.1: The divide-and-conquer approach
======================================

The merge sort algorithm closely follows the divide-and-conquer paradigm. Intuitively,
it operates as follows.

Divide: Divide the n-element sequence to be sorted into two subsequences of n / 2
elements each.

Conquer: Sort the two subsequences recursively using merge sort.

Combine: Merge the two sorted subsequences to produce the sorted answer.

The recursion "bottoms out" when the sequence to be sorted has length 1, in which case
there is no work to be done, since every sequence of length 1 is already in sorted
order.

merge_sort() repeatedly splits the problem in half until we reach the base case where
there's only one element in the array. merge() then compares the single element arrays,
sorts them, and combines them into a new array. Each successive call to merge() sees
increasingly larger arrays until we end up comparing half of the original array with its
other half and doing one last final sort between each of the two sorted halves.

Merge sort is an asymptotically optimal comparison sort.

Merge sort is a stable sorting algorithm.

Complexity
==========

Time
----

merge(): Theta(n).
merge_sort(): Theta(n * lg n).
"""


def merge_sort(a):
    mid = len(a) // 2
    return a if len(a) == 1 else merge(merge_sort(a[:mid]), merge_sort(a[mid:]))


def merge(l, r):
    i, j, a = 0, 0, []
    while i < len(l) and j < len(r):
        if l[i] <= r[j]:
            a.append(l[i])
            i += 1
        else:
            a.append(r[j])
            j += 1
    if i < len(l):
        a.extend(l[i:])
    if j < len(r):
        a.extend(r[j:])
    return a
