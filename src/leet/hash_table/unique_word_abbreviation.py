"""
Unique Word Abbreviation
------------------------

The abbreviation of a word is a concatenation of its first letter, the number of
characters between the first and last letter, and its last letter. If a word has only
two characters, then it is an abbreviation of itself.

For example:

    - dog --> d1g because there is one letter between the first letter 'd' and the last
letter 'g'.
    - internationalization --> i18n because there are 18 letters between the first
letter 'i' and the last letter 'n'.
    - it --> it because any word with only two characters is an abbreviation of itself.

Implement the ValidWordAbbr class:

    - ValidWordAbbr(String[] dictionary) Initializes the object with a dictionary of
words.
    - boolean isUnique(string word) Returns true if either of the following conditions
are met (otherwise returns false):
        - There is no word in dictionary whose abbreviation is equal to word's
abbreviation.
        - For any word in dictionary whose abbreviation is equal to word's abbreviation,
that word and word are the same.

Complexity
==========

Time
----

Sol:
    def __init__(self, dictionary): O(n).
    def is_unique(self, word): O(1).

Space
-----

Sol:
    self.dict: O(n).
"""


# Standard Library
from collections import defaultdict


class Sol:
    def __init__(self, dictionary):
        self.dict = defaultdict(set)
        for word in dictionary:
            self.dict[self.abbrev(word)].add(word)

    @staticmethod
    def abbrev(word):
        return word if len(word) < 3 else word[0] + str(len(word) - 2) + word[-1]

    def is_unique(self, word: str) -> bool:
        abbrev = self.abbrev(word)
        if abbrev not in self.dict:
            return True
        if len(self.dict[abbrev]) == 1 and next(iter(self.dict[abbrev])) == word:
            return True
        return False
