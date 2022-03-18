"""
Logger Rate Limiter
-------------------

Design a logger system that receives a stream of messages along with their timestamps.
Each unique message should only be printed at most every 10 seconds (i.e., a message
printed at timestamp t will prevent other identical messages from being printed until
timestamp t + 10).

All messages will come in chronological order. Several messages may arrive at the same
timestamp.

Implement the Logger class:
    - Logger() Initializes the logger object.
    - bool shouldPrintMessage(int timestamp, string message) Returns true if the message
should be printed in the given timestamp, otherwise returns false.

Complexity
==========

Time
----

Time
----

Sol:
    def __init__(self): O(1).
    def print(self, ts, msg): O(1).

Space
-----

Sol:
    self.times: O(m), where m is the size of all incoming messages. Over time, the hash
table would have an entry for each unique message that has appeared.
"""


class Sol:
    def __init__(self):
        self.times = {}

    def print(self, ts, msg):
        if msg not in self.times or ts >= self.times[msg] + 10:
            self.times[msg] = ts
            return True
        return False
