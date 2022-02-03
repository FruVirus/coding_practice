"""
2.1 Insertion sort
==================

Insertion sort is an efficient algorithm for sorting a small number of elements.
Insertion sort works the way many people sort a hand of playing cards. We start with an
empty left hand and the cards face down on the table. We then remove one card at a time
from the table and insert it into the correct position in the left hand. To find the
correct position for a card, we compare it with each of the cards already in the hand,
from right to left. At all times, the cards held in the left hand are sorted, and these
cards were originally the top cards of the pile on the table.

The algorithm sorts the input numbers in place: it rearranges the numbers within the
array A, with at most a constant number of them stored outside the array at any time.
The input array A contains the sorted output sequence when the insertion sort procedure
is finished.

We iterate over each item in the array in the for-loop, beginning with the second item
in the array. In the while-loop, we compare each previous item in the array with the
current item. If the previous item is smaller than the current item, then we perform a
swap of the two items and decrement the index position of the previous item. By swapping
and decrementing the index position of the previous item, we continuously move the i-th
item in a to its correctly sorted position.

NB: Even if we use binary search to find each insertion point, the complexity is still
O(n^2). While binary insertion sorting improves the time it takes to find the right
position for the next element being inserted, it may still take O(n) time to perform the
swaps necessary to shift it into place.

Insertion sort is stable.

Complexity
==========

Time
----

insertion_sort(): Theta(n^2), Theta(n) if array is already sorted.
"""


def insertion_sort(a):
    for i in range(1, len(a)):
        j, temp = i - 1, a[i]
        while j > -1 and a[j] > temp:
            a[j + 1] = a[j]
            j -= 1
        a[j + 1] = temp
