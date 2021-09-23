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

Open Hashing - Chaining
=======================

In chaining, we place all the elements that has to the same slot into the same linked
list. Slot j contains a pointer to the head of the list of all stored elements that hash
to j; if there are no such elements, slot j contains NIL.

NB: HashChain mimics table doubling for practice even though it's redundant in Python.

insertion: O(1) if we assume that the element x being inserted is not already present in
the table. Otherwise, searching for the element will take O(L) time or an average-case
time of Theta(1 + n/m), where n is the total number of elements and m is the total
number of slots in the hash table.

deletion: O(1) if we use a doubly linked list. Otherwise, O(n) if we use a singly linked
list since we have to search for the element previous to the element being deleted
first.

search: Theta(1 + n / m)
"""

# Standard Library
import random

# Repository Library
from src.clrs.lists.doubly_linked_list import DLL
from src.clrs.lists.singly_linked_list import Node


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
            self.size = int(self.size / 2)
            self.table = self._rehash()

    def _rehash(self):
        table = [None] * self.size
        key_list = []
        for ll in self.table:
            if ll is not None:
                head = ll.head
                while head is not None:
                    key_list.append(head.k)
                    head = head.next
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


def is_prime(n):
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    for i in range(5, n // 2 + 1, 6):
        if n % i == 0 or n % (i + 2) == 0:
            return False
    return True


def next_prime(n):
    if n <= 1:
        return 2
    while True:
        n += 1
        if is_prime(n):
            return n
