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
search() takes O(n) time.
"""


class Node:
    def __init__(self, k):
        self.k, self.next, self.prev = k, None, None


class SLL:
    def __init__(self):
        self.head = None

    @staticmethod
    def _get_middle(h):
        slow, fast = h, h.next
        while fast is not None and fast.next is not None:
            slow, fast = slow.next, fast.next.next
        return slow

    def delete(self, x):
        if isinstance(x, (int, float)):
            x = self.search(x)
        curr, prev = self.head, None
        while curr is not None and curr.k != x.k:
            prev, curr = curr, curr.next
        if prev is None:
            self.head = curr.next
        else:
            prev.next = curr.next

    def insert(self, x):
        x.next = self.head
        self.head = x

    def merge(self, l, r):
        if l is None:
            return r
        if r is None:
            return l
        if l.k <= r.k:
            result = l
            result.next = self.merge(l.next, r)
        else:
            result = r
            result.next = self.merge(l, r.next)
        return result

    def merge_sort(self, h):
        if h is None or h.next is None:
            return h
        mid = self._get_middle(h)
        mid_next, mid.next = mid.next, None
        l = self.merge_sort(h)
        r = self.merge_sort(mid_next)
        return self.merge(l, r)

    def sort(self, sort="merge_sort"):
        result, sorted_list = None, []
        if sort == "merge_sort":
            result = self.merge_sort(self.head)
        else:
            pass
        if result is not None:
            curr = result
            while curr is not None:
                sorted_list.append(curr.k)
                curr = curr.next
        return sorted_list

    def search(self, k):
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
