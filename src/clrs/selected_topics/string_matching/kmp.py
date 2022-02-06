"""
32.4 The Knuth-Morris-Pratt algorithm
=====================================

The Knuth-Morris-Pratt algorithm avoids computing the transition function altogether,
and its matching time is O(n) using just an auxiliary function pi, which we precompute
from the pattern in time O(m) and store in an array pi[1...m]. The array pi allows us to
compute the transition function efficiently (in an amortized sense) on the fly as
needed. The value pi[q] contains the information we need to compute the transition of
(q, a) but does not depend on a.

The prefix function for a pattern
---------------------------------

The prefix function pi for a pattern encapsulates knowledge about how the pattern
matches against shifts of itself. We can take advantage of this information to avoid
testing useless shifts in the naive pattern-matching algorithm and to avoid precomputing
the full transition function for a string-matching automaton.

The information that q characters have matched successfully determines the corresponding
text characters. Knowing these q text characters allows us to determine immediately that
certain shifts are invalid.

pi[q] is the length of the longest prefix of P that is a proper suffix of P_q.

Intuition
---------

KMP avoids backtracking through the text during the matching process.

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

prefix:     a, ab, abc, abcd, ..., c
suffix:     c, bc, abc, dabc, ..., a

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

i:  1   2   3   4   5   6   7   8   9
P:  a   a   a   a   b   a   a   c   d
    0   1   2   3   0   1   2   0   0 --> matching indices of pi table

Example:

string:     a   b   a   b   c   a   b   c   a   b   a   b   a   b   d
i:          1   2   3   4   5   6   7   8   9   10  11  12  13  14  15

pattern:    a   b   a   b   d
j:          1   2   3   4   5

1. Create pi table for pattern.

pi table: [0, 0, 1, 2, 0]

The pi table is filled in with the i indices for each longest prefix match. When a
mismatch occurs, the values in the pi table transitions back to a previous longest
longest prefix match if there is one or the value becomes 0 again.

2. Find matching starting with i = j = 0.

We iterate through all characters in the text, t, to find occurrences of the complete
pattern P.

If p[j] == t[i], then we have a character match at index i in t and index j in p. Thus,
we increment both indices by one. This occurs until i = j = 5.

At i = j = 5, we have a mismatch between p[j] = d and t[i] = c. In addition, j != m so
we don't have a complete pattern match yet. Thus, we can either transition index j back
to the previous state in the pi table or advance index i by one position. If we can
still transition index j back in the pi table (i.e., j != 0), then we do so; this means
that we may have a potential partial match so far and so we don't want to advance index
i until we are sure that there are no more partial matches at index j.

In other words, since we did not match ababc with ababd, we go back to ab and check if
aba matches with abc. Since aba does not match with abc either, we transition index j
back in the pi table again so that j = 0 and check if a matches with c. Since a does not
match with c and j = 0, we have no choice but to advance the index i; this effectively
starts the search over again in the text.

If we have a partial match at any point when transitioning j back in the pi table, we
we continue to check if p[j] == t[i] and increment the indices j and i accordingly.

Once j == m, then we have a complete match of the pattern. The index j then transitions
back to the previous state in the pi table.

Complexity
==========

Time
----

compute_pi_table(): O(m) preprocessing.
kmp(): O(n) matching.

Space
-----

compute_pi_table(): O(m) for pi table.
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
    n, m, q, indices = len(t), len(p), 0, []
    pi_table = compute_pi_table(p, m)
    for i in range(n):
        while q > 0 and p[q] != t[i]:
            q = pi_table[q - 1]
        if p[q] == t[i]:
            q += 1
        if q == m:
            indices.append(i - m + 1)
            q = pi_table[q - 1]
    return indices
