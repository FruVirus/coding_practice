"""
Odd Even Linked List
--------------------

Given the head of a singly linked list, group all the nodes with odd indices together
followed by the nodes with even indices, and return the reordered list.

The first node is considered odd, and the second node is even, and so on.

Note that the relative order inside both the even and odd groups should remain as it was
in the input.

You must solve the problem in O(1) extra space complexity and O(n) time complexity.

Complexity
==========

Time
----

oddEvenList(head): O(n).

Space
-----

oddEvenList(head): O(1).
"""


def sol(head):
    if not head:
        return None
    odd, even, even_start = head, head.next, head.next
    while even and even.next:
        odd.next, even.next = odd.next.next, even.next.next
        odd, even = odd.next, even.next
    odd.next = even_start
    return head
