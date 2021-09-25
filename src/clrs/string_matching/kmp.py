"""The Knuth-Morris-Pratt algorithm avoids computing the transition function altogether,
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

Complexity
==========

Preprocessing time: O(m)

Matching time: O(n)
"""


def kmp_prefix(p, m):
    pi, k = [0] * m, 0
    for q in range(1, m):
        while k > 0 and p[k] != p[q]:
            k = pi[k]
        if p[k] == p[q]:
            k += 1
        pi[q] = k
    return pi


def kmp(t, p):
    n, m, indices, i, j = len(t), len(p), [], 0, 0
    pi = kmp_prefix(p, m)
    while i < n:
        if p[j] == t[i]:
            i += 1
            j += 1
        if j == m:
            indices.append(i - j)
            j = pi[j - 1]
        elif i < n and p[j] != t[i]:
            if j != 0:
                j = pi[j - 1]
            else:
                i += 1
    return indices
