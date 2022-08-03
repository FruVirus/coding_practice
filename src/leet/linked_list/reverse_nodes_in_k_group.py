"""
Reverse Nodes in k-Group
------------------------

Given the head of a linked list, reverse the nodes of the list k at a time, and return
the modified list.

k is a positive integer and is less than or equal to the length of the linked list. If
the number of nodes is not a multiple of k then left-out nodes, in the end, should
remain as it is.

You may not alter the values in the list's nodes, only nodes themselves may be changed.

Intuition
---------

The basic idea is to make use of our reversal function for a linked list. Usually, we
start with the head of the list and keep running the reversal algorithm all the way to
the end. However, in this case, we will only process k nodes.

However, the problem statement also mentions that if there are < k nodes left in the
linked list, then we don't have to reverse them. This implies that we first need to
count k nodes before we get on with our reversal. If at any point, we find that we don't
have k nodes, then we don't reverse that portion of the linked list. Right off the bat,
this implies at least two traversals of the list overall. One for counting, and the
next, for reversals.

Recursive Approach

0. First, we see if there are at least k nodes left in the linked list. If we have k
nodes, then we reverse them.

1. The recursion starts from the head of the original linked list. The first step we do
is count k nodes and then reverse them. The remaining linked list is a linked list in
itself.

2. The recursion starts from the head of the remaining linked list. The first step we do
is count k nodes and then reverse them.

3. Once we don't have enough nodes left over, we just return the head of the remaining
linked list.

Iterative Approach

In addition to the "head" and "rev_head" variables from before, we need to know the
"tail" node of the previous set of k nodes as well. The recursive approach reverses k
nodes from left to right, but it establishes the connections from right to left or back
to front. In this approach we will be reversing and establishing the connections while
going from front to back.

Complexity
==========

Time
----

reverseKGroup_one(head, k) and reverseKGroup_two(head, k): O(n).

Space
-----

reverseKGroup_one(head, k): O(1).
reverseKGroup_two(head, k): O(n / k).
"""


def sol_one(head, k):
    new_head, new_tail, node = None, None, head
    while node:
        count = 0
        while count < k and node:
            count, node = count + 1, node.next
        if count == k:
            rev_head = reverse(head, k)
            if not new_head:
                new_head = rev_head
            if new_tail:
                new_tail.next = rev_head
            new_tail, head = head, node
    if new_tail:
        new_tail.next = head
    return new_head or head


def sol_two(head, k):
    count, node = 0, head
    while count < k and node:
        count, node = count + 1, node.next
    if count == k:
        rev_head = reverse(head, k)
        head.next = sol_two(node, k)
        return rev_head
    return head


def reverse(head, k):
    temp, curr = None, head
    while k:
        next, curr.next = curr.next, temp
        curr, temp = next, curr
        k -= 1
    return temp
