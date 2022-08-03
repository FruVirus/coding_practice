"""
Minimum Window Substring
------------------------

Given two strings s and t of lengths m and n respectively, return the minimum window
substring of s such that every character in t (including duplicates) is included in the
window. If there is no such substring, return the empty string "".

The testcases will be generated such that the answer is unique.

A substring is a contiguous sequence of characters within the string.

Intuition
---------

The question asks us to return the minimum window from the string S which has all the
characters of the string T. Let us call a window desirable if it has all the characters
from T.

We can use a simple sliding window approach to solve this problem.

In any sliding window based problem we have two pointers. One right pointer whose job is
to expand the current window and then we have the left pointer whose job is to contract
a given window. At any point in time only one of these pointers move and the other one
remains fixed.

The solution is pretty intuitive. We keep expanding the window by moving the right
pointer. When the window has all the desired characters, we contract (if possible) and
save the smallest window till now.

The answer is the smallest desirable window.

formed is used to keep track of how many unique characters in t are present in the
current window in its desired frequency. For example, if t is "AABC" then the window
must have two A's, one B and one C. Thus formed would be = 3 when all these conditions
are met.

Complexity
==========

Time
----

minWindow(s, t): O().

Space
-----

minWindow(s, t): O(|s| + |t|).
"""

# Standard Library
from collections import Counter, defaultdict


def sol(s, t):
    if not t or not s:
        return ""
    dict_t = Counter(t)
    formed, required = 0, len(dict_t)
    window_counts = defaultdict(int)
    min_width, min_left, min_right = float("inf"), None, None
    i = j = 0
    while j < len(s):
        char = s[j]
        window_counts[char] += 1
        if window_counts[char] == dict_t[char]:
            formed += 1
        while i <= j and formed == required:
            char, width = s[i], j - i + 1
            if width < min_width:
                min_width, min_left, min_right = width, i, j
            window_counts[char] -= 1
            i += 1
            if char in dict_t and window_counts[char] < dict_t[char]:
                formed -= 1
                break
        j += 1
    return "" if min_width == float("inf") else s[min_left : min_right + 1]
