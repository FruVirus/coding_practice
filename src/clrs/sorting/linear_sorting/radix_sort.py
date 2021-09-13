"""Radix sort sorts numbers based on least significant digits first. Only d passes
through the array is required for an array whose numbers have d digits. If radix sort
uses counting sort, then radix sort is also stable.

O(d * (n + k))
"""


def counting_sort(a, exp, base):
    n = len(a)
    output, count = [0] * n, [0] * base
    for i in range(n):
        index = (a[i] // exp) % base
        count[index] += 1
    for i in range(1, base):
        count[i] += count[i - 1]
    for i in range(n - 1, -1, -1):
        index = (a[i] // exp) % base
        output[count[index] - 1] = a[i]
        count[index] -= 1
    return output


def radix_sort(a, base=10):
    exp = 1
    while max(a) / exp > 1:
        a = counting_sort(a, exp, base)
        exp *= base
    return a
