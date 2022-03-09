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
    i, reverse_s = 0, ""
    while i < len(s):
        word = ""
        while i < len(s) and s[i] != " ":
            word = s[i] + word
            i += 1
        i += 1
        reverse_s += word + " "
    return reverse_s[:-1]
