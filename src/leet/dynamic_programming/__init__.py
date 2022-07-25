"""
What is Dynamic Programming?
============================

Dynamic Programming (DP) is a programming paradigm that can systematically and
efficiently explore all possible solutions to a problem. As such, it is capable of
solving a wide variety of problems that often have the following characteristics:

    1. The problem can be broken down into "overlapping subproblems" - smaller versions
of the original problem that are re-used multiple times.
    2. The problem has an "optimal substructure" - an optimal solution can be formed
from optimal solutions to the overlapping subproblems of the original problem.

As a beginner, these theoretical definitions may be hard to wrap your head around. Don't
worry though - at the end of this chapter, we'll talk about how to practically spot when
DP is applicable. For now, let's look a little deeper at both characteristics.

These attributes may seem familiar to you. Greedy problems have optimal substructure,
but not overlapping subproblems. Divide and conquer algorithms break a problem into
subproblems, but these subproblems are not overlapping (which is why DP and divide and
conquer are commonly mistaken for one another).

Dynamic programming is a powerful tool because it can break a complex problem into
manageable subproblems, avoid unnecessary recalculation of overlapping subproblems, and
use the results of those subproblems to solve the initial complex problem. DP not only
aids us in solving complex problems, but it also greatly improves the time complexity
compared to brute force solutions. For example, the brute force solution for calculating
the Fibonacci sequence has exponential time complexity, while the dynamic programming
solution will have linear time complexity because it reuses the results of subproblems
rather than recalculating the results for previously seen subproblems.

Top-down and Bottom-up
======================

There are two ways to implement a DP algorithm:

1. Bottom-up, also known as tabulation.
2. Top-down, also known as memoization.

Bottom-up (Tabulation)
----------------------

Bottom-up is implemented with iteration and starts at the base cases.

Top-down (Memoization)
----------------------

Top-down is implemented with recursion and made efficient with memoization.

    memoizing a result means to store the result of a function call, usually in a
hashmap or an array, so that when the same function call is made again, we can simply
return the memoized result instead of recalculating the result.

Which is better?
----------------

Any DP algorithm can be implemented with either method, and there are reasons for
choosing either over the other. However, each method has one main advantage that stands
out:

    - A bottom-up implementation's runtime is usually faster, as iteration does not have
the overhead that recursion does.
    - A top-down implementation is usually much easier to write. This is because with
recursion, the ordering of subproblems does not matter, whereas with tabulation, we need
to go through a logical ordering of solving subproblems.

When to Use DP
==============

When it comes to solving an algorithm problem, especially in a high-pressure scenario
such as an interview, half the battle is figuring out how to even approach the problem.
In the first section, we defined what makes a problem a good candidate for dynamic
programming. Recall:

    1. The problem can be broken down into "overlapping subproblems" - smaller versions
of the original problem that are re-used multiple times
    2. The problem has an "optimal substructure" - an optimal solution can be formed
from optimal solutions to the overlapping subproblems of the original problem

Unfortunately, it is hard to identify when a problem fits into these definitions.
Instead, let's discuss some common characteristics of DP problems that are easy to
identify.

The first characteristic that is common in DP problems is that the problem will ask for
the optimum value (maximum or minimum) of something, or the number of ways there are to
do something. For example:

    - What is the minimum cost of doing...
    - What is the maximum profit from...
    - How many ways are there to do...
    - What is the longest possible...
    - Is it possible to reach a certain point...

    Note: Not all DP problems follow this format, and not all problems that follow these
formats should be solved using DP. However, these formats are very common for DP
problems and are generally a hint that you should consider using dynamic programming.

When it comes to identifying if a problem should be solved with DP, this first
characteristic is not sufficient. Sometimes, a problem in this format (asking for the
max/min/longest etc.) is meant to be solved with a greedy algorithm. The next
characteristic will help us determine whether a problem should be solved using a greedy
algorithm or dynamic programming.

The second characteristic that is common in DP problems is that future "decisions"
depend on earlier decisions. Deciding to do something at one step may affect the ability
to do something in a later step. This characteristic is what makes a greedy algorithm
invalid for a DP problem - we need to factor in results from previous decisions.
Admittedly, this characteristic is not as well defined as the first one, and the best
way to identify it is to go through some examples.

When you're solving a problem on your own and trying to decide if the second
characteristic is applicable, assume it isn't, then try to think of a counterexample
that proves a greedy algorithm won't work. If you can think of an example where earlier
decisions affect future decisions, then DP is applicable.

To summarize: if a problem is asking for the maximum/minimum/longest/shortest of
something, the number of ways to do something, or if it is possible to reach a certain
point, it is probably greedy or DP. With time and practice, it will become easier to
identify which is the better approach for a given problem. Although, in general, if the
problem has constraints that cause decisions to affect other decisions, such as using
one element prevents the usage of other elements, then we should consider using dynamic
programming to solve the problem. These two characteristics can be used to identify if a
problem should be solved with DP.

Framework for DP Problems
=========================

Now that we understand the basics of DP and how to spot when DP is applicable to a
problem, we've reached the most important part: actually solving the problem. In this
section, we're going to talk about a framework for solving DP problems. This framework
is applicable to nearly every DP problem and provides a clear step-by-step approach to
developing DP algorithms.

    For this article's explanation, we're going to use the problem Climbing Stairs as an
example, with a top-down (recursive) implementation.

Before we start, we need to first define a term: state. In a DP problem, a state is a
set of variables that can sufficiently describe a scenario. These variables are called
state variables, and we only care about relevant ones. For example, to describe every
scenario in Climbing Stairs, there is only 1 relevant state variable, the current step
we are on. We can denote this with an integer i. If i = 6, that means that we are
describing the state of being on the 6th step. Every unique value of i represents a
unique state.

    You might be wondering what "relevant" means here. Picture this problem in real
life: you are on a set of stairs, and you want to know how many ways there are to climb
to say, the 10th step. We're definitely interested in what step you're currently
standing on. However, we aren't interested in what color your socks are. You could
certainly include sock color as a state variable. Standing on the 8th step wearing green
socks is a different state than standing on the 8th step wearing red socks. However,
changing the color of your socks will not change the number of ways to reach the 10th
step from your current position. Thus the color of your socks is an irrelevant variable.
In terms of figuring out how many ways there are to climb the set of stairs, the only
relevant variable is what stair you are currently on.

The Framework
-------------

To solve a DP problem, we need to combine 3 things:

1. A function or data structure that will compute/contain the answer to the problem for
every given state.

    Typically, top-down is implemented with a recursive function and hash map, whereas
bottom-up is implemented with nested for loops and an array. When designing this
function or array, we also need to decide on state variables to pass as arguments.

2. A recurrence relation to transition between states.

    A recurrence relation is an equation that relates different states with each other.

3. Base cases, so that our recurrence relation doesn't go on infinitely.

    Finding the base cases is often the easiest part of solving a DP problem, and just
involves a little bit of logical thinking. When coming up with the base case(s) ask
yourself: What state(s) can I find the answer to without using dynamic programming? In

To Summarize
------------

With DP problems, we can use logical thinking to find the answer to the original problem
for certain inputs. We can then use a recurrence relation to find the answer to the
original problem for any state. Finding the recurrence relation involves thinking about
how moving from one state to another changes the answer to the problem.

Multidimensional DP
===================

The dimensions of a DP algorithm refer to the number of state variables used to define
each state.

Typically, the more dimensions a DP problem has, the more difficult it is to solve.
Two-dimensional problems are common, and sometimes a problem might even require five
dimensions. The good news is, the framework works regardless of the number of
dimensions.

The following are common things to look out for in DP problems that require a state
variable:

    - An index along some input. This is usually used if an input is given as an array
or string.
    - A second index along some input. Sometimes, you need two index state variables,
say i and j. In some questions, these variables represent the answer to the original
problem if you considered the input starting at index i and ending at index j.
    - Explicit numerical constraints given in the problem. For example, "you are only
allowed to complete k transactions", or "you are allowed to break up to k obstacles",
etc.
    - Variables that describe statuses in a given state. For example "true if currently
holding a key, false if not", "currently holding k packages" etc.
    - Some sort of data like a tuple or bitmask used to indicate things being "visited"
or "used". For example, "bitmask is a mask where the ith bit indicates if the ith city
has been visited". Note that mutable data structures like arrays cannot be used -
typically, only immutable data structures like numbers and strings can be hashed, and
therefore memoized.

Time and Space Complexity
=========================

Finding the time and space complexity of a dynamic programming algorithm may sound like
a daunting task. However, this task is usually not as difficult as it sounds.
Furthermore, justifying the time and space complexity in an explanation is relatively
simple as well. One of the main points with DP is that we never repeat calculations,
whether by tabulation or memoization, we only compute a state once. Because of this, the
time complexity of a DP algorithm is directly tied to the number of possible states.

If computing each state requires F time, and there are n possible states, then the time
complexity of a DP algorithm is O(n * F). With all the problems we have looked at so
far, computing a state has just been using a recurrence relation equation, which is
O(1). Therefore, the time complexity has just been equal to the number of states. To
find the number of states, look at each of your state variables, compute the number of
values each one can represent, and then multiply all these numbers together.

Let's say we had 3 state variables: i, k, and holding for some made up problem. i is an
integer used to keep track of an index for an input array nums, k is an integer given in
the input which represents the maximum actions we can do, and holding is a boolean
variable. What will the time complexity be for a DP algorithm that solves this problem?
Let n = nums.length and K be the maximum actions possible given in the input. i can be
from 0 to nums.length, k can be from 0 to K, and holding }can be true or false.
Therefore, there are n * K * 2 states. If computing each state is O(1), then the time
complexity will be O(n * K).

Whenever we compute a state, we also store it so that we can refer to it in the future.
In bottom-up, we tabulate the results, and in top-down, states are memoized. Since we
store states, the space complexity is equal to the number of states. That means that in
problems where calculating a state is O(1), the time and space complexity are the same.

Iteration in the recurrence relation
====================================

In all the problems we have looked at so far, the recurrence relation is a static
equation - it never changes.

What if the question was rephrased so that we could take up to k steps at a time? The
recurrence relation would become dynamic - it would be:

dp(i)=min(dp(j) + cost[j]) for all (i - k)≤j<i

We would need iteration in our recurrence relation.

While iteration usually increases the difficulty of a DP problem, particularly with
bottom-up implementations, the idea isn't too complicated. Instead of choosing from a
static number of options, we usually add a for-loop to iterate through a dynamic number
of options and choose the best one.

State Transition by Inaction
============================

This is a small pattern that occasionally shows up in DP problems. Here, "doing nothing"
refers to two different states having the same value. We're calling it "doing nothing"
because often the way we arrive at a new state with the same value as the previous state
is by "doing nothing". Of course, a decision making process needs to coexist with this
pattern, because if we just had all states having the same value, the problem wouldn't
really make sense. It is just that if we are trying to maximize or minimize a score for
example, sometimes the best option is to "do nothing", which leads to two states having
the same value.

Usually when we "do nothing", it is by moving to the next element in some input array.
As mentioned above, this will be part of a decision making process due to some
restriction in the problem. For example, think back to House Robber: we could choose to
rob or not rob each house we were at. Sometimes, not robbing the house is the best
decision (because we aren't allowed to rob adjacent houses), then dp(i) = dp(i - 1).

State Reduction
===============

In an earlier chapter when we used the framework to solve Maximum Score from Performing
Multiplication Operations, we mentioned that we could use 2 state variables instead of 3
because we could derive the information the 3rd one would have given us from the other
2. By doing this, we greatly reduced the number of states (as we learned earlier, the
number of states is the product of the number of values each state variable can take).
In most cases, reducing the number of states will reduce the time and space complexity
of the algorithm.

This is called state reduction, and it is applicable for many DP problems, including a
few that we have already looked at. State reduction usually comes from a clever trick or
observation. Sometimes, as is in the case of Maximum Score from Performing
Multiplication Operations, state reduction can result in lower time and space
complexity. Other times, only the space complexity will be improved while the time
complexity remains the same.

State reduction can also be achieved in the recurrence relation. Recall when we looked
at House Robber. Only one state variable was used, i, which indicates what house we are
currently at.

    Note: state reductions for space complexity usually only apply to bottom-up
implementations, while improving time complexity by reducing the number of state
variables applies to both implementations.

Another common scenario where we can improve space complexity is when the recurrence
relation is static (no iteration) along one dimension.

    Whenever you notice that values calculated by a DP algorithm are only reused a few
times and then never used again, try to see if you can save on space by replacing an
array with some variables. A good first step for this is to look at the recurrence
relation to see what previous states are used. For example, in Fibonacci, we only refer
to the previous two states, so all results before n - 2 can be discarded.

Counting DP
===========

Most of the problems we have looked at in earlier chapters ask for either the maximum,
minimum, or longest of something. However, it is also very common for a DP problem to
ask for the number of distinct ways to do something. In fact, one of the first examples
we looked at did this - recall that Climbing Stairs asked us to find the number of ways
to climb to the top of the stairs.

Another term used to describe this class of problems is "counting DP".

What are the differences with counting DP? With the maximum/minimum problems, the
recurrence relation typically involves a max() or min() function. This is true for all
types of problems we have looked at - iteration, multi-dimensional, etc. With counting
DP, the recurrence relation typically just sums the results of multiple states together.
For example, in Climbing Stairs, the recurrence relation was
dp(i) = dp(i - 1) + dp(i - 2). There is no max() or min(), just addition.

Another difference is in the base cases. In most of the problems we have looked at, if
the state goes out of bounds, the base case equals 0. For example, in the Best Time to
Buy and Sell Stock questions, when we ran out of transactions or ran out of days to
trade, we returned 0 because we can't make any more profit. In Longest Common
Subsequence, when we run out of characters for either string, we return 0 because the
longest common subsequence of any string and an empty string is 0. With counting DP, the
base cases are often not set to 0. This is because the recurrence relation usually only
involves addition terms with other states, so if the base case was set to 0 then you
would only ever add 0 to itself. Finding these base cases involves some logical
thinking - for example, when we looked at Climbing Stairs - we reasoned that there is 1
way to climb to the first step and 2 ways to climb to the second step.

Kadane's Algorithm
==================

Kadane's Algorithm is an algorithm that can find the maximum sum subarray given an array
of numbers in O(n) time and O(1) space. Its implementation is a very simple example of
dynamic programming, and the efficiency of the algorithm allows it to be a powerful tool
in some DP algorithms.

Kadane's Algorithm involves iterating through the array using an integer variable
current, and at each index i, determines if elements before index i are "worth" keeping,
or if they should be "discarded". The algorithm is only useful when the array can
contain negative numbers. If current becomes negative, it is reset, and we start
considering a new subarray starting at the current index.

Pathing Problems
================

The last pattern we'll be looking at is pathing problems on a matrix. These problems
have matrices as part of the input and give rules for "moving" through the matrix in the
problem description. Typically, DP will be applicable when the allowed movement is
constrained in a way that prevents moving "backwards", for example if we are only
allowed to move down and right.
"""
