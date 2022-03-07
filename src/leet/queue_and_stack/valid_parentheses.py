"""
Valid Parentheses
-----------------

Given a string s containing just the characters '(', ')', '{', '}', '[' and ']',
determine if the input string is valid.

An input string is valid if:

    1. Open brackets must be closed by the same type of brackets.
    2. Open brackets must be closed in the correct order.

Complexity
==========

Time
----

isValid(s): O(n).

Space
-----

isValid(s): O(n).
"""


def sol(s):
    stack, openings = [], {"(": ")", "[": "]", "{": "}"}
    for char in s:
        if char in openings:
            stack.append(char)
        elif not stack or char != openings[stack[-1]]:
            return False
        else:
            stack.pop()
    return stack == []
