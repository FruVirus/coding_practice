"""bubble_sort() works backwards through the list N times, where N is the number of
items in the list. For each backwards pass, we compare two adjacent items in the list
and swap their places if necessary.

O(n^2)
"""


def bubble_sort(a):
    for i in range(len(a) - 1):
        for j in range(len(a) - 1, i, -1):
            if a[j] < a[j - 1]:
                a[j], a[j - 1] = a[j - 1], a[j]
    return a
