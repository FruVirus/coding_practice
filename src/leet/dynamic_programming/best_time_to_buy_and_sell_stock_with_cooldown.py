"""
Best Time to Buy and Sell Stock with Cooldown
---------------------------------------------

You are given an array prices where prices[i] is the price of a given stock on the i-th
day.

Find the maximum profit you can achieve. You may complete as many transactions as you
like (i.e., buy one and sell one share of the stock multiple times) with the following
restrictions:

    - After you sell your stock, you cannot buy stock on the next day (i.e., cooldown
one day).

Note: You may not engage in multiple transactions simultaneously (i.e., you must sell
the stock before you buy again).

Approach
--------

1. A function that answers the problem for a given state

    dp(i, holding)

2. A recurrence relation to transition between states

    dp(i, holding) = max(do_nothing, sell_stock) if holding == 1 else
                     max(do_nothing, buy_stock)

    where,
        do_nothing = dp(i + 1, holding),
        sell_stock = prices[i] + dp(i + 2, 0), and
        buy_stock = -prices[i] + dp(i + 1, 1).

3. Base cases

    If the stock is no longer on the market (i >= prices.length), then we should return
0, as we cannot make any more money.

Complexity
==========

Time
----

maxProfit_bu(prices) and maxProfit_td(prices): O(n), where n is the length of prices.

Space
-----

maxProfit_bu(prices) and maxProfit_td(prices): O(n).
"""


def sol_bu(prices):
    n = len(prices)
    dp = [[0] * 2 for _ in range(n + 2)]
    for i in reversed(range(n)):
        for holding in range(2):
            do_nothing = dp[i + 1][holding]
            if holding:
                do_something = prices[i] + dp[i + 2][0]
            else:
                do_something = -prices[i] + dp[i + 1][1]
            dp[i][holding] = max(do_nothing, do_something)
    return dp[0][0]


def sol_td(prices):
    memo, n = {}, len(prices)

    def dp(i, holding):
        if i >= n:
            return 0
        if (i, holding) not in memo:
            do_nothing = dp(i + 1, holding)
            if holding:
                do_something = prices[i] + dp(i + 2, 0)
            else:
                do_something = -prices[i] + dp(i + 1, 1)
            memo[(i, holding)] = max(do_nothing, do_something)
        return memo[(i, holding)]

    return dp(0, 0)
