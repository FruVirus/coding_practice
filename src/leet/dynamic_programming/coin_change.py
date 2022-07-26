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

The idea is to find the minimum # of coins required to make x value in the range 0 to
the input amount. This is done by iterating through all of the coins, and for each
possible value the coin can create, saving to a global list the minimum number of coins
required. dp[i] stores the number of coins required, while the index, i, is the value
that we are trying to create with x number of coins.

Example

coins = [1, 2, 3], amount = 4

We first have coin = 1 and amount 4, then dp = [0, 1, 2, 3, 4], where the number in each
index of the array signifies how many 1c coins it would take to make 0, 1, 2, 3, and 4
cents, respectively. In this case, since our only denomination is 1c, it takes 0, 1, 2,
3, and 4 1c coins, respectively.

Then we have coin = 2 and amount 4, then dp = [0, 1, 1, 2, 2]. In this case, it takes 1
coin to make amount 1, 1 coin to make amount 2, 2 coins to make amount 3, and 2 coins to
make amount 4.

Then we have coin = 3 and amount 4, then dp = [0, 1, 1, 1, 2]. In this case, it takes 1
coin to make amount 1, 1 coin to make amount 2, 1 coin to make amount 3, and 2 coins to
make amount 4.

The indexes in dp correspond to the various increments of amount, from 0 to amount, and
the values in dp correspond to how many coins it takes to make that amount if the coin
denominations are specified by coins.

Complexity
==========

Time
----

coinChange_bu(coins, amount) and coinChange_td(coins, amount): O(n * s), where s is the
amount and n is the denomination count.

Space
-----

coinChange_bu(coins, amount) and coinChange_td(coins, amount): O(s).
"""


def sol_bu(coins, amount):
    dp = [0] + [float("inf")] * amount
    for coin in coins:
        for i in range(coin, amount + 1):
            dp[i] = min(dp[i], dp[i - coin] + 1)
    return dp[-1] if dp[-1] != float("inf") else -1


def sol_td(coins, amount):
    memo = {}

    def dp(amount):
        if amount <= 0:
            return amount
        if amount not in memo:
            val = float("inf")
            for coin in coins:
                rem = dp(amount - coin)
                if 0 <= rem < val:
                    val = rem + 1
            memo[amount] = val if val != float("inf") else -1
        return memo[amount]

    return dp(amount)
