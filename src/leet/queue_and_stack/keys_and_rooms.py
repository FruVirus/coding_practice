"""
Keys and Rooms
--------------

There are n rooms labeled from 0 to n - 1 and all the rooms are locked except for room
0. Your goal is to visit all the rooms. However, you cannot enter a locked room without
having its key.

When you visit a room, you may find a set of distinct keys in it. Each key has a number
on it, denoting which room it unlocks, and you can take all of them with you to unlock
the other rooms.

Given an array rooms where rooms[i] is the set of keys that you can obtain if you
visited room i, return true if you can visit all the rooms, or false otherwise.

Complexity
==========

Time
----

canVisitAllRooms(rooms): O(n + e), where n is the number of rooms and e is the total
number of keys.

Space
-----

canVisitAllRooms(rooms): O(n).
"""


def sol(rooms):
    seen = [False] * len(rooms)
    seen[0], stack = True, [0]
    while stack:
        for key in rooms[stack.pop()]:
            if not seen[key]:
                seen[key] = True
                stack.append(key)
    return all(seen)
