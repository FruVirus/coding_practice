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
    reverse_word(s)


def reverse(s, left, right):
    while left < right:
        s[left], s[right] = s[right], s[left]
        left, right = left + 1, right - 1


def reverse_word(s):
    start, end, n = 0, 0, len(s)
    while start < n:
        while end < n and s[end] != " ":
            end += 1
        reverse(s, start, end - 1)
        start = end + 1
        end += 1
