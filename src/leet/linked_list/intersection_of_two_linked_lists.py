"""
Intersection of Two Linked Lists
--------------------------------

Given the heads of two singly linked-lists headA and headB, return the node at which the
two lists intersect. If the two linked lists have no intersection at all, return null.

Complexity
==========

Time
----

intersect(): O(n + m).

Space
-----

intersect(): O(1).
"""


def intersect(heada, headb):
    starta, startb = heada, headb
    while starta is not startb:
        starta = headb if not starta else starta.next
        startb = heada if not startb else startb.next
    return starta
