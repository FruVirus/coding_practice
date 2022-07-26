"""
Coin Change
-----------

You are given an integer array coins representing coins of different denominations and
an integer amount representing a total amount of money.

Return the number of combinations that make up that amount. If that amount of money
cannot be made up by any combination of the coins, return 0.

You may assume that you have an infinite number of each kind of coin.

The answer is guaranteed to fit into a signed 32-bit integer.

Intuition
---------

If the total amount of money is zero, there is only one combination: to take zero coins.

Another base case is no coins: zero combinations for amount > 0 and one combination for
amount == 0.

Example

coins = [1, 2, 3], amount = 4

We first have coin = 1 and amount 4, then dp = [1, 1, 1, 1, 1], where the number in each
index of the array signifies how many different ways a 1c coin can make amounts 1, 2, 3,
and 4. In this case, since our only denomination is 1c, there is exactly 1 way to make
amounts 1, 2, 3, and 4.

Then we have coin = 2 and amount 4, then dp = [1, 1, 2, 2, 3]. In this case, we have 1
way to make amount 1, 2 ways to make amount 2, 2 ways to make amount 3, and 3 ways to
make amount 4.

Then we have coin = 3 and amount 4, then dp = [1, 1, 2, 3, 4]. In this case, we have 1
way to make amount 1, 2 ways to make amount 2, 3 ways to make amount 3, and 4 ways to
make amount 4.

The indexes in dp correspond to the various increments of amount, from 0 to amount, and
the values in dp correspond to how many different ways you can make amount using the
number of current coins.

Note: To understand how the coin loop being outside resolves the double counting, you
should pay attention to the fact that when the coin loop is outside, we will count how
many combinations are possible with say 2c coin and then add that number to the ways in
which the same amount can be created using 3c coin. This imposition of order removes the
double counting. Compare that with the situation where the coins are in the inner loop.
Here we would calculate how many ways we can create an amount using all coins (i.e., 1
and 2 both) and then for the next amount of interest, we will count using all coins
(i.e., 1 and 2 both again). As you see, we are counting both 1c after 2c and 2c after 1c
scenarios, causing the double counting.

Complexity
==========

Time
----

change(coins, amount): O(n * amount), where n is the length of coins.

Space
-----

change(coins, amount): O(n).
"""


def sol_bu(coins, amount):
    dp = [1] + [0] * amount
    for coin in coins:
        for i in range(coin, amount + 1):
            dp[i] += dp[i - coin]
    return dp[-1]
