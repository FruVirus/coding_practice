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

insertion: O(1) if we assume that the element x being inserted is not alrady present in
the table. Otherwise, searching for the element will take O(L) time or an average-case
time of Theta(1 + n/m), where n is the total number of elements and m is the total
number of slots in the hash table.

deletion: O(1) if we use a doubly linked list. Otherwise, O(n) if we use a singly linked
list since we have to search for the element previous to the element being deleted
first.

search: Theta(1++ n/m)

Closed Hashing - Open Addressing - Linear Probing
=================================================
XXX

Closed Hashing - Open Addressing - Quadratic Probing
====================================================
XXX
"""

# Repository Library
from src.clrs.lists.doubly_linked_list import DLL


class Hash:
    def __init__(self, size, hash_func="hash_div"):
        self.hash_func = getattr(self, hash_func)
        self.size = size
        self.table = [None] * self.size
        self.a, self.m = 0.62, 2 ** self.size

    def hash_div(self, k):
        return k % self.size

    def hash_mul(self, k):
        return int(self.m * ((k * self.a) % 1))

    def delete(self, x):
        if isinstance(x, (int, float)):
            hash_value = self.hash_func(x)
        else:
            hash_value = self.hash_func(x.k)
        self.table[hash_value].delete(x)

    def insert(self, x):
        hash_value = self.hash_func(x.k)
        if self.table[hash_value] is None:
            self.table[hash_value] = DLL()
        self.table[hash_value].insert(x)

    def search(self, k):
        hash_value = self.hash_func(k)
        return self.table[hash_value].search(k)
