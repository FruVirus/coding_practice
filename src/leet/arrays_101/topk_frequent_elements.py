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

1. Build a hash map element -> its frequency and convert its keys into the array unique
of unique elements. Note that elements are unique, but their frequencies are not. That
means we need a partition algorithm that works fine with duplicates.

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


def sol_two(nums, k):
    count = Counter(nums)
    unique = list(count.keys())
    n = len(unique)

    def partition(low, high, pivot_index) -> int:
        pivot_freq, i = count[unique[pivot_index]], low - 1
        unique[high], unique[pivot_index] = unique[pivot_index], unique[high]
        for j in range(low, high):
            if count[unique[j]] <= pivot_freq:
                i += 1
                unique[i], unique[j] = unique[j], unique[i]
        unique[high], unique[i + 1] = unique[i + 1], unique[high]
        return i + 1

    def quickselect(low, high, i) -> None:
        pivot = partition(low, high, random.randrange(low, high + 1))
        if i == pivot:
            return
        if i < pivot:
            return quickselect(low, pivot - 1, i)
        return quickselect(pivot + 1, high, i)

    quickselect(0, n - 1, n - k)
    return unique[n - k:]
