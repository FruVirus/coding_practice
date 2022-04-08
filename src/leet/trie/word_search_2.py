"""
Word Search II
--------------

Given an m x n board of characters and a list of strings words, return all words on the
board.

Each word must be constructed from letters of sequentially adjacent cells, where
adjacent cells are horizontally or vertically neighboring. The same letter cell may not
be used more than once in a word.

Intuition
---------

The problem is actually a simplified crossword puzzle game, where the word solutions
have been given on the board embedded with some noise letters. All we need to do is to
cross them out.

Intuitively, in order to cross out all potential words, the overall strategy would be to
iterate the cell one by one, and from each cell we walk along its neighbors in four
potential directions to find matched words. While wandering around the board, we would
stop the exploration when we know it would not lead to the discovery of new words.

The key of the solution lies on how we find the matches of word from the dictionary.
Intuitively, one might resort to the hashset data structure (e.g. set() in Python). This
could work.

However, during the backtracking process, one would encounter more often the need to
tell if there exists any word that contains certain prefix, rather than if a string
exists as a word in the dictionary. Because if we know that there does not exist any
match of word in the dictionary for a given prefix, then we would not need to further
explore certain direction. And this, would greatly reduce the exploration space,
therefore improve the performance of the backtracking algorithm.

The overall workflow of the algorithm is intuitive, which consists of a loop over each
cell in the board and a recursive function call starting from the cell. Here is the
skeleton of the algorithm.

    - We build a Trie out of the words in the dictionary, which would be used for the
matching process later.

    - Starting from each cell, we start the backtracking exploration (i.e.,
backtracking(cell)), if there exists any word in the dictionary that starts with the
letter in the cell.

    - During the recursive function call backtracking(cell), we explore the neighbor
cells (i.e., neighborCell) around the current cell for the next recursive call
backtracking(neighborCell). At each call, we check if the sequence of letters that we
traverse so far matches any word in the dictionary, with the help of the Trie data
structure that we built at the beginning.

For improvements, we can gradually prune the nodes in Trie during the backtracking.

    - The idea is motivated by the fact that the time complexity of the overall
algorithm sort of depends on the size of the Trie. For a leaf node in Trie, once we
traverse it (i.e., find a matched word), we would no longer need to traverse it again.
As a result, we could prune it out from the Trie.

    - Gradually, those non-leaf nodes could become leaf nodes later, since we trim their
children leaf nodes. In the extreme case, the Trie would become empty, once we find a
match for all the words in the dictionary. This pruning measure could reduce up to 50%
of the running time for the test cases of the online judge.

For example:

["oath","pea","eat","rain"]

{
    'o': {
    'a': {
    't': {
    'h': {'$': 'oath'}}}},

    'p': {
    'e': {
    'a': {'$': 'pea'}}},

    'e': {
    'a': {
    't': {'$': 'eat'}}},

    'r': {
    'a': {
    'i': {
    'n': {'$': 'rain'}}}}
}

Complexity
==========

Time
----

findWords(board, words): O(m * (4 * 3^(l - 1)), where m is the number of cells in the
board and l is the maximum length of words. Assume the maximum length of word is L,
starting from a cell, initially we would have at most 4 directions to explore. Assume
each direction is valid (i.e., worst case), during the following exploration, we have at
most 3 neighbor cells (excluding the cell where we come from) to explore. As a result,
we would traverse at most 4 * 3^(L − 1) cells during the backtracking exploration.

Space
-----

findWords(board, words): O(n), where n is the total number of letters in the dictionary.
"""


def sol(board, words):
    sol, m, n, trie = [], len(board), len(board[0]), build_trie(words)

    def backtrack(i, j, node):
        char, start = board[i][j], node
        if char in node:
            board[i][j], node = "#", node[char]
            if "$" in node:
                sol.append(node["$"])
                del node["$"]
            for r, c in [(i - 1, j), (i + 1, j), (i, j - 1), (i, j + 1)]:
                if 0 <= r < m and 0 <= c < n:
                    backtrack(r, c, node)
            board[i][j] = char
            if not node:
                start.pop(char)

    for i in range(m):
        for j in range(n):
            backtrack(i, j, trie)
    return sol


def build_trie(words):
    trie = {}
    for word in words:
        node = trie
        for char in word:
            node = node.setdefault(char, {})
        node["$"] = word
    return trie
