"""
8.4 Bucket sort
===============

Bucket sort assumes that the input is drawn from a uniform distribution and has an
average-case running time of O(n). Whereas counting sort assumes that the input consists
of integers in a small range, bucket sort assumes that the input is generated by a
random process that distributes elements uniformly and independently over the interval
[0, 1).

Bucket sort divides the interval [0, 1) into n equal-sized sub-intervals, or buckets,
and then distributes the n input numbers into the buckets. Since the inputs are
uniformly and independently distributed over [0, 1), we do not expect many numbers to
fall into each bucket. To produce the output, we simply sort the numbers in each bucket
and then go through the buckets in order, listing the elements in each.

NB: Counting sort cannot be used here since we use the keys as indices in counting sort.
In bucket sort, the keys are floating point numbers.

Bucket sort is stable if the underlying sort is stable.

Complexity
==========

Time
----

bucket_sort(): O(n)/O(n^2) average/worst case using insertion sort.

Space
-----

bucket_sort(): O(n) for the B array of buckets.
"""

# Repository Library
from src.clrs.sorting_and_order_statistics.sorting.comparison_sorting.insertion_sort import (  # noqa: E501
    insertion_sort,
)


def bucket_sort(a):
    amin, amax, num_buckets = min(a), max(a), len(a) // 5
    b, w = [[] for _ in range(num_buckets)], (amax - amin) / num_buckets
    for num in a:
        float_index = (num - amin) / w
        bucket_index = int(float_index)
        if float_index == bucket_index and num != amin:
            bucket_index -= 1
        b[bucket_index].append(num)
    i = 0
    for list_ in b:
        if list_:
            insertion_sort(list_)
            a[i : i + len(list_)], i = list_, i + len(list_)
