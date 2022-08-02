"""
Add Binary
----------

Given two binary strings a and b, return their sum as a binary string.

Intuition
---------

Adding two number using bit manipulation involves summing the answer without carry and
carry. The loop continues until the carry is 0.

XOR is a sum of two binaries without taking carry into account.
Carry is the AND of two binaries, shifted one bit to the left.

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
