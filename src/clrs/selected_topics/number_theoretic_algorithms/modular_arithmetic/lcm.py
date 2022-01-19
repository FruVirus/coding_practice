"""
Overview
========

lcm_multi() finds the least common multiple for a range of numbers using Euclid's
algorithm.

Complexity
==========

lcm(): O(lg b) recursive calls.
"""

# Repository Library
from src.clrs.selected_topics.number_theoretic_algorithms.modular_arithmetic.gcd import (  # noqa: E501
    gcd,
)


def lcm(a, b):
    return abs(a * b) // gcd(a, b)[0]


def lcm_multi(*args):
    while len(args) > 2:
        args = args[:-2] + (lcm(args[-2], args[-1]),)
    return lcm(args[0], args[1])
