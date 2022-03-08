"""
Add Binary
----------

Given two binary strings a and b, return their sum as a binary string.

Complexity
==========

Time
----

addBinary(a, b): O(n + m).

Space
-----

addBinary(a, b): O(max(n, m)).
"""


def sol(a, b):
    x, y = int(a, 2), int(b, 2)
    while y != 0:
        without_carry, carry = x ^ y, (x & y) << 1
        x, y = without_carry, carry
    return bin(x)[2:]
