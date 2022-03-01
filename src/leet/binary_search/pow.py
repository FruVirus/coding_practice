"""
Find Minimum in Rotated Sorted Array
------------------------------------

Implement pow(x, n), which calculates x raised to the power n (i.e., x^n).

Complexity
==========

Time
----

my_pow(): O(lg n).

Space
-----

my_pow(): O(1).
"""


def my_pow(x, n):
    n, x = (n, x) if n > 0 else (-n, 1 / x)
    ans = 1
    while n > 0:
        if n % 2 == 1:
            ans *= x
        x *= x
        n //= 2
    return ans
