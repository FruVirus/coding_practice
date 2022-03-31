"""
Count Vowels Permutation
------------------------

Given an integer n, your task is to count how many strings of length n can be formed
under the following rules:

    - Each character is a lower case vowel ('a', 'e', 'i', 'o', 'u')
    - Each vowel 'a' may only be followed by an 'e'.
    - Each vowel 'e' may only be followed by an 'a' or an 'i'.
    - Each vowel 'i' may not be followed by another 'i'.
    - Each vowel 'o' may only be followed by an 'i' or a 'u'.
    - Each vowel 'u' may only be followed by an 'a'.

Since the answer may be too large, return it modulo 10^9 + 7.

Intuition
---------

If we are given the number of strings of length i that end in each vowel, like aCount,
eCount, iCount, oCount, and uCount, we can compute the number of strings of length i + 1
that end in each vowel by simple addition:

    - aCountNew = eCount + iCount + uCount
    - eCountNew = aCount + iCount
    - iCountNew = eCount + oCount
    - oCountNew = iCount
    - uCountNew = iCount + oCount

In the bottom-up approach, we initialize the first element in each of the five arrays to
1. This is because for each starting vowel there is only one permutation when the length
of the string is 1. In addition, the i-th element in each array only depends on the
i - 1-th element in some of the arrays. Therefore, the space complexity can be optimized
by using five long variables (instead of 5 arrays of length n) to store the counts.

In the top-down approach, dp(i, vowel) is a function that returns the number of strings
of length i that end with vowel. When i is 0, the string is already of length n, so we
return 1 by signifying that 1 string has been formed.

Complexity
==========

Time
----

countVowelPermutation(n): O(n).

Space
-----

countVowelPermutation_bu(n): O(1).
countVowelPermutation_td(n): O(n).
"""


def sol_bu(n):
    a = e = i = o = u = 1
    mod = 10 ** 9 + 7
    for _ in range(1, n):
        a_new = (e + i + u) % mod
        e_new = (a + i) % mod
        i_new = (e + o) % mod
        o_new = i % mod
        u_new = (i + o) % mod
        a, e, i, o, u = a_new, e_new, i_new, o_new, u_new
    return (a + e + i + o + u) % mod


def sol_td(n):
    memo, mod = {}, 10 ** 9 + 7

    def dp(i, vowel):
        if i <= 1:
            return 1
        if (i, vowel) not in memo:
            if vowel == "a":
                total = dp(i - 1, "e") + dp(i - 1, "i") + dp(i - 1, "u")
            elif vowel == "e":
                total = dp(i - 1, "a") + dp(i - 1, "i")
            elif vowel == "i":
                total = dp(i - 1, "e") + dp(i - 1, "o")
            elif vowel == "o":
                total = dp(i - 1, "i")
            else:
                total = dp(i - 1, "i") + dp(i - 1, "o")
            memo[(i, vowel)] = total % mod
        return memo[(i, vowel)]

    return sum(dp(n, vowel) for vowel in "aeiou") % mod
