"""
Reverse Words in a String
-------------------------

Given an input string s, reverse the order of the words.

A word is defined as a sequence of non-space characters. The words in s will be
separated by at least one space.

Return a string of the words in reverse order concatenated by a single space.

Note that s may contain leading or trailing spaces or multiple spaces between two words.
The returned string should only have a single space separating the words. Do not include
any extra spaces.

Complexity
==========

Time
----

reverseWords(s) O(n).

Space
-----

reverseWords(s): O(n).
"""


def sol(s):
    i, reverse_s = 0, ""
    while i != len(s):
        if s[i] == " ":
            i += 1
            continue
        word = ""
        while i != len(s) and s[i] != " ":
            word += s[i]
            i += 1
        reverse_s = " " + word + reverse_s
    return reverse_s[1:]
