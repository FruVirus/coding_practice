"""
String to Integer (atoi)
------------------------

Implement the myAtoi(string s) function, which converts a string to a 32-bit signed
integer (similar to C/C++'s atoi function).

The algorithm for myAtoi(string s) is as follows:

    1. Read in and ignore any leading whitespace.
    2. Check if the next character (if not already at the end of the string) is '-' or
'+'. Read this character in if it is either. This determines if the final result is
negative or positive respectively. Assume the result is positive if neither is present.
    3. Read in next the characters until the next non-digit character or the end of the
input is reached. The rest of the string is ignored.
    4. Convert these digits into an integer (i.e. "123" -> 123, "0032" -> 32). If no
digits were read, then the integer is 0. Change the sign as necessary (from step 2).
    5. If the integer is out of the 32-bit signed integer range [-^231, 2^31 - 1], then
clamp the integer so that it remains in the range. Specifically, integers less than
-2^31 should be clamped to -2^31, and integers greater than 2^31 - 1 should be clamped
to 2^31 - 1.

Return the integer as the final result.
Note:

    - Only the space character ' ' is considered a whitespace character.
    - Do not ignore any characters other than the leading whitespace or the rest of the
string after the digits.

Intuition
---------

Let's first consider the case for overflow.

We will denote the maximum 32-bit integer value 2^31 - 1 = 2147483647 with INT_MAX, and
we will append the digits one by one to the final number.

So there could be 3 cases:

    - Case 1: If the current number is less than INT_MAX / 10 = 214748364, we can append
any digit, and the new number will always be less than INT_MAX.
    - Case 2: If the current number is more than INT_MAX / 10 = 214748364, appending any
digit will result in a number greater than INT_MAX.
    - Case 3: If the current number is equal to INT_MAX / 10 = 214748364, we can only
append digits from 0-7 such that the new number will always be less than or equal to
INT_MAX.

Similarly for underflow.

The minimum 32-bit integer value is -2^31= -2147483648 denote it with INT_MIN.

We append the digits one by one to the final number. Just like before, there could be 3
cases:

    - Case 1: If the current number is greater than INT_MIN / 10 = -214748364, then we
can append any digit and the new number will always be greater than INT_MIN.
    - Case 2: If the current number is less than INT_MIN / 10 = -214748364, appending
any digit will result in a number less than INT_MIN.
    - Case 3: If the current number is equal to INT_MIN / 10 = -214748364, then we can
only append digits from 0-8, such that the new number will always be greater than or
equal to INT_MIN.

Notice that cases 1 and 2 are similar for overflow and underflow. The only difference is
case 3: for overflow, we can append any digit between 0 and 7, but for underflow, we can
append any digit between 0 and 8.

So we can combine both the underflow and overflow checks as follows:

    - Initially, store the sign for the final result and consider only the absolute
values to build the integer and return the final result with a correct sign at the end.
    - If the current number is less than 214748364 = (INT_MAX / 10), we can append the
next digit.
    - If the current number is greater than 214748364:
        - And, the sign for the result is '+', then the result will overflow, so return
INT_MAX;
        - Or, the sign for the result is '-', then the result will underflow, so return
INT_MIN.
    - If the current number is equal to 214748364:
        - If the next digit is between 0-7, the result will always be in range.
        - If, next digit is 8:
            - And the sign is '+' the result will overflow, so return INT_MAX;
            - Or, the sign is '-', the result will not underflow but will still be equal
to INT_MIN, so that we can return INT_MIN.
        - But if, the next digit is greater than 8:
            - And the sign is '+' the result will overflow, so return INT_MAX;
            - Or, the sign is '-', the result will underflow, so return INT_MIN.

Complexity
==========

Time
----

myAtoi(s): O(n).

Space
-----

myAtoi(s): O(1).
"""


def sol(s):
    n = len(s)
    i, integer, sign = 0, 0, 1
    int_max, int_min = 2 ** 31 - 1, -(2 ** 31)
    threshold, last_digit = int_max // 10, int_max % 10
    while i < n and s[i] == " ":
        i += 1
    if i < n:
        if s[i] == "-":
            sign = -1
        if s[i] in ["+", "-"]:
            i += 1
    while i < n and s[i].isdigit():
        digit = int(s[i])
        if (integer > threshold) or (integer == threshold and digit > last_digit):
            return int_max if sign == 1 else int_min
        integer = 10 * integer + digit
        i += 1
    return sign * integer
