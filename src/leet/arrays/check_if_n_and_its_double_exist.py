"""
Check If N and Its Double Exist
-------------------------------

Given an array arr of integers, check if there exists two integers N and M such that N
is the double of M ( i.e. N = 2 * M).

Complexity
==========

Time
----

checkIfExist(arr): O(n).

Space
-----

checkIfExist(arr): O(n).
"""


def sol(arr):
    double = set()
    for i in arr:
        if 2 * i in double or (i % 2 == 0 and i // 2 in double):
            return True
        double.add(i)
    return False
