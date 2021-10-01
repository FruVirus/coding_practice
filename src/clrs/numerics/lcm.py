"""
Overview
========

lcm_multi() finds the least common multiple for a range of numbers using Euclid's
algorithm.

Complexity
==========

O(lg(b)) recursive calls.
"""

# Repository Library
from src.clrs.numerics.gcd import gcd


def lcm(a, b):
    return abs(a * b) // gcd(a, b)[0]


def lcm_multi(*args):
    while len(args) > 2:
        a, b = args[-2], args[-1]
        args = args[:-2] + (lcm(a, b),)
    return lcm(args[0], args[1])
