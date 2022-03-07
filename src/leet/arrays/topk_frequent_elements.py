"""
Top K Frequent Elements
-----------------------

Given an integer array nums and an integer k, return the k most frequent elements. You
may return the answer in any order.

Complexity
==========

Time
----

topKFrequent(nums, k): O(n).

Space
-----

topKFrequent(nums, k): O(n).
"""

# Standard Library
from collections import Counter


def sol(nums, k):
    b = [[] for _ in range(len(nums) + 1)]
    for num, freq in Counter(nums).items():
        b[freq].append(num)
    flat = [item for sublist in b for item in sublist]
    return flat[len(flat) - k :]
