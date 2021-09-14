"""Counting sort assumes that each of the n input elements is an integer in the range 0
to k, for some integer k. When k = O(n), the sort runs in Theta(n) time.

Counting sort determines, for each input element x, the number of elements less than x.
It uses this information to place element x directly into its position in the output
array.

An important property of counting sort is that it is stable: numbers with the same value
appear in the output array in the same order as they do in the input array. That is, it
breaks ties between two numbers by the rule that whichever number appears first in the
input array appears first in the output array. The property of stability is important
when satellite data are carried around with the element being sorted.

Counting sort's stability is the reason why it's also used as a subroutine in radix
sort.

Stable
O(n)
"""


def counting_sort(a, k):
    n = len(a)
    b, c = [0] * n, [0] * (k + 1)
    for i in range(n):
        c[a[i]] += 1
    for i in range(1, k + 1):
        c[i] += c[i - 1]
    for i in range(n - 1, -1, -1):
        b[c[a[i]] - 1] = a[i]
        c[a[i]] -= 1
    return b
