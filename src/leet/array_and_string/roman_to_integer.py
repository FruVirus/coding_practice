"""
Roman to Integer
----------------

Roman numerals are represented by seven different symbols: I, V, X, L, C, D and M.

Symbol       Value
I             1
V             5
X             10
L             50
C             100
D             500
M             1000

For example, 2 is written as II in Roman numeral, just two one's added together. 12 is
written as XII, which is simply X + II. The number 27 is written as XXVII, which is
XX + V + II.

Roman numerals are usually written largest to smallest from left to right. However, the
numeral for four is not IIII. Instead, the number four is written as IV. Because the one
is before the five we subtract it making four. The same principle applies to the number
nine, which is written as IX. There are six instances where subtraction is used:

    - I can be placed before V (5) and X (10) to make 4 and 9.
    - X can be placed before L (50) and C (100) to make 40 and 90.
    - C can be placed before D (500) and M (1000) to make 400 and 900.

Given a roman numeral, convert it to an integer.

Intuition
---------

Each symbol adds its own value, except for when a smaller valued symbol is before a
larger valued symbol. In those cases, instead of adding both symbols to the total, we
need to subtract the large from the small, adding that instead.

Therefore, the simplest algorithm is to use a pointer to scan through the string, at
each step deciding whether to add the current symbol and go forward 1 place, or add the
difference of the next 2 symbols and go forward 2 places.

Observe the following:

    1. Without looking at the next symbol, we don't know whether or not the left-most
symbol should be added or subtracted.
    2. The right-most symbol is always added. It is either by itself, or the additive
part of a pair.

So, what we can do is initialise sum to be the value of the right-most (last) symbol.
Then, we work backwards through the string, starting from the second-to-last-symbol. We
check the symbol after (i + 1) to determine whether the current symbol should be "added"
or "subtracted".

Because we're starting at the second-to-last-index, we know that index i + 1 always
exists. We no longer need to handle its potential non-existence as a special case, and
additionally we're able to (cleanly) use a for loop, as we're always moving along by 1
index at at time, unlike before where it could have been 1 or 2.

Complexity
==========

Time
----

romanToInt(s): O(n).

Space
-----

romanToInt(s): O(1).
"""


mapping = {
    "I": 1,
    "V": 5,
    "X": 10,
    "L": 50,
    "C": 100,
    "D": 500,
    "M": 1000,
}


def sol(s):
    total = mapping.get(s[-1])
    for i in reversed(range(len(s) - 1)):
        if mapping[s[i]] < mapping[s[i + 1]]:
            total -= mapping[s[i]]
        else:
            total += mapping[s[i]]
    return total
