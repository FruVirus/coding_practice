"""Binary counter implements a k-bit binary counter that counts upwards from 0. We use
an array A[0...k - 1] of bits, where len(A) = k, as the counter. A binary number x that
is stored in the counter has its lowest-order bit in A[0] and its highest-order bit in
A[k - 1].

Theta(k)
"""


def binary_counter(a):
    i = 0
    while i < len(a) and a[i] == 1:
        a[i] = 0
        i += 1
    if i < len(a):
        a[i] = 1
