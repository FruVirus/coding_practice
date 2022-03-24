"""
Maximum Frequency Stack
-----------------------

Design a stack-like data structure to push elements to the stack and pop the most
frequent element from the stack.

Implement the FreqStack class:

    - FreqStack() constructs an empty frequency stack.
    - void push(int val) pushes an integer val onto the top of the stack.
    - int pop() removes and returns the most frequent element in the stack.
        - If there is a tie for the most frequent element, the element closest to the
stack's top is removed and returned.

Intuition
---------

Evidently, we care about the frequency of an element. Let freq be a Map from x to the
number of occurrences of x.

Also, we (probably) care about maxfreq, the current maximum frequency of any element in
the stack. This is clear because we must pop the element with the maximum frequency.

The main question then becomes: among elements with the same (maximum) frequency, how do
we know which element is most recent? We can use a stack to query this information: the
top of the stack is the most recent.

To this end, let group be a map from frequency to a stack of elements with that
frequency. We now have all the required components to implement FreqStack.

Actually, as an implementation level detail, if x has frequency f, then we'll have x in
all group[i] (i <= f), not just the top. This is because each group[i] will store
information related to the ith copy of x.

Complexity
==========

Time
----

Sol:
    def __init__(self): O(1).
    def pop(self): O(1).
    def push(self, val): O(1).

Space
-----

Sol:
    self.freq and self.group: O(n), where n is the number of elements in the stack.
"""


# Standard Library
from collections import Counter, defaultdict


class Sol:
    def __init__(self):
        self.freq, self.group, self.max_freq = Counter(), defaultdict(list), 0

    def pop(self):
        x = self.group[self.max_freq].pop()
        self.freq[x] -= 1
        if not self.group[self.max_freq]:
            self.max_freq -= 1
        return x

    def push(self, val):
        self.freq[val] += 1
        self.max_freq = max(self.max_freq, self.freq[val])
        self.group[self.freq[val]].append(val)
