"""
Interleaving String
-------------------

Given strings s1, s2, and s3, find whether s3 is formed by an interleaving of s1 and s2.

An interleaving of two strings s and t is a configuration where they are divided into
non-empty substrings such that:

    - s = s1 + s2 + ... + sn
    - t = t1 + t2 + ... + tm
    - |n - m| <= 1
    - The interleaving is s1 + t1 + s2 + t2 + s3 + t3 + ... or
t1 + s1 + t2 + s2 + t3 + s3 + ...

Note: a + b is the concatenation of strings a and b.

Intuition
---------

The most basic idea is to find every string possible by all interleavings of the two
given strings s1 and s2. In order to implement this method, we are using recursion. We
start by taking the current character of the first string s1 and then appending all
possible interleavings of the remaining portion of the first string s1 and the second
string s2 and comparing each result formed with the required interleaved string s3.
Similarly, we choose one character from the second string s2 and form all the
interleavings with the remaining portion of s2 and s1 to check if the required string s3
can be formed.

In the recursive approach discussed above, we are considering every possible string
formed by interleaving the two given strings. But, there will be cases encountered in
which, the same portion of s1 and s2 would have been processed already but in different
orders (permutations). But irrespective of the order of processing, if the resultant
string formed till now is matching with the required string (s3), the final result is
dependent only on the remaining portions of s1 and s2, but not on the already processed
portion. Thus, the recursive approach leads to redundant computations.

Thus, here we have called the function by incrementing the pointers i and k since the
portion of strings up to those indices has already been processed. Similarly, we choose
one character from the second string and continue. The recursive function ends when
either of the two strings s1 or s2 has been fully processed. If, let's say, the string
s1 has been fully processed, we directly compare the remaining portion of s2 with the
remaining portion of s3.

The top-down approach above included a character from one of the strings s1 or s2 in the
resultant interleaved string and called a recursive function to check whether the
remaining portions of s1 and s2 can be interleaved to form the remaining portion of s3.

In the bottom-up approach, we look at the same problem the other way around. Here, we
include one character from s1 or s2 and check whether the resultant string formed so far
by one particular interleaving of the current prefix of s1 and s2 form a prefix of s3.
Thus, this approach relies on the fact that in order to determine whether a substring of
s3 (up to index k), can be formed by interleaving strings s1 and s2 up to indices i and
j respectively, solely depends on the characters of s1 and s2 up to indices i and j only
and not on the characters coming afterwards.

To implement this method, we'll make use of a 2D boolean array dp. In this array
dp[i][j] implies if it is possible to obtain a substring of length (i + j + 2) which is
a prefix of s3 by some interleaving of prefixes of strings s1 and s2 having lengths
(i + 1) and (j + 1) respectively. For filling in the entry of dp[i][j], we need to
consider two cases:

    1. The character just included i.e. either at i-th index of s1 or at j-th index of
s2 doesn't match the character at k-th index of s3, where k = i + j + 1. In this case,
the resultant string formed using some interleaving of prefixes of s1 and s2 can never
result in a prefix of length k + 1 in s3. Thus, we enter False at the character
dp[i][j].

    2. The character just included i.e. either at i-th index of s1 or at j-th index of
s2 matches the character at k-th index of s3, where k = i + j + 1. Now, if the character
just included (say x) which matches the character at k-th index of s3, is the character
at i-th index of s1, we need to keep x at the last position in the resultant interleaved
string formed so far. Thus, in order to use string s1 and s2 up to indices i and j to
form a resultant string of length (i + j + 2) which is a prefix of s3, we need to ensure
that the strings s1 and s2 up to indices (i − 1) and j respectively obey the same
property.

    3. Similarly, if we just included the j-th character of s2, which matches with the
k-th character of s3, we need to ensure that the strings s1 and s2 up to indices i and
(j − 1) also obey the same property to enter a true at dp[i][j].

Complexity
==========

Time
----

isInterleave(s1, s2, s3): O(m * n).

Space
-----

isInterleave_bu(s1, s2, s3): O(n), where n is the length of s1.
isInterleave_td(s1, s2, s3): O(m * n).
"""


def sol_bu(s1, s2, s3):
    l1, l2, l3 = len(s1), len(s2), len(s3)
    if l1 + l2 != l3:
        return False
    dp = [False] * (l2 + 1)
    for i in range(l1 + 1):
        for j in range(l2 + 1):
            k = i + j
            if i == j == 0:
                dp[j] = True
            elif i == 0:
                dp[j] = dp[j - 1] and s2[j - 1] == s3[k - 1]
            elif j == 0:
                dp[j] = dp[j] and s1[i - 1] == s3[k - 1]
            else:
                a = dp[j] and s1[i - 1] == s3[k - 1]
                b = dp[j - 1] and s2[j - 1] == s3[k - 1]
                dp[j] = a or b
    return dp[-1]


def sol_td(s1, s2, s3):
    memo, l1, l2, l3 = {}, len(s1), len(s2), len(s3)

    def dp(i, j, k):
        if i == l1:
            return s2[j:] == s3[k:]
        if j == l2:
            return s1[i:] == s3[k:]
        if (i, j) not in memo:
            a = s1[i] == s3[k] and dp(i + 1, j, k + 1)
            b = s2[j] == s3[k] and dp(i, j + 1, k + 1)
            memo[(i, j)] = a or b
        return memo[(i, j)]

    return dp(0, 0, 0) if l1 + l2 == l3 else False
