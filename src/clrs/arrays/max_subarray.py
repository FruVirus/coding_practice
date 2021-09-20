"""Maximum subarray finds the longest contiguous span of an input array that contains
the greatest sum over its elements. This problem is only interesting if there is a
combination of negative and positive numbers in the list. The longest, contiguous
sub-array must exist in either the left half, right half, or cross over the midpoint of
the original array. Thus, the problem is divided into finding the longest contiguous
span in the left half, right half, and cross span.

O(n*lg(n))
"""


def find_max(a, low, high):
    if low == high:
        return low, high, a[low]
    mid = (low + high) // 2
    llow, lhigh, lsum = find_max(a, low, mid)
    rlow, rhigh, rsum = find_max(a, mid + 1, high)
    clow, chigh, csum = find_cross(a, low, mid, high)
    if lsum >= rsum and lsum >= csum:
        return llow, lhigh, lsum
    if rsum >= lsum and rsum >= csum:
        return rlow, rhigh, rsum
    return clow, chigh, csum


def find_cross(a, low, mid, high):
    lsum = rsum = -float("inf")
    lcsum = rcsum = 0
    clow = chigh = -1
    for i in range(mid, low - 1, -1):
        lcsum += a[i]
        if lcsum > lsum:
            lsum = lcsum
            clow = i
    for i in range(mid + 1, high + 1):
        rcsum += a[i]
        if rcsum > rsum:
            rsum = rcsum
            chigh = i
    return clow, chigh, lsum + rsum
