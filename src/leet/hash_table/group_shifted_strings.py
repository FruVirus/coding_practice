"""
Group Shifted Strings
---------------------

We can shift a string by shifting each of its letters to its successive letter.

    - For example, "abc" can be shifted to be "bcd".

We can keep shifting the string to form a sequence.

    - For example, we can keep shifting "abc" to form the sequence:
"abc" -> "bcd" -> ... -> "xyz".

Given an array of strings, group all strings[i] that belong to the same shifting
sequence. You may return the answer in any order.

Complexity
==========

Time
----

groupStrings(strings): O(n * k), where n is the length of strings and k is the maximum
length of a string in strings. We iterate over all n strings and for each string, we
iterate over all the characters to generate the hash value, which takes O(k) time.

Space
-----

groupStrings(strings): O(n * k). We need to store all the strings plus their hash
values. In the worst scenario, when each string in the given list belongs to a different
hash value, the maximum number of strings stored is 2 * n. Each string takes at most
O(k) space.
"""

# Standard Library
from collections import defaultdict


def sol(strings):
    shifts = defaultdict(list)
    for s in strings:
        str_len = len(s)
        str_diff = tuple((ord(s[i + 1]) - ord(s[i])) % 26 for i in range(str_len - 1))
        shifts[(str_len, str_diff)].append(s)
    return shifts.values()
