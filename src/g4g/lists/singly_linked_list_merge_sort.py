"""
Overview
========

Merge sort is often preferred for sorting a linked list. The slow random-access
performance of a linked list makes some other algorithms (e.g., quicksort) perform
poorly, and others (e.g., heapsort) completely impossible.

Let the head be the first node of the linked list to be sorted and the head reference be
the pointer to head. Note that we need a reference to the head in merge_sort9) as the
implementation changes next links to sort the linked lists (instead of the manipulating
the node keys), so the head node has to be changed if the key at the original head is
not the smallest value in the linked list.

_get_middle() finds the middle of the linked list using the tortoise and hare approach.
Note that we cannot simply find the length of the linked list and take the middle index
since linked lists are implemented using pointers and not arrays.

merge(l, r):
    1. Take a pointer (e.g., merged) to store the merged linked list and store a dummy
node in it.
    2. Take a pointer (e.g., temp) and assign merge to it.
    3. If the key of l is less than or equal to (the equal to makes this sort stable)
the key of r, then store l in next of temp and move l to the next of l.
    4. Otherwise, store r in next of temp and move r to the next of r.
    5. Move temp to the next of temp.
    6. Repeat steps 3, 4, and 5 until l is None and r is None.
    7. Now add any remaining nodes of the first or the second linked list to the merged
linked list.
    8. Return the next of merged (that will ignore the dummy and return the head of the
final merged linked list).

merge_sort(self, h):
    1. If the size of the linked list is 1 then return the head.
    2. Find the middle of the linked list using The Tortoise and The Hare Approach.
    3. Store the next of middle in mid_next; i.e., the right sub-linked list.
    4. Then make the next midpoint None.
    5. Recursively call merge_sort() on both left and right sub-linked list and store
the new head of the left and right linked list.
    6. Call merge() given the arguments new heads of left and right sub-linked lists and
store the final head returned after merging.
    7. Return the final head of the merged linked list.

Complexity
==========

O(n * lg(n)) --> time
O(lg(n)) --> space
"""

# Repository Library
from src.clrs.lists.singly_linked_list import SLL, Node


class SLLMergeSort(SLL):
    @staticmethod
    def _get_middle(h):
        slow, fast = h, h.next
        while fast is not None and fast.next is not None:
            slow, fast = slow.next, fast.next.next
        return slow

    @staticmethod
    def merge(l, r):
        merged = Node(-1)
        temp = merged
        while l is not None and r is not None:
            if l.k <= r.k:
                temp.next = l
                l = l.next
            else:
                temp.next = r
                r = r.next
            temp = temp.next
        while l is not None:
            temp.next = l
            l, temp = l.next, temp.next
        while r is not None:
            temp.next = r
            r, temp = r.next, temp.next
        return merged.next

    def merge_sort(self, h):
        if h.next is None:
            return h
        mid = self._get_middle(h)
        mid_next, mid.next = mid.next, None
        l = self.merge_sort(h)
        r = self.merge_sort(mid_next)
        return self.merge(l, r)

    def sort(self):
        result, sorted_list = self.merge_sort(self.head), []
        if result is not None:
            curr = result
            while curr is not None:
                sorted_list.append(curr.k)
                curr = curr.next
        return sorted_list
