"""
Open the Lock
-------------

You have a lock in front of you with 4 circular wheels. Each wheel has 10 slots:
'0', '1', '2', '3', '4', '5', '6', '7', '8', '9'. The wheels can rotate freely and wrap
around: for example we can turn '9' to be '0', or '0' to be '9'. Each move consists of
turning one wheel one slot.

The lock initially starts at '0000', a string representing the state of the 4 wheels.

You are given a list of dead ends, meaning if the lock displays any of these codes, the
wheels of the lock will stop turning and you will be unable to open it.

Given a target representing the value of the wheels that will unlock the lock, return
the minimum total number of turns required to open the lock, or -1 if it is impossible.

Complexity
==========

Time
----

openLock(deadends, target): O(n^2 * a^n * d), where n is the number of digits in the
lock, a is the number of digits in the alphabet, and d is the size of deadends.

Space
-----

openLock(deadends, target): O(a^n + d).
"""

# pylint: disable=C0200

# Standard Library
from collections import deque


def sol(deadends, target):
    def get_combos(combo):
        for i, c in enumerate(combo):
            for d in [-1, 1]:
                yield combo[:i] + str((int(c) + d) % 10) + combo[i + 1 :]

    visited, queue = {"0000"}, deque([("0000", 0)])
    while queue:
        combo, num_turns = queue.popleft()
        if combo == target:
            return num_turns
        if combo in deadends:
            continue
        for c in get_combos(combo):
            if c not in visited:
                visited.add(c)
                queue.append((c, num_turns + 1))
    return -1
