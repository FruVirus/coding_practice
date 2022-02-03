"""
8.2 Counting sort
=================

Counting sort assumes that each of the n input elements is an integer in the range 0 to
k, for some (non-negative) integer k. When k = O(n), the sort runs in Theta(n) time.

Counting sort determines, for each input element x, the number of elements less than x.
It uses this information to place element x directly into its position in the output
array.

The first for-loop inspects each input element. If the value of an input element is i,
we increment C[i]. Thus, after the first for-loop C[i] holds the number of input
elements equal to i for each integer i = 0, 1, ..., k.

The second for-loop determines for each i = 0, 1, ..., k, how many input elements are
less than or equal to i by keeping a running sum of the array C.

The third for-loop places each element A[j] into its correct sorted position in the
output array B. If all n elements are distinct, then when we first enter the third
for-loop, for each A[j], the value C[A[j]] is the correct final position of A[j] in the
output array, since there are C[A[j]] elements less than or equal to A[j]. Because the
elements might not be distinct, we decrement C[A[j]] each time we place a value A[j]
into the B array. Decrementing C[A[j]] causes the next input element with a value equal
to A[j], if one exists, to go to the position immediately before A[j] in the output
array.

An important property of counting sort is that it is stable: numbers with the same value
appear in the output array in the same order as they do in the input array. That is, it
breaks ties between two numbers by the rule that whichever number appears first in the
input array appears first in the output array. The property of stability is important
when satellite data are carried around with the element being sorted.

In practice, we usually use counting sort when we have k = O(n), in which case the
running time is Theta(n).

Counting sort's stability is the reason why it's also used as a subroutine in radix
sort.

NB: For radix sort, counting sort makes use of the base and exp arguments and
incrementally sorts from least to most significant digit. If counting sort is used to
sort a given array with provided base and exp arguments, it will NOT always sort
correctly since counting sort is stable. For example, sorting the array
[329, 457, 657, 839, 436, 720, 355] with base = 10 and exp = 100 will result in
[329, 355, 457, 436, 657, 720, 839] since 457 came before 436 in the original array and
their most significant digit is the same (i.e, 4) and counting sort is a stable sorting
algorithm. In other words, counting sort only sorts properly if it is ITERATIVELY called
with increasing significant digit.

Counting sort is stable.

Complexity
==========

Time
----

counting_sort(): Theta(n)

Space
-----

counting_sort(): O(k) for the C array. O(n) for the B array.
"""


def counting_sort(a, base=None, exp=None, k=None):
    assert k or (base and exp)
    n, base = len(a), base or (k + 1)
    b, c = [0] * n, [0] * base
    for i in range(n):
        index = (a[i] // exp) % base if k is None else a[i]
        c[index] += 1
    for i in range(1, base):
        c[i] += c[i - 1]
    for i in reversed(range(n)):
        index = (a[i] // exp) % base if k is None else a[i]
        b[c[index] - 1] = a[i]
        c[index] -= 1
    return b
