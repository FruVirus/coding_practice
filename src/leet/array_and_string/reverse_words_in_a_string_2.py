"""
Reverse Words in a String II
----------------------------

Given a character array s, reverse the order of the words.

A word is defined as a sequence of non-space characters. The words in s will be
separated by a single space.

Your code must solve the problem in-place, i.e. without allocating extra space.

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
    reverse(s, 0, len(s) - 1)
    reverse_words(s)


def reverse(s, i, j):
    while i < j:
        s[i], s[j] = s[j], s[i]
        i, j = i + 1, j - 1


def reverse_words(s):
    i, j, n = 0, 0, len(s)
    while i < n:
        while j < n and s[j] != " ":
            j += 1
        reverse(s, i, j - 1)
        i = j + 1
        j += 1
