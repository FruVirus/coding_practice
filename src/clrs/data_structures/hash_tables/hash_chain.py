"""
11.2 Hash tables
================

Collision resolution by chaining
--------------------------------

In chaining, we place all the elements that hash to the same slot into the same linked
list. Slot j contains a pointer to the head of the list of all stored elements that hash
to j; if there are no such elements, slot j contains NIL.

The worst case running time for insertion is O(1). THe insertion procedure is fast in
part because it assumes that the element x being inserted is not already present in the
table; if necessary we can check this assumption (at additional cost) by searching for
an element whose key is x.key before we insert. For searching, the worst case running
time is proportional to the length of the list. We can delete an element in O(1) time if
the lists are doubly linked. If the hash table supports deletion, then its linked lists
should be doubly linked so that we can delete an item quickly. If the lists were only
singly linked, then to delete element x, we would first have to find x in the list
T[h(x.key)] so that we could update the next attribute of x's predecessor. With singly
linked lists, both deletion and searching would have the same asymptotic running times.

Analysis of hashing with chaining
---------------------------------

Given a hash table T with m slots that stores n elements, we define the load factor
alpha for T as n / m, that is, the average number of elements stored in a chain. Alpha
can be less than, equal to, or greater than 1.

The worst case behavior of hashing with chaining is terrible: all n keys hash to the
same slot, creating a list of length n. The worst case time for searching is thus
Theta(n) plus the time to compute the hash function---no better than if we used one
linked list for all the elements.

The average case performance of hashing depends on how well the hash function h
distributes the set of keys to be stored among the m slots, on the average. We assume
that any given element is equally likely to hash into any of the m slots, independently
of where any other element has hashed to. We call this the assumption of simple uniform
hashing.

If the number of hash-table slots is at least proportional to the number of elements in
the table, we have n = O(m) and, consequently, alpha = n / m = O(m) / m = O(1). Thus,
searching takes constant time on average.

NB: HashChain mimics table doubling for practice even though it's redundant in Python.

Complexity
==========

Time
----

insert(): O(1) if we assume that the element x being inserted is not already present in
the table. Otherwise, searching for the element will take O(L) time or an average-case
time of Theta(1 + n / m), where n is the total number of elements and m is the total
number of slots in the hash table.
delete(): O(1) if we use a doubly linked list. Otherwise, O(n) if we use a singly linked
list since we have to search for the element previous to the element being deleted
first.
search(): Theta(1 + n / m) under the assumption of simple uniform hashing.
"""

# Standard Library
import random

# Repository Library
from src.clrs.data_structures.elementary_data_structures.linked_list import DLL, Node
from src.clrs.selected_topics.number_theoretic_algorithms.numerical_methods.next_prime import (  # noqa: E501
    next_prime,
)


class HashChain:
    def __init__(self, size, ahf="hash_div", table_double=False):
        self.size = size
        self.ahf = getattr(self, ahf)
        self.table_double = table_double
        self.table = [None] * self.size
        self.a, self.m = 0.62, 2 ** self.size

    def _grow(self):
        if self.table_double and self.table.count(None) == 0:
            self.size *= 2
            self.table = self._rehash()

    def _insert(self, k, table):
        hash_value = self.ahf(k)
        if table[hash_value] is None:
            table[hash_value] = DLL()
        table[hash_value].insert(Node(k))

    def _reduce(self):
        if self.table_double and self.table.count(None) == int(3 * self.size / 4):
            self.size //= 2
            self.table = self._rehash()

    def _rehash(self):
        table, key_list = [None] * self.size, []
        for ll in self.table:
            if ll is not None:
                node = ll.head
                while node is not None:
                    key_list.append(node.k)
                    node = node.next
        for k in key_list:
            self._insert(k, table)
        return table

    def delete(self, x):
        hash_value = self.ahf(x if isinstance(x, (int, float)) else x.k)
        self.table[hash_value].delete(x)
        if self.table_double and self.table[hash_value].head is None:
            self.table[hash_value] = None
        self._reduce()

    def hash_div(self, k):
        return k % self.size

    def hash_mul(self, k):
        return int(self.m * ((k * self.a) % 1))

    def hash_uni(self, k, keys, **kwargs):
        p = kwargs.get("p", None) or next_prime(max(keys))
        a = kwargs.get("a", None) or random.randrange(1, p)
        b = kwargs.get("b", None) or random.randrange(0, p)
        return ((a * k + b) % p) % self.size

    def insert(self, x):
        self._grow()
        self._insert(x.k, self.table)

    def search(self, k):
        hash_value = self.ahf(k)
        if self.table[hash_value] is not None:
            return self.table[hash_value].search(k)
        return None
