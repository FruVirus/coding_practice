"""
Overview
========

Min-max finds the minimum and maximum elements in an array in O(n) time.

Complexity
==========

O(n) time in no more than 3 * floor(n / 2) comparisons.
"""


def mms(x, y):
    return (x, y) if x < y else (y, x)


def minmax(a):
    n = len(a)
    if n % 2 != 0:
        cmin = cmax = a[0]
        start_index = 1
    else:
        cmin, cmax = mms(a[0], a[1])
        start_index = 2
    for i in range(start_index, n, 2):
        amin, amax = mms(a[i], a[i + 1])
        cmin = min(amin, cmin)
        cmax = max(amax, cmax)
    return cmin, cmax
