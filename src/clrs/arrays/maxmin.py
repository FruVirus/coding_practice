"""Maxmin finds the minimum and maximum elements in an array in O(n) time.

O(n) time in no more than 3 * floor(n / 2) comparison.
"""


def maxminsort(x, y):
    return (x, y) if x < y else (y, x)


def maxmin(a):
    n = len(a)
    if n % 2 > 0:
        cmin = cmax = a[0]
        start_index = 1
    else:
        cmin, cmax = maxminsort(a[0], a[1])
        start_index = 2
    for i in range(start_index, n, 2):
        amin, amax = maxminsort(a[i], a[i + 1])
        if amin < cmin:
            cmin = amin
        if amax > cmax:
            cmax = amax
    return cmin, cmax
