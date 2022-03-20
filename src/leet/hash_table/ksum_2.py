"""
kSum II
-------

Given four integer arrays nums1, nums2, nums3, and nums4 all of length n, return the
number of tuples (i, j, k, l) such that:

    - 0 <= i, j, k, l < n
    - nums1[i] + nums2[j] + nums3[k] + nums4[l] == 0

Intuition
---------

Brute Force Approach

A brute force solution will be to enumerate all combinations of elements using four
nested loops, which results in O(n^4) time complexity. A faster approach is to use three
nested loops, and, for each sum a + b + c, search for a complementary value
d = -(a + b + c) in the fourth array. We can do the search in O(1) if we populate the
fourth array into a hashmap.

Building further on this idea, we can observe that if the sum is zero, then this means
a + b = -(c + d). First, we will count sums of elements a + b from the first two arrays
using a hashmap. Then, we will enumerate elements from the third and fourth arrays, and
search for a complementary sum a + b = -(c + d) in the hashmap.

kSum II Approach

After you solve 4Sum II, an interviewer can follow-up with 5Sum II, 6Sum II, and so on.
What they are really expecting is a generalized solution for k input arrays.
Fortunately, the hashmap approach can be easily extended to handle more than 4 arrays.

Above, we divided 4 arrays into two equal groups, and processed each group
independently. Same way, we will divide k arrays into two groups. For the first group,
we will have k / 2 nested loops to count sums. Another k / 2 nested loops will enumerate
arrays in the second group and search for complements.

Complexity
==========

Time
----

fourSumCount(nums1, nums2, nums3, nums4): O(n^(k / 2)). We have k / 2 nested loops to
count sums and another k / 2 nested loops to find complements. If the number of arrays
is odd, the time complexity will be O(n^((k + 1) / 2)). We will pass k / 2 arrays to
count sums and (k + 1) / 2 arrays to find complements.

Space
-----

fourSumCount(nums1, nums2, nums3, nums4): O(n^(k / 2)), for the hashmaps since there
could be up to O(n^(k / 2)) distinct keys.
"""

# Standard Library
from collections import defaultdict


def sol(nums1, nums2, nums3, nums4):
    m, lists = defaultdict(int), [nums1, nums2, nums3, nums4]

    def add_to_hash(i, total):
        if i == len(lists) // 2:
            m[total] += 1
        else:
            for num in lists[i]:
                add_to_hash(i + 1, total + num)

    def count_coms(i, com):
        if i == len(lists):
            return m[com]
        count = 0
        for num in lists[i]:
            count += count_coms(i + 1, com - num)
        return count

    def ksum_count():
        add_to_hash(0, 0)
        return count_coms(len(lists) // 2, 0)

    return ksum_count()
