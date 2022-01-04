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
from src.clrs.data_structures.elementary_data_structures.linked_list import SLL


class SLLInsertionSort(SLL):
    @staticmethod
    def insertion_sort(sorted_, node):
        if sorted_ is None or sorted_.k >= node.k:
            node.next, sorted_ = sorted_, node
        else:
            curr = sorted_
            while curr.next is not None and curr.next.k < node.k:
                curr = curr.next
            node.next, curr.next = curr.next, node
        return sorted_

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
        return sorted_list
