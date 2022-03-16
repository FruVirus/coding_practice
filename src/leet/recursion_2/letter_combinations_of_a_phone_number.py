"""
Letter Combinations of a Phone Number
-------------------------------------

Given a string containing digits from 2-9 inclusive, return all possible letter
combinations that the number could represent. Return the answer in any order.

A mapping of digit to letters (just like on the telephone buttons) is given below. Note
that 1 does not map to any letters.

Intuition
---------

Use a backtracking function to generate all possible combinations.

    1. The function should take 2 primary inputs: the current combination of letters we
have, path, and the index we are currently checking.

    2. As a base case, if our current combination of letters is the same length as the
input digits, that means we have a complete combination. Therefore, add it to our
answer, and backtrack.

    3. Otherwise, get all the letters that correspond with the current digit we are
looking at, digits[index].

    4. Loop through these letters. For each letter, add the letter to our current path,
and call backtrack again, but move on to the next digit by incrementing index by 1.

    5. Make sure to remove the letter from path once finished with it.

Complexity
==========

Time
----

letterCombinations(digits): O(m^n * n), where m is the number of digits in the digits
string.

Space
-----

letterCombinations(digits): O(n).
"""

mapping = {
    "2": ["a", "b", "c"],
    "3": ["d", "e", "f"],
    "4": ["g", "h", "i"],
    "5": ["j", "k", "l"],
    "6": ["m", "n", "o"],
    "7": ["p", "q", "r", "s"],
    "8": ["t", "u", "v"],
    "9": ["w", "x", "y", "z"],
}


def sol(digits):
    sol, curr = [], []
    if not digits:
        return sol

    def backtrack(index, combo):
        if len(combo) == len(digits):
            sol.append("".join(combo))
            return
        for letter in mapping[digits[index]]:
            combo.append(letter)
            backtrack(index + 1, combo)
            combo.pop()

    backtrack(0, curr)
    return sol
