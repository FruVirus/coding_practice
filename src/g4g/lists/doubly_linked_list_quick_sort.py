"""
Overview
========

The idea is simple: we first find the pointer to the last node. Once we have a pointer
to the last node, we can recursively sort the linked list using pointers to the first
and last nodes of a linked list, similar to quick sort on arrays where we pass the
indices of the first and last array elements. The partition function for a linked list
is also similar to the partition function for arrays. Instead of returning the index of
the pivot element, we return a pointer to the pivot element. In the following
implementation, quicksort() is just a wrapper function --> the main recursive function
is _quicksort() which is similar to quicksort() for arrays.

Quicksort can be implemented for linked Lists only when we can pick a fixed point as the
pivot (e.g., the last element). Random QuickSort cannot be efficiently implemented for
linked lists.

Complexity
==========

quicksort():
    O(n^2) worst case --> when the partitioning routine produces one sub-problem with
        n - 1 elements and one with 0 elements or when the input array is already sorted
    O(n*lg(n)) expected case --> when we can equally balance the two sides of the
        partition at every level of the recursion (only possible when we can choose the
        median value with each recursion)

partition():
    O(n) = O(h - l + 1)
"""

# Repository Library
from src.clrs.lists.doubly_linked_list import DLL


class DLLQuickSort(DLL):
    def _get_last(self):
        node = self.head
        while node.next is not None:
            node = node.next
        return node

    @staticmethod
    def partition(low, high):
        x, i = high.k, low.prev
        j = low
        while j != high:
            if j.k <= x:
                i = low if i is None else i.next
                temp = i.k
                i.k, j.k = j.k, temp
            j = j.next
        i = low if i is None else i.next
        temp = i.k
        i.k, high.k = high.k, temp
        return i

    def quicksort(self, low, high):
        if high is not None and low != high and low != high.next:
            temp = self.partition(low, high)
            self.quicksort(low, temp.prev)
            self.quicksort(temp.next, high)

    def sort(self):
        self.quicksort(self.head, self._get_last())
        node, sorted_list = self.head, []
        while node is not None:
            sorted_list.append(node.k)
            node = node.next
        return sorted_list
