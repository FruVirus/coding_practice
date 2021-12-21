"""
Overview
========

A string finite automaton is a simple function that scans the text string t for all
occurrences of the pattern p. These automata are very efficient: they examine each text
character exactly once, taking constant time per text character. The matching time used
(after preprocessing the pattern to build the automaton) is therefore O(n).

At each step, the automaton is merely keeping track of the longest prefix of the pattern
that is a suffix of what has been read so far.

Complexity
==========

Preprocessing time: O(m * sigma)

Matching time: O(n)
"""


def compute_transition(p, m, sigma):
    lps, tf = 0, [[0] * sigma for _ in range(m + 1)]
    tf[0][ord(p[0])] = 1
    for i in range(1, m + 1):
        for j in range(sigma):
            tf[i][j] = tf[lps][j]
        if i < m:
            tf[i][ord(p[i])] = i + 1
            lps = tf[lps][ord(p[i])]
    return tf


def fa(t, p, sigma=256):
    n, m, q, indices = len(t), len(p), 0, []
    tf = compute_transition(p, m, sigma)
    for i in range(n):
        q = tf[q][ord(t[i])]
        if q == m:
            indices.append(i - m + 1)
    return indices
