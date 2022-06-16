"""
Merge Intervals
---------------

Given an array of intervals where intervals[i] = [start_i, end_i], merge all overlapping
intervals, and return an array of the non-overlapping intervals that cover all the
intervals in the input.

Complexity
==========

Time
----

merge(intervals): O(n * lg n).

Space
-----

merge(intervals): O(lg n), for the space required by the sorting algorithm.
"""


def sol(intervals):
    intervals.sort()
    sol = []
    for interval in intervals:
        if not sol or sol[-1][1] < interval[0]:
            sol.append(interval)
        else:
            sol[-1][1] = max(sol[-1][1], interval[1])
    return sol
