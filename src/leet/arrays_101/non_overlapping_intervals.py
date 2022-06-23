"""
Non-overlapping Intervals
-------------------------

Given an array of intervals where intervals[i] = [start_i, end_i], return the minimum
number of intervals you need to remove to make the rest of the intervals
non-overlapping.

Intuition
---------

If two intervals are overlapping, we want to remove the interval that has the longer end
point -- the longer interval will always overlap with more or the same number of future
intervals compared to the shorter one.

Complexity
==========

Time
----

eraseOverlapIntervals(intervals): O(n * lg n).

Space
-----

eraseOverlapIntervals(intervals): O(1).
"""


def sol(intervals):
    intervals.sort()
    count, prev_end = 0, intervals[0][1]
    for start, end in intervals[1:]:
        if prev_end > start:
            prev_end = min(prev_end, end)
            count += 1
        else:
            prev_end = end
    return count
