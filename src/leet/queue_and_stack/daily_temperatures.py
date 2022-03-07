"""
Daily Temperatures
------------------

Given an array of integers temperatures represents the daily temperatures, return an
array answer such that answer[i] is the number of days you have to wait after the ith
day to get a warmer temperature. If there is no future day for which this is possible,
keep answer[i] == 0 instead.

Complexity
==========

Time
----

dailyTemperatures(temperatures): O(n).

Space
-----

dailyTemperatures(temperatures): O(1).
"""


def sol(temperatures):
    stack, hottest = [0] * len(temperatures), -float("inf")
    for curr_day in reversed(range(len(temperatures))):
        if temperatures[curr_day] >= hottest:
            hottest = temperatures[curr_day]
        else:
            days = 1
            while temperatures[curr_day + days] <= temperatures[curr_day]:
                days += stack[curr_day + days]
            stack[curr_day] = days
    return stack
