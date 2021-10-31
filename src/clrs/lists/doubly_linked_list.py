"""
Overview
========

A linked list is a data structure in which the objects are arranged in a linear order.
Unlike an array, however, in which the linear order is determined by the array indices,
the order in a linked list is determined by a pointer in each object.

A doubly linked list L is an object with an attribute key and two other pointer
attributes: next and prev. Given an element x in the list, x.next points to its
successor in the linked list and x.prev points to its predecessor. If x.prev is None,
the element x has no predecessor and is therefore the first element, or head, of the
list. If x.next = None, the element x has no successor and is therefore the last
element, or tail, of the list. An attribute L.head points to the first element of the
list. If L.head = None, the list is empty.

Complexity
==========

delete() takes O(1) time.
insert() takes O(1) time.
search() takes O(n) time.
"""

# Repository Library
from src.clrs.lists.singly_linked_list import SLL


class DLL(SLL):
    def delete(self, x):
        x = self.search(x)
        if x.prev is not None:
            x.prev.next = x.next
        else:
            self.head = x.next
        if x.next is not None:
            x.next.prev = x.prev

    def insert(self, x):
        x.next = self.head
        if self.head is not None:
            self.head.prev = x
        self.head, x.prev = x, None
