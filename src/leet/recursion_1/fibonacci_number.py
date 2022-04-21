"""
Fibonacci Number
----------------

The Fibonacci numbers, commonly denoted F(n) form a sequence, called the Fibonacci
sequence, such that each number is the sum of the two preceding ones, starting from 0
and 1.

Given n, calculate F(n).

Complexity
==========

Time
----

fib(n): O(n).

Space
-----

fib(n): O(n).
"""


def sol(n):
    if n < 2:
        return n
    one, two, curr = 1, 0, 0
    for _ in range(2, n + 1):
        curr = one + two
        one, two = curr, one
    return curr
