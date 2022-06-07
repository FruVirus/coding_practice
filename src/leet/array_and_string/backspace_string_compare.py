"""
Backspace String Compare
------------------------

Given two strings s and t, return true if they are equal when both are typed into empty
text editors. '#' means a backspace character.

Note that after backspacing an empty text, the text will continue empty.

Intuition
---------

When writing a character, it may or may not be part of the final string depending on how
many backspace keystrokes occur in the future.

If instead we iterate through the string in reverse, then we will know how many
backspace characters we have seen, and therefore whether the result includes our
character.

Complexity
==========

Time
----

backspaceCompare(s, t): O(m + n).

Space
-----

backspaceCompare(s, t): O(1).
"""

# Standard Library
from itertools import zip_longest


def sol(s, t):
    def helper(s):
        skip = 0
        for char in reversed(s):
            if char == "#":
                skip += 1
            elif skip:
                skip -= 1
            else:
                yield char

    return all(x == y for x, y in zip_longest(helper(s), helper(t)))
