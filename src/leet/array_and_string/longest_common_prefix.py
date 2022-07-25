"""
Longest Common Prefix
---------------------

Write a function to find the longest common prefix string amongst an array of strings.

If there is no common prefix, return an empty string "".

Intuition
---------

string max()/min() returns the maximum/minimum alphabetical ordering of strings. Also
note that we are trying to find the longest common prefix amongst ALL the strings in the
array of strings.

Complexity
==========

Time
----

longestCommonPrefix(strs): O(n + m).

Space
-----

longestCommonPrefix(strs): O(k), where k is the longest common prefix in strs.
"""


def sol(strs):
    lcp = ""
    for x, y in zip(min(strs), max(strs)):
        if x != y:
            break
        lcp += x
    return lcp
