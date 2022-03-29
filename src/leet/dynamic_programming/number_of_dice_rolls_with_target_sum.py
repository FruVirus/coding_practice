"""
Number of Dice Rolls With Target Sum
------------------------------------

You have n dice and each die has k faces numbered from 1 to k.

Given three integers n, k, and target, return the number of possible ways (out of the
k^n total ways) to roll the dice so the sum of the face-up numbers equals target. Since
the answer may be too large, return it modulo 109 + 7.

Complexity
==========

Time
----

numRollsToTarget(n, k, target): O(n * k).

Space
-----

numRollsToTarget(n, k, target): O(n * k).
"""


def sol_td(n, k, target):
    memo, mod = {}, 10 ** 9 + 7

    def dp(d, curr_sum):
        if d == n:
            return int(curr_sum == target)
        if (d, curr_sum) not in memo:
            total_sum = sum(dp(d + 1, curr_sum + i) for i in range(1, k + 1)) % mod
            memo[(d, curr_sum)] = total_sum
        return memo[(d, curr_sum)]

    return dp(0, 0) % mod
