"""
Word Break
----------

Given a string s and a dictionary of strings wordDict, return true if s can be segmented
into a space-separated sequence of one or more dictionary words.

Note that the same word in the dictionary may be reused multiple times in the
segmentation.

Intuition
---------

For the bottom-up approach, the given problem (s) can be divided into subproblems s1 and
s2. If these subproblems individually satisfy the required conditions, the complete
problem, s also satisfies the same. For example, "catsanddog" can be split into two
substrings "catsand", "dog". The subproblem "catsand" can be further divided into
"cats","and", which individually are a part of the dictionary making "catsand" satisfy
the condition. Going further backwards, "catsand", "dog" also satisfy the required
criteria individually leading to the complete string "catsanddog" also to satisfy the
criteria.

Now, we'll move onto the process of dp array formation. We make use of dp array of size
n + 1, where n is the length of the given string. We also use two index pointers i and
j, where i refers to the length of the substring (s') considered currently starting from
the beginning, and j refers to the index partitioning the current substring (s') into
smaller substrings s'(0, j) and s'(j + 1, i). To fill in the dp array, we initialize the
element dp[0] as true, since the null string is always present in the dictionary, and
the rest of the elements of dp as false. We consider substrings of all possible lengths
starting from the beginning by making use of index i. For every such substring, we
partition the string into two further substrings s1' and s2' in all possible ways using
the index j (Note that the i now refers to the ending index of s2'). Now, to fill in the
entry dp[i], we check if the dp[j] contains true, i.e. if the substring s1′ fulfills the
required criteria. If so, we further check if s2' is present in the dictionary. If both
the strings fulfill the criteria, we make dp[i] as true, otherwise as false.

For the top-down approach, we check every possible prefix of the string in the
dictionary of words---if it is found in the dictionary, then the recursive function is
called for the remaining portion of the string. And, if in some function call the whole
string is found in the dictionary, then it will return True.

Complexity
==========

Time
----

wordBreak_bu(s, word_dict) and wordBreak_td(s, word_dict): O(n * k * l), where n =
len(s), k = len(word_dict), and l is the average length of the words in word_dict. At
each state i, we iterate through word_dict and splice s to a new string with average
length l.

Space
-----

wordBreak_bu(s, word_dict) and wordBreak_td(s, word_dict): O(n).
"""


def sol_bu(s, word_dict):
    n = len(s)
    dp = [True] + [False] * n
    for i in range(1, n + 1):
        for j in range(i):
            if dp[j] and s[j:i] in word_dict:
                dp[i] = True
                break
    return dp[-1]


def sol_td(s, word_dict):
    memo, n = {}, len(s)

    def dp(i):
        if i == n:
            return True
        if i not in memo:
            memo[i] = False
            for j in range(i + 1, n + 1):
                if dp(j) and s[i:j] in word_dict:
                    memo[i] = True
                    break
        return memo[i]

    return dp(0)
