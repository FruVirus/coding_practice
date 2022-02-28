"""
Design Linked List
------------------

Design your implementation of the linked list. You can choose to use a singly or doubly
linked list.

A node in a singly linked list should have two attributes: val and next. val is the
value of the current node, and next is a pointer/reference to the next node.

If you want to use the doubly linked list, you will need one more attribute prev to
indicate the previous node in the linked list. Assume all nodes in the linked list are
0-indexed.

Complexity
==========

Time
----

SLL:
    add_at_head(): O(1).
    get(), add_at_index(), delete_at_index(): O(index).
    add_at_tail: O(n).

DLL:
    add_at_head() and add_at_tail(): O(1).
    get(), add_at_index(), delete_at_index(): O(min(index, N - index)).

Space
-----

All: O(1).
"""


class Node:
    def __init__(self, val):
        self.val, self.prev, self.next = val, None, None


class SLL:
    def __init__(self):
        self.head, self.size = Node(0), 0

    def add_at_head(self, val):
        self.add_at_index(0, val)

    def add_at_index(self, index, val):
        if index > self.size:
            return
        index, prev, node = max(0, index), self.head, Node(val)
        for _ in range(index):
            prev = prev.next
        self.size += 1
        prev.next, node.next = node, prev.next

    def add_at_tail(self, val):
        self.add_at_index(self.size, val)

    def delete_at_index(self, index):
        if index < 0 or index >= self.size:
            return
        prev = self.head
        for _ in range(index):
            prev = prev.next
        self.size -= 1
        prev.next = prev.next.next

    def get(self, index):
        if index < 0 or index >= self.size:
            return -1
        curr = self.head
        for _ in range(index + 1):
            curr = curr.next
        return curr.val


class DLL:
    def __init__(self):
        self.head, self.tail, self.size = Node(0), Node(0), 0
        self.head.next, self.tail.prev = self.tail, self.head

    def _add(self, prev, next, val):
        self.size += 1
        node = Node(val)
        prev.next, next.prev, node.prev, node.next = node, node, prev, next

    def add_at_head(self, val):
        self._add(self.head, self.head.next, val)

    def add_at_index(self, index, val):
        if index > self.size:
            return
        index = max(0, index)
        if index < self.size - index:
            prev = self.head
            for _ in range(index):
                prev = prev.next
            next = prev.next
        else:
            next = self.tail
            for _ in range(self.size - index):
                next = next.prev
            prev = next.prev
        self._add(prev, next, val)

    def add_at_tail(self, val):
        self._add(self.tail.prev, self.tail, val)

    def delete_at_index(self, index):
        if index < 0 or index >= self.size:
            return
        if index < self.size - index:
            prev = self.head
            for _ in range(index):
                prev = prev.next
            next = prev.next.next
        else:
            next = self.tail
            for _ in range(self.size - index - 1):
                next = next.prev
            prev = next.prev.prev
        self.size -= 1
        prev.next, next.prev = next, prev

    def get(self, index):
        if index < 0 or index >= self.size:
            return -1
        if index + 1 < self.size - index:
            curr = self.head
            for _ in range(index + 1):
                curr = curr.next
        else:
            curr = self.tail
            for _ in range(self.size - index):
                curr = curr.prev
        return curr.val
