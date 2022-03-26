"""
Coin Change
-----------

You are given an integer array coins representing coins of different denominations and
an integer amount representing a total amount of money.

Return the fewest number of coins that you need to make up that amount. If that amount
of money cannot be made up by any combination of the coins, return -1.

You may assume that you have an infinite number of each kind of coin.

Intuition
---------

First, let's define:

    F(S) - minimum number of coins needed to make change for amount S using coin
denominations [c_0, ..., c_(n - 1)]

How do we split the problem into subproblems? Let's assume that we know F(S) where some
change val_1, val_2, ..., for S which is optimal and the last coin's denomination is C.
Then the following equation should be true because of the optimal substructure of the
problem.

    F(S) = F(S - C) + 1

But we don't know which is the denomination of the last coin C. We compute F(S - c_i)
for each possible denomination c_0, c_1, c_2, ..., c_(n - 1) and choose the minimum
among them. Then the following recurrence relation holds:

F(S) = min(F(S - c_i)) + 1 subject to S - c_i >= 0

F(S) = 0 when S = 0
F(S) = -1 when n = 0

Example

coins = [1, 2, 3], amount = 4

If we had coins = [1] and amount 4, then dp = [0, 1, 2, 3, 4], where the number in each
index of the array signifies how many 1c coins it would take to make 0, 1, 2, 3, and 4
cents, respectively. In this case, since our only denomination is 1c, it takes 0, 1, 2,
3, and 4 1c coins, respectively.

If we had coins = [1, 2] and amount 4, then dp = [0, 1, 1, 2, 2].

If we had coins = [1, 2, 3] and amount 4, then dp = [0, 1, 1, 1, 2].

The indexes in dp correspond to the various increments of amount, from 0 to amount, and
the values in dp correspond to how many coins it takes to make that amount if the coin
denominations are specified by coins.

Complexity
==========

Time
----

coinChange(coins, amount): O(n * s), where s is the amount and n is the denomination
count.

Space
-----

coinChange(coins, amount): O(s).
"""


def sol_bu(coins, amount):
    dp = [float("inf")] * (amount + 1)
    dp[0] = 0
    for coin in coins:
        for i in range(coin, amount + 1):
            dp[i] = min(dp[i], dp[i - coin] + 1)
    return dp[amount] if dp[amount] != float("inf") else -1


def sol_td(coins, amount):
    if amount == 0:
        return 0
    count = [0] * amount

    def dp(coins, amount):
        if amount <= 0:
            return amount
        if count[amount - 1] != 0:
            return count[amount - 1]
        val = float("inf")
        for coin in coins:
            rem = dp(coins, amount - coin)
            if 0 <= rem < val:
                val = 1 + rem
        count[amount - 1] = -1 if val == float("inf") else val
        return count[amount - 1]

    return dp(coins, amount)
