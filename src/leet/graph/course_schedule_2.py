"""
Course Schedule II
------------------

There are a total of numCourses courses you have to take, labeled from 0 to
numCourses - 1. You are given an array prerequisites where prerequisites[i] = [a_i, b_i]
indicates that you must take course b_i first if you want to take course a_i.

    - For example, the pair [0, 1], indicates that to take course 0 you have to first
take course 1.

Return the ordering of courses you should take to finish all courses. If there are many
valid answers, return any of them. If it is impossible to finish all courses, return an
empty array.

Intuition
---------

DFS Approach

Suppose we are at a node in our graph during the depth first traversal. Let's call this
node A.

The way DFS would work is that we would consider all possible paths stemming from A
before finishing up the recursion for A and moving onto other nodes. All the nodes in
the paths stemming from the node A would have A as an ancestor. The way this fits in our
problem is, all the courses in the paths stemming from the course A would have A as a
prerequisite.

If a valid ordering of courses is possible, the course A would come before all the other
set of courses that have it as a prerequisite.

An important thing to note about topologically sorted order is that there won't be just
one ordering of nodes (courses). There can be multiple.

Kahn's Approach

The first node in the topological ordering will be the node that doesn't have any
incoming edges. Essentially, any node that has an in-degree of 0 can start the
topologically sorted order. If there are multiple such nodes, their relative order
doesn't matter and they can appear in any order.

We first process all the nodes/course with 0 in-degree implying no prerequisite courses
required. If we remove all these courses from the graph, along with their outgoing
edges, we can find out the courses/nodes that should be processed next. These would
again be the nodes with 0 in-degree. We can continuously do this until all the courses
have been accounted for.

Complexity
==========

Time
----

findOrder_dfs(num_courses, prereqs) and findOrder_kahn(num_courses, prereqs): O(v + e).

Space
-----

findOrder_dfs(num_courses, prereqs) and findOrder_kahn(num_courses, prereqs): O(v + e).
"""


def sol_dfs(num_courses, prereqs):
    graph, done = {i: [] for i in range(num_courses)}, {}
    for v, u in prereqs:
        graph[u].append(v)

    def is_dag(u):
        if u in done:
            return done[u]
        done[u] = False
        if not all(is_dag(v) for v in graph[u]):
            return False
        done[u] = True
        return True

    if not all(is_dag(u) for u in graph):
        return []
    done, sol = {}, []

    def backtrack(u):
        if u in done:
            return done[u]
        done[u] = False
        for v in graph[u]:
            backtrack(v)
        done[u] = True
        sol.append(u)
        return True

    for u in range(num_courses):
        backtrack(u)
    return sol[::-1]


def sol_kahn(num_courses, prereqs):
    graph = {i: [] for i in range(num_courses)}
    indeg = {i: 0 for i in range(num_courses)}
    for v, u in prereqs:
        graph[u].append(v)
        indeg[v] += 1
    stack, sol = [u for u in indeg if indeg[u] == 0], []
    while stack:
        u = stack.pop()
        sol.append(u)
        for v in graph[u]:
            indeg[v] -= 1
            if indeg[v] == 0:
                stack.append(v)
    return sol if len(sol) == num_courses else []
