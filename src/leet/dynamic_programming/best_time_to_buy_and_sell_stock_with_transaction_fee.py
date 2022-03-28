"""
Best Time to Buy and Sell Stock with Transaction Fee
----------------------------------------------------

You are given an array prices where prices[i] is the price of a given stock on the i-th
day, and an integer fee representing a transaction fee.

Find the maximum profit you can achieve. You may complete as many transactions as you
like, but you need to pay the transaction fee for each transaction.

Note: You may not engage in multiple transactions simultaneously (i.e., you must sell
the stock before you buy again).

Intuition
---------

If I am holding a share after today, then either I am just continuing holding the share
I had yesterday, or that I held no share yesterday, but bought in one share today:
hold = max(hold, cash - prices[i])

If I am not holding a share after today, then either I did not hold a share yesterday,
or that I held a share yesterday but I decided to sell it out today:
cash = max(cash, hold + prices[i] - fee).

Make sure fee is only incurred once.

Complexity
==========

Time
----

maxProfit(prices, fee): O(n).

Space
-----

maxProfit(prices, fee): O(1).
"""


def sol_bu(prices, fee):
    cash, hold = 0, -prices[0]
    for i in range(1, len(prices)):
        cash = max(cash, hold + prices[i] - fee)
        hold = max(hold, cash - prices[i])
    return cash
