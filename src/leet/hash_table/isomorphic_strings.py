"""
Isomorphic Strings
------------------

Given two strings s and t, determine if they are isomorphic.

Two strings s and t are isomorphic if the characters in s can be replaced to get t.

All occurrences of a character must be replaced with another character while preserving
the order of characters. No two characters may map to the same character, but a
character may map to itself.

Complexity
==========

Time
----

isIsomorphic(s, t): O(n).

Space
-----

isIsomorphic(s, t): O(1), since the size of the ASCII character set is fixed and the
keys in the dictionaries are all valid ASCII characters.
"""


def sol(s, t):
    map_s, map_t = {}, {}
    for char_s, char_t in zip(s, t):
        if char_s not in map_s and char_t not in map_t:
            map_s[char_s], map_t[char_t] = char_t, char_s
        elif map_s.get(char_s) != char_t or map_t.get(char_t) != char_s:
            return False
    return True
