"""
Palindrome Linked List
----------------------

Given the head of a singly linked list, return true if it is a palindrome.

Complexity
==========

Time
----

is_palindrome(): O(n).

Space
-----

is_palindrome(): O(1).
"""


def is_palindrome(head):
    curr, fast, temp = head, head.next, None
    while fast and fast.next:
        curr, temp = reverse(curr, temp)
        fast = fast.next.next
    curr, head = (curr.next, temp) if not fast else reverse(curr, temp)
    while head:
        if head.val != curr.val:
            return False
        head, curr = head.next, curr.next
    return True


def reverse(curr, temp):
    next, curr.next = curr.next, temp
    curr, temp = next, curr
    return curr, temp
