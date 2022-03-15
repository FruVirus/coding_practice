"""
Generate Parentheses
--------------------

Given n pairs of parentheses, write a function to generate all combinations of
well-formed parentheses.

Complexity
==========

Time
----

generateParenthesis(n): O(4^n / sqrt(n)).

Space
-----

generateParenthesis(n): O(4^n / sqrt(n)).
"""


def sol(n):
    sol = []

    def backtrack(s, left=0, right=0):
        if len(s) == 2 * n:
            sol.append("".join(s))
            return
        if left < n:
            s.append("(")
            backtrack(s, left + 1, right)
            s.pop()
        if right < left:
            s.append(")")
            backtrack(s, left, right + 1)
            s.pop()

    backtrack([])
    return sol
