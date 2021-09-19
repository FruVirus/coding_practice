"""A hash table is an effective data structure for implementing dictionaries and their
operations: INSERT, DELETE, and SEARCH. Although searching for an element in a hash
table can take as long as searching for an element in a linked list (Theta(n) time), in
practice, hashing performs extremely well. Under reasonable assumptions, the average
time to search for an element in a hash table is O(1).

When the number of keys actually stored is small relative to the total number of
possible keys, hash tables become an effective alternative to directly addressing an
array, since a hash table typically uses an array of size proportional to the number of
keys actually stored. Instead of using the key as an array index directly, the array
index is computed from the key using a hash function.

Perfect Hashing
===============

Perfect hashing provides an excellent worst-case performance when the set of keys is
static: once the keys are stored in the table, the set of keys never changes. Some
applications naturally have static sets of keys: consider the set of reserved words in
a programming language, or the set of file names on a CD-ROM.

Perfect hashing requires O(n) memory space.

NB: When m = n^2, a hash function chosen randomly from the set of universal hash
functions is more likely than not to have no collisions. However, one must still perform
some trial and error before finding a collision-free hash function for a given set of
(static) keys.

search: O(1) in the worst case.
"""

# Standard Library
import random

# Repository Library
from src.clrs.hash_tables.hash_chain import next_prime


class HashPerfect:
    _DELETED = "DELETED"

    def __init__(self, keys, **kwargs):
        self.keys = keys
        self.m = len(self.keys)
        self.p = kwargs["p"] or next_prime(max(self.keys))
        self.a = kwargs["a"] or random.choice(list(range(1, self.p)))
        self.b = kwargs["b"] or random.choice(list(range(0, self.p)))
        self.a_list = [27, None, 48, None, None, 16, None, 48, None]
        self.b_list = [83, None, 51, None, None, 59, None, 35, None]
        self._create_table()

    def _create_table(self):
        self.n = [0] * self.m
        self.table = [None] * self.m
        for k in self.keys:
            hash_value = ((self.a * k + self.b) % self.p) % self.m
            self.n[hash_value] += 1
        for m in range(self.m):
            if self.n[m] > 1:
                self.table[m] = [None] * self.n[m] ** 2
        for k in self.keys:
            hash_value, index = self.hash(k)
            if index is not None:
                self.table[hash_value][index] = k
            else:
                self.table[hash_value] = k

    def hash(self, k):
        hash_value = ((self.a * k + self.b) % self.p) % self.m
        a = self.a_list[hash_value]
        b = self.b_list[hash_value]
        if isinstance(self.table[hash_value], list):
            m = len(self.table[hash_value])
            index = ((a * k + b) % self.p) % m
            return hash_value, index
        return hash_value, None

    def search(self, k):
        hash_value, index = self.hash(k)
        if index is not None:
            return hash_value, index
        return hash_value
