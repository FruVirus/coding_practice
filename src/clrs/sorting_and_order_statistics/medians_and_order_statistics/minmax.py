"""
9.1 Minimum and maximum
=======================

We can easily obtain an upper bound of n - 1 comparisons to find the minimum/maximum of
a set of n elements: examine each element of the set in turn and keep track of the
smallest/largest element seen so far.

Simultaneous minimum and maximum
--------------------------------

To determine both the minimum and maximum of a set of n elements, using Theta(n)
comparisons, we can simply find the minimum and maximum independently, using n - 1
comparisons for each, for a total of 2 * n - 2 comparisons.

In fact, we can find both the minimum and the maximum using at most 3 * floor(n / 2)
comparisons. We do so by maintaining both the minimum and maximum elements seen thus
far. Rather than processing each element of the input by comparing it against the
current minimum and maximum, at a cost of 2 comparisons per element, we process elements
in pairs. We compare pairs of elements from the input first with each other, and then we
compare the smaller with the current minimum and the larger with the current maximum, at
a cost of 3 comparisons for every 2 elements.

Complexity
==========

Time
----

minmax(): O(n) in no more than 3 * floor(n / 2) comparisons.
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
        if amin < cmin:
            cmin = amin
        if amax > cmax:
            cmax = amax
    return cmin, cmax
