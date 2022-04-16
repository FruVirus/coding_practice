"""
Cheapest Flights Within K Stops
-------------------------------

There are n cities connected by some number of flights. You are given an array flights
where flights[i] = [from_i, to_i, price_i] indicates that there is a flight from city
from_i to city to_i with cost price_i.

You are also given three integers src, dst, and k, return the cheapest price from src to
dst with at most k stops. If there is no such route, return -1.

Intuition
---------

An important part to understanding the Bellman Ford's working is that at each step, the
relaxations lead to the discovery of new shortest paths to nodes. After the first
iteration over all the vertices, the algorithm finds out all the shortest paths from the
source to nodes which can be reached with one hop (one edge). That makes sense because
the only edges we'll be able to relax are the ones that are directly connected to the
source as all the other nodes have shortest distances set to inf initially.

Similarly, after the k + 1-th step, Bellman-Ford will find the shortest distances for
all the nodes that can be reached from the source using a maximum of K stops. Isn't that
what the question asks us to do? If we run Bellman-Ford for k + 1 iterations, it will
find out shortest paths of length k or less and it will find all such paths. We can then
check if our destination node was reached or not and if it was, then the value for that
node would be our shortest path!

1. We have a loop that does k + 1 iterations. The plus one is because we need to find
the cheapest flight route with at most k stops in between. That translates to k + 1
edges at most.

2. In each iteration, we loop over all the edges in the graph and try to relax each one
of them. Again, note that the edges or the flights are already given to us in the input
and don't need to build any kind of adjacency list or matrix structure which is
otherwise standard for other graph algorithms.

3. After k + 1 iterations, we check if the destination has been reached or not. If it's
been discovered, then the distance at that point will be the shortest using at most
k + 1 edges.

4. We use an array to store the current shortest distances of each node from the source.
This is possible because the number of nodes is less and we don't need to use a
dictionary here. However, a single array is not sufficient here because any values
updated in a particular iteration cannot be used to update other values in the same
iteration. Thus, we need another distance array which will kind of serve as values in
the previous iteration. So we essentially use 2 arrays of size V and we swap between
them in each iteration.

Complexity
==========

Time
----

findCheapestPrice(n, flights, src, dst, k): O(k * e),

Space
-----

findCheapestPrice(): O(v).
"""


def sol(n, flights, src, dst, k):
    prev, curr = [float("inf")] * n, [float("inf")] * n
    prev[src] = curr[src] = 0
    for _ in range(k + 1):
        for u, v, w in flights:
            du, dv = prev[u], curr[v]
            if dv > du + w:
                curr[v] = du + w
        prev, curr = curr, prev
    return -1 if prev[dst] == float("inf") else prev[dst]
