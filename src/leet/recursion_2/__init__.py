"""
D&C Introduction
================

Divide and conquer (D&C) is one of the most important paradigms in algorithm design and
is widely used.

    A divide-and-conquer algorithm works by recursively breaking the problem down into
two or more subproblems of the same or related type, until these subproblems become
simple enough to be solved directly. Then one combines the results of subproblems to
form the final solution.

As you can see, divide-and-conquer algorithm is naturally implemented in the form of
recursion. Another subtle difference that tells a divide-and-conquer algorithm apart
from other recursive algorithms is that we break the problem down into two or more
subproblems in the divide-and-conquer algorithm, rather than a single smaller
subproblem. The latter recursive algorithm sometimes is called decrease and conquer
instead, such as Binary Search.

There are in general three steps that one can follow in order to solve the problem in a
divide-and-conquer manner.

    1. Divide. Divide the problem S into a set of subproblems: {S_1, S_2, ... S_n},
where n >= 2, i.e. there are usually more than one subproblem.
    2. Conquer. Solve each subproblem recursively.
    3. Combine. Combine the results of each subproblem.

Backtracking
============

In this article, we introduce another paradigm called backtracking, which is also often
implemented in the form of recursion.

    Backtracking is a general algorithm for finding all (or some) solutions to some
computational problems (notably Constraint satisfaction problems or CSPs), which
incrementally builds candidates to the solution and abandons a candidate ("backtracks")
as soon as it determines that the candidate cannot lead to a valid solution.

Conceptually, one can imagine the procedure of backtracking as the tree traversal.
Starting from the root node, one sets out to search for solutions that are located at
the leaf nodes. Each intermediate node represents a partial candidate solution that
could potentially lead us to a final valid solution. At each node, we would fan out to
move one step further to the final solution, i.e. we iterate the child nodes of the
current node. Once we can determine if a certain node cannot possibly lead to a valid
solution, we abandon the current node and backtrack to its parent node to explore other
possibilities. It is due to this backtracking behaviour, the backtracking algorithms are
often much faster than the brute-force search algorithm, since it eliminates many
unnecessary exploration.

Backtracking Template
=====================

In this article, we will present you a pseudocode template that summarizes some common
patterns for the backtracking algorithms. Furthermore, we will demonstrate with some
concrete examples on how to apply the template.

Template
--------

With the N-queen example as we presented in the previous article, one might have noticed
some patterns about the backtracking algorithm. In the following, we present you a
pseudocode template, which could help you to clarify the idea and structure the code
when implementing the backtracking algorithms.

Here are a few notes about the above pseudocode.

    - Overall, the enumeration of candidates is done in two levels: 1). at the first
level, the function is implemented as recursion. At each occurrence of recursion, the
function is one step further to the final solution.  2). as the second level, within the
recursion, we have an iteration that allows us to explore all the candidates that are of
the same progress to the final solution.

    - The backtracking should happen at the level of the iteration within the recursion.

    - Unlike brute-force search, in backtracking algorithms we are often able to
determine if a partial solution candidate is worth exploring further (i.e.
is_valid(next_candidate)), which allows us to prune the search zones. This is also known
as the constraint, e.g. the attacking zone of queen in N-queen game.

    - There are two symmetric functions that allow us to mark the decision
(place(candidate)) and revert the decision (remove(candidate)).

Unfold Recursion
================

In this article, we illustrate how to convert a recursion algorithm to non-recursion
one, i.e. unfold the recursion.

Recursion could be an elegant and intuitive solution, when applied properly.
Nevertheless, sometimes, one might have to convert a recursive algorithm to iterative
one for various reasons.

Risk of Stackoverflow

    The recursion often incurs additional memory consumption on the system stack, which
is a limited resource for each program. If not used properly, the recursion algorithm
could lead to stackoverflow. One might argue that a specific type of recursion called
tail recursion could solve this problem. Unfortunately, not every recursion can be
converted to tail recursion, and not every compiler supports the optimization of the
tail recursion.

Efficiency

    Along with the additional memory consumption, the recursion could impose at least
the additional cost of function calls, and in a worse case duplicate calculation, i.e.
one of the caveats of recursion that we discussed previously in the Explore card of
Recursion I.

Complexity

    The nature of recursion is quite close to the mathematics, which is why the
recursion appears to be more intuitive and comprehensive for many people. However, when
we abuse the recursion, the recursive program could become more difficult to read and
understand than the non-recursive one, e.g. nested recursion etc.

The good news is that we can always convert a recursion to iteration. In order to do so,
in general, we use a data structure of stack or queue, which replaces the role of the
system call stack during the process of recursion.

To convert a recursion approach to an iteration one, we could perform the following two
steps:

    1. We use a stack or queue data structure within the function, to replace the role
of the system call stack. At each occurrence of recursion, we simply push the parameters
as a new element into the data structure that we created, instead of invoking a
recursion.

    2. In addition, we create a loop over the data structure that we created before. The
chain invocation of recursion would then be replaced with the iteration within the loop.

Beyond Recursion
================

Divide and Conquer VS. Backtracking
----------------------------------

1. Often the case, the divide-and-conquer problem has a sole solution, while the
backtracking problem has unknown number of solutions. For example, when we apply the
merge sort algorithm to sort a list, we obtain a single sorted list, while there are
many solutions to place the queens for the N-queen problem.

2. Each step in the divide-and-conquer problem is indispensable to build the final
solution, while many steps in backtracking problem might not be useful to build the
solution, but serve as atttempts to search for the potential solutions. For example,
each step in the merge sort algorithm, i.e. divide, conquer and combine, are all
indispensable to build the final solution, while there are many trials and errors during
the process of building solutions for the N-queen problem.

3. When building the solution in the divide-and-conquer algorithm, we have a clear and
predefined path, though there might be several different manners to build the path.
While in the backtracking problems, one does not know in advance the exact path to the
solution. For example, in the top-down merge sort algorithm, we first recursively divide
the problems into two subproblems and then combine the solutions of these subproblems.
The steps are clearly defined and the number of steps is fixed as well. While in the
N-queen problem, if we know exactly where to place the queens, it would only take N
steps to do so. When applying the backtracking algorithm to the N-queen problem, we try
many candidates and many of them do not eventually lead to a solution but abandoned at
the end. As a result, we do not know beforehand how many steps exactly it would take to
build a valid solution.
"""
