"""
Two Sum III - Data structure design
-----------------------------------

Design a data structure that accepts a stream of integers and checks if it has a pair of
integers that sum up to a particular value.

Implement the TwoSum class:

    - TwoSum() Initializes the TwoSum object, with an empty array initially.
    - void add(int number) Adds number to the data structure.
    - boolean find(int value) Returns true if there exists any pair of numbers whose sum
is equal to value, otherwise, it returns false.

Intuition
---------

First, we initialize a hashtable container in our data structure.

For the add(number) function, we build a frequency hashtable with the number as key and
the frequency of the number as the value in the table.

For the find(value) function, we then iterate through the hashtable over the keys. For
each key (number), we check if there exists a complement (value - number) in the table.
If so, we could terminate the loop and return the result.

In a particular case, where the number and its complement are equal, we then need to
check if there exists at least two copies of the number in the table.

Complexity
==========

Time
----

Sol:
    def __init__(self): O(1).
    def add(self, val): O(1).
    def find(self, val): O(n), where n is the total number of unique numbers. In the
worst case, we would iterate through the entire table.

Space
-----

Sol:
    self.num_counts: O(n), where n is the total number of unique numbers that we will
see during the stream.
"""

# Standard Library
from collections import defaultdict


class Sol:
    def __init__(self):
        self.num_counts = defaultdict(int)

    def add(self, number):
        self.num_counts[number] += 1

    def find(self, value):
        for num in self.num_counts:
            com = value - num
            if num != com:
                if com in self.num_counts:
                    return True
            elif self.num_counts[num] > 1:
                return True
        return False
