"""
Integer to Roman
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
CM            900
CD            400
XC            90
XL            40
IX            9
IV            4

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

Given an integer, convert it to a roman numeral.

Intuition
---------

The system we use to decide is to select the representation with the largest possible
symbols, working from left to right. For example, the representations above with the
largest symbol at the start are the ones starting with C.

To decide which of these to go with, we look at the next symbol. Two of them have an X,
which is worth 10, and one of them has an XL, which is worth 40. Because the XL is worth
more, we go with that representation. Therefore, the representation for 140 is CXL.

Representing a given integer as a Roman Numeral requires finding a sequence of the above
13 symbols, where their corresponding values add up to the integer. This sequence must
be in order from largest to smallest, based on symbol value.

As explained in the overview, the representation should use the largest possible
symbols, working from the left. Therefore, it makes sense to use a Greedy algorithm. A
Greedy algorithm is an algorithm that makes the best possible decision at the current
time; in this case taking out the largest possible symbol it can.

So to represent a given integer, we look for the largest symbol that fits into it. We
subtract that, and then look for the largest symbol that fits into the remainder, and so
on until the remainder is 0. Each of the symbols we take out are appended onto the
output Roman Numeral string.

The cleanest way to implement this in code is to loop over each symbol, from largest to
smallest, checking how many copies of the current symbol fit into the remaining integer.

Complexity
==========

Time
----

intToRoman(num): O(n).

Space
-----

intToRoman(num): O(1).
"""

mapping = [
    (1000, "M"),
    (900, "CM"),
    (500, "D"),
    (400, "CD"),
    (100, "C"),
    (90, "XC"),
    (50, "L"),
    (40, "XL"),
    (10, "X"),
    (9, "IX"),
    (5, "V"),
    (4, "IV"),
    (1, "I"),
]


def sol(num):
    roman = []
    while num != 0:
        for val, char in mapping:
            count, num = num // val, num % val
            roman.append(char * count)
    return "".join(roman)
