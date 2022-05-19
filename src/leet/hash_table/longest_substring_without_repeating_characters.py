"""
Longest Substring Without Repeating Characters
----------------------------------------------

Given a string s, find the length of the longest substring without repeating characters.

Complexity
==========

Time
----

lengthOfLongestSubstring(s): O(n), where n is the length of the string s.

Space
-----

lengthOfLongestSubstring(s): O(m), where m is the length of the longest substring
without repeating characters in s.
"""


def sol(s):
    longest, sub = 0, ""
    for char in s:
        if char not in sub:
            sub += char
            longest = max(longest, len(sub))
        else:
            sub = sub[sub.index(char) + 1 :] + char
    return longest
