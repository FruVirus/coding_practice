"""
Overview
========

The idea is simple: we first find the pointer to the last node in the doubly linked list
(i.e., the node whose next attribute is None initially). Once we have a pointer to the
last node, we can recursively sort the linked list using pointers to the first and last
nodes of a linked list, similar to quicksort on arrays where we pass the indices of the
first and last array elements. The partition function for a linked list is also similar
to the partition function for arrays. Instead of returning the index of the pivot
element, we return a pointer to the pivot element. In the following implementation,
sort() is just a wrapper function --> the main recursive function is quicksort() which
is similar to quicksort() for arrays.

Quicksort can be implemented for linked Lists only when we can pick a fixed point as the
pivot (e.g., the last element). Random QuickSort cannot be efficiently implemented for
linked lists.

NB: In partition(), we don't actually need to explicitly change the prev and next
attributes of any node in the doubly linked list, just the k attribute corresponding to
the node keys.

For example, if we have:

1 -> 4 -> 16 -> 9

then, 16.prev = 4, 16.next = 9, 9.prev = 16, and 9.next = None. If we just change the k
attribute of node 16 to 9 and change the k attribute of node 9 to 16, then we have:

1 -> 4 -> 9 -> 16

and 9.prev = 4, 9.next = 16, and 16.prev = 9 and 16.next = None.

NB: In partition(), i = low if i is None else i.next is equivalent to i += 1 in the
array version. If i = low.prev is None, then this means that low was the first element
in the doubly linked list (i.e., the node whose prev attribute is None initially) and
thus, the next value of i should be low. Otherwise, the next value of i should be
i.next which corresponds to i += 1 in the array version.

NB: In partition(), the last two lines after the while-loop can potentially exchange the
pointers to low and high in quicksort().

NB: In the array version of quicksort(), the while-loop continues if low < high. When
working with doubly linked lists, we have to deal with pointers. In order for the
statement low < high to make sense when dealing with pointers we have to ensure that:
1) high cannot be None (i.e., it still has to be a valid Node object), 2) low is not
high (i.e., low != high), and 3) low is not high.next (i.e., low is not > high). The
first condition can occur if pivot.prev is None when recursively calling quicksort().
The second condition can occur if low and high switch pointers inside of partition() and
then low = pivot.next is high inside of quicksort(). The third condition can occur if
if pivot is high after returning from partition().

Complexity
==========

Time
----

get_last(): O(n).
partition(): O(n) = O(h - l + 1).
quicksort():
    O(n^2) worst case --> when the partitioning routine produces one sub-problem with
        n - 1 elements and one with 0 elements or when the input array is already
        sorted.
    O(n * lg n) expected case --> when we can equally balance the two sides of the
        partition at every level of the recursion (only possible when we can choose the
        median value with each recursion)
"""

# Repository Library
from src.clrs.data_structures.elementary_data_structures.linked_list import DLL


class DLLQuickSort(DLL):
    def get_last(self):
        node = self.head
        while node.next is not None:
            node = node.next
        return node

    @staticmethod
    def partition(low, high):
        x, i = high.k, low.prev
        j = low
        while j is not high:
            if j.k <= x:
                i = low if i is None else i.next
                i.k, j.k = j.k, i.k
            j = j.next
        i = low if i is None else i.next
        high.k, i.k = i.k, high.k
        return i

    def quicksort(self, low, high):
        while not (high is None or low is high or low is high.next):
            pivot = self.partition(low, high)
            self.quicksort(low, pivot.prev)
            low = pivot.next

    def sort(self):
        self.quicksort(self.head, self.get_last())
        node, sorted_list = self.head, []
        while node is not None:
            sorted_list.append(node.k)
            node = node.next
        return sorted_list
