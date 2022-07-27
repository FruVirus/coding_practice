"""
The Principle of Hash Table
===========================

Hash Table is a data structure which organizes data using hash functions in order to
support quick insertion and search.

The Principle of Hash Table
---------------------------

The key idea of Hash Table is to use a hash function to map keys to buckets. To be more
specific,

    1. When we insert a new key, the hash function will decide which bucket the key
should be assigned and the key will be stored in the corresponding bucket;
    2. When we want to search for a key, the hash table will use the same hash function
to find the corresponding bucket and search only in the specific bucket.

An Example
----------

1. Insertion: we parse the keys through the hash function to map them into the
corresponding bucket.
2. Search: we parse the keys through the same hash function and search only in the
specific bucket.

Keys to Design a Hash Table
===========================

There are two essential factors that you should pay attention to when you are going to
design a hash table.

1. Hash Function
----------------

The hash function is the most important component of a hash table which is used to map
the key to a specific bucket.

The hash function will depend on the range of key values and the number of buckets.

It is an open problem to design a hash function. The idea is to try to assign the key to
the bucket as uniformly as you can. Ideally, a perfect hash function will be a one-one
mapping between the key and the bucket. However, in most cases, a hash function is not
perfect and it is a tradeoff between the amount of buckets and the capacity of a bucket.

2. Collision Resolution
-----------------------

Ideally, if our hash function is a perfect one-one mapping, we will not need to handle
collisions. Unfortunately, in most cases, collisions are almost inevitable. For
instance, in our previous hash function (y = x % 5), both 1987 and 2 are assigned to
bucket 2. That is a collision.

A collision resolution algorithm should solve the following questions:

    1. How to organize the values in the same bucket?
    2. What if too many values are assigned to the same bucket?
    3. How to search for a target value in a specific bucket?

These questions are related to the capacity of the bucket and the number of keys which
might be mapped into the same bucket according to our hash function.

Let's assume that the bucket, which holds the maximum number of keys, has N keys.

Typically, if N is constant and small, we can simply use an array to store keys in the
same bucket. If N is variable or large, we might need to use height-balanced binary
search tree instead.

Complexity Analysis - Hash Table
================================

Complexity Analysis
-------------------

If there are M keys in total, we can achieve the space complexity of O(M) easily when
using a hash table.

However, you might have noticed that the time complexity of hash table has a strong
relationship with the design.

Most of us might have used an array in each bucket to store values in the same bucket.
Ideally, the bucket size is small enough to be regarded as a constant. The time
complexity of both insertion and search will be O(1).

But in the worst case, the maximum bucket size will be N. And the time complexity will
be O(1) for insertion but O(N) for search.

The Principle of Built-in Hash Table
------------------------------------

The typical design of built-in hash table is:

    1. The key value can be any hashable type. And a value which belongs to a hashable
type will have a hashcode. This code will be used in the mapping function to get the
bucket index.
    2. Each bucket contains an array to store all the values in the same bucket
initially.
    3. If there are too many values in the same bucket, these values will be maintained
in a height-balanced binary search tree instead.

The average time complexity of both insertion and search is still O(1). And the time
complexity in the worst case is O(log N) for both insertion and search by using
height-balanced BST. It is a trade-off between insertion and search.

Design the Key - Summary
========================

1. When the order of each element in the string/array doesn't matter, you can use the
sorted string/array as the key.

2. If you only care about the offset of each value, usually the offset from the first
value, you can use the offset as the key.

3. In a tree, you might want to directly use the TreeNode as key sometimes. But in most
cases, the serialization of the subtree might be a better idea.

4. In a matrix, you might want to use the row index or the column index as key.

5. In a Sudoku, you can combine the row index and the column index to identify which
block this element belongs to.

6. Sometimes, in a matrix, you might want to aggregate the values in the same diagonal
line.
"""
