"""
Generate Parentheses
--------------------

Given n pairs of parentheses, write a function to generate all combinations of
well-formed parentheses.

Intuition
---------

Let's only add "(" or ")" when we know it will remain a valid sequence. We can do this
by keeping track of the number of opening and closing brackets we have placed so far.

We can start an opening bracket if we still have one (of n) left to place. And we can
start a closing bracket if it would not exceed the number of opening brackets. Once a
combination equals 2 * n, then we have a well-formed parenthesis.

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
