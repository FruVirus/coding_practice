"""
Implement Queue using Stacks
----------------------------

A trie (pronounced as "try") or prefix tree is a tree data structure used to efficiently
store and retrieve keys in a dataset of strings. There are various applications of this
data structure, such as autocomplete and spellchecker.

Implement the Trie class:

    - Trie() Initializes the trie object.
    - void insert(String word) Inserts the string word into the trie.
    - boolean search(String word) Returns true if the string word is in the trie (i.e.,
was inserted before), and false otherwise.
    - boolean startsWith(String prefix) Returns true if there is a previously inserted
string word that has the prefix, and false otherwise.

Complexity
==========

Time
----

Sol:
    def __init__(self): O(1).
    def insert(self, word): O(m), where m is the word length.
    def search(self, word): O(m).
    def starts_with(self, prefix): O(m).

Space
-----

Sol:
    def __init__(self): O(1).
    def insert(self, word): O(m).
    def search(self, word): O(1).
    def starts_with(self, prefix): O(1).
"""


class TrieNode:
    def __init__(self):
        self.children, self.is_end = {}, False


class Sol:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        node = self.root
        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
        node.is_end = True

    def search(self, word):
        node = self.root
        for char in word:
            if char not in node.children:
                return False
            node = node.children[char]
        return node.is_end

    def starts_with(self, prefix):
        node = self.root
        for char in prefix:
            if char not in node.children:
                return False
            node = node.children[char]
        return True
