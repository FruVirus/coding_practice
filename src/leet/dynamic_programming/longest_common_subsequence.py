"""
Longest Common Subsequence
--------------------------

Given two strings text1 and text2, return the length of their longest common
subsequence. If there is no common subsequence, return 0.

A subsequence of a string is a new string generated from the original string with some
characters (can be none) deleted without changing the relative order of the remaining
characters.

    - For example, "ace" is a subsequence of "abcde".

A common subsequence of two strings is a subsequence that is common to both strings.

Intuition
---------

If the first character of each string is not the same, then either one or both of those
characters will not be used in the final result. Therefore, the length of the longest
common subsequence is max(LCS(p1 + 1, p2), LCS(p1, p2 + 1)).

When the first character of each string is the same, the length of the longest common
subsequence is 1 + LCS(p1 + 1, p2 + 1). In other words, we add 1 to represent the same
first character from both strings and then solve the resulting subproblem (that has the
first character removed from each string).

In the standard approach, we only ever looked at the current column and the previous
column. After that, previously computed columns are no longer needed. We can save a lot
of space by only keeping track of the last two columns. This reduces the space
complexity to be proportional to the length of the shorter word. We should make sure
this is the shortest of the two words.

Complexity
==========

Time
----

longestCommonSubsequence(text1, text2): O(m * n).

Space
-----

longestCommonSubsequence(text1, text2): O(min(m, n)).
"""


def sol_bu(text1, text2):
    if len(text1) > len(text2):
        text1, text2 = text2, text1
    m, n = len(text1), len(text2)
    prev, curr = [0] * (m + 1), [0] * (m + 1)
    for col in range(1, n + 1):
        for row in range(1, m + 1):
            cond = text1[row - 1] == text2[col - 1]
            curr[row] = 1 + prev[row - 1] if cond else max(prev[row], curr[row - 1])
        prev, curr = curr, prev
    return prev[-1]
