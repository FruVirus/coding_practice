"""
Overview
========

The naive algorithm finds all valid shifts using a loop that checks the condition
P[1...m] = T[s + 1...s + m] for each of the n - m + 1 possible values of s, where P is
the pattern to find, T is the text from which to find the pattern, and s is the shift
value where the pattern occurs.

Because the naive algorithm requires no preprocessing, its running time equals its
matching time.

Complexity
==========

O((n - m + 1) * m), where n is the length of the text and m is the length of the
pattern.
"""


def naive(t, p):
    return [s for s in range(len(t) - len(p)) if p == t[s : s + len(p)]]
