"""
Merge k Sorted Lists
--------------------

You are given an array of k linked-lists lists, each linked-list is sorted in ascending
order.

Merge all the linked-lists into one sorted linked-list and return it.

Intuition
---------

We could, in theory, convert merge k lists problem to merge 2 lists (k - 1) times. This
would work but runs into TLE.

Instead, we can pair up k lists and merge each pair using merge sort.

Complexity
==========

Time
----

mergeKLists(lists): O(n * log k).

Space
-----

mergeKLists(lists): O(1).
"""


class Node:
    def __init__(self, val=0, next=None):
        self.val, self.next = val, next


def sol(lists):
    interval, n = 1, len(lists)
    while interval < n:
        for i in range(0, n - interval, 2 * interval):
            lists[i] = merge(lists[i], lists[i + interval])
        interval *= 2
    return lists[0] if n > 0 else None


def merge(l1, l2):
    merged = Node()
    temp = merged
    while l1 and l2:
        if l1.val <= l2.val:
            temp.next, l1 = l1, l1.next
        else:
            temp.next, l2 = l2, l2.next
        temp = temp.next
    temp.next = l1 or l2
    return merged.next
