"""
Overview
========

A linked list is a data structure in which the objects are arranged in a linear order.
Unlike an array, however, in which the linear order is determined by the array indices,
the order in a linked list is determined by a pointer in each object.

A singly linked list L is an object with an attribute key and one other pointer
attributes: next. Given an element x in the list, x.next points to its successor in the
linked list. If x.next = None, the element x has no successor and is therefore the last
element, or tail, of the list. An attribute L.head points to the first element of the
list. If L.head = None, the list is empty.

The major difference between singly and doubly linked lists is that the former also
requires O(n) time for deletion.

Complexity
==========

delete() takes O(n) time.
insert() takes O(1) time.
reverse() takes O(n) time.
search() takes O(n) time.
"""


class Node:
    def __init__(self, k):
        self.k, self.next, self.prev = k, None, None


class SLL:
    def __init__(self):
        self.head = None

    def delete(self, x):
        x = self.search(x)
        curr, prev = self.head, None
        while curr is not None and curr.k != x.k:
            prev, curr = curr, curr.next
        if prev is None:
            self.head = curr.next
        else:
            prev.next = curr.next

    def insert(self, x):
        x.next, self.head = self.head, x

    def reverse(self):
        curr, temp = self.head, None
        while curr is not None:
            next, curr.next = curr.next, temp
            curr, temp = next, curr
        self.head = temp

    def search(self, k):
        if not isinstance(k, (int, float)):
            return k
        x = self.head
        while x is not None and k != x.k:
            x = x.next
        return x

    def size(self):
        count, x = 0, self.head
        while x is not None:
            count += 1
            x = x.next
        return count
