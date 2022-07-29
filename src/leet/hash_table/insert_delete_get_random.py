"""
Insert Delete GetRandom O(1) - Duplicates allowed
-------------------------------------------------

Implement the RandomizedSet class:

    - RandomizedSet() Initializes the RandomizedSet object.
    - bool insert(int val) Inserts an item val into the set if not present. Returns true
if the item was not present, false otherwise.
    - bool remove(int val) Removes an item val from the set if present. Returns true if
the item was present, false otherwise.
    - int getRandom() Returns a random element from the current set of elements (it's
guaranteed that at least one element exists when this method is called). Each element
must have the same probability of being returned.

You must implement the functions of the class such that each function works in average
O(1) time complexity.

Intuition
---------

Using a hashmap provides insert and remove in average constant time, although it has
problems with getting a random value since there are no indices in a hashmap. Hence, to
get the true random value, one has to build a list of keys aside and use this list to
compute a random value in constant time.

Using an array provides insert and get_random in average constant time, although it has
problems with deleting a value. To delete a value at an arbitrary index takes linear
time. The solution here is swap the element to delete with the last one and pop the
last element out. In order to do this in constant time, one needs a hashmap which maps
the element to its index.

In either case, we need a hashmap that maps elements to their indices.

With duplicates, we also have to map values to all indices that have those values.

Example:

insert(1)
insert(1)
insert(2)

self.dict = {1: {0, 1}, 2: {2}}
self.list = [1, 1, 2]

remove(1)

First, we swap the number we want to remove from self.list with the last number from
self.list. The most recent index of the number we want to remove comes from self.dict.
The last number comes from the end of self.list.

Second, we swap the number we want to remove from self.list with the last number from
self.list.

Third, we update self.dict for the last number to reflect its new index in self.list.

Last, we remove the old index in self.dict for the last number and remove the last
number from its old position in self.list.

Complexity
==========

Time
----

Sol:
    def __init__(self, dups=False): O(1).
    def get_random(self): O(1).
    def insert(self, val): O(1), average case.
    def remove(self, val): O(1), average case.

Space
-----

Sol:
    self.dict: O(n), to store n elements.
    self.list: O(n), to store n elements.
"""


# Standard Library
import random

from collections import defaultdict


class Sol:
    def __init__(self, dups=False):
        self.dict, self.dups, self.list = defaultdict(set) if dups else {}, dups, []

    def get_random(self):
        return random.choice(self.list)

    def insert(self, val):
        if self.dups:
            self.dict[val].add(len(self.list))
            self.list.append(val)
            return len(self.dict[val]) == 1
        if val not in self.dict:
            self.dict[val] = len(self.list)
            self.list.append(val)
            return True
        return False

    def remove(self, val):
        if self.dups:
            if self.dict[val]:
                last, index = self.list[-1], self.dict[val].pop()
                self.list[index] = last
                self.dict[last].add(index)
                self.dict[last].discard(len(self.list) - 1)
                self.list.pop()
                return True
            return False
        if val in self.dict:
            last, index = self.list[-1], self.dict[val]
            self.list[index] = last
            self.dict[last] = index
            del self.dict[val]
            self.list.pop()
            return True
        return False
