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

Intuition
---------

Instead of keeping track of just one value in the chain, we keep track of 2, called the
slow runner and the fast runner. At each step of the algorithm, the slow runner goes
forward by 1 number in the chain, and the fast runner goes forward by 2 numbers (nested
calls to the getNext(n) function).

If n is a happy number, i.e. there is no cycle, then the fast runner will eventually get
to 1 before the slow runner.

If n is not a happy number, then eventually the fast runner and the slow runner will be
on the same number.

Complexity
==========

Time
----

isHappy(n): O(lg n).

Space
-----

isHappy(n): O(1).
"""


def sol(n):
    def get_next(num):
        sum_ = 0
        while num > 0:
            num, digit = num // 10, num % 10
            sum_ += digit ** 2
        return sum_

    slow, fast = n, get_next(n)
    while slow != fast and fast != 1:
        slow, fast = get_next(slow), get_next(get_next(fast))
    return fast == 1
