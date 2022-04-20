"""
Parallel Courses
----------------

You are given an integer n, which indicates that there are n courses labeled from 1 to
n. You are also given an array relations where relations[i] =
[prevCourse_i, nextCourse_i], representing a prerequisite relationship between course
prevCourse_i and course nextCourse_i: course prevCourse_i has to be taken before course
nextCourse_i.

In one semester, you can take any number of courses as long as you have taken all the
prerequisites in the previous semester for the courses you are taking.

Return the minimum number of semesters needed to take all courses. If there is no way to
take all the courses, return -1.

Intuition
---------

Kahn's Approach

We can treat the problem as a directed graph problem (the courses are nodes and the
prerequisites are edges). What we need to do is somehow iterate over all the nodes in
the graph.

To achieve the fastest learning speed, our strategy is:

    - Learn all courses available in each semester.

This is intuitive. Even if we deliberately choose not to learn one available course, we
still need to learn it in the following semesters. There is no harm to learn it now.
Also, if we learn it later, then we have to postpone all courses whose prerequisite is
that course.

Now, the first question is:

    - Where to start? (Which courses are available?)

We can not start from courses with prerequisites.

    - We start from nodes with no prerequisites.

By using this strategy to allocate courses to semesters, we are guaranteed to minimize
the number of semesters needed. This is because in each semester, we're learning every
course that isn't "locked" by a prerequisite, and so there is no possible way to be
faster.

In some other cases, we can not learn all nodes. If the number of nodes we visited is
strictly less than the number of total nodes, then there is no way to learn all the
courses and we can do nothing but return -1.

DFS Approach

There is an important insight:

    - The number of semesters needed is equal to the length of the longest path in the
graph.

Why? Treat the path as a sequence of prerequisites, and for each prerequisite, we need
to spend one semester to advance to the next node.

But there is a problem: if the graph has a cycle, then the longest path would be
infinite.

So firstly, we need to check if the graph has a cycle. If it does, we can directly
return -1 since we can never finish all courses.

Check If the Graph Has A Cycle

Each node has one of the three states: unvisited, visiting, and visited.

Before the DFS, we initialize all nodes in the graph to unvisited.

When performing a DFS, we mark the current node as visiting until we search all paths
out of the node from the node. If we meet a node marked with processing, it must come
from the upstream path and therefore, we've detected a cycle.

If DFS finishes, and all node are marked as visited, then the graph contains no cycle.

Calculate the Length of the Longest Path

The DFS function should return the maximum out of the recursive calls for its child
nodes, plus one (the node itself).

In order to prevent redundant calculations, we need to store the calculated results.
This is an example of dynamic programming, as we're storing the result of subproblems.

Complexity
==========

Time
----

minimumSemesters_dfs(n, relations) and minimumSemesters_kahn(n, relations): O(n + e),
where n is the number of courses and e is the length of relations.

Space
-----

minimumSemesters_dfs(n, relations) and minimumSemesters_kahn(n, relations): O().
"""


def sol_dfs(n, relations):
    graph, done = {i: [] for i in range(1, n + 1)}, {}
    for u, v in relations:
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
        return -1
    done = {}

    def backtrack(u):
        if u in done:
            return done[u]
        max_courses = 1
        for v in graph[u]:
            num_courses = backtrack(v)
            max_courses = max(max_courses, num_courses + 1)
        done[u] = max_courses
        return max_courses

    return max(backtrack(u) for u in graph)


def sol_kahn(n, relations):
    graph, indeg = {i: [] for i in range(1, n + 1)}, {i: 0 for i in range(1, n + 1)}
    for u, v in relations:
        graph[u].append(v)
        indeg[v] += 1
    stack = [u for u in indeg if indeg[u] == 0]
    num_semesters = num_courses = 0
    while stack:
        num_semesters += 1
        next_stack = []
        while stack:
            u = stack.pop()
            num_courses += 1
            for v in graph[u]:
                indeg[v] -= 1
                if indeg[v] == 0:
                    next_stack.append(v)
        stack = next_stack
    return num_semesters if num_courses == n else -1
