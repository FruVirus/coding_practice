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

dailyTemperatures(temps): O(n).

Space
-----

dailyTemperatures(temps): O(1).
"""


def sol(temps):
    stack, hottest = [0] * len(temps), -float("inf")
    for curr_day in reversed(range(len(temps))):
        if temps[curr_day] >= hottest:
            hottest = temps[curr_day]
        else:
            days = 1
            while temps[curr_day + days] <= temps[curr_day]:
                days += stack[curr_day + days]
            stack[curr_day] = days
    return stack
