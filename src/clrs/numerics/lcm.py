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


def lcm_multi(*args):
    while len(args) > 2:
        a, b = args[-2], args[-1]
        m = abs(a * b) // gcd(a, b)[0]
        args = args[:-2] + (m,)
    a, b = args[0], args[1]
    return abs(a * b) // gcd(a, b)[0]
