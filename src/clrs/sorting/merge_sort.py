"""merge_sort() repeatedly splits the problem in half until we reach the base case where
there's only one element in the list. merge() then compares the single element lists,
sorts them, and combines them into a new list. Each successive call to merge() sees
increasingly larger lists until we end up comparing half of the original list with its
other half and doing one last final sort between each of the two sorted halves.

O(n*lg(n))
"""


def merge_sort(a):
    n = len(a)
    if n == 1:
        return a
    mid = n // 2
    l = merge_sort(a[:mid])
    r = merge_sort(a[mid:])
    return merge(l, r)


def merge(l, r):
    i, j, a = 0, 0, []
    while i < len(l) and j < len(r):
        if l[i] < r[j]:
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


assert merge_sort([5, 4, 3, 2, 1, -4]) == [-4, 1, 2, 3, 4, 5]
