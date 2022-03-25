"""
Min Cost Climbing Stairs
------------------------

You are given an integer array cost where cost[i] is the cost of ith step on a
staircase. Once you pay the cost, you can either climb one or two steps.

You can either start from the step with index 0, or the step with index 1.

Return the minimum cost to reach the top of the floor.

Complexity
==========

Time
----

minCostClimbingStairs(cost): O(n).

Space
-----

minCostClimbingStairs_bu(cost): O(1).
minCostClimbingStairs_td(cost): O(n).
"""


def sol_bu(cost):
    one = two = 0
    for i in range(2, len(cost) + 1):
        temp = one
        one, two = min(one + cost[i - 1], two + cost[i - 2]), temp
    return one


def sol_td(cost):
    memo = {}

    def dp(i):
        if i <= 1:
            return 0
        if i not in memo:
            memo[i] = min(dp(i - 1) + cost[i - 1], dp(i - 2) + cost[i - 2])
        return memo[i]

    return dp(len(cost))
