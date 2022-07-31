"""
Word Ladder
-----------

A transformation sequence from word beginWord to word endWord using a dictionary
wordList is a sequence of words beginWord -> s1 -> s2 -> ... -> sk such that:

    - Every adjacent pair of words differs by a single letter.
    - Every s_i for 1 <= i <= k is in wordList. Note that beginWord does not need to be
in wordList.
    - s_k == endWord

Given two words, beginWord and endWord, and a dictionary wordList, return the number of
words in the shortest transformation sequence from beginWord to endWord, or 0 if no such
sequence exists.

Example 1:

    Input: beginWord = "hit", endWord = "cog", wordList =
["hot","dot","dog","lot","log","cog"]
    Output: 5
    Explanation: One shortest transformation sequence is "hit" -> "hot" -> "dot" ->
"dog" -> cog", which is 5 words long.

Intuition
---------

We are given a beginWord and an endWord. Let these two represent start node and end node
of a graph. We have to reach from the start node to the end node using some intermediate
nodes/words. The intermediate nodes are determined by the wordList given to us. The only
condition for every step we take on this ladder of words is the current word should
change by just one letter.

We will essentially be working with an undirected and unweighted graph with words as
nodes and edges between words which differ by just one letter. The problem boils down to
finding the shortest path from a start node to a destination node, if there exists one.
Hence it can be solved using Breadth First Search approach.

One of the most important step here is to figure out how to find adjacent nodes i.e.
words which differ by one letter. To efficiently find the neighboring nodes for any
given word we do some pre-processing on the words of the given wordList. The
pre-processing involves replacing the letter of a word by a non-alphabet say, *.

This pre-processing helps to form generic states to represent a single letter change.

For e.g. Dog ----> D*g <---- Dig

Both Dog and Dig map to the same intermediate or generic state D*g.

The preprocessing step helps us find out the generic one letter away nodes for any word
of the word list and hence making it easier and quicker to get the adjacent nodes.
Otherwise, for every word we will have to iterate over the entire word list and find
words that differ by one letter. That would take a lot of time. This preprocessing step
essentially builds the adjacency list first before beginning the breadth first search
algorithm.

For example, while doing BFS if we have to find the adjacent nodes for Dug we can first
find all the generic states for Dug.

    1. Dug => *ug
    2. Dug => D*g
    3. Dug => Du*

The second transformation D*g could then be mapped to Dog or Dig, since all of them
share the same generic state. Having a common generic transformation means two words are
connected and differ by one letter.

Complexity
==========

Time
----

ladderLength(begin_word, end_word, word_list): O(m^2 * n), where m is the length of each
word and n is the total number of words in the input word list.

Space
-----

ladderLength(begin_word, end_word, word_list): O(m^2 * n).
"""

# Standard Library
from collections import deque


def sol(begin_word, end_word, word_list):
    def get_word(word, index):
        return word[:index] + "*" + word[index + 1:]

    n, combos = len(begin_word), defaultdict(list)
    for word in word_list:
        for i in range(n):
            combos[get_word(word, i)].append(word)
    queue, seen = deque([(begin_word, 1)]), {begin_word}
    while queue:
        current_word, level = queue.popleft()
        for i in range(n):
            intermediate_word = get_word(current_word, i)
            for word in combos[intermediate_word]:
                if word == end_word:
                    return level + 1
                if word not in seen:
                    seen.add(word)
                    queue.append((word, level + 1))
            combos[intermediate_word] = []
    return 0
