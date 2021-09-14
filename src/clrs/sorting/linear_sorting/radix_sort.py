"""Radix sort sorts numbers based on least significant digits first. Only d passes
through the array is required for an array whose numbers have d digits. If radix sort
uses counting sort, then radix sort is also stable.

NB: The csort() function here is NOT the same as the original counting_sort() function.
This csort() is specifically used by radix sort for incrementally sorting by least
significant digit. If csort() is used to sort a given array with provided exp and base
arguments, it will NOT always sort correctly since csort() is stable. For example,
sorting the array [329, 457, 657, 839, 436, 720, 355] with exp = 100 and base 10 will
result in [329, 355, 457, 436, 657, 720, 839] since 457 came before 436 in the original
array and their most significant digit is the same (i.e, 4) and csort (just like the
original counting_sort()) is a stable sorting algorithm. In any words, csort() only
sorts properly if it is iteratively called with increasing significant digit.

O(d * (n + k))
"""


def csort(a, exp, base):
    n = len(a)
    b, c = [0] * n, [0] * base
    for i in range(n):
        index = (a[i] // exp) % base
        c[index] += 1
    for i in range(1, base):
        c[i] += c[i - 1]
    for i in range(n - 1, -1, -1):
        index = (a[i] // exp) % base
        b[c[index] - 1] = a[i]
        c[index] -= 1
    return b


def radix_sort(a, base=10):
    exp = 1
    while max(a) / exp > 1:
        a = csort(a, exp, base)
        exp *= base
    return a
