"""
Palindrome Linked List
----------------------

Given the head of a singly linked list, return true if it is a palindrome.

Intuition
---------

1. Reverse the first half of the list.
2. Get the point to the start of the second half of the list.
3. Compare elements between the reversed first half and the second half one by one.

Complexity
==========

Time
----

isPalindrome(head): O(n).

Space
-----

isPalindrome(head): O(1).
"""


def sol(head):
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
