"""
11.5 Perfect hashing
====================

Perfect hashing provides an excellent worst-case performance when the set of keys is
static: once the keys are stored in the table, the set of keys never changes. Some
applications naturally have static sets of keys: consider the set of reserved words in
a programming language, or the set of file names on a CD-ROM. We call a hashing
technique perfect hashing if O(1) memory accesses are required to perform a search in
the worst case.

In perfect hashing, we create two levels of hashing, with universal hashing at each
level. The first level is essentially the same as for hashing with chaining: we hash the
n keys into m slots using a hash function h carefully selected from a family of
universal hash functions. Instead of making a linked list of the keys hashing to slot j,
however, we use a small secondary hash table with its own associated hash function. By
choosing the secondary hash functions carefully, we can guarantee that there are no
collisions at the secondary level. In order to guarantee that there are no collisions
at the secondary level, however, we will need to let the size of the secondary tables be
the square of the number of keys hashing to that slot.

Intuition
---------

When m = n^2, a hash function chosen randomly from the set of universal hash functions
is more likely than not to have no collisions. However, one must still perform some
trial and error before finding a collision-free hash function for a given set of
(static) keys. The values in A and B are pre-specified from trial and error.

Complexity
==========

Time
----

_create_table(): O(n + m).
hash() and search(): O(1) in the worst case.

Space
-----

self.table: O(n).
"""

# Standard Library
import random

# Repository Library
from src.clrs.selected_topics.number_theoretic_algorithms.numerical_methods.next_prime import (  # noqa: E501
    next_prime,
)

# Define globals.
A_LIST = [0, None, 10, None, None, 0, None, 23, None]
B_LIST = [0, None, 18, None, None, 0, None, 88, None]


class HashPerfect:
    def __init__(self, keys, **kwargs):
        self.keys = keys
        self.m = len(self.keys)
        self.p = kwargs.get("p", None) or next_prime(max(self.keys))
        self.a = kwargs.get("a", None) or random.randrange(1, self.p)
        self.b = kwargs.get("b", None) or random.randrange(0, self.p)
        self._create_table()

    def _create_table(self):
        n, self.table = [0] * self.m, [None] * self.m
        for k in self.keys:
            n[self._get_hash_value(k=k)] += 1
        for m in range(self.m):
            if n[m] > 1:
                self.table[m] = [None] * n[m] ** 2
        for k in self.keys:
            hash_value, index = self.hash(k)
            if index is None:
                self.table[hash_value] = k
            else:
                self.table[hash_value][index] = k

    def _get_hash_value(self, a=None, b=None, m=None, p=None, k=None):
        a = a or self.a
        b = b or self.b
        m = m or self.m
        p = p or self.p
        return ((a * k + b) % p) % m

    def hash(self, k):
        hash_value = self._get_hash_value(k=k)
        a, b, index = A_LIST[hash_value], B_LIST[hash_value], None
        if isinstance(self.table[hash_value], list):
            index = self._get_hash_value(a, b, len(self.table[hash_value]), k=k)
        return hash_value, index

    def search(self, k):
        return self.hash(k)
