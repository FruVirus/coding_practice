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

NB: HashOpen mimics table doubling for practice even though it's redundant in Python.

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

# Repository Library
from src.clrs.hash_tables.hash_chain import HashChain, is_prime


class HashOpen(HashChain):
    _DELETED = "DELETED"

    def __init__(self, size, hash_func="linear_probe", table_double=False):
        super().__init__(size, table_double=table_double)
        self.hash_func = getattr(self, hash_func)

    def _grow(self):
        if self.table_double:
            none, deleted = self.table.count(None), self.table.count(self._DELETED)
            if none == deleted == 0:
                self.size *= 2
                self.table = self._rehash()

    def _insert(self, k, table):
        i = 0
        while i != self.size:
            hash_value = self.hash_func(k, i)
            if table[hash_value] in [None, self._DELETED]:
                table[hash_value] = k
                return hash_value
            i += 1
        raise OverflowError()

    def _reduce(self):
        if self.table_double:
            none, deleted = self.table.count(None), self.table.count(self._DELETED)
            if none + deleted == int(3 * self.size / 4):
                self.size = int(self.size / 2)
                self.table = self._rehash()

    def _rehash(self):
        table = [None] * self.size
        key_list = [slot for slot in self.table if slot not in [None, self._DELETED]]
        for k in key_list:
            self._insert(k, table)
        return table

    def delete(self, k):
        hash_value = self.search(k)
        self.table[hash_value] = self._DELETED
        self._reduce()

    def double_hashing(self, k, i):
        if (self.size & (self.size - 1) == 0) and self.size != 0:
            h1, h2 = self.hash_div(k), self.hash_mul(k)
            if h2 % 2 == 0:
                h2 += 1
        else:
            assert is_prime(self.size)
            h1 = k % self.size
            h2 = 1 + (k % (self.size - 1))
        return (h1 + i * h2) % self.size

    def insert(self, k):
        self._grow()
        self._insert(k, self.table)

    def linear_probe(self, k, i):
        return (self.ahf(k) + i) % self.size

    def quadratic_probe(self, k, i):
        return (self.ahf(k) + i ** 2) % self.size

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
