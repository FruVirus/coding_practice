"""
Merge Two Sorted Lists
----------------------

You are given the heads of two sorted linked lists list1 and list2.

Merge the two lists in a one sorted list. The list should be made by splicing together
the nodes of the first two lists.

Return the head of the merged linked list.

Complexity
==========

Time
----

mergeTwoLists(list1, list2): O(n + m).

Space
-----

mergeTwoLists(list1, list2): O(n + m).
"""


def sol(list1, list2):
    if not list1:
        return list2
    if not list2:
        return list1
    if list1.val < list2.val:
        list1.next = sol(list1.next, list2)
        return list1
    list2.next = sol(list1, list2.next)
    return list2
