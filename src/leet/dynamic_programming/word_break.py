"""
Word Break
----------

Given a string s and a dictionary of strings wordDict, return true if s can be segmented
into a space-separated sequence of one or more dictionary words.

Note that the same word in the dictionary may be reused multiple times in the
segmentation.

Intuition
---------

For the recursive approach, we check every possible prefix of the string in the
dictionary of words---if it is found in the dictionary, then the recursive function is
called for the remaining portion of the string. And, if in some function call the whole
string is found in the dictionary, then it will return True.

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
    dp = [True] + [False] * len(s)
    for i in range(1, len(s) + 1):
        for j in range(i):
            if dp[j] and s[j:i] in word_dict:
                dp[i] = True
                break
    return dp[-1]


def sol_td(s, word_dict):
    memo = {}

    def dp(i):
        if i == len(s):
            return True
        if i not in memo:
            memo[i] = False
            for j in range(i + 1, len(s) + 1):
                if s[i:j] in word_dict and dp(j):
                    memo[i] = True
                    break
        return memo[i]

    return dp(0)
