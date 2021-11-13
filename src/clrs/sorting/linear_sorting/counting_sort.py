"""
Overview
========

Counting sort assumes that each of the n input elements is an integer in the range 0 to
k, for some integer k. When k = O(n), the sort runs in Theta(n) time.

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

NB: For radix sort, counting sort makes use of the exp and base arguments and
incrementally sorts by least significant digit.  If counting_sort() is used to sort a
given array with provided exp and base arguments, it will NOT always sort correctly
since counting_sort() is stable. For example, sorting the array
[329, 457, 657, 839, 436, 720, 355] with exp = 100 and base 10 will result in
[329, 355, 457, 436, 657, 720, 839] since 457 came before 436 in the original array and
their most significant digit is the same (i.e, 4) and counting_sort is a stable sorting
algorithm. In other words, counting_sort() only sorts properly if it is iteratively
called with increasing significant digit.

Complexity
==========

Stable
O(n)
"""


def counting_sort(a, k=None, exp=None, base=None):
    if k is None:
        assert exp is not None and base is not None
    n, base = len(a), base or (k + 1)
    b, c = [0] * n, [0] * base
    for i in range(n):
        index = (a[i] // exp) % base if k is None else a[i]
        c[index] += 1
    for i in range(1, base):
        c[i] += c[i - 1]
    for i in range(n - 1, -1, -1):
        index = (a[i] // exp) % base if k is None else a[i]
        b[c[index] - 1] = a[i]
        c[index] -= 1
    return b
