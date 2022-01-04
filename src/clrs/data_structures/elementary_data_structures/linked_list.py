"""
10.2 Linked lists
=================

A linked list is a data structure in which the objects are arranged in a linear order.
Unlike an array, however, in which the linear order is determined by the array indices,
the order in a linked list is determined by a pointer in each object.

A singly linked list L is an object with an attribute key and one other pointer
attribute: next. Given an element x in the list, x.next points to its successor in the
linked list. If x.next = None, the element x has no successor and is therefore the last
element, or tail, of the list. An attribute L.head points to the first element of the
list. If L.head = None, the list is empty.

A doubly linked list L is an object with an attribute key and two other pointer
attributes: next and prev. Given an element x in the list, x.next points to its
successor in the linked list and x.prev points to its predecessor. If x.prev is None,
the element x has no predecessor and is therefore the first element, or head, of the
list. If x.next = None, the element x has no successor and is therefore the last
element, or tail, of the list. An attribute L.head points to the first element of the
list. If L.head = None, the list is empty.

The major difference between singly and doubly linked lists is that the former also
requires O(n) time for deletion.

A list may have one of several forms. It may be either singly or doubly linked, it may
be sorted or not, and it may be circular or not. If a list is singly linked, we omit the
prev pointer in each element. If a list is sorted, the linear order of the list
corresponds to the linear order of keys stored in elements of the list; the minimum
element is then the head of the list, and the maximum element is the tail. If the list
is unsorted, the elements can appear in any order. In a circular list, the prev pointer
of the head of the list points to the tail, and the next pointer of the tail points to
the head.

Complexity
==========

Time
----

SLL:
    delete(): O(n).
    insert(): O(1).
    reverse(): O(n).
    search(): O(n).
    size(): O(n).

DLL:
    delete(): O(1).
    insert(): O(1).
    reverse(): O(n).
    search(): O(n).
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

    def reverse(self):
        curr, temp = self.head, None
        while curr is not None:
            temp = curr.prev
            curr.next, curr.prev = curr.prev, curr.next
            curr = curr.prev
        if temp is not None:
            self.head = temp.prev


dll = DLL()
dll.insert(Node(1))
dll.insert(Node(4))
dll.insert(Node(16))
dll.insert(Node(9))
