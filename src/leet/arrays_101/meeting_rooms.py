"""
Meeting Rooms
-------------

Given an array of meeting time intervals where intervals[i] = [start_i, end_i],
determine if a person could attend all meetings.

Complexity
==========

Time
----

canAttendMeetings(intervals): O(n * lg(n)).

Space
-----

canAttendMeetings(intervals): O(1).
"""


def sol(intervals):
    intervals.sort()
    for i in range(len(intervals) - 1):
        if intervals[i][1] > intervals[i + 1][0]:
            return False
    return True
