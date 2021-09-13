"""Radix sort sorts numbers based on least significant digits first. Only d passes
through the array is required for an array whose numbers have d digits. If radix sort
uses counting sort, then radix sort is also stable.

O(d * (n + k))
"""


def counting_sort(a, exp, base):
    n = len(a)
    output = [0] * n
    count = [0] * base
    for i in range(n):
        index = a[i] // exp
        count[index % base] += 1
    for i in range(1, base):
        count[i] += count[i - 1]
    for i in range(n - 1, -1, -1):
        index = a[i] // exp
        output[count[index % base] - 1] = a[i]
        count[index % base] -= 1
    return output


def radix_sort(a, base=10):
    exp = 1
    while max(a) / exp > 1:
        a = counting_sort(a, exp, base)
        exp *= base
    return a
