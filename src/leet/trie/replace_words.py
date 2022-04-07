"""
Replace Words
-------------

In English, we have a concept called root, which can be followed by some other word to
form another longer word - let's call this word successor. For example, when the root
"an" is followed by the successor word "other", we can form a new word "another".

Given a dictionary consisting of many roots and a sentence consisting of words separated
by spaces, replace all the successors in the sentence with the root forming it. If a
successor can be replaced by more than one root, replace it with the root that has the
shortest length.

Return the sentence after the replacement.

Example

Input: dictionary = ["cat","bat","rat"],
sentence = "the cattle was rattled by the battery"

Output: "the cat was rat by the bat"

Complexity
==========

Time
----

replaceWords(dictionary, sentence): O(n), where n is the length of the sentence.

Space
-----

replaceWords(dictionary, sentence): O(n).
"""


# Standard Library
from collections import defaultdict


class TrieNode:
    def __init__(self):
        self.children, self.is_end = defaultdict(TrieNode), False


class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        node = self.root
        for char in word:
            node = node.children[char]
        node.is_end = True

    def search(self, word):
        node, sol = self.root, ""
        for char in word:
            node = node.children.get(char, None)
            if not node:
                return word
            sol += char
            if node.is_end:
                return sol
        return word


def sol(dictionary, sentence):
    trie = Trie()
    for word in dictionary:
        trie.insert(word)
    return " ".join(trie.search(word) for word in sentence.split(" "))
