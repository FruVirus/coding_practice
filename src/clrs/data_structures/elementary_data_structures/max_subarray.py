"""
4.1: The maximum-subarray problem
=================================

In the maximum subarray problem, we are given an array of numbers (positive and
negative) and we wish to find a sequence of indices in the original array that
correspond to a subarray whose values give the largest sum. The maximum subarray problem
is interesting only when the array contains some negative numbers. If all of the array
entries were non-negative, then the maximum subarray problem would present no challenge,
since summing the entire array would give the greatest sum.

Given an array of numbers, we want to find a sequence of indices over which the net
change of values is maximum. Instead of looking at the array values themselves, let us
instead consider the change in values between indices. The sequence of indices forms a
non-empty, contiguous subarray whose values have the largest sum.

The longest, contiguous subarray must exist in either the left half, right half, or
cross over the midpoint of the original array. Thus, the problem is divided into finding
the longest contiguous span in the left half, right half, and cross span. In fact, a
maximum subarray of A[low...high] must have the greatest sum over all subarrays entirely
in A[low...mid], entirely in A[mid + 1...high], or crossing the midpoint. We can find
maximum subarrays of A[low...mid] and A[mid + 1...high] recursively, because these two
subproblems are smaller instances of the problem of finding a maximum subarray. Thus,
all that is left to do is find a maximum subarray that crosses the midpoint, and take a
subarray with the largest sum of the three spans.

We can easily find a maximum subarray crossing the midpoint in time linear in the size
of the subarray A[low...high]. This problem is NOT a smaller instance of our original
problem, because it has the added restriction that the subarray it chooses must cross
the midpoint. Any subarray crossing the midpoint is itself made of two subarrays
A[i...mid] and A[mid + 1...j], where low <= i <= mid and mid < j <= high. Therefore, we
just need to find maximum subarrays of the form A[i...mid] and A[mid + 1...j] and then
combine them.

The procedure find_cross() essentially builds the maximum subarray starting from mid
outwards towards low and from mid outwards towards high.

The procedure find_max_iterative() runs in Theta(n) time by starting at the left end of
the array and progressing toward the right while keeping track of the maximum subarray
seen so far. If csum becomes negative, then the index of clow is updated. If csum is
greater than max_sum, then max_sum is updated to be csum.

Intuition
---------

find_max_iterative() works since, if we know a maximum subarray of A[1...j], then a
maximum subarray of A[1...j + 1] is either a maximum subarray of A[1...j] or a subarray
of A[i...j + 1] for some 1 <= i <= j + 1.

For example, consider a = [2, -5, 6, 10].

The change in a is: a_ = [-7, 11, 4].

i = 0: clow, csum = 0, -7 --> low, high, max_sum = 0, 0, -7
i = 1: clow, csum = 1, 11 --> low, high, max_sum = 1, 1, 11
i = 2: clow, csum = 1, 15 --> low, high, max_sum = 1, 2, 15

Thus, the solution is that the sum of a[0] to a[3] gives the largest sum in the original
array, a.

Now consider a = [2, -5, 6, -10].

The change in a is: a_ = [-7, 11, -16].

i = 0: clow, csum = 0, -7 --> low, high, max_sum = 0, 0, -7
i = 1: clow, csum = 1, 11 --> low, high, max_sum = 1, 1, 11
i = 2: clow, csum = 1, -5 --> low, high, max_sum = 1, 1, 11

Thus, the solution is that the sum of a[0] to a[2] gives the largest sum in the original
array, a.

Now consider a = [2, -5, 6, -10, 4, 20].

The change in a is: a_ = [-7, 11, -16, 14, 16].

i = 0: clow, csum = 0, -7 --> low, high, max_sum = 0, 0, -7
i = 1: clow, csum = 1, 11 --> low, high, max_sum = 1, 1, 11
i = 2: clow, csum = 1, -5 --> low, high, max_sum = 1, 1, 11
i = 3: clow, csum = 3, 14 --> low, high, max_sum = 3, 3, 14
i = 4: clow, csum = 3, 30 --> low, high, max_sum = 3, 4, 30

Thus, the solution is that the sum of a[2] to a[5] gives the largest sum in the original
array, a.

In other words, the value for clow resets to i each time csum becomes negative, which
means that the current low index is always the index that gave the previous negative
change in the cumulative sum. Once csum goes negative, we don't have to worry about the
values in a that came before the previous value of clow since the cumulative sum of
those values became negative. Thus, we can reset clow to i and start the cumulative sum
over again with a_[i].

Complexity
==========

Time
----

find_cross() and find_max_iterative(): Theta(n).
find_max(): Theta(n * lg n).
"""


# pylint: disable=C0200


def find_max_iterative(a):
    a = [a[i] - a[i - 1] for i in range(1, len(a))]
    clow = low = high = -1
    csum = max_sum = -float("inf")
    for i in range(len(a)):
        clow, csum = (clow, csum + a[i]) if csum > 0 else (i, a[i])
        if csum > max_sum:
            low, high, max_sum = clow, i, csum
    return low, high, max_sum


def find_max(a, low=None, high=None):
    if low is None or high is None:
        a = [a[i] - a[i - 1] for i in range(1, len(a))]
        low, high = 0, len(a) - 1
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
            lsum, clow = lcsum, i
    for i in range(mid + 1, high + 1):
        rcsum += a[i]
        if rcsum > rsum:
            rsum, chigh = rcsum, i
    return clow, chigh, lsum + rsum
