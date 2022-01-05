"""
11.4 Open addressing
====================

In open addressing, all elements occupy the hash table itself. That is, each table entry
contains either an element of the dynamic set or NIL. When searching for an element, we
systematically examine table slots until either we find the desired element or we have
ascertained that the element is not in the table. No lists and no elements are stored
outside the table, unlike in chaining. Thus, in open addressing, the hash table can
"fill up" so that no further insertions can be made; one consequence is that the load
factor alpha = n / m can never exceed 1.

The advantage of open addressing is that it avoids pointers altogether. Instead of
following pointers, we compute the sequence of slots to be examined. The extra memory
freed by not storing pointers provides the hash table with a larger number of slots for
the same amount of memory, potentially yielding fewer collisions and faster retrieval.

To perform insertion using open addressing, we successively examine, or probe, the hash
table until we find an empty slot in which to put the key. Instead of being fixed in the
order 0, 1, ..., m - 1 (which requires Theta(n) search time), the sequence of positions
probed depends upon the key being inserted. To determine which slots to probe, we extend
the hash function to include the probe number (starting from 0) as a second input. With
open addressing, we require that for every key k, the probe sequence is a permutation of
the number of slots, so that every hash table position is eventually considered as a
slot for a new key as the table fills up.

When we delete a key from slot i, we cannot simply mark that slot as empty by storing
NIL in it. If we did, we might be unable to retrieve any key k during whose insertion we
had probed slot i and found it occupied. This is because searching terminates when it
finds a NIL slot, since k would have been inserted there and not later in its probe
sequence. We can solve this problem by marking the slot, storing in it the special value
DELETED instead of NIL. When we use the special value DELETED, however, search times no
longer depend on the load factor alpha, and for this reason chaining is more commonly
selected as a collision resolution technique when keys must be deleted.

The analysis of open addressing assumes uniform hashing: the probe sequence of each key
is equally likely to be any of the m! permutations of <0, 1, ..., m - 1>. Uniform
hashing generalizes the notion of simple uniform hashing to a hash function that
produces not just a single number, but a whole probe sequence.

Three commonly used techniques for computing the probe sequences required for open
addressing are: linear probing, quadratic probing, and double hashing. These techniques
all guarantee that the permutation of probe sequences is a permutation of the slots for
each key k. None of these techniques fulfills the assumption of uniform hashing,
however, since none of them is capable of generating more than m^2 different probe
sequences (instead of the m! that uniform hashing requires). Double hashing has the
greatest number of probe sequences and, as one might expect, seems to give the best
results.

Linear probing
--------------

Because the initial probe determines the entire probe sequence, there are only m
distinct probe sequences (instead of the m! probe sequences required by uniform
hashing).

Linear probing is easy to implement, but it suffers from a problem known as primary
clustering. Long runs of occupied slots build up, increasing the average search time.
Clusters arise because an empty slot preceded by i full slots gets filled next with
probability (i + 1) / m. Long runs of occupied slots tend to get longer, and the average
search time increases.

Quadratic probing
-----------------

This method works much better than linear probing, but to make full use of the hash
table, the values of c_1, c_2, and m are constrained. Also, if two keys have the same
initial probe position, then their probe sequences are the same. This property leads to
a milder form of clustering, called secondary clustering. As in linear probing, the
initial probe determines the entire sequence, and so only m distinct probe sequences are
used.

Double hashing
--------------

Double hashing offers one of the best methods available for open addressing because the
permutations produced have many of the characteristics of randomly chosen permutations.
Unlike the case of linear or quadratic probing, the probe sequence here depends in two
ways upon the key k, since the initial probe position, the offset, or both may vary.
When m is prime or a power of 2, double hashing improves over linear or quadratic
probing in that Theta(m^2) probe sequences are used, rather than Theta(m), since each
possible (h_1(k), h_2(k)) pair yields a distinct probe sequence.

NB: HashOpen mimics table doubling for practice even though it's redundant in Python.

Complexity
==========

Time
----

insert(): Requires at most 1 / (1 - n / m) probes on average, assuming uniform hashing.

delete(): O(1) if we use a doubly linked list. Otherwise, O(n) if we use a singly linked
list since we have to search for the element previous to the element being deleted
first.

search(): Expected number of probes in an unsuccessful search is at most
1 / (1 - n / m). Expected number of probes in a successful search is at most
(1 / n / m) * ln(1 / (1 - n / m)). When we use the special value "DELETED", search times
no longer depend on the load factor alpha, and for this reason chaining is more commonly
selected as a collision resolution technique when keys must be deleted.
"""

# Repository Library
from src.clrs.data_structures.hash_tables.hash_chain import HashChain
from src.clrs.selected_topics.number_theoretic_algorithms.next_prime import is_prime


class HashOpen(HashChain):
    _DELETED = "DELETED"

    def __init__(self, size, hash_func="hash_linear", table_double=False):
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
            hash_value = self.hash_func(i, k)
            if table[hash_value] in [None, self._DELETED]:
                table[hash_value] = k
                return hash_value
            i += 1
        raise OverflowError()

    def _reduce(self):
        if self.table_double:
            none, deleted = self.table.count(None), self.table.count(self._DELETED)
            if none + deleted == int(3 * self.size / 4):
                self.size //= 2
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

    def hash_double(self, i, k):
        if (self.size & (self.size - 1) == 0) and self.size != 0:
            h1, h2 = self.hash_div(k), self.hash_mul(k)
            if h2 % 2 == 0:
                h2 += 1
        else:
            assert is_prime(self.size)
            h1 = k % self.size
            h2 = 1 + (k % (self.size - 1))
        return (h1 + i * h2) % self.size

    def hash_linear(self, i, k):
        return (self.ahf(k) + i) % self.size

    def hash_quadratic(self, i, k):
        return (self.ahf(k) + i + i ** 2) % self.size

    def insert(self, k):
        self._grow()
        self._insert(k, self.table)

    def search(self, k):
        i = 0
        hash_value = self.hash_func(i, k)
        while self.table[hash_value] is not None and i != self.size:
            if self.table[hash_value] == k:
                return hash_value
            i += 1
            hash_value = self.hash_func(i, k)
        return None
