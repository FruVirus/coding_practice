"""
Word Break
----------

Given a string s and a dictionary of strings wordDict, return true if s can be segmented
into a space-separated sequence of one or more dictionary words.

Note that the same word in the dictionary may be reused multiple times in the
segmentation.

Intuition
---------

In summary, the criteria is:

    1. A word from wordDict can end at the current index i.

    2. If that word is to end at index i, then it starts at index i - word.length + 1.
The index before that i - word.length should also be formable from wordDict.

The base case for this problem is another simple one. The first word used from wordDict
starts at index 0, which means we would need to check dp[-1] for the second criteria,
which is out of bounds. To fix this, we say that the second criteria can also be
satisfied by i == word.length - 1.

In the top-down approach, we can check for the base case by returning true if i < 0.

Complexity
==========

Time
----

wordBreak(s, word_dict): O(n * k * l), where n = len(s), k = len(word_dict), and l is
the average length of the words in word_dict. At each state i, we iterate through
word_dict and splice s to a new string with average length l.

Space
-----

wordBreak(s, word_dict): O(n).
"""


def sol_bu(s, word_dict):
    dp = [False] * len(s)
    for i in range(len(s)):
        for word in word_dict:
            if i >= len(word) - 1 and (i == len(word) - 1 or dp[i - len(word)]):
                if s[i - len(word) + 1 : i + 1] == word:
                    dp[i] = True
                    break
    return dp[-1]


def sol_td(s, word_dict):
    memo = {}

    def dp(i):
        if i < 0:
            return True
        if i not in memo:
            for word in word_dict:
                if i >= len(word) - 1 and dp(i - len(word)):
                    if s[i - len(word) + 1 : i + 1] == word:
                        memo[i] = True
                        break
            else:
                memo[i] = False
        return memo[i]

    return dp(len(s) - 1)
