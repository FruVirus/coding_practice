"""
Decode Ways
-----------

A message containing letters from A-Z can be encoded into numbers using the following
mapping:

    - 'A' -> "1"
    - 'B' -> "2"
    ...
    - 'Z' -> "26"

To decode an encoded message, all the digits must be grouped then mapped back into
letters using the reverse of the mapping above (there may be multiple ways). For
example, "11106" can be mapped into:

    - "AAJF" with the grouping (1 1 10 6)
    - "KJF" with the grouping (11 10 6)

Note that the grouping (1 11 06) is invalid because "06" cannot be mapped into 'F' since
"6" is different from "06".

Given a string s containing only digits, return the number of ways to decode it.

The test cases are generated so that the answer fits in a 32-bit integer.

Intuition
---------

At any given time for a string we enter a recursion after successfully decoding two
digits to a single character or a single digit to a character. This leads to multiple
paths to decoding the entire string. If a given path leads to the end of the string this
means we could successfully decode the string. If at any point in the traversal we
encounter digits which cannot be decoded, we backtrack from that path.

The number of ways for the given string is determined by making a recursive call to the
function with index + 1 for next substring string and index + 2 after checking for valid
2-digit decode.

For the iterative approach, we use an array for DP to store the results for subproblems.
A cell with index i of the dp array is used to store the number of decode ways for
substring of s from index 0 to index i - 1.

We initialize the starting two indices of the dp array. It's similar to relay race where
the first runner is given a baton to be passed to the subsequent runners. The first two
indices of the dp array hold a baton. As we iterate the dp array from left to right this
baton which signifies the number of ways of decoding is passed to the next index or not
depending on whether the decode is possible.

dp[i] can get the baton from two other previous indices, either i - 1 or i - 2. Two
previous indices are involved since both single and two digit decodes are possible.

Unlike the relay race we don't get only one baton in the end. The batons add up as we
pass on. If someone has one baton, they can provide a copy of it to everyone who comes
to them with a success. Thus, leading to number of ways of reaching the end.

dp[i] = Number of ways of decoding substring s[:i]. So we might say dp[i] = dp[i - 1] +
dp[i - 2], which is not always true for this decode ways problem---only when the decode
is possible we add the results of the previous indices. Thus, in this race we don't just
pass the baton. The baton is passed to the next index or not depending on possibility
of the decode.

Complexity
==========

Time
----

numDecodings(s): O(n).

Space
-----

numDecodings_bu(s): O(1).
numDecodings_td(s): O(n).
"""


def sol_bu(s):
    if s[0] == "0":
        return 0
    one = two = 1
    for i in range(1, len(s)):
        curr = 0
        if s[i] != "0":
            curr = one
        if 10 <= int(s[i - 1 : i + 1]) <= 26:
            curr += two
        one, two = curr, one
    return one


def sol_td(s):
    memo = {}

    def dp(s, index):
        if index == len(s):
            return 1
        if s[index] == "0":
            return 0
        if index == len(s) - 1:
            return 1
        if index not in memo:
            num_decodes = dp(s, index + 1)
            if int(s[index : index + 2]) <= 26:
                num_decodes += dp(s, index + 2)
            memo[index] = num_decodes
        return memo[index]

    return dp(s, 0)
