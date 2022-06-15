"""
Number of 1 Bits
----------------

Write a function that takes an unsigned integer and returns the number of '1' bits it
has (also known as the Hamming weight).

Intuition
---------

We repeatedly flip the least-significant 1-bit of the number to 0, and add 1 to the sum.
As soon as the number becomes 0, we know that it does not have any more 1-bits, and we
return the sum.

The key idea here is to realize that for any number n, doing a bit-wise AND of n and
n - 1 flips the least-significant 1-bit in n to 0.

In the binary representation, the least significant 1-bit in n always corresponds to a
0-bit in n - 1. Therefore, anding the two numbers n and n - 1 always flips the least
significant 1-bit in n to 0, and keeps all other bits the same.

Complexity
==========

Time
----

hammingWeight(n): O(1).

Space
-----

hammingWeight(n): O(1).
"""


def sol(n):
    count = 0
    while n != 0:
        count += 1
        n &= n - 1
    return count
