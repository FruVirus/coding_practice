"""
Moving Average from Data Stream
-------------------------------

Given a stream of integers and a window size, calculate the moving average of all
integers in the sliding window.

Implement the MovingAverage class:

    MovingAverage(int size) Initializes the object with the size of the window size.
    double next(int val) Returns the moving average of the last size values of the
stream.

Complexity
==========

Time
----

MovingAverage:
    def __init__(self, size): O(1).
    def next(self, val): O(1).

Space
-----

MovingAverage: O(n), where n is the window size.
"""


class Sol:
    def __init__(self, size):
        self.capacity, self.count, self.tail_index, self.queue = size, 0, 0, [0] * size
        self.wsum = 0

    def next(self, val):
        self.count += 1
        self.tail_index = (self.tail_index + 1) % self.capacity
        self.wsum = self.wsum - self.queue[self.tail_index] + val
        self.queue[self.tail_index] = val
        return self.wsum / min(self.capacity, self.count)
