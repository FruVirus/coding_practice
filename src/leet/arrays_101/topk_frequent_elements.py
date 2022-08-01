"""
Top K Frequent Elements
-----------------------

Given an integer array nums and an integer k, return the k most frequent elements. You
may return the answer in any order.

Intuition
---------

Bucket Sort

The idea behind using bucket sort is that no element in nums can have a frequency more
than n. Thus, they can be put into buckets according to their frequencies (-1 due to
0-indexing).

Quick Select

The approach is the same as for quicksort. One chooses a pivot and defines its position
in a sorted array in a linear time using so-called partition algorithm.

As an output, we have an array where the pivot is on its perfect position in the
ascending sorted array, sorted by the frequency. All elements on the left of the pivot
are less frequent than the pivot, and all elements on the right are more frequent or
have the same frequency.

Hence the array is now split into two parts. If by chance our pivot element took N - kth
final position, then k elements on the right are these top k frequent we're looking for.
If not, we can choose one more pivot and place it in its perfect position.


Complexity
==========

Time
----

topKFrequent_one(nums, k): O(n).
topKFrequent_two(nums, k): O(n) expected, O(n^2) worst case.

Space
-----

topKFrequent_one(nums, k) and topKFrequent_two(nums, k): O(n).
"""

# Standard Library
from collections import Counter


def sol_one(nums, k):
    b = [[] for _ in range(len(nums))]
    for num, freq in Counter(nums).items():
        b[freq - 1].append(num)
    flat = [item for sublist in b for item in sublist]
    return flat[len(flat) - k :]
