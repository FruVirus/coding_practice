"""
What Is an Array?
=================

An Array is a collection of items. The items could be integers, strings, DVDs, games,
books—anything really. The items are stored in neighboring (contiguous) memory
locations. Because they're stored together, checking through the entire collection of
items is straightforward.

Creating an Array
-----------------

On a computer, Arrays can hold up to N items. The value of N is decided by you, the
programmer, at the time you create the Array. Additionally, you also need to specify the
type of item that will be going into the Array.

Accessing Elements in Arrays
============================

The two most primitive Array operations are writing elements into them, and reading
elements from them. All other Array operations are built on top of these two primitive
operations.

Writing Items into an Array
---------------------------

To put a DVD into the Array, we need to decide which of the 15 places we'd like it to go
in. Each of the places is identified using a number in the range of 0 to N - 1. The 1st
place is 0, the 2nd place is 1, the 3rd place is 2... all the way up to the 15th place,
which is 14. We call these numbers that identify each place indexes.

Reading Items from an Array
---------------------------

We can check what's at a particular Array index.

Writing Items into an Array with a Loop
---------------------------------------

We commonly use a loop to put lots of values into an Array.

Reading Items from an Array with a Loop
---------------------------------------

We can also use a loop to print out everything that's in the Array.

Array Capacity VS Length
========================

    If somebody asks you how long the DVD Array is, what would your answer be?

There are two different answers you might have given.

1. The number of DVDs the box could hold, if it was full, or
2. The number of DVDs currently in the box.

Both answers are correct, and both have very different meanings! It's important to
understand the difference between them, and use them correctly. We call the first one
the capacity of the Array, and the second one the length of the Array.

Basic Array Operations
======================

Now that we have a fairly good understanding of what an Array actually is, and how it is
stored inside the computer's physical memory, the next important thing to look at is all
the operations that Arrays support. An Array is a data structure, which means that it
stores data in a specific format and supports certain operations on the data it stores.
Consider the DVD inventory management software from the introduction section. Let's look
at some operations you might want to perform using this software:

- Insert a new DVD into the collection at a specific location.
- Delete a DVD from the existing collection if it doesn't make sense to keep it in the
inventory anymore.
- Search for a particular DVD in the collection. This is one of the most commonly
executed operation on our collection, because our inventory management software would be
used hundreds of times a day to look for a particular DVD asked for by the user.

Array Insertions
================

In the previous chapter, we looked at how to write elements to an Array. There is a lot
more to inserting elements though, as we're about to see!

Inserting a new element into an Array can take many forms:

1. Inserting a new element at the end of the Array.
2. Inserting a new element at the beginning of the Array.
3. Inserting a new element at any given index inside the Array.

Inserting at the End of an Array
--------------------------------

At any point in time, we know the index of the last element of the Array, as we've kept
track of it in our length variable. All we need to do for inserting an element at the
end is to assign the new element to one index past the current last element.

Inserting at the Start of an Array
----------------------------------

To insert an element at the start of an Array, we'll need to shift all other elements in
the Array to the right by one index to create space for the new element. This is a very
costly operation, since each of the existing elements has to be shifted one step to the
right. The need to shift everything implies that this is not a constant time operation.
In fact, the time taken for insertion at the beginning of an Array will be proportional
to the length of the Array. In terms of time complexity analysis, this is a linear time
complexity: O(N), where N is the length of the Array.

Inserting Anywhere in the Array
-------------------------------

Similarly, for inserting at any given index, we first need to shift all the elements
from that index onwards one position to the right. Once the space is created for the new
element, we proceed with the insertion. If you think about it, insertion at the
beginning is basically a special case of inserting an element at a given index—in that
case, the given index was 0.

Again, this is also a costly operation since we could potentially have to shift almost
all the other elements to the right before actually inserting the new element. As you
saw above, shifting lots of elements one place to the right adds to the time complexity
of the insertion task.

Array Deletions
===============

Now that we know how insertion works, it's time to look at its complement—deletion!

Deletion in an Array works in a very similar manner to insertion, and has the same three
different cases:

1. Deleting the last element of the Array.
2. Deleting the first element of the Array.
3. Deletion at any given index.

Deleting From the End of an Array
---------------------------------

Deletion at the end of an Array is similar to people standing in a line, also known as a
queue. The person who most recently joined the queue (at the end) can leave at any time
without disturbing the rest of the queue. Deleting from the end of an Array is the least
time consuming of the three cases. Recall that insertion at the end of an Array was also
the least time-consuming case for insertion.

Deleting From the Start of an Array
-----------------------------------

Next comes the costliest of all deletion operations for an Array—deleting the first
element. If we want to delete the first element of the Array, that will create a vacant
spot at the 0th index. To fill that spot, we will shift the element at index 1 one step
to the left. Going by the ripple effect, every element all the way to the last one will
be shifted one place to the left. This shift of elements takes O(N) time, where N is the
number of elements in the Array.

Deleting From Anywhere in the Array
-----------------------------------

For deletion at any given index, the empty space created by the deleted item will need
to be filled. Each of the elements to the right of the index we're deleting at will get
shifted to the left by one. Deleting the first element of an Array is a special case of
deletion at a given index, where the index is 0. This shift of elements takes O(K) time
where K is the number of elements to the right of the given index. Since potentially
K = N, we say that the time complexity of this operation is also O(N).

Search in an Array
==================

Finally, we're going to look at the most important operation of all. More often than
not, it comes down to the speed of searching for an element in a data structure that
helps programmers make design choices for their codebases.

There's more than one way of searching an Array, but for now, we're going to focus on
the simplest way. Searching means to find an occurrence of a particular element in the
Array and return its position. We might need to search an Array to find out whether or
not an element is present in the Array. We might also want to search an Array that is
arranged in a specific fashion to determine which index to insert a new element at.

If we know the index in the Array that may contain the element we're looking for, then
the search becomes a constant time operation—we simply go to the given index and check
whether or not the element is there.

Linear Search
-------------

If the index is not known, which is the case most of the time, then we can check every
element in the Array. We continue checking elements until we find the element we're
looking for, or we reach the end of the Array. This technique for finding an element by
checking through all elements one by one is known as the linear search algorithm. In the
worst case, a linear search ends up checking the entire Array. Therefore, the time
complexity for a linear search is O(N).

Binary Search
-------------

There is another way of searching an Array. If the elements in the Array are in sorted
order, then we can use binary search. Binary search is where we repeatedly look at the
middle element in the Array, and determine whether the element we're looking for must be
to the left, or to the right. Each time we do this, we're able to halve the number of
elements we still need to search, making binary search a lot faster than linear search!

The downside of binary search though is that it only works if the data is sorted. If we
only need to perform a single search, then it's faster to just do a linear search, as it
takes longer to sort than to linear search. If we're going to be performing a lot of
searches, it is often worth sorting the data first so that we can use binary search for
the repeated searches.

In-Place Array Operations Introduction
======================================

In programming interviews, the interviewer often expects you to minimise the time and
space complexity of your implementation. In-place Array operations help to reduce space
complexity, and so are a class of techniques that pretty much everybody encounters
regularly in interviews.

So, what are in-place array operations?

The best way of answering this question is to look at an example.

    Given an Array of integers, return an Array where every element at an even-indexed
position is squared.

An important difference for in-place vs not in-place is that in-place modifies the input
Array. This means that other functions can no longer access the original data, because
it has been overwritten.

A Better Repeated Deletion Algorithm - Intro
============================================

Let's look at one more example. This time, the result Array is smaller than the input
Array! How's this going to work? Let's find out! Here's the problem description:

    Given a sorted array, remove the duplicates such that each element appears only
once.

A Better Repeated Deletion Algorithm - Answer
=============================================

When to Use In-Place Array Operations
-------------------------------------

It's important to know when to use in-place Array operations—they might not always be
the way to go.

For example, if we'll need the original array values again later, then we shouldn't be
overwriting them. In these cases, it's best to create a copy to work with, or to simply
not use in-place techniques. It's important to be very careful when working with
existing code that somebody else has written. If other code is depending on the original
Array to work, then you might completely break the program if you modify that Array!

In-place operations are valuable when appropriate because they reduce the space
complexity of an algorithm. Instead of requiring O(N) space, we can reduce it down to
O(1).
"""
