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
    - int countWordsEqualTo(String word) Returns the number of instances of the string
word in the trie.
    - int countWordsStartingWith(String prefix) Returns the number of strings in the
trie that have the string prefix as a prefix.
    - void erase(String word) Erases the string word from the trie.

Complexity
==========

Time
----

Sol:
    def __init__(self): O(1).
    def erase(self, word): O(m).
    def insert(self, word): O(m), where m is the word length.
    def num_search(self, word): O(m).
    def num_starts_with(self, prefix): O(m).
    def search(self, word): O(m).
    def starts_with(self, prefix): O(m).

Space
-----

Sol:
    def __init__(self): O(1).
    def erase(self, word): O(1).
    def insert(self, word): O(m).
    def num_search(self, word): O(1).
    def num_starts_with(self, prefix): O(1).
    def search(self, word): O(1).
    def starts_with(self, prefix): O(1).
"""


# Standard Library
from collections import defaultdict


class TrieNode:
    def __init__(self):
        self.children, self.is_end, self.count = defaultdict(TrieNode), False, 0


class Sol:
    def __init__(self):
        self.root = TrieNode()

    def erase(self, word):
        node = self.root
        for char in word:
            if char not in node.children:
                return
            node = node.children[char]
        node.count -= 1

    def insert(self, word):
        node = self.root
        for char in word:
            node = node.children[char]
        node.is_end = True
        node.count += 1

    def num_search(self, word):
        node = self.root
        for char in word:
            if char not in node.children:
                return 0
            node = node.children[char]
        return node.count

    def num_starts_with(self, prefix):
        node = self.root
        for char in prefix:
            if char not in node.children:
                return 0
            node = node.children[char]

        def dfs(node):
            if not node.children:
                return node.count
            return sum(dfs(child) for child in node.children.values()) + node.count

        return dfs(node)

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
