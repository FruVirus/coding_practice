"""Computes a fast inner product of two lists assuming that each list has been sorted by
their first elements.

O(|l1| + |l2|) vs. O(|l1|*|l2|) for a brute force inner product implementation.
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
