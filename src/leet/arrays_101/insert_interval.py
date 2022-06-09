"""
Insert Interval
---------------

You are given an array of non-overlapping intervals intervals where intervals[i] =
[start_i, end_i] represent the start and the end of the ith interval and intervals is
sorted in ascending order by start_i. You are also given an interval newInterval =
[start, end] that represents the start and end of another interval.

Insert newInterval into intervals such that intervals is still sorted in ascending order
by start_i and intervals still does not have any overlapping intervals (merge
overlapping intervals if necessary).

Return intervals after the insertion.

Intuition
---------

The straightforward one-pass strategy could be implemented in three steps.

1. Add to the output all the intervals starting before newInterval.
2. Add to the output newInterval, merge it with the last added interval if needed.
3. Add the next intervals one by one, merge if needed.

Complexity
==========

Time
----

insert(intervals, new_interval): O(n), where n is the length of new_interval.

Space
-----

insert(intervals, new_interval): O(n).
"""


def sol(intervals, new_interval):
	i, n, sol = 0, len(intervals), []
	while i < n and intervals[i][1] < new_interval[0]:
		sol.append(intervals[i])
		i += 1
	while i < n and intervals[i][0] <= new_interval[1]:
		new_interval[0] = min(intervals[i][0], new_interval[0])
		new_interval[1] = max(intervals[i][1], new_interval[1])
		i += 1
	sol.append(new_interval)
	while i < n:
		sol.append(intervals[i])
		i += 1
	return sol
