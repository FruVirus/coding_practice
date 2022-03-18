"""
Group Anagrams
--------------

Given an array of strings strs, group the anagrams together. You can return the answer
in any order.

An anagram is a word or phrase formed by rearranging the letters of a different word or
phrase, typically using all the original letters exactly once.

Intuition
---------

Two strings are anagrams if and only if their sorted strings are equal.

Two strings are anagrams if and only if their character counts (respective number of
occurrences of each character) are the same.

Complexity
==========

Time
----

groupAnagrams(strs): O(n * k), where n is the length of strs and k is the maximum length
of a string in strs. Counting each string is linear in the size of the string and we
count every string.

Space
-----

groupAnagrams(strs): O(n * k), the total information content stored in anagram.
"""

# Standard Library
from collections import defaultdict


def sol(strs):
    anagram = defaultdict(list)
    for s in strs:
        count = [0] * 26
        for char in s:
            count[ord(char) - ord("a")] += 1
        anagram[tuple(count)].append(s)
    return anagram.values()
