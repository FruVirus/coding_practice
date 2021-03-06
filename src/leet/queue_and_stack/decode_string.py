"""
Decode String
-------------

Given an encoded string, return its decoded string.

The encoding rule is: k[encoded_string], where the encoded_string inside the square
brackets is being repeated exactly k times. Note that k is guaranteed to be a positive
integer.

You may assume that the input string is always valid; there are no extra white spaces,
square brackets are well-formed, etc.

Furthermore, you may assume that the original data does not contain any digits and that
digits are only for those repeat numbers, k. For example, there will not be input like
3a or 2[4].

Complexity
==========

Time
----

decodeString(s): O(max(k) * n), max(k) is the maximum number of times we have to iterate
through the string to decode a pattern and n is the size of the string s.

Space
-----

decodeString(s): O(m + n), where m is the number of letters and n is the number of
digits in string s.
"""


def sol(s):
    stack = []
    for char in s:
        if char != "]":
            stack.append(char)
            continue
        num = str_ = ""
        while stack:
            char = stack.pop()
            if char == "[":
                continue
            if not char.isdigit():
                str_ = char + str_
            else:
                num = char + num
                if not (stack and stack[-1].isdigit()):
                    stack.append(int(num) * str_)
                    break
    return "".join(stack)
