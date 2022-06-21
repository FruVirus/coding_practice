"""
Longest Palindromic Substring
-----------------------------

Given a string s, return the longest palindromic substring in s.

Intuition
---------

Consider the case "ababa". If we already knew that "bab" is a palindrome, it is obvious
that "ababa" must be a palindrome since the two left and right end letters are the same.

First, we define a function P:

P(i, j) = {
    True if s[i:j] is palindromic
    False if s[i:j] is not palindromic
}

Thus, P(i, j) = P(i + 1, j - 1) and s[i] == s[j]

The base cases are: P(i, i) = True and P(i, i + 1) = s[i] == s[i + 1]

This yields a straight forward DP solution, which we first initialize the one and two
letters palindromes, and work our way up finding all three letters palindromes, and so
on.

In addition, for each line of j, dp only depends on previous line of j. Thus, we just
need a n by 1 array instead of n by n matrix.

Complexity
==========

Time
----

longestPalindrome_bu(s): O(n^2).

Space
-----

longestPalindrome_bu(s): O(n).
"""


def sol_bu(s):
    sol, n = "", len(s)
    dp = [False] * n
    for i in range(n):
        for j in range(i + 1):
            if i == j:
                dp[j] = True
            elif i == j + 1:
                dp[j] = s[i] == s[j]
            else:
                dp[j] = dp[j + 1] and s[i] == s[j]
            if dp[j] and i - j + 1 > len(sol):
                sol = s[j : i + 1]
    return sol
