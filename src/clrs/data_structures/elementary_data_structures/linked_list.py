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

Intuition
---------

For singly linked lists and merge sort:

Merge sort is often preferred for sorting a linked list. The slow random-access
performance of a linked list makes some other algorithms (e.g., quicksort with random
partitioning) perform poorly, and others (e.g., heapsort) completely impossible.

NB: This implementation using merge sort can be used for either singly or doubly linked
lists! This is because we only need to have the next attribute of the last node in the
linked list be None (this is true for both singly and doubly linked lists). However,
performing merge sort on a doubly linked list does not correctly order the pointers to
previous nodes in the doubly linked list. The quicksort implementation for doubly linked
lists does however.

Let the head be the first node of the linked list to be sorted and the head reference be
the pointer to head. Note that we need a reference to the head in merge_sort() as the
implementation changes next pointers to sort the linked list (instead of manipulating
the node keys), so the head node has to be changed if the key of the original head is
not the smallest value in the linked list.

merge(l, r):
    1. Take a pointer, merged, to store the merged linked list and store a dummy node in
it initially. The head of merged will be None but the pointer that is returned from
merge() (i.e., merged.next) will contain the starting node to the actual merged linked
list.
    2. Take a pointer, temp, and assign merged to it. temp is used to step through the
next pointers for merged as we construct the merger of the sub-linked lists l and r. If
we didn't have another variable to do this, then merged would contain the final node in
the merged linked list but we would have no way of accessing the first node in the
merged linked list.
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
merged.next since the first node of merged is a dummy node). In other words, we return
merged.next but the temp variable actually keeps the information on the sorted values in
merged.

For doubly linked lists and quicksort:

The idea is simple: we first find the pointer to the last node in the doubly linked list
(i.e., the node whose next attribute is None initially). Once we have a pointer to the
last node, we can recursively sort the doubly linked list using pointers to the first
and last nodes of the doubly linked list, similar to quicksort on arrays where we pass
the indices of the first and last array elements.

The partition function for a doubly linked list is also similar to the partition
function for arrays. Instead of returning the index of the pivot element, we return a
pointer to the pivot element.

Quicksort can be implemented for doubly linked lists only when we can pick a fixed point
as the pivot (e.g., the last element). Random quicksort cannot be efficiently
implemented for doubly linked lists. In particular, sorting algorithms that rely on a
previous element (e.g., quicksort, insertion sort, etc.) cannot be implemented
efficiently for singly linked lists since singly linked lists do not have a pointer to
the previous node in the list.

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

SLL:
    delete(), get_last(), get_middle(), reverse(), search(), and size(): O(n).
    insert(): O(1).
    merge(): Theta(n).
    merge_sort(): Theta(n * lg n).
DLL:
    insert(), delete(): O(1).
    partition(): O(n) = O(h - l + 1).
    reverse(): O(n).
    quicksort(): O(n^2) worst case, O(n * lg n) expected case.

Space
-----

SLL:
    merge(): O(n).
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

    def get_last(self):
        node = self.head
        while node.next is not None:
            node = node.next
        return node

    @staticmethod
    def get_middle(h):
        slow, fast = h, h.next
        while not (fast is None or fast.next is None):
            slow, fast = slow.next, fast.next.next
        return slow

    def insert(self, x):
        x.next, self.head = self.head, x

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

    def sort(self):
        if isinstance(self, DLL):
            self.quicksort(self.head, self.get_last())
            node = self.head
        else:
            node = self.merge_sort(self.head)
        sorted_list = []
        while node is not None:
            sorted_list.append(node.k)
            node = node.next
        return sorted_list


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

    def reverse(self):
        curr, temp = self.head, None
        while curr is not None:
            temp = curr.prev
            curr.prev, curr.next = curr.next, curr.prev
            curr = curr.prev
        if temp is not None:
            self.head = temp.prev
