"""
Largest Number
--------------

Given a list of non-negative integers nums, arrange them such that they form the largest
number and return it.

Since the result may be very large, so you need to return a string instead of an
integer.

Intuition
---------

To construct the largest number, we want to ensure that the most significant digits are
occupied by the largest digits.

First, we convert each integer to a string. Then, we sort the array of strings.

While it might be tempting to simply sort the numbers in descending order, this causes
problems for sets of numbers with the same leading digit. For example, sorting the
problem example in descending order would produce the number 9534303, while the correct
answer can be achieved by transposing the 3 and the 30. Therefore, for each pairwise
comparison during the sort, we compare the numbers achieved by concatenating the pair in
both orders.

Once the array is sorted, the most "significant" number will be at the front. There is a
minor edge case that comes up when the array consists of only zeroes (e.g., [0, 0]), so
if the most significant number is 0, we can simply return 0. Otherwise, we build a
string out of the sorted array and return it.

Complexity
==========

Time
----

largestNumber(nums): O(n * lg n).

Space
-----

largestNumber(nums): O(n).
"""


class LargerNum(str):
    def __lt__(self, x):
        return x + self < self + x


def sol(nums):
    largest_num = "".join(sorted(map(str, nums), key=LargerNum))
    return "0" if largest_num[0] == "0" else largest_num
