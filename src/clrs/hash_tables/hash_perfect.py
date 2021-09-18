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

Closed Hashing - Open Addressing
================================

In open addressing, all elements occupy the hash table itself. That is, each table entry
contains either an element of the dynamic set or None. When searching for an element, we
systematically examine table slots until either we find the desired element or we have
ascertained that the element is not in the table. No lists and no elements are stored
outside the table, unlike in chaining. Thus, in open addressing, the hash table can
"fill up" so that no further insertions can be made; one consequence is that the load
factor alpha = n / m can never exceed 1.

The advantage of open addressing is that it avoids pointers altogether. Instead of
following pointers, we compute the sequence of slots to be examined. The extra memory
freed by not storing pointers provides the hash table with a larger number of slots for
the same amount of memory, potentially yielding fewer collisions and faster retrieval.

To determine which slots to probe, we extend the hash function to include the probe
number (starting from 0) as a second input. With open addressing, we require that for
every key k, the probe sequence is a permutation of the number of slots, so that every
hash table position is eventually considered as a slot for a new key as the table fills
up.

insertion: Requires at most 1 / (1 - alpha) probes on average, assuming uniform hashing.

deletion: O(1) if we use a doubly linked list. Otherwise, O(n) if we use a singly linked
list since we have to search for the element previous to the element being deleted
first.

search: Expected number of probes in an unsuccessful search is at most 1 / (1 - alpha).
Expected number of probes in a successful search is at most
(1 / alpha) * ln(1 / (1 - alpha)). When we use the special value "DELETED", search times
no longer depend on the load factor alpha, and for this reason chaining is more commonly
selected as a collision resolution technique when keys must be deleted.
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
        self.a_list = [None] * self.m
        self.b_list = [None] * self.m
        self.n = [0] * self.m
        self.table = [None] * self.m
        self.hash()

    def hash(self):
        for k in self.keys:
            hash_value = ((self.a * k + self.b) % self.p) % self.m
            self.n[hash_value] += 1
            self.a_list[hash_value] = random.choice(list(range(1, self.p)))
            self.b_list[hash_value] = random.choice(list(range(0, self.p)))
        for m in range(self.m):
            if self.n[m] > 1:
                self.table[m] = [None] * self.n[m] ** 2
        for k in self.keys:
            hash_value = ((self.a * k + self.b) % self.p) % self.m
            a = self.a_list[hash_value]
            b = self.b_list[hash_value]
            if isinstance(self.table[hash_value], list):
                m = len(self.table[hash_value])
                index = ((a * k + b) % self.p) % m
                self.table[hash_value][index] = k
            else:
                self.table[hash_value] = k

    def search(self, k):
        i = 0
        while True:
            hash_value = self.hash_func(k, i)
            if self.table[hash_value] == k:
                return hash_value
            i += 1
            if self.table[hash_value] is None or i == self.size:
                break
        return None
