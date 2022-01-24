"""
Overview
========

Merge sort is often preferred for sorting a linked list. The slow random-access
performance of a linked list makes some other algorithms (e.g., quicksort with random
partitioning) perform poorly, and others (e.g., heapsort) completely impossible.

NB: This implementation using merge sort can be used for either singly or doubly linked
lists! This is because we only need to have the next attribute of the last node in the
linked list be None (this is true for both singly and doubly linked lists).

Let the head be the first node of the linked list to be sorted and the head reference be
the pointer to head. Note that we need a reference to the head in merge_sort() as the
implementation changes next pointers to sort the linked list (instead of the
manipulating the node keys), so the head node has to be changed if the key of the
original head is not the smallest value in the linked list.

merge(l, r):
    1. Take a pointer, merged, to store the merged linked list and store a dummy node in
it initially. The head of merged will be None but the pointer that is returned from
merge() (i.e., merged.next) will contain the starting node to the actual merged linked
list.
    2. Take a pointer, temp, and assign merged to it. temp is used to step through the
next pointers for merged as we merge the sub-linked lists l and r. If we didn't have
another variable to do this, then merged would contain the final node in the merged
linked list but we would have no way of accessing the first node in the merged linked
list.
    3. If the key of l is less than or equal to (the equal to makes this sort stable)
the key of r, then store l in next of temp and move l to the next of l.
    4. Otherwise, store r in next of temp and move r to the next of r.
    5. Move temp to the next of temp.
    6. Repeat steps 3, 4, and 5 until l is None and r is None.
    7. Now add any remaining nodes of the first or the second linked list to the merged
linked list.
    8. Return the next of merged (that will ignore the dummy node and return the head of
the final merged linked list).

merge_sort(self, h):
    1. h and mid determine the starting nodes of the left and right halves of the linked
list that will be recursively sorted.
    2. If the size of the linked list passed to merge_sort() is 1 then return the head.
This corresponds to the base case of the recursion where there is only one item to sort.
    3. Otherwise, find the middle node of the linked list using The Tortoise and The
Hare Approach.
    4. Store the next of middle in mid_next; i.e., the right sub-linked list. Make
mid.next = None. This effectively creates two separate linked lists: one for head up to
and including mid and another from the node right after mid to the end.
    5. Recursively call merge_sort() on both the left and right sub-linked lists and
store the new head of the left and right linked lists.
    6. Call merge() given the argument's new heads of left and right sub-linked lists
and store the final head returned after merging.
    7. Return the final head of the merged linked list.

Intuition
---------

1. merge_sort() is recursively called until the base cause when the linked list h just
contains one node. When this happens, merge_sort() just returns the linked list as is.
Then, merge() is called to join the left and right halves of the overall linked list
together.

2. When merge(l, r) gets called, l and r are pointers to the HEADS of their respective
linked lists. If the linked lists corresponding to l and r just have one node, then
merge(l, r) essentially just needs to (potentially) swap two nodes in order to sort them
by their keys. If the linked lists corresponding to l and r have multiple nodes, then
merge(l, r) cycles through the sub-linked lists using the next pointer.

3. Suppose merge(l, r) gets calls when l = 1 -> 4 -> 9 -> 16 and r = 2 -> 5 -> 7.
merge() starts its pointer calculations with l.k = 1 and r.k = 2. The first while-loop
terminates with 1 -> 2 -> 4 -> 5 -> 7 if we start at merged.next. This is because the
condition r is None is reached first. The second while-loop then "extends" the rest of
the nodes in l (i.e., 9 and 16) to the end of temp so that we have
1 -> 2 -> 4 -> 5 -> 7 -> 9 -> 16 as the sorted merged linked list when we return
merged.next at the end. Note that the assignment to temp.next and temp inside the second
and third while-loops are necessary since this is what essentially produces the merged
linked list that is returned (recall that temp is a pointer to merged and we return
merged.next since the first node of merged is a dummy node).

Complexity
==========

Time
----

get_middle(): O(n).
merge(): Theta(n).
merge_sort(): Theta(n * lg n).

Space
-----

merge(): O(n).
"""

# Repository Library
from src.clrs.data_structures.elementary_data_structures.linked_list import SLL, Node


class SLLMergeSort(SLL):
    @staticmethod
    def get_middle(h):
        slow, fast = h, h.next
        while not (fast is None or fast.next is None):
            slow, fast = slow.next, fast.next.next
        return slow

    @staticmethod
    def merge(l, r):
        merged = Node(None)
        temp = merged
        while not (l is None or r is None):
            if l.k <= r.k:
                temp.next, l = l, l.next
            else:
                temp.next, r = r, r.next
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
        mid = self.get_middle(h)
        mid_next, mid.next = mid.next, None
        return self.merge(self.merge_sort(h), self.merge_sort(mid_next))

    def sort(self):
        node, sorted_list = self.merge_sort(self.head), []
        while node is not None:
            sorted_list.append(node.k)
            node = node.next
        return sorted_list
