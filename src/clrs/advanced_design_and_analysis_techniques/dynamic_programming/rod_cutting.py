"""
15.1 Rod cutting
================

The rod-cutting problem is the following. Given a rod length n inches and a table of
prices p_i for rod pieces of length i = 1, 2, ..., n, determine the maximum revenue r_n
obtainable by cutting up the rod and selling the pieces. Note that if the price p_n for
a rod of length n is large enough, an optimal solution may require no cutting at all.

We can cut up a rod of length n in 2^(n - 1) ways, since we have an independent option
of cutting, or not cutting, at distance i inches from the left end, for
i = 1, 2, ..., n - 1. We denote a decomposition into pieces using ordinary additive
notation, so that 7 = 2 + 2 + 3 indicates that a rod of length 7 is cut into three
pieces---two of length 2 and one of length 3. If an optimal solution cuts the rod into
k pieces, for some 1 <= k <= n, then an optimal decomposition

n = i_1 + i_2 + ... + i_k

of the rod into pieces of lengths i_1, i_2, ..., i_k provides maximum corresponding
revenue

r_n = p_i_1 + p_i_2 + ... + p_i_k.

More generally, we can frame the values r_n for n >= 1 in terms of optimal revenues from
shorter rods:

r_n = max(p_n, r_1 + r_(n - 1), r_2 + r_(n - 2), ..., r_(n - 1) + r_1).  (15.1)

The first argument, p_n, corresponds to making no cuts at all and selling the rod of
length n as is. The other n - 1 arguments to equation (15.1) correspond to the maximum
revenue obtained by making an initial cut of the rod into two pieces of size i and
n - i, for each i = 1, 2, ..., n - 1, and then optimally cutting up those pieces
further, obtaining revenues r_i and r_(n - i) from those two pieces. Since we don't know
ahead of time which value of i optimizes revenue, we have to consider all possible
values for i and pick the one that maximizes revenue. We also have the option of picking
no i at all if we can obtain more revenue by selling the rod uncut.

Note that to solve the original problem of size n, we solve smaller problems of the same
type, but of smaller sizes. Once we make the first cut, we may consider the two pieces
as independent instances of the rod-cutting problem. The overall optimal solution
incorporates optimal solutions to the two related subproblems, maximizing the revenue
from each of those two pieces. We say that the rod-cutting problem exhibits optimal
substructure: optimal solutions to a problem incorporate optimal solutions to related
subproblems, which we may solve independently.

We can also view a decomposition as consisting of a first piece of length i cut off the
left-hand end, and then a right-hand remainder of length n - i. Only the remainder, and
not the first piece, may be further divided. We may view every decomposition of a
length-n rod in this way: as a first piece followed by some decomposition of the
remainder. When doing so, we can couch the solution with no cuts at all as saying that
the first piece has size i = n and revenue p_n and that the remainder has size 0 with
corresponding revenue r_0 = 0. We thus obtain the simpler version of equation (15.1).

r_n = max(p_i + r_(n - i)) for 1 <= i <= n.

In this formulation, an optimal solution embodies the solution to only one related
subproblem---the remainder---rather than two.

Recursive top-down implementation
---------------------------------

A naive implementation would call itself recursively over and over again with the same
parameter values; it solves the same subproblems repeatedly. When the process unfolds
recursively, the amount of work done, as a function of n, grows exponentially.

Since there are 2^(n - 1) possible ways of cutting up a rod of length n, the naive
solution is exponential in n.

Using dynamic programming for optimal rod cutting
-------------------------------------------------

The dynamic-programming method works as follows. Having observed that a naive recursive
solution is inefficient because it solves the same subproblems repeatedly, we arrange
for each subproblem to be solved only once, saving its solution. If we need to refer to
this subproblem's solution again later, we can just look it up, rather than recompute
it. Dynamic programming thus uses additional memory to save computation time; it serves
as an example of a time-memory trade-off. A dynamic-programming approach runs in
polynomial time when the number of distinct subproblems involved is polynomial in the
input size and we can solve each such subproblem in polynomial time.

There are usually two equivalent ways to implement a dynamic-programming approach. We
shall illustrate both of them with our rod-cutting example.

The first approach is top-down with memoization. In this approach, we write the
procedure recursively in a natural manner, but modified to save the result of each
subproblem (usually in an array or hash table). The procedure now first checks to see
whether it has previously solved this subproblem. If so, it returns the saved value,
saving further computation at this level; if not, the procedure computes the value in
the usual manner. We say that the recursive procedure has been memoized; it "remembers"
what results it has computed previously.

The second approach is the bottom-up method. This approach typically depends on some
natural notion of the "size" of a subproblem, such that solving any particular
subproblem depends only on solving "smaller" subproblems. We sort the subproblems by
size and solve them in size order, smallest first. When solving a particular subproblem,
we have already solved all of the smaller subproblems its solution depends upon, and we
have saved their solutions. We solve each subproblem only once, and when we first see
it, we have already solved all of its prerequisite subproblems.

These two approaches yield algorithms with the same asymptotic running time, except in
unusual circumstances where the top-down approach does not actually recurse to examine
all possible subproblems. The bottom-up approach often has much better constant factors,
since it has less overhead for procedure calls.

Subproblem graphs
-----------------

When we think about a dynamic-programming problem, we should understand the set of
problems involved and how subproblems depend on one another.

The subproblem graph for the problem embodies exactly this information. It is a directed
graph, containing one vertex for each distinct subproblem. The subproblem graph has a
directed edge from the vertex for subproblem x to the vertex for subproblem y if
determining an optimal solution for subproblem x involves directly considering an
optimal solution for subproblem y. For example, the subproblem graph contains an edge
from x to y if a top-down recursive procedure for solving x directly calls itself to
solve y.

The bottom-up method for dynamic programming considers the vertices of the subproblem
graph in such an order that we solve the subproblems y adjacent to a given subproblem
x before we solve subproblem x. In a bottom-up dynamic-programming algorithm, we
consider the vertices of the subproblem graph in an order that is a "reverse topological
sort," or a "topological sort of the transpose" of the subproblem graph. In other words,
no subproblem is considered until all of the subproblems it depends upon have been
solved. Similarly, we can view the top-down method for dynamic programming as a
"depth-first search" of the subproblem graph.

The size of the subproblem graph G = (V, E) can help us determine the running time of
the dynamic programming algorithm. Since we solve each subproblem just once, the running
time is the sum of the times needed to solve each subproblem. Typically, the time to
compute the solution to a subproblem is proportional to the out-degree of the
corresponding vertex in the subproblem graph, and the number of subproblems is equal to
the number of vertices in the subproblem graph. In this common case, the running time
of dynamic programming is linear in the number of vertices and edges.

Intuition
---------

The p array holds the price for each length of rod; i.e., the first element in p is the
price of a rod of length 1, the second element in p is the price of a rod of length 2,
and so on.

The r array holds the maximum revenue that can be obtained by cutting a rod of a certain
length---r[0] holds the maximum revenue obtained from cutting a rod of length 0
(i.e., 0), r[1] holds the maximum revenue obtained from cutting a rod of length 1, and
so on.

For example:

r_4 = max(p_1 + r_3, p_2 + r_2, p_3 + r_1, p_4 + r_0)
r_3 = max(p_1 + r_2, p_2 + r_1, p_3 + r_0)
r_2 = max(p_1 + r_1, p_2 + r_0)
r_1 = max(p_1 + r_0)

The s array holds the cut that must be made in order to obtain a given maximum revenue.
For example, if r = [0, 1, 5, 8, 10] and s = [0, 1, 2, 3, 2], then the maximum revenue
for a rod of length n = 4 is r[4] = 10 and the cut(s) that must be made start from s[4].
After making a cut equal to s[4], the remainder rod has length 4 - s[4] = 4 - 2 = 2.
s[2] then gives the next cut to make, and so on.

Complexity
==========

The bottom-up and top-down versions have the same asymptotic running time. The running
time of the bottom-up version is Theta(n^2), due to its doubly nested loop structure.
The running time of the top-down version is also Theta(n^2) because a recursive call to
solve a previously solved subproblem returns immediately. and we solve each subproblem
exactly once.

Time
----

rc_bu() and rc_td(): Theta(n^2).
"""


def rc_bu(p, n, r, s):
    r[0] = 0
    for i in range(1, n + 1):
        q = -float("inf")
        for j in range(1, i + 1):
            t = p[j - 1] + r[i - j]
            if q < t:
                q, s[i] = t, j
        r[i] = q


def rc_td(p, n, r, s):
    if r[n] >= 0:
        q = r[n]
    elif n == 0:
        q = 0
    else:
        q = -float("inf")
        for i in range(n):
            t = p[i] + rc_td(p, n - i - 1, r, s)
            if q < t:
                q, s[n] = t, i + 1
    r[n] = q
    return q


def rc(p, n, td=False):
    r, s, sol = [-float("inf")] * (n + 1), [0] * (n + 1), []
    rc_ = rc_td if td else rc_bu
    rc_(p, n, r, s)
    while n > 0:
        sol.append(s[n])
        n -= s[n]
    return sol, sum(p[i - 1] for i in sol)
