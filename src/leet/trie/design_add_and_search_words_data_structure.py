"""
Design Add and Search Words Data Structure
------------------------------------------

Design a data structure that supports adding new words and finding if a string matches
any previously added strings.

Implement the WordDictionary class:

    - WordDictionary() Initializes the object.
    - void addWord(word) Adds word to the data structure, it can be matched later.
    - bool search(word) Returns true if there is any string in the data structure that
matches word or false otherwise. word may contain dots '.' where dots can be matched
with any letter.

Intuition
---------

Everytime we see ".", we essentially skip over the current node and recurse the search
into the node's children. During the recursion, we would return True if we eventually
reach a leaf node or False if a character in word is not found in the Trie.

Complexity
==========

Time
----

Sol:
    def __init__(self): O(1).
    def add_word(self, word): O(m), where m is the word length.
    def search(self, word): O(m) for words without dots and O(n * 26^m) for a word with
all dots, where n is the number of keys.

Space
-----

Sol:
    def __init__(self): O(1).
    def add_word(self, word): O(m). In the worst case, the newly inserted word doesn't
share a prefix with the keys already inserted in the trie.
    def search(self, word): O(1) for words without dots and O(m) for a word with all
dots.
"""


# Standard Library
from collections import defaultdict


class TrieNode:
    def __init__(self):
        self.children, self.is_end = defaultdict(TrieNode), False


class Sol:
    def __init__(self):
        self.root = TrieNode()

    def add_word(self, word):
        node = self.root
        for char in word:
            node = node.children[char]
        node.is_end = True

    def search(self, word):
        def search_(index, node):
            for i, char in enumerate(word[index:], index):
                if char == ".":
                    for child in node.children.values():
                        if search_(i + 1, child):
                            return True
                    return False
                if char not in node.children:
                    return False
                node = node.children[char]
            return node.is_end

        return search_(0, self.root)
