"""
Happy Number
------------

Write an algorithm to determine if a number n is happy.

A happy number is a number defined by the following process:

    1. Starting with any positive integer, replace the number by the sum of the squares
of its digits.
    2. Repeat the process until the number equals 1 (where it will stay), or it loops
endlessly in a cycle which does not include 1.
    3. Those numbers for which this process ends in 1 are happy.

Return true if n is a happy number, and false if not.

Complexity
==========

Time
----

singleNumber(nums): O(n).

Space
-----

singleNumber(nums): O(1).
"""


def sol(nums):
    a = 0
    for num in nums:
        a ^= num
    return a
