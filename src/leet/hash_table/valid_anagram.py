"""
Valid Anagram
-------------

Given two strings s and t, return true if t is an anagram of s, and false otherwise.

An Anagram is a word or phrase formed by rearranging the letters of a different word or
phrase, typically using all the original letters exactly once.

Complexity
==========

Time
----

isAnagram(s, t): O(n).

Space
-----

isAnagram(s, t): O(1).
"""


def sol(s, t):
    if len(s) != len(t):
        return False
    count = [0] * 26
    for char in s:
        count[ord(char) - ord("a")] += 1
    for char in t:
        count[ord(char) - ord("a")] -= 1
        if count[ord(char) - ord("a")] < 0:
            return False
    return True
