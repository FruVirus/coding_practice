"""
Network Delay Time
------------------

You are given a network of n nodes, labeled from 1 to n. You are also given times, a
list of travel times as directed edges times[i] = (u_i, v_i, w_i), where u_i is the
source node, v_i is the target node, and w_i is the time it takes for a signal to travel
from source to target.

We will send a signal from a given node k. Return the time it takes for all the n nodes
to receive the signal. If it is impossible for all the n nodes to receive the signal,
return -1.

Complexity
==========

Time
----

networkDelayTime(times, n, k): O(n + e * lg n), where n is the number of nodes and e is
the number of total edges in the given network.

Space
-----

networkDelayTime(times, n, k): O(n + e).
"""


# Standard Library
import heapq


def sol(times, n, k):
    graph = {i: [] for i in range(1, n + 1)}
    for u, v, w in times:
        graph[u].append((v, w))
    heap, visited, max_time = [(0, k)], set(), 0
    while heap:
        time, u = heapq.heappop(heap)
        if u not in visited:
            visited.add(u)
            max_time = max(max_time, time)
            for v, w in graph[u]:
                if v not in visited:
                    heapq.heappush(heap, (time + w, v))
    return max_time if len(visited) == n else -1
