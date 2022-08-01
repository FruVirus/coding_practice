"""
Intersection of Two Linked Lists
--------------------------------

Given the heads of two singly linked-lists headA and headB, return the node at which the
two lists intersect. If the two linked lists have no intersection at all, return null.

Intuition
---------

In this problem, the two linked lists eventually join into one linked list if they have
an intersection. For example


A:       4 --> 1 -->
                     --> 8 --> 4 --> 5
B: 5 --> 6 --> 1 -->

Otherwise, they are just two separated linked lists.

In essence, this is similar to Floyd's cycle detection algorithm. The two pointers will
eventually meet at the same node if there is an intersection. Otherwise, they will both
end up at a null node and the loop terminates.

Complexity
==========

Time
----

getIntersectionNode(heada, headb): O(n + m).

Space
-----

getIntersectionNode(heada, headb): O(1).
"""


def sol(heada, headb):
    starta, startb = heada, headb
    while starta is not startb:
        starta = headb if not starta else starta.next
        startb = heada if not startb else startb.next
    return starta
