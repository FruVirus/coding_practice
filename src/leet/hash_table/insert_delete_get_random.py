"""
Insert Delete GetRandom O(1)
----------------------------

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

Complexity
==========

Time
----

Sol:
    def __init__(self): O(1).
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


class Sol:
    def __init__(self):
        self.dict, self.list = {}, []

    def get_random(self):
        return random.choice(self.list)

    def insert(self, val):
        if val in self.dict:
            return False
        self.dict[val] = len(self.list)
        self.list.append(val)
        return True

    def remove(self, val):
        if val in self.dict:
            last, index = self.list[-1], self.dict[val]
            self.list[index], self.dict[last] = last, index
            self.list.pop()
            del self.dict[val]
            return True
        return False
