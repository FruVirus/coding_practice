"""
Rotate List
-----------

Given the head of a linked list, rotate the list to the right by k places.

Complexity
==========

Time
----

rotateRight(head, k): O(n).

Space
-----

rotateRight(head, k): O(1).
"""


def sol(head, k):
    if not (head and head.next) or k == 0:
        return head
    count, old_tail = 1, head
    while old_tail.next:
        count, old_tail = count + 1, old_tail.next
    k %= count
    old_tail.next, new_tail = head, head
    for _ in range(count - k - 1):
        new_tail = new_tail.next
    head, new_tail.next = new_tail.next, None
    return head
