"""
Overview
========

Euclid's algorithm efficiently computes the greatest common divisor of two integers. The
Fibonacci numbers yield a worst-case input for Euclid's algorithm. We can restrict
ourselves to the set of non-negative integers since gcd(a, b) = gcd(|a|, |b|).

Euclid's algorithm relies on the following theorem:

    For any non-negative integer a and any positive integer b,

        gcd(a, b) = gcd(b, a mod b)

The algorithm cannot recurse indefinitely, since the second argument strictly decreases
in each recursive call and is always non-negative.

We can assume that a > b >= 0. If b > a >=0, then gcd() spends one recursive call
swapping its arguments and then proceeds. if b = a > 0, then gcd() terminates after one
recursive call since a % b = 0. The overall running time of gcd() is proportional to the
number of recursive calls it makes.

For the extended version, we also compute the integer coefficients x and y such that:
d = gcd(a, b) = ax + by, where x and y acn be zero or negative. These coefficients are
useful for compute modular multiplicative inverses.

The number of recursive calls made in the extended version is equal to the number of
recursive calls in the original version. Thus, the running times of both are the same,
to within a constant factor.

gcd_multi() can take arbitrary number of arguments and return a list of (unique)
coefficients for each argument in order.

Complexity
==========

O(lg(b)) recursive calls.
"""


def gcd(a, b):
    if b == 0:
        return a, 1, 0
    d, x, y = gcd(b, a % b)
    return d, y, x - (a // b) * y


def gcd_multi(*args):
    c_list, i = [None] * len(args), -1
    while len(args) > 2:
        d, x_, y_ = gcd(args[-2], args[-1])
        c_list[i] = y_ if c_list[i] is None else c_list[i] * y_
        if abs(i - 1) != len(args):
            c_list[i - 1] = x_ if c_list[i - 1] is None else c_list[i - 1] * x_
        args = args[:-2] + (d,)
        i -= 1
    d, x, y = gcd(args[0], args[1])
    c_list[0] = x
    for i in range(1, len(c_list)):
        c_list[i] = y if c_list[i] is None else c_list[i] * y
    return d, c_list
