"""
Meeting Rooms II
----------------

Given an array of meeting time intervals, intervals, where intervals[i] =
[start_i, end_i], return the minimum number of conference rooms required.

Complexity
==========

Time
----

MinMeetingRooms: O(n * lg n).

Space
-----

MinMeetingRooms: O(n).
"""

# pylint: disable=R0201


class MinMeetingRooms:
    def min_meeting_rooms(self, intervals):
        start_times = sorted([i[0] for i in intervals])
        end_times = sorted([i[1] for i in intervals])
        start_ptr = end_ptr = num_rooms = 0
        for _ in range(len(intervals)):
            if start_times[start_ptr] < end_times[end_ptr]:
                num_rooms += 1
            else:
                end_ptr += 1
            start_ptr += 1
        return num_rooms
