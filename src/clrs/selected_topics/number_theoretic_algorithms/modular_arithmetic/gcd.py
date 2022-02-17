"""
31.2 Greatest common divisor
============================

Euclid's algorithm efficiently computes the greatest common divisor of two integers. The
Fibonacci numbers yield a worst-case input for Euclid's algorithm.

We can restrict ourselves to the set of non-negative integers since gcd(a, b) =
gcd(|a|, |b|).

Euclid's algorithm relies on the following theorem:

For any non-negative integer a (a >= 0) and any positive integer b (b > 0),

    gcd(a, b) = gcd(b, a mod b)

Euclid's algorithm
------------------

The algorithm cannot recurse indefinitely, since the second argument strictly decreases
in each recursive call and is always non-negative.

The running time of Euclid's algorithm
--------------------------------------

We can assume that a > b >= 0. If b > a >=0, then gcd() spends one recursive call
swapping its arguments and then proceeds. if b = a > 0, then gcd() terminates after one
recursive call since a % b = 0.

The overall running time of gcd() is proportional to the number of recursive calls it
makes.

The extended form of Euclid's algorithm
---------------------------------------

We extend the algorithm to compute the integer coefficients x and y such that:
d = gcd(a, b) = ax + by, where x and y can be zero or negative. These coefficients are
useful for computing modular multiplicative inverses.

The number of recursive calls made in the extended version is equal to the number of
recursive calls in the original version. Thus, the running times of both are the same,
to within a constant factor.

gcd_binary() avoids the remainder computations used in gcd() since most computers can
perform the operations of subtraction, parity testing of a binary integer, and halving
more quickly than computing remainders.

gcd_multi() can take arbitrary number of arguments and return a list of (unique)
coefficients for each argument in order.

Complexity
==========

Time
----

gcd(): O(lg b) recursive calls.
gcd_binary(): O(lg a) recursive calls.
"""


def gcd(a, b):
    if b == 0:
        return a, 1, 0
    d, x, y = gcd(b, a % b)
    return d, y, x - (a // b) * y


def gcd_binary(a, b):
    if a < b:
        a, b = b, a
    if b == 0:
        return a
    if a & 1 == b & 1 == 0:
        return gcd_binary(a >> 1, b >> 1) << 1
    if a & 1 == 0 or b & 1 == 0:
        if b & 1 != 0:
            a, b = b, a
        return gcd_binary(a, b >> 1)
    return gcd_binary((a - b) >> 1, b)


def gcd_multi(*args):
    clist, i = [None] * len(args), -1
    while len(args) > 2:
        d, x, y = gcd(args[-2], args[-1])
        clist[i] = y if clist[i] is None else clist[i] * y
        if abs(i - 1) != len(args):
            clist[i - 1] = x if clist[i - 1] is None else clist[i - 1] * x
        args = args[:-2] + (d,)
        i -= 1
    d, x, y = gcd(args[0], args[1])
    clist[0] = x
    for i in range(1, len(clist)):
        clist[i] = y if clist[i] is None else clist[i] * y
    return d, clist
