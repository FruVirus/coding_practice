"""
Find All Anagrams in a String
-----------------------------

Given two strings s and p, return an array of all the start indices of p's anagrams in
s. You may return the answer in any order.

An Anagram is a word or phrase formed by rearranging the letters of a different word or
phrase, typically using all the original letters exactly once.

Intuition
---------
Patterns are known in advance, and the set of characters in the patterns is very limited
as well: 26 lowercase English letters. Hence one could allocate array or hashmap with 26
elements and use it as a letter counter in the sliding window.

Complexity
==========

Time
----

findAnagrams(s, p): O(n_s), where n_s is the length of s.

Space
-----

findAnagrams(s, p): O(k), where k is the maximum possible number of distinct characters.
"""


def sol(s, p):
    ns, np, pcount, scount, sol = len(s), len(p), [0] * 26, [0] * 26, []
    for char in p:
        pcount[ord(char) - ord("a")] += 1
    for i in range(ns):
        scount[ord(s[i]) - ord("a")] += 1
        if i >= np:
            scount[ord(s[i - np]) - ord("a")] -= 1
        if pcount == scount:
            sol.append(i - np + 1)
    return sol
