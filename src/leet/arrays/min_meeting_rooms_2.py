"""
Meeting Rooms II
----------------

Given an array of meeting time intervals, intervals, where intervals[i] =
[start_i, end_i], return the minimum number of conference rooms required.

Complexity
==========

Time
----

min_meeting_rooms(): O(n * lg n).

Space
-----

min_meeting_rooms(): O(n).
"""


def min_meeting_rooms(intervals):
    start_times = sorted([i[0] for i in intervals])
    end_times = sorted([i[1] for i in intervals])
    start = end = num_rooms = 0
    while start < len(intervals) and end < len(intervals):
        if start_times[start] < end_times[end]:
            num_rooms += 1
        else:
            end += 1
        start += 1
    return num_rooms
