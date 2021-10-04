"""
Overview
========

1. Create an empty sorted list for results.
2. Traverse the given list and do following for every node:
    2a. Insert current node in a sorted way in the empty sorted list.
3. Change head of given linked list to head of sorted list.

Complexity
==========

Stable
O(n^2)
O(n) if a is already sorted
"""

# Repository Library
from src.clrs.lists.singly_linked_list import SLL, Node


class SLLInsertionSort(SLL):
    def sort(self):
        curr, sorted_ = self.head, None
        while curr is not None:
            next = curr.next
            sorted_ = self.insertion_sort(sorted_, curr)
            curr = next
        sorted_list = []
        while sorted_ is not None:
            sorted_list.append(sorted_.k)
            sorted_ = sorted_.next

    def insertion_sort(self, h, node):
        if h is None or h.k >= node.k:
            node.next = h
            h = node
        else:
            curr = h
            while curr.next is not None and curr.next.k < node.k:
                curr = curr.next
            node.next = curr.next
            curr.next = node
        return h


sll = SLLInsertionSort()
sll.insert(Node(9))
sll.insert(Node(16))
sll.insert(Node(4))
sll.insert(Node(1))
print(sll.sort())
