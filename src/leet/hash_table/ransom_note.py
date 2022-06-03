"""
Ransom Note
-----------

Given two strings ransomNote and magazine, return true if ransomNote can be constructed
from magazine and false otherwise.

Each letter in magazine can only be used once in ransomNote.

Complexity
==========

Time
----

canConstruct(ransom_note, magazine): O(m), where m is the number of characters in
magazine.

Space
-----

canConstruct(ransom_note, magazine): O(1).
"""

# Standard Library
from collections import Counter


def sol(ransom_note, magazine):
    if len(ransom_note) > len(magazine):
        return False
    letters = Counter(magazine)
    for char in ransom_note:
        if letters[char] == 0:
            return False
        letters[char] -= 1
    return True
