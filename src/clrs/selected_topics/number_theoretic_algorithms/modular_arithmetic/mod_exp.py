"""
31.6 Powers of an element
=========================

A frequently occurring operation in numerics is raising one number to a power modulo
another number, also known as modular exponentiation. More precisely, we would like an
efficient way of compute a^b mod n, where a and b are non-negative integers and n is a
positive integer. The method of repeated squares solves this problem efficiently using
the binary representation of b.

This method relies on Fermat's theorem, which states that if p is prime, then
a^(p - 1) = 1 mod p for all a in Z_star_p. Equivalently, if p is prime, then
a^p = a mod p.

Intuition
---------

A "non-trivial square root of 1" means the following. 1 is congruent to 9 mod 8, thus 3
is a non-trivial square of 1 mod 8 since 1 mod 8 = 9 mod 8.

The procedure computes a^c mod n as c is increased by doublings and incrementations from
0 to b.

This method is fast (bit-wise) and saves memory since we are doing modulo operations
each time in order to ensure that the rolling results are small. That is, keeping the
numbers smaller requires additional modular reduction operations, but the reduced size
makes each operation faster, saving time (as well as memory) overall.

At each step of the for-loop (and before entering the for-loop), the condition
d = a^c mod n remains true (i.e., c = 1). When the loop terminates, we have c = b and
thus, d = a^c mod n = a^b mod n.

For example, suppose a = 7, b = 560, n = 561 and we want to compute 7^560 mod 561.
The binary representation of 560 is 1 000 11 0000. When the for-loop gets to the second
1 (going from left to right), we have d = 160 and c = 17, so that 160 = 7^17 mod 561. At
the end of the for-loop, we have that the number c = 560 so that
d = a^c mod n = a^b mod n.

Complexity
==========

Assuming a, b, and n are beta-bit numbers.

Time
----

mod_exp(): O(beta) arithmetic operations, O(beta^3) bit operations.
"""


def mod_exp(a, b, n):
    assert a >= 0 and b >= 0 and n > 0
    b, d = [int(i) for i in list(bin(b)[2:])], 1
    for i in b:
        d = (d * d) % n
        if i == 1:
            d = (d * a) % n
    return d
