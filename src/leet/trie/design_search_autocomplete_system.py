"""
Design Search Autocomplete System
---------------------------------

Design a search autocomplete system for a search engine. Users may input a sentence (at
least one word and end with a special character '#').

You are given a string array sentences and an integer array times both of length n where
sentences[i] is a previously typed sentence and times[i] is the corresponding number of
times the sentence was typed. For each input character except '#', return the top 3
historical hot sentences that have the same prefix as the part of the sentence already
typed.

Here are the specific rules:

    - The hot degree for a sentence is defined as the number of times a user typed the
exactly same sentence before.
    - The returned top 3 hot sentences should be sorted by hot degree (The first is the
hottest one). If several sentences have the same hot degree, use ASCII-code order
(smaller one appears first).
    - If less than 3 hot sentences exist, return as many as you can.
    - When the input is a special character, it means the sentence ends, and in this
case, you need to return an empty list.

Implement the AutocompleteSystem class:

    - AutocompleteSystem(String[] sentences, int[] times) Initializes the object with
the sentences and times arrays.
    - List<String> input(char c) This indicates that the user typed the character c.
        - Returns an empty array [] if c == '#' and stores the inputted sentence in the
system.
        - Returns the top 3 historical hot sentences that have the same prefix as the
part of the sentence already typed. If there are fewer than 3 matches, return them all.

Intuition
---------

def __init__(self, sentences, times, k=3):
    We call add_word() to construct a trie using all the sentences.

def add_word(self, word):
    For each character in word, we build a nested dictionary (i.e., a trie) for that
word. Since word can also be a sentence here, we are effectively building a trie for
sentences. In other words, we are treating sentences as "words". The key for each nested
dictionary can be any character (just choose "$").

def input(self, c):
    1. Python sorted() will automatically sort based on ASCII-code order. In addition,
we negate the times so that the hottest sentences are first (since they have the highest
value for times).
    2. If the current character is not "#", then we just keep appending the character to
the current sentence so far and call starts_with() to get the top k sentences with the
current sentence prefix so far.
    3. If the current character is "#", then this means we've reached the end of the
current sentence and we should return an empty list. Before we return the empty list, we
need to do one of two things:
        a. If the current sentence is part of self.idx_map, this means that it was a
previously existing sentence. Thus, we should increment its hot degree by 1 for future
searches.
        b. Otherwise, this means we have a new sentence being searched for. We update
self.sents, self.idx_map, self.times, and self.num_sents accordingly and add the new
sentence to the trie.
        c. Finally, we reset self.curr_sent to an empty string and return an empty list.

def starts_with(self):
    We return the indices of nodes in the trie that starts with the characters in the
current input sentence.

Complexity
==========

Time
----

Sol:
    def __init__(self, sentences, times, k=3): O(m), where m is the word length.
    def add_word(self, word): O(m).
    def input(self, c): O(m * lg m).
    def starts_with(self): O(m).

Space
-----

Sol:
    def __init__(self, sentences, times, k=3): O(m).
    def add_word(self, word): O(m).
    def input(self, c): O(1).
    def starts_with(self): O(1).
"""


class Sol:
    def __init__(self, sentences, times, k=3):
        self.k, self.sents, self.times = k, sentences, times
        self.curr_sent, self.num_sents = "", len(self.sents)
        self.idx_map, self.trie = {s: i for i, s in enumerate(self.sents)}, {}
        for s in self.sents:
            self.add_word(s)

    def add_word(self, word):
        node = self.trie
        for char in word:
            node = node.setdefault(char, {"$": []})
            node["$"].append(self.idx_map[word])

    def input(self, c):
        if c != "#":
            self.curr_sent += c
            topk = sorted([(-self.times[i], self.sents[i]) for i in self.starts_with()])
            return [s[1] for s in topk[: self.k]]
        if self.curr_sent in self.idx_map:
            self.times[self.idx_map[self.curr_sent]] += 1
        else:
            self.sents.append(self.curr_sent)
            self.idx_map[self.curr_sent] = self.num_sents
            self.times.append(1)
            self.num_sents += 1
            self.add_word(self.curr_sent)
        self.curr_sent = ""
        return []

    def starts_with(self):
        node = self.trie
        for char in self.curr_sent:
            if char not in node:
                return []
            node = node[char]
        return node["$"]
