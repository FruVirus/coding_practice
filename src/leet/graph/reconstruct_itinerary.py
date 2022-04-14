"""
Reconstruct Itinerary
---------------------

You are given a list of airline tickets where tickets[i] = [from_i, to_i] represent the
departure and the arrival airports of one flight. Reconstruct the itinerary in order and
return it.

All of the tickets belong to a man who departs from "JFK", thus, the itinerary must
begin with "JFK". If there are multiple valid itineraries, you should return the
itinerary that has the smallest lexical order when read as a single string.

    For example, the itinerary ["JFK", "LGA"] has a smaller lexical order than
["JFK", "LGB"].

You may assume all tickets form at least one valid itinerary. You must use all the
tickets once and only once.

Intuition
---------

At each airport, one might have several possible destinations to fly to. With
backtracking, we enumerate each possible destination. We mark the choice at each
iteration (i.e., trial) before we move on to the chosen destination. If the destination
does not lead to a solution (i.e., fail), we would then fallback to the previous state
and start another iteration of trial-fail-and-fallback cycle.

At each airport, given a list of possible destinations, while backtracking, at each step
we would pick the destination greedily in lexical order, i.e., the one with the smallest
lexical order would have its trial first.

As the first step, we build a graph data structure from the given input. This graph
should allow us to quickly identify a list of potential destinations, given an origin.
Here we adopted the hashmap (or dictionary) data structure, with each entry as
<origin, [destinations]>.

Then due to our greedy strategy, we then should order the destination list for each
entry in lexical order. As an alternative solution, one could use PriorityQueue data
structure in the first step to keep the list of destinations, which would maintain the
order at the moment of constructing the list.

As the final step, we kick off the backtracking traversal on the above graph, to obtain
the final result.
    - At the beginning of the backtracking function, as the bottom case, we check if we
have already obtained a valid itinerary.
    - Otherwise, we enumerate the next destinations in order.
    - We mark the status of visit, before and after each backtracking loop.

Complexity
==========

Time
----

findItinerary(tickets): O(abs(e)^d), where e is the number of total flights and d is the
maximum number of flights from an airport.

Space
-----

findItinerary(tickets): O(v + e), where v is the number of airports.
"""


# Standard Library
from collections import defaultdict


def sol(tickets):
    graph, visited, sol = defaultdict(list), {}, []
    for ticket in tickets:
        origin, dest = ticket[0], ticket[1]
        graph[origin].append(dest)
    for origin, dests in graph.items():
        dests.sort()
        visited[origin] = [False] * len(dests)

    def backtrack(origin, route):
        if len(route) == len(tickets) + 1:
            sol.extend(route)
            return True
        for i, dest in enumerate(graph[origin]):
            if not visited[origin][i]:
                visited[origin][i] = True
                done = backtrack(dest, route + [dest])
                visited[origin][i] = False
                if done:
                    return True
        return False

    backtrack("JFK", ["JFK"])
    return sol
