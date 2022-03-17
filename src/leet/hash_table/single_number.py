"""
Single Number
-------------

Given a non-empty array of integers nums, every element appears twice except for one.
Find that single one.

You must implement a solution with a linear runtime complexity and use only constant
extra space.

Intuition
---------

If we take XOR of zero and some bit, it will return that bit.

If we take XOR of two same bits, it will return 0.

a XOR b XOR a = (a XOR a) XOR b = 0 XOR b = b

So we can XOR all bits together to find the unique number.

nums = [4, 1, 2, 1, 2]

0 ^ 4 = 4
4 ^ 1 = 5
5 ^ 2 = 7
7 ^ 1 = 6
6 ^ 2 = 4

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
