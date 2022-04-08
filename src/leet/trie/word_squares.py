"""
Word Squares
------------

Given an array of unique strings words, return all the word squares you can build from
words. The same word from words can be used multiple times. You can return the answer in
any order.

A sequence of strings forms a valid word square if the k-th row and column read the same
string, where 0 <= k < max(numRows, numColumns).

    - For example, the word sequence ["ball","area","lead","lady"] forms a word square
because each word reads the same both horizontally and vertically.

Intuition
---------

For a word square with equal-sized row and column, the resulting letter matrix should be
symmetrical across its diagonal.

In other words, if we know the upper-right part of the word square, we could infer its
lower-left part, and vice versa.

The idea is that we construct the word square row by row from top to down. At each row,
we simply do trial and error; i.e., we try with one word, if it does not meet the
constraint then we try another one. At the end, if one repeats the above steps with each
word as the starting word, one would exhaust all the possibilities to construct a valid
word square.

Note that, we tweak the Trie data structure a bit, in order to further optimize the time
and space complexity.

    - Instead of labeling the word at the leaf node of the Trie, we label the word at
each node so that we don't need to perform a further traversal once we reach the last
node in the prefix. This trick could help us with the time complexity.

    - Instead of storing the actual words in the Trie, we keep only the index of the
word, which could greatly save the space.

For example:

["area","lead","wall","lady","ball"]

{
    'a': {
    '#': [0],
    'r': {
    '#': [0],
    'e': {
    '#': [0],
    'a': {'#': [0]}}}},

    'l': {
        '#': [1, 3],
        'e': {
        '#': [1],
        'a': {
        '#': [1],
        'd': {'#': [1]}}},

        'a': {
        '#': [3],
        'd': {
        '#': [3],
        'y': {'#': [3]}}}
    },

    'w': {
    '#': [2],
    'a': {
    '#': [2],
    'l': {
    '#': [2],
    'l': {
    '#': [2]}}}},

    'b': {
    '#': [4],
    'a': {
    '#': [4],
    'l': {
    '#': [4],
    'l': {
    '#': [4]}}}}
}

Complexity
==========

Time
----

wordSquares(words): O(n * 26^l * l), where n is the number of input words and l is the
length of a single word.

Space
-----

wordSquares(words): O(n * l + n * l / 2) = O(n * l). The first half of the space
complexity (i.e., n * l) is the word indices we store in the Trie, where we store l
times the index for each word. The second half (i.e., n * l / 2) is the space for the
prefixes of all words (in the worst case, we have no overlapping prefixes).
"""


def sol(words):
    sol, trie = [], build_trie(words)

    def backtrack(index, word_squares):
        if index == len(words[0]):
            sol.append(word_squares[:])
            return
        prefix = "".join([word[index] for word in word_squares])
        for word in starts_with(prefix, words, trie):
            word_squares.append(word)
            backtrack(index + 1, word_squares)
            word_squares.pop()

    for word in words:
        backtrack(1, [word])
    return sol


def build_trie(words):
    trie = {}
    for i, word in enumerate(words):
        node = trie
        for char in word:
            node = node.setdefault(char, {"#": []})
            node["#"].append(i)
    return trie


def starts_with(prefix, words, trie):
    node = trie
    for char in prefix:
        if char not in node:
            return []
        node = node[char]
    return [words[i] for i in node["#"]]
