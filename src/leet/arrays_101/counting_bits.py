"""
Counting Bits
-------------

Given an integer n, return an array ans of length n + 1 such that for each i
(0 <= i <= n), ans[i] is the number of 1's in the binary representation of i.

Intuition
---------

Let's look at the relation between x and x' = x / 2.

x  = (1001011101)_2 = (605)_10
x' = (100101110)_2  = (302)_10

We can see that x' is different than x by one bit, because x' can be considered as the
result of removing the least significant bit of x.

Thus, we have the following transition function of pop count P(x):

P(x) = P(x / 2) + (x mod 2).

Complexity
==========

Time
----

countBits(n): O(n).

Space
-----

countBits(n): O(1).
"""


def sol(n):
    sol = [0] * (n + 1)
    for i in range(1, n + 1):
        sol[i] = sol[i >> 1] + (i & 1)
    return sol
