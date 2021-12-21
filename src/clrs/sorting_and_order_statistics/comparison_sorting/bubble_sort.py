"""
Overview
========

Bubble sort is a popular, but inefficient, sorting algorithm. It works by repeatedly
swapping adjacent elements that are out of order.

bubble_sort() works backwards through the array N times, where N is the number of items
in the array. For each backwards pass, we compare two adjacent items in the array and
swap their places if necessary.

Complexity
==========

Time
----

bubble_sort(): O(n^2).
"""


def bubble_sort(a):
    for i in range(len(a) - 1):
        for j in range(len(a) - 1, i, -1):
            if a[j] < a[j - 1]:
                a[j], a[j - 1] = a[j - 1], a[j]
