"""
Reverse Words in a String III
-----------------------------

Given a string s, reverse the order of characters in each word within a sentence while
still preserving whitespace and initial word order.

Input: s = "Let's take LeetCode contest"
Output: "s'teL ekat edoCteeL tsetnoc"

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
    i, rs = 0, ""
    while i < len(s):
        word = ""
        while i < len(s) and s[i] != " ":
            word = s[i] + word
            i += 1
        i += 1
        rs += word + " "
    return rs[:-1]
