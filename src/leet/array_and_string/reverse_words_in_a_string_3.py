"""
Reverse Words in a String III
-----------------------------

Given a string s, reverse the order of characters in each word within a sentence while
still preserving whitespace and initial word order.

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
    i, reverse_s = len(s) - 1, ""
    while i >= 0:
        word = ""
        while i >= 0 and s[i] != " ":
            word += s[i]
            i -= 1
        reverse_s = " " + word + reverse_s
        i -= 1
    return reverse_s[1:]
