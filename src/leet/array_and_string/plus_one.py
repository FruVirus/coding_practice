"""
Plus One
--------

You are given a large integer represented as an integer array digits, where each
digits[i] is the ith digit of the integer. The digits are ordered from most significant
to least significant in left-to-right order. The large integer does not contain any
leading 0's.

Increment the large integer by one and return the resulting array of digits.

Complexity
==========

Time
----

plusOne(digits): O(n).

Space
-----

plusOne(digits): O(n).
"""


def sol(digits):
    for i in reversed(range(len(digits))):
        if digits[i] != 9:
            digits[i] += 1
            return digits
        digits[i] = 0
    return [1] + digits
