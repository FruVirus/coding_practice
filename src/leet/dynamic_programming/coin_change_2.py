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

All amounts less than x coin are not impacted by the presence of x coins. Starting from
x coin, one could use x coins in the combinations.

For example, suppose we have a 2 cent coin. The number of combinations to make less than
2 cents is not impacted by a 2 cent coin. Starting from 2 cents, we have the following:

To make 2 cents using a 2 cent coin: # of ways to make 2 cents using no coins +
# of ways to make 2 cents using a 2 cent coin = 0 + 1 = 1.

Now the strategy is here:

    - Add coins one-by-one, starting from base case "no coins".

    - For each added coin, compute recursively the number of combinations for each
amount of money from 0 to amount.

    - Initiate number of combinations array with the base case "no coins": dp[0] = 1,
and all the rest = 0.

    - Loop over all coins:

        - For each coin, loop over all amounts from 0 to amount:
            - For each amount x, compute the number of combinations:
dp[x] += dp[x - coin].

    - Return dp[amount].

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
