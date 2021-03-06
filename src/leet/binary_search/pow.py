"""
Find Minimum in Rotated Sorted Array
------------------------------------

Implement pow(x, n), which calculates x raised to the power n (i.e., x^n).

Intuition
---------

The method is based on the observation that, for a positive integer n, we have:

    x^n =   x * (x^2)^((n - 1) / 2), if n is odd
            (x^2) * (n / 2), if n is even

Initially, x^1 = x, and for each i > 1, we can use the result of x^(2 * i - 1) to get
x^(2 * i).

Complexity
==========

Time
----

myPow(x, n): O(lg n).

Space
-----

myPow(x, n): O(1).
"""


def sol(x, n):
    n, x = (n, x) if n > 0 else (-n, 1 / x)
    ans = 1
    while n > 0:
        if n % 2 != 0:
            ans *= x
        x *= x
        n //= 2
    return ans
