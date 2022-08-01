"""
Number of Dice Rolls With Target Sum
------------------------------------

You have n dice and each die has k faces numbered from 1 to k.

Given three integers n, k, and target, return the number of possible ways (out of the
k^n total ways) to roll the dice so the sum of the face-up numbers equals target. Since
the answer may be too large, return it modulo 10^9 + 7.

Intuition
---------

We have n dice, each having k faces with a number from 1 to k. We need to find the
number of ways to roll these nn dice such that the sum of numbers on them is equal to
target.

There are two characteristics of this problem that we should take note of at this time.
First, as we iterate over the dice, we need to decide the number for each dice. The
feasible options for number at the current dice depend upon the current sum, which is in
turn dependent on the number we chose for the previous dice. It implies each decision we
make is affected by the previous decisions we have made. Second, the problem is asking
to count all the ways to roll n dice.

Complexity
==========

Time
----

numRollsToTarget_bu(n, k, target): O(n * t).
numRollsToTarget_td(n, k, target): O(n * k).

Space
-----

numRollsToTarget_bu(n, k, target): O(t).
numRollsToTarget_td(n, k, target): O(n * k).
"""


def sol_bu(n, k, target):
    dp = [0] * (target + 1)
    for i in range(1, min(target + 1, k + 1)):
        dp[i] = 1
    for d in range(2, n + 1):
        for curr_sum in reversed(range(target + 1)):
            dp[curr_sum] = sum(dp[max(d - 1, curr_sum - k) : curr_sum])
    return dp[-1]


def sol_td(n, k, target):
    memo = {}

    def dp(d, curr_sum):
        if d == n:
            return 1 if curr_sum == target else 0
        if (d, curr_sum) not in memo:
            memo[(d, curr_sum)] = sum(dp(d + 1, curr_sum + i) for i in range(1, k + 1))
        return memo[(d, curr_sum)]

    return dp(0, 0)
