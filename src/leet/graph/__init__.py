"""
Overview of Disjoint Set
========================

Given the vertices and edges between them, how could we quickly check whether two
vertices are connected? We can do so by using the “disjoint set” data structure, also
known as the “union-find” data structure.

The primary use of disjoint sets is to address the connectivity between the components
of a network. The “network“ here can be a computer network or a social network. For
instance, we can use a disjoint set to determine if two people share a common ancestor.

Terminologies
-------------

- Parent node: the direct parent node of a vertex.
- Root node: a node without a parent node; it can be viewed as the parent node of
itself.

The two important functions of a “disjoint set.”
------------------------------------------------

- The find function finds the root node of a given vertex.
- The union function unions two vertices and makes their root nodes the same.

There are two ways to implement a “disjoint set”.
-------------------------------------------------

- Implementation with Quick Find: in this case, the time complexity of the find function
will be O(1). However, the union function will take more time with the time complexity
of O(N).
- Implementation with Quick Union: compared with the Quick Find implementation, the time
complexity of the union function is better. Meanwhile, the find function will take more
time in this case.

Quick Find - Disjoint Set
=========================

Time Complexity
---------------

                Union-find Constructor	Find	Union	Connected
Time Complexity	O(N)	                O(1)	O(N)	O(1)

Note: N is the number of vertices in the graph.

- When initializing a union-find constructor, we need to create an array of size N with
the values equal to the corresponding array indices; this requires linear time.
- Each call to find will require O(1) time since we are just accessing an element of the
array at the given index.
- Each call to union will require O(N) time because we need to traverse through the
entire array and update the root vertices for all the vertices of the set that is going
to be merged into another set.
- The connected operation takes O(1) time since it involves the two find calls and the
equality check operation.

Space Complexity
----------------

We need O(N) space to store the array of size N.

Quick Union - Disjoint Set
==========================

Time Complexity
---------------

                Union-find Constructor	Find	Union	Connected
Time Complexity	O(N)	                O(N)	O(N)	O(N)

Note: N is the number of vertices in the graph. In the worst-case scenario, the number
of operations to get the root vertex will be H where H is the height of the tree.
Because this implementation does not always point the root of the shorter tree to the
root of the taller tree, H can be at most N when the tree forms a linked list.

- The same as in the quick find implementation, when initializing a union-find
constructor, we need to create an array of size N with the values equal to the
corresponding array indices; this requires linear time.
- For the find operation, in the worst-case scenario, we need to traverse every vertex
to find the root for the input vertex. The maximum number of operations to get the root
vertex would be no more than the tree's height, so it will take O(N) time.
- The union operation consists of two find operations which (only in the worst-case)
will take O(N) time, and two constant time operations, including the equality check and
updating the array value at a given index. Therefore, the union operation also costs
O(N) in the worst-case.
- The connected operation also takes O(N) time in the worst-case since it involves two
find calls.

Space Complexity
----------------

We need O(N) space to store the array of size N.

Union by Rank - Disjoint Set
============================

Disjoint Set - Union by Rank
----------------------------

We have implemented two kinds of “disjoint sets” so far, and they both have a concerning
inefficiency. Specifically, the quick find implementation will always spend O(n) time on
the union operation and in the quick union implementation, it is possible for all the
vertices to form a line after connecting them using union, which results in the
worst-case scenario for the find function. Is there any way to optimize these
implementations?

Of course, there is; it is to union by rank. The word “rank” means ordering by specific
criteria. Previously, for the union function, we always chose the root node of x and set
it as the new root node for the other vertex. However, by choosing the parent node based
on certain criteria (by rank), we can limit the maximum height of each vertex.

To be specific, the “rank” refers to the height of each vertex. When we union two
vertices, instead of always picking the root of x (or y, it doesn't matter as long as
we're consistent) as the new root node, we choose the root node of the vertex with a
larger “rank”. We will merge the shorter tree under the taller tree and assign the root
node of the taller tree as the root node for both vertices. In this way, we effectively
avoid the possibility of connecting all vertices into a straight line. This optimization
is called the “disjoint set” with union by rank.

Time Complexity
---------------

                Union-find Constructor	Find	    Union	    Connected
Time Complexity	O(N)	                O(log N)	O(log N)	O(log N)

Note: N is the number of vertices in the graph.

- For the union-find constructor, we need to create two arrays of size N each.
- For the find operation, in the worst-case scenario, when we repeatedly union
components of equal rank, the tree height will be at most log(N) + 1, so the find
operation requires O(log N) time.
- For the union and connected operations, we also need O(log N) time since these
operations are dominated by the find operation.

Space Complexity
----------------

We need O(N) space to store the array of size N.

Path Compression Optimization - Disjoint Set
============================================

Path Compression Optimization - Disjoint Sets
---------------------------------------------

In the previous implementation of the “disjoint set”, notice that to find the root node,
we need to traverse the parent nodes sequentially until we reach the root node. If we
search the root node of the same element again, we repeat the same operations. Is there
any way to optimize this process?

The answer is yes! After finding the root node, we can update the parent node of all
traversed elements to their root node. When we search for the root node of the same
element again, we only need to traverse two elements to find its root node, which is
highly efficient. So, how could we efficiently update the parent nodes of all traversed
elements to the root node? The answer is to use “recursion”. This optimization is called
“path compression”, which optimizes the find function.

Time Complexity
===============

Time complexities shown below are for the average case, since the worst-case scenario is
rare in practice.

                Union-find Constructor	Find	    Union	    Connected
Time Complexity	O(N)	                O(log N)	O(log N)	O(log N)

Note: N is the number of vertices in the graph.

- As before, we need O(N) time to create and fill the root array.
- For the find, union, and connected operations (the latter two operations both depend
on the find operation), we need O(1) time for the best case (when the parent node for
some vertex is the root node itself). In the worst case, it would be O(N) time when the
tree is skewed. However, on average, the time complexity will be O(log N).

Space Complexity
----------------

We need O(N) space to store the array of size N.

Optimized “disjoint set” with Path Compression and Union by Rank
================================================================

Time Complexity
---------------

                Union-find Constructor	Find	Union	Connected
Time Complexity	O(N)	                O(α(N))	O(α(N))	O(α(N))

Note: N is the number of vertices in the graph. alpha refers to the Inverse Ackermann
function. In practice, we assume it's a constant. In other words, O(α(N)) is regarded as
O(1) on average.

- For the union-find constructor, we need to create two arrays of size N each.
- When using the combination of union by rank and the path compression optimization, the
find operation will take O(α(N)) time on average. Since union and connected both make
calls to find and all other operations require constant time, union and connected
functions will also take O(α(N)) time on average.

Space Complexity
----------------

We need O(N) space to store the array of size N.

Summary of the “disjoint set” data structure
============================================

The main idea of a “disjoint set” is to have all connected vertices have the same parent
node or root node, whether directly or indirectly connected. To check if two vertices
are connected, we only need to check if they have the same root node.

The two most important functions for the “disjoint set” data structure are the find
function and the union function. The find function locates the root node of a given
vertex. The union function connects two previously unconnected vertices by giving them
the same root node. There is another important function named connected, which checks
the “connectivity” of two vertices. The find and union functions are essential for any
question that uses the “disjoint set” data structure.

Overview of Depth-First Search Algorithm
========================================

Previously, we learned how to check the connectivity between two vertices with the
“disjoint set” data structure. Now, let's switch gears and consider: Given a graph, how
can we find all of its vertices, and how can we find all paths between two vertices?

The depth-first search algorithm is ideal in solving these kinds of problems because it
can explore all paths from the start vertex to all other vertices.

In Graph theory, the depth-first search algorithm (abbreviated as DFS) is mainly used
to:

    1. Traverse all vertices in a “graph”;
    2. Traverse all paths between any two vertices in a “graph”.

Overview of Breadth-First Search Algorithm
==========================================

Previously, we discussed the “depth-first search” algorithm. This section will talk
about a closely related and equally popular algorithm called “breadth-first search”.
Similarly, the “breadth-first search” algorithm can traverse all vertices of a “graph”
and traverse all paths between two vertices. However, the most advantageous use case of
“breadth-first search” is to efficiently find the shortest path between two vertices in
a “graph” where all edges have equal and positive weights.

Although the “depth-first search” algorithm can find the shortest path between two
vertices in a “graph” with equal and positive weights, it must traverse all paths
between two vertices before finding the shortest one. The “breadth-first search”
algorithm, in most cases, can find the shortest path without traversing all paths. This
is because when using "breadth-first search", as soon as a path between the source
vertex and target vertex is found, it is guaranteed to be the shortest path between the
two nodes.

In Graph theory, the primary use cases of the “breadth-first search” (“BFS”) algorithm
are:

    1. Traversing all vertices in the “graph”;
    2. Finding the shortest path between two vertices in a graph where all edges have
equal and positive weights.

Overview of Minimum Spanning Tree
=================================

You might wonder: what is a spanning tree? A spanning tree is a connected subgraph in an
undirected graph where all vertices are connected with the minimum number of edges. An
“undirected graph” can have multiple spanning trees.

After learning what a spanning tree is, you might have another question: what is a
minimum spanning tree? A minimum spanning tree is a spanning tree with the minimum
possible total edge weight in a “weighted undirected graph”. A “weighted undirected
graph” can have multiple minimum spanning trees.

Cut Property
============

What is a “cut”? Although many theorems are named after people’s names, “cut” is not one
of them. To understand the “cut property”, we need to understand two basic concepts.

- First, in Graph theory, a “cut” is a partition of vertices in a “graph” into two
disjoint subsets.
- Second, a crossing edge is an edge that connects a vertex in one set with a vertex in
the other set.

After knowing the basics of a graph cut, let’s delve into the “cut property”. The cut
property provides theoretical support for Kruskal’s algorithm and Prim’s algorithm. So,
what is the “cut property”? According to Wikipedia, the “cut property” refers to:

    For any cut C of the graph, if the weight of an edge E in the cut-set of C is
strictly smaller than the weights of all other edges of the cut-set of C, then this edge
belongs to all MSTs of the graph.

Kruskal’s Algorithm
===================

“Kruskal’s algorithm” is an algorithm to construct a “minimum spanning tree” of a
“weighted undirected graph”.

Visual Example
--------------

Kruskal's algorithm grows the minimum spanning tree by adding edges. In this example,
the distance between two vertices is the edge weight. We try adding each edge, one at a
time, from the lowest weight edge up to the highest weight edge. If either of the edges'
vertices is not already part of the MST, then the edge is added to the MST.

Why does Kruskal’s Algorithm only choose N-1 edges?
---------------------------------------------------

We need to choose exactly N-1 edges of the graph with N vertices in total to construct a
“minimum spanning tree” of that graph.

Prim’s Algorithm
================

"Prim's algorithm" can be used to construct a “minimum spanning tree” of a “weighted
undirected graph”.

Visual Example
--------------

The above illustration demonstrates how Prim's algorithm works by adding vertices. In
this example, the distance between two vertices is the edge weight. Starting from an
arbitrary vertex, Prim's algorithm grows the minimum spanning tree by adding one vertex
at a time to the tree. The choice of a vertex is based on the greedy strategy, i.e., the
addition of the new vertex incurs the minimum cost.

The difference between the “Kruskal’s algorithm” and the “Prim’s algorithm”
---------------------------------------------------------------------------

“Kruskal’s algorithm” expands the “minimum spanning tree” by adding edges. Whereas
“Prim’s algorithm” expands the “minimum spanning tree” by adding vertices.

Overview of Single Source Shortest Path
=======================================

Previously, we used the “breadth-first search” algorithm to find the “shortest path”
between two vertices. However, the “breadth-first search” algorithm can only solve the
“shortest path” problem in “unweighted graphs”. But in real life, we often need to find
the “shortest path” in a “weighted graph”.

For example, there may be many routes from your home to a target location, such as a bus
station, and the time needed for each route may be different. The route with the
shortest distance may not be the one that requires the least amount of time because of
the speed limit and traffic jams. So, if we want to find the route that takes the least
time from home to a certain bus station, then the weights should be time instead of
distance. With that in mind, how can we solve the “shortest path” problem given two
vertices in a “weighted graph”?

The main focus of this chapter is to solve such “single source shortest path” problems.
Given the starting vertex, find the “shortest path” to any of the vertices in a weighted
graph. Once we solve this, we can easily acquire the shortest paths between the starting
vertex and a given target vertex.

Edge Relaxation
---------------

The Edge Relaxation operation that is a key element in solving the “single-source
shortest path” problem.

An alternative way to understand why this process is called ‘relaxation’ is to imagine
that each path is a rubber band of length 1. The original path from A to D is of length
3, so the rubber band was stretched to 3 times its original length. When we relax the
path to length 2, by visiting C first, the rubber band is now only stretched to twice
its length, so you can imagine the rubber band being relaxed, hence the term edge
relaxation.

In this chapter, we will learn two “single source shortest path” algorithms:

    1. Dijkstra’s algorithm
    2. Bellman-Ford algorithm

“Dijkstra's algorithm” can only be used to solve the “single source shortest path”
problem in a graph with non-negative weights.

“Bellman-Ford algorithm”, on the other hand, can solve the “single-source shortest path”
in a weighted directed graph with any weights, including, of course, negative weights.

Dijkstra's Algorithm
====================

“Dijkstra’s algorithm” solves the “single-source shortest path” problem in a weighted
directed graph with non-negative weights.

The Main Idea
-------------

We take the starting point u as the center and gradually expand outward while updating
the “shortest path” to reach other vertices.

“Dijkstra's Algorithm” uses a “greedy approach”. Each step selects the “minimum weight”
from the currently reached vertices to find the “shortest path” to other vertices.

Bellman Ford Algorithm
======================

As discussed previously, the “Dijkstra algorithm” is restricted to solving the “single
source shortest path” problem in graphs without negative weights. So, how could we solve
the “single source shortest path” problem in graphs with negative weights? In this
chapter, we will introduce the Bellman-Ford algorithm.

Basic Theorem
-------------

Theorem 1: In a “graph with no negative-weight cycles” with N vertices, the shortest
path between any two vertices has at most N-1 edges.

Theorem 2: In a “graph with negative weight cycles”, there is no shortest path.

How does the Bellman-Ford algorithm detect “negative weight cycles”?
--------------------------------------------------------------------

Although the “Bellman-Ford algorithm” cannot find the shortest path in a graph with
“negative weight cycles”, it can detect whether there exists a “negative weight cycle”
in the “graph”.

Detection method: After relaxing each edge N-1 times, perform the Nth relaxation.
According to the “Bellman-Ford algorithm”, all distances must be the shortest after
relaxing each edge N-1 times. However, after the Nth relaxation, if there exists
distances[u] + weight(u, v) < distances(v) for any edge(u, v), it means there is a
shorter path . At this point, we can conclude that there exists a “negative weight
cycle”.

Improved Bellman-Ford Algorithm with Queue — SPFA Algorithm
===========================================================

Previously, we introduced the “Bellman-Ford Algorithm” along with an improvement. The
improvement is that for a graph without negative cycles, after relaxing each edge N-1
times, we can get the minimum distance from the starting vertex to all other vertices.
However, there could be unnecessary computation when relaxing all edges N-1 times,
resulting in suboptimal time complexity in some cases.

SPFA algorithm
--------------

To address the limitations, we introduce an improved variation of the Bellman-Ford
algorithm by using a queue. This improvement is known as “the Shortest Path Faster
Algorithm” (SPFA algorithm).

Instead of choosing among any untraversed edges, as one does by using the “Bellman-Ford”
algorithm, the “SPFA” Algorithm uses a “queue” to maintain the next starting vertex of
the edge to be traversed. Only when the shortest distance of a vertex is relaxed and
that the vertex is not in the “queue”, we add the vertex to the queue. We iterate the
process until the queue is empty. At this point, we have calculated the minimum distance
from the given vertex to any vertices.

Overview of Kahn's Algorithm
============================

When selecting courses for the next semester in college, you might have noticed that
some advanced courses have prerequisites that require you to take some introductory
courses first. There are many courses that you must complete for an academic degree. You
do not want to find out in the last semester that you have not completed some
prerequisite courses for an advanced course. So, how can we arrange the order of the
courses adequately while considering these prerequisite relationships between them?

“Topological sorting” helps solve the problem. It provides a linear sorting based on the
required ordering between vertices in directed acyclic graphs. To be specific, given
vertices u and v, to reach vertex v, we must have reached vertex u first. In
“topological sorting”, u has to appear before v in the ordering. The most popular
algorithm for “topological sorting” is Kahn’s algorithm.

Note, for simplicity while introducing Kahn's algorithm, we iterated over all of the
courses and reduced the in-degree of those for which the current course is a
prerequisite. This requires us to iterate over all E prerequisites for all V courses
resulting in O(V⋅E) time complexity at the cost of O(V) space to store the in degree for
each vertex.

However, this step can be performed more efficiently by creating an adjacency list where
adjacencyList[course] contains a list of courses that depend on course. Then when each
course is taken, we will only iterate over the courses that have the current course as a
prerequisite. This will reduce the total time complexity to O(V + E) at the cost of an
additional O(E) space to store the adjacency list.

Limitation of the Algorithm
---------------------------

- “Topological sorting” only works with graphs that are directed and acyclic.
- There must be at least one vertex in the “graph” with an “in-degree” of 0. If all
vertices in the “graph” have a non-zero “in-degree”, then all vertices need at least one
vertex as a predecessor. In this case, no vertex can serve as the starting vertex.


"""
