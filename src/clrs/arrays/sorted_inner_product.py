"""
Overview
========

Computes a fast inner product of two lists assuming that each list has been sorted by
their first elements. In other words:

l1 = [[3, 2], [4, 1], [6, 1], [8, 1], [9, 1]] and
l2 = [[2, 1], [3, 1], [6, 1], [7, 1], [8, 1]] should give 4.0.

Note that the the arrays l1 and l2 have been sorted by their first elements and only
contain values for relevant dimensions. For example, l1 has no 2 dimension and thus,
there's no point in multiplying [2, 0] by [2, 1] in l2. The brute force approach would
do this multiplication.

Complexity
==========

O(|l1| + |l2|) time complexity
"""


def sorted_inner_product(l1, l2):
    i = j = sum = 0
    while i < len(l1) and j < len(l2):
        if l1[i][0] == l2[j][0]:
            sum += l1[i][1] * l2[j][1]
            i += 1
            j += 1
        elif l1[i][0] < l2[j][0]:
            i += 1
        else:
            j += 1
    return sum
