"""
Introduction to Array
=====================

An array is a basic data structure to store a collection of elements sequentially. But
elements can be accessed randomly since each element in the array can be identified by
an array index.

An array can have one or more dimensions.

Introduction to Dynamic Array
=============================

An array has a fixed capacity and we need to specify the size of the array when we
initialize it. Sometimes this will be somewhat inconvenient and wasteful.

Therefore, most programming languages offer built-in dynamic array which is still a
random access list data structure but with variable size. For example, we have vector in
C++ and ArrayList in Java.

Introduction to 2D Array
========================

Similar to a one-dimensional array, a two-dimensional array also consists of a sequence
of elements. But the elements can be laid out in a rectangular grid rather than a line.

Principle
---------

In some languages, the multidimensional array is actually implemented internally as a
one-dimensional array while in some other languages, there is actually no
multidimensional array at all.

Dynamic 2D Array
----------------

Similar to the one-dimensional dynamic array, we can also define a dynamic
two-dimensional array. Actually, it can be just a nested dynamic array.

Introduction to String
======================

A string is actually an array of unicode characters. You can perform almost all the
operations we used in an array.

However, there are some differences. In this article, we will go through some of them
which you should be aware of when dealing with a string. These features might vary a lot
from one language to another.

Compare Function
----------------

String has its own compare function

However, there is a problem:

    Can we use "==" to compare two strings?

It depends on the answer to the question:

    Does the language support operator overloading?

1. If the answer is yes (like C++), we may use "==" to compare two strings.
2. If the answer is no (like Java), we may not use "==" to compare two strings. When we
use "==", it actually compares whether these two objects are the same object.

Immutable or Mutable
--------------------

Immutable means that you can't change the content of the string once it's initialized.

1. In some languages (like C++), the string is mutable. That is to say, you can modify
the string just like what you did in an array.

2. In some other languages (like Java), the string is immutable. This feature will bring
several problems. We will illustrate the problems and solutions in the next article.

You can determine whether the string in your favorite language is immutable or mutable
by testing the modification operation.

Extra Operations
----------------

You should be aware of the time complexity of these built-in operations.

For instance, if the length of the string is N, the time complexity of both finding
operation and substring operation is O(N).

Also, in languages which the string is immutable, you should be careful with the
concatenation operation (we will explain this in next article as well).

Never forget to take the time complexity of built-in operations into consideration when
you compute the time complexity for your solution.

Immutable String - Problems & Solutions
=======================================

You should know whether the string in your favorite language is immutable or not in the
previous article. If the string is immutable, it will bring some problems. Hopefully, we
will also provide the solution at the end.

Modification Operation
----------------------

Obviously, an immutable string cannot be modified. If you want to modify just one of the
characters, you have to create a new string.

Beware of String Concatenation in Java
--------------------------------------

You should be very careful with string concatenation. Let's look at an example when we
do string concatenation repeatedly in a for loop:

Notice how slow string concatenation is for Java? On the other hand, there is no
noticeable performance impact in C++.

In Java, since the string is immutable, concatenation works by first allocating enough
space for the new string, copy the contents from the old string and append to the new
string.

Therefore, the time complexity in total will bes O(n^2).

Two-pointer Technique - Scenario I
==================================

In the previous chapter, we solve some problems by iterating the array. Typically, we
only use one pointer starting from the first element and ending at the last one to do
iteration. However, sometimes, we might need to use two pointers at the same time to do
the iteration.

An Example
----------

Let's start with a classic problem:

    Reverse the elements in an array.

The idea is to swap the first element with the end, advance to the next element and
swapping repeatedly until it reaches the middle position.

We can use two pointers at the same time to do the iteration: one starts from the first
element and another starts from the last element. Continue swapping the elements until
the two pointers meet each other.

Summary
-------

To summarize, one of the typical scenarios to use two-pointer technique is that you want
to

    Iterate the array from two ends to the middle.

So you can use the two-pointer technique:

    One pointer starts from the beginning while the other pointer starts from the end.

And it is worth noting that this technique is often used in a sorted array.

Two-pointer Technique - Scenario II
-----------------------------------

Sometimes, we can use two pointers with different steps to solve problems.

An Example
----------

Let's start with another classic problem:

    Given an array and a value, remove all instances of that value in-place and return
the new length.

If we don't have the limitation of space complexity, it will be easier. We can
initialize a new array to store the answer. Iterate the original array and add the
element to the new array if the element is not equal to the given target value.

Actually, it is equivalent to using two pointers, one is used for the iteration of the
original array and another one always points at the last position of the new array.

Reconsider the Space Limitation
-------------------------------

Now let's reconsider the space limitation.

We can use a similar strategy. We still use two pointers: one is still used for the
iteration while the second one always points at the position for next addition.

We use two pointers, one faster-runner i and one slower-runner k, in the example above.
i moves one step each time while k moves one step only if a new needed value is added.

Summary
-------

This is a very common scenario of using the two-pointer technique when you need:

    One slow-runner and one fast-runner at the same time.

The key to solving this kind of problems is to

    Determine the movement strategy for both pointers.

Similar to the previous scenario, you might sometimes need to sort the array before
using the two-pointer technique. And you might need a greedy thought to determine your
movement strategy.

Array-related Techniques
========================

There are more array-related data structures or techniques you might want to know. We
will not go deeper into most of the concepts in this card but provide the links to the
corresponding card in this article.

1. There are some other data structures which are similar to the array but have some
different properties:

- String (has been introduced in this card)
- Hash Table
- Linked List
- Queue
- Stack

2. As we mentioned, we can call the built-in function to sort an array. But it is useful
to understand the principle of some widely-used sorting algorithms and their complexity.

3. Binary search is also an important technique used to search a specific element in a
sorted array.

4. We have introduced two-pointer technique in this chapter. It is not easy to use this
technique flexibly. This technique can also be used to solve:

    - Slow-pointer and fast-pointer problem in Linked List
    - Sliding Window Problem

5. The two-pointer technique sometimes will relate to Greedy Algorithm which helps us
design our pointers' movement strategy.
"""
