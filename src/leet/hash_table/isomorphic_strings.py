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
    maps, mapt = {}, {}
    for chars, chart in zip(s, t):
        if not (chars in maps or chart in mapt):
            maps[chars], mapt[chart] = chart, chars
        elif maps.get(chars) != chart or mapt.get(chart) != chars:
            return False
    return True
