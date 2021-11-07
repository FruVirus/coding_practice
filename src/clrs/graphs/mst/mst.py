"""
23 Minimum Spanning Tress
=========================

Minimum spanning trees (MST) are useful for when we want to find an acyclic subset of
edges, T, that connect certain vertices and we wish to minimize the total weight of
those edges. Since T is acyclic and connects all of the desired vertices, it must form
a tree, which we call a spanning tree since it "spans" the graph G. We call the problem
of determining the tree T the minimum-spanning-tree problem.

Two main algorithms for solving the MST problem are Kruskal's algorithm and Prim's
algorithm. We can easily make each of them run in time O(E * lg(V)) using ordinary
binary heaps.

The two algorithms are greedy algorithms. Each step of a greedy algorithm must make one
of several possible choices. The greedy strategy advocates making the choice that is the
best at the moment. Such a strategy does not generally guarantee that it will always
find globally optimal solutions to problems. For the MST problem, however, we can prove
that certain greedy strategies do yield a spanning tree with minimum weight.

A minimum-spanning tree is also not unique. There can be multiple MSTs with the same
minimum weight.

23.1 Growing a minimum spanning tree
====================================



Complexity
==========

Time
----

"""
