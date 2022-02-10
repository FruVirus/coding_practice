"""
Overview
========

lcm_multi() finds the least common multiple for a range of numbers using Euclid's
algorithm.

Because gcd(a, b) is a divisor of both a and b, it is more efficient to compute the LCM
by dividing before multiplying since this reduces the size of one input for both the
division and multiplication, and reduces the required storage needed for intermediate
results (i.e., divide a by gcd(a, b) and then multiply by b).

Complexity
==========

Time
----

lcm(): O(lg b) recursive calls.
"""

# Repository Library
from src.clrs.selected_topics.number_theoretic_algorithms.modular_arithmetic.gcd import (  # noqa: E501
    gcd,
)


def lcm(a, b):
    return 0 if a == b == 0 else (abs(a) / gcd(a, b)[0]) * b


def lcm_multi(*args):
    while len(args) > 2:
        args = args[:-2] + (lcm(args[-2], args[-1]),)
    return lcm(args[0], args[1])
