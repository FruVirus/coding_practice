"""
Minimum Cost For Tickets
------------------------

You have planned some train traveling one year in advance. The days of the year in which
you will travel are given as an integer array days. Each day is an integer from 1 to
365.

Train tickets are sold in three different ways:

    - a 1-day pass is sold for costs[0] dollars,
    - a 7-day pass is sold for costs[1] dollars, and
    - a 30-day pass is sold for costs[2] dollars.

The passes allow that many days of consecutive travel.

    - For example, if we get a 7-day pass on day 2, then we can travel for 7 days:
2, 3, 4, 5, 6, 7, and 8.

Return the minimum number of dollars you need to travel every day in the given list of
days.

Intuition
---------

We only need to buy a travel pass on a day we intend to travel. For each day, if you
don't have to travel today, then it's strictly better to wait to buy a pass. If you have
to travel today, you have up to 3 choices: you must buy either a 1-day, 7-day, or
30-day pass.

Let's say dp(i) is the cost to fulfill your travel plan from day i to the end of the
plan. Then, if you have to travel today, your cost is:

    - dp(i) = min(dp(i + 1) + costs[0], dp(i + 7) + costs[1], dp(i + 30) + costs[2])

Complexity
==========

Time
----

mincostTickets_bu(days, costs): O(n), where n is the number of unique days.
mincostTickets_td(days, costs): O(w), where w = 365 is the maximum numbered day in the
travel plan.

Space
-----

mincostTickets_bu(days, costs): O(n).
mincostTickets_td(days, costs): O(w).
"""


def sol_bu(days, costs):
    dp = [0] * (days[-1] + 1)
    for i in range(1, days[-1] + 1):
        if i in days:
            dp[i] = min(
                dp[max(i - 1, 0)] + costs[0],
                dp[max(i - 7, 0)] + costs[1],
                dp[max(i - 30, 0)] + costs[2],
            )
        else:
            dp[i] = dp[i - 1]
    return dp[-1]


def sol_td(days, costs):
    memo = {}

    def dp(i):
        if i > 365:
            return 0
        if i not in memo:
            if i in days:
                memo[i] = min(dp(i + d) + c for c, d in zip(costs, [1, 7, 30]))
            else:
                memo[i] = dp(i + 1)
        return memo[i]

    return dp(days[0])
