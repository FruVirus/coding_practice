"""
Evaluate Reverse Polish Notation
--------------------------------

Evaluate the value of an arithmetic expression in Reverse Polish Notation.

Valid operators are +, -, *, and /. Each operand may be an integer or another
expression.

Note that division between two integers should truncate toward zero.

It is guaranteed that the given RPN expression is always valid. That means the
expression would always evaluate to a result, and there will not be any division by zero
operation.

Example

Input: tokens = ["2","1","+","3","*"]

Output: 9

Explanation: ((2 + 1) * 3) = 9

Complexity
==========

Time
----

evalRPN(tokens): O(n).

Space
-----

evalRPN(tokens): O(n).
"""


def sol(tokens):
    operators = {
        "+": lambda x, y: x + y,
        "-": lambda x, y: x - y,
        "*": lambda x, y: x * y,
        "/": lambda x, y: int(x / y),
    }
    stack = []
    for i in tokens:
        if i not in operators:
            stack.append(i)
        else:
            right, left = int(stack.pop()), int(stack.pop())
            stack.append(operators[i](left, right))
    return stack.pop()
