"""
Top K Frequent Elements
-----------------------

Given an integer array nums and an integer k, return the k most frequent elements. You
may return the answer in any order.

Intuition
---------

The idea behind using bucket sort is that no element in nums can have a frequency more
than n. Thus, they can be put into buckets according to their frequencies (-1 due to
0-indexing).

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
    b = [[] for _ in range(len(nums))]
    for num, freq in Counter(nums).items():
        b[freq - 1].append(num)
    flat = [item for sublist in b for item in sublist]
    return flat[len(flat) - k :]
