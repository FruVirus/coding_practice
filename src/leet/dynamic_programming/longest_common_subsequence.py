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

In the standard approach, we only ever looked at the current column and the previous
column. After that, previously computed columns are no longer needed.

We can save a lot of space by only keeping track of the last two columns.

This reduces the space complexity to be proportional to the length of the word going
down. We should make sure this is the shortest of the two words.

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
    prev, curr = [0] * (len(text1) + 1), [0] * (len(text1) + 1)
    for i in reversed(range(len(text2))):
        for j in reversed(range(len(text1))):
            if text2[i] == text1[j]:
                curr[j] = 1 + prev[j + 1]
            else:
                curr[j] = max(prev[j], curr[j + 1])
        prev, curr = curr, prev
    return prev[0]
