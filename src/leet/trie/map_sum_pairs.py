"""
Map Sum Pairs
-------------

Design a map that allows you to do the following:

    - Maps a string key to a given value.
    - Returns the sum of the values that have a key with a prefix equal to a given
string.

Implement the MapSum class:

    - MapSum() Initializes the MapSum object.
    - void insert(String key, int val) Inserts the key-val pair into the map. If the key
already existed, the original key-value pair will be overridden to the new one.
    - int sum(string prefix) Returns the sum of all the pairs' value whose key starts
    with the prefix.

Example

Input
["MapSum", "insert", "sum", "insert", "sum"]
[[], ["apple", 3], ["ap"], ["app", 2], ["ap"]]

Output
[null, null, 3, null, 5]

Explanation

MapSum mapSum = new MapSum();
mapSum.insert("apple", 3);
mapSum.sum("ap");           // return 3 (apple = 3)
mapSum.insert("app", 2);
mapSum.sum("ap");           // return 5 (apple + app = 3 + 2 = 5)

Intuition
---------

We can remember the answer for all possible prefixes in a HashMap score. When we get a
new (key, val) pair, we update every prefix of key appropriately: each prefix will be
changed by delta = val - map[key], where map is the previously associated value of key
(zero if undefined.)

Since we are dealing with prefixes, a Trie (prefix tree) is a natural data structure to
approach this problem. For every node of the trie corresponding to some prefix, we will
remember the desired answer (score) and store it at this node. As in Approach #2, this
involves modifying each node by delta = val - map[key].

Complexity
==========

Time
----

Sol:
    def __init__(self): O(1).
    def insert(self, key, val): O(k), where k is the length of the key.
    def sum(self, prefix): O(k).

Space
-----

Sol:
    def __init__(self): Linear in the size of the total input.
"""


# Standard Library
from collections import defaultdict


class TrieNode:
    def __init__(self):
        self.children, self.score = defaultdict(TrieNode), 0


class Sol:
    def __init__(self):
        self.map, self.root = defaultdict(int), TrieNode()

    def insert(self, key, val):
        delta = val - self.map[key]
        self.map[key] = val
        node = self.root
        node.score += delta
        for char in key:
            node = node.children[char]
            node.score += delta

    def sum(self, prefix):
        node = self.root
        for char in prefix:
            if char not in node.children:
                return 0
            node = node.children[char]
        return node.score
