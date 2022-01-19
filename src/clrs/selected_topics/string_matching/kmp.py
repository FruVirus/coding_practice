"""
32.4 The Knuth-Morris-Pratt algorithm
=====================================

The Knuth-Morris-Pratt algorithm avoids computing the transition function altogether,
and its matching time is O(n) using just an auxiliary function pi, which we precompute
from the pattern in time O(m) and store in an array pi[1...m]. The array pi allows us to
compute the transition function efficiently (in an amortized sense) on the fly as
needed. The value pi[q] contains the information we need to compute the transition of
(q, a) but does not depend on a.

The prefix function, pi, for a pattern encapsulates knowledge about how the pattern
matches against shifts of itself. The information that q characters have matched
successfully determines the corresponding text characters. Knowing these q text
characters allows us to determine immediately that certain shifts are invalid.

KMP avoids backtracking through the text during the matching process.

kmp_prefix() matches the pattern p against itself. At each position in the pattern, we
check to see if the prefix so far has been seen already in the pattern. If so, then we
increment the counter at that position in the pi table.

kmp() matches the text t against the pattern as follows:

1. If t[i] matches with p[j], then both i and j are incremented to their next positions.
2. If j == m, then we have a match and we can revert back the previous position in the
pi table.
3. If j != m and j != 0, then this means we can revert back to the previous position in
the pi table to check the matching.
4. If j != m and j == 0, then we have reverted back to the beginning of the pi table,
found no matches, and thus, we increment i and start the search for the pattern anew.

In essence, kmp() iterates through the states in the pi table in decreasing order,
stopping at some state x and then possibly moving to state x + 1 if strings continue to
match.

Intuition
---------

Consider the following example:

string:     a   b   c   d   a   b   c   a   b   c   d   f
i:          1   2   3   4   5   6   7   8   9   10  11  12

pattern:    a   b   c   d   f
j:          1   2   3   4   5

We start with i = j = 1.

At i = j = 1, we have a match --> j moves to 2 and i moves to 2.
At i = j = 2, we have a match --> j moves to 3 and i moves to 3.
At i = j = 3, we have a match --> j moves to 4 and i moves to 4.
At i = j = 4, we have a match --> j moves to 5 and i moves to 5.
At i = j = 5, we have a mismatch --> j moves back to 1 and i moves back to 2.

And repeat the process of finding a match.

This naive approach is inefficient because we move i all the way back to index 2 and
start again. This effectively throws away information regarding the characters we have
seen so far. We want to avoid this backtracking of the index i through the string.

Worst case:

string:     a   a   a   a   a   a   a   b
i:          1   2   3   4   5   6   7   8

pattern:    a   a   a   b
j:          1   2   3   4

This pattern matching will cause i to increment by one position each time the pattern
matching is repeated! This results in O((n - m + 1) * m) complexity. However, once we
get to i = 4 and find the mismatch, we already know that i = [2, 4] is a match for the
pattern so far. Thus, we should only have to check if i = 5 is b. In other words, we
should have a way to keep information about the past so that the index i only moves
forward during the pattern matching.

The KMP algorithm works as follows:

A given pattern has prefixes and suffixes. For example, consider:

pattern:    a   b   c   d   a   b   c
i:          1   2   3   4   5   6   7

prefix:     a, ab, abc, abcd, ...
suffix:     c, bc, abc, dabc, ...

Note that abc is both a prefix and suffix of the pattern.

The main idea of KMP is: inside the pattern, are there any prefixes that are also
suffixes of the pattern. In other words, does the beginning part of a pattern appear
anywhere else in the pattern?

KMP algorithm generates a pi table (longest prefix suffix table) as follows:

i:  1   2   3   4   5   6   7   8   9   10
P:  a   b   c   d   a   b   e   a   b   f
    0   0   0   0   1   2   0   1   2   0  --> matching indices of pi table

i:  1   2   3   4   5   6   7   8   9   10  11
P:  a   b   c   d   e   a   b   f   a   b   c
    0   0   0   0   0   1   2   0   1   2   3 --> matching indices of pi table

i:  1   2   3   4   5   6   7   8   9   10
P:  a   a   b   c   a   d   a   a   b   e
    0   1   0   0   1   0   1   2   3   0 --> matching indices of pi table

Complexity
==========

Time
----

compute_pi_table(): O(m) preprocessing.
kmp(): O(n) matching.
"""


def compute_pi_table(p, m):
    pi_table, k = [0] * m, 0
    for i in range(1, m):
        while k > 0 and p[k] != p[i]:
            k = pi_table[k - 1]
        if p[k] == p[i]:
            k += 1
        pi_table[i] = k
    return pi_table


def kmp(t, p):
    n, m, indices, i, j = len(t), len(p), [], 0, 0
    pi_table = compute_pi_table(p, m)
    while i < n:
        if p[j] == t[i]:
            i += 1
            j += 1
        if j == m:
            indices.append(i - j)
            j = pi_table[j - 1]
        elif i < n and p[j] != t[i]:
            if j != 0:
                j = pi_table[j - 1]
            else:
                i += 1
    return indices
