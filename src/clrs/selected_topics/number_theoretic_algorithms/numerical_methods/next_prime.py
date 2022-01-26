"""
Overview
========

Find the next largest prime number given an input number n.

NB: is_prime() can be improved if we are allowed to use math.sqrt() function. In this
case, we can change the for-loop to:

    for i in range(5, sqrt(n) + 1, 6):

Complexity
==========

Time
----

is_prime(): O(n).
"""


def is_prime(n):
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    for i in range(5, n // 2 + 1, 6):
        if n % i == 0 or n % (i + 2) == 0:
            return False
    return True


def next_prime(n):
    if n <= 1:
        return 2
    n += 1
    while not is_prime(n):
        n += 1
    return n
