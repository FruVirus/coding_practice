"""
Meeting Rooms II
----------------

Given an array of meeting time intervals, intervals, where intervals[i] =
[start_i, end_i], return the minimum number of conference rooms required.

Complexity
==========

Time
----

minMeetingRooms(intervals): O(n * lg n).

Space
-----

minMeetingRooms(intervals): O(n).
"""


def sol(intervals):
    s = sorted([i[0] for i in intervals])
    f = sorted([i[1] for i in intervals])
    k = num_rooms = 0
    for i in range(len(intervals)):
        if s[i] < f[k]:
            num_rooms += 1
        else:
            k += 1
    return num_rooms
