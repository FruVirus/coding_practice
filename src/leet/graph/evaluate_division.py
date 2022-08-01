"""
Evaluate Division
-----------------

You are given an array of variable pairs equations and an array of real numbers values,
where equations[i] = [A_i, B_i] and values[i] represent the equation A_i / B_i =
values[i]. Each A_i or B_i is a string that represents a single variable.

You are also given some queries, where queries[j] = [C_j, D_j] represents the jth query
where you must find the answer for C_j / D_j = ?.

Return the answers to all queries. If a single answer cannot be determined, return -1.0.

Note: The input is always valid. You may assume that evaluating the queries will not
result in division by zero and that there is no contradiction.

Intuition
---------

Each division implies the reverse of the division is also a valid value. While by
chaining up equations, we could obtain new equations with new values.



Backtrack/DFS Approach

We could reformulate the equations with the graph data structure, where each variable
can be represented as a node in the graph, and the division relationship between
variables can be modeled as edge with direction and weight. Since each division implies
the reverse of the division, the reverse edge has the reciprocal weight.

To evaluate a query (e.g., a / c = ?) is equivalent to performing two tasks on the
graph: 1) find if there exists a path between the two entities. 2) If so, calculate the
cumulative products along the paths.

As one can see, we just transform the problem into a path searching problem in a graph.

More precisely, we can reinterpret the problem as "given two nodes, we are asked to
check if there exists a path between them. If so, we should return the cumulative
products along the path as the result.

Essentially, we can break down the algorithm into two steps overall:

    Step 1) We build the graph out of the list of input equations.
        Each equation corresponds to two edges in the graph.

    Step 2) Once the graph is built, we then can evaluate the query one by one.

        The evaluation of the query is done via searching the path between the given two
variables.
        Other than the above searching operation, we need to handle two exceptional
cases as follows:
            Case 1): If either of the nodes does not exist in the graph, i.e., the
variables did not appear in any of the input equations, then we can assert that no path
exists.
            Case 2): If the origin and the destination are the same node, i.e., a / a,
we can assume that there exists an invisible self-loop path for each node and the result
is one.

Union-Find Approach

Thanks to the characteristic of the Union-Find data structure, we can easily determine
whether the nodes of a and c belong to the same group in the above graph, which
accomplishes the first task that we need to perform, i.e., determining if there exists a
path between two nodes.

However, one important task is missing, which is how can we calculate the cumulative
product along the path, with the Union-Find data structure.

As a spoiler alert, it suffices to adapt the Union-Find data structure and algorithm a
little bit.

First of all, essentially we will build a table which contains an entry for each node in
the graph, with the help of Union-Find.

The entry is defined as key -> (group_id, weight). For example, initially, given a node
a, its entry in the table would look like 'a' -> ('a', 1), where the first 'a' indicates
the id of the node, the second 'a' indicates the id of the group that the node belongs
to, and finally the value 1 indicates the weight of the node.

With the above definitions, the tasks become simple. Given two nodes (variables a and b)
with entries as (a_group_id, a_weight) and (b_group_id, b_weight) respectively, to
evaluate the query of a / b = ?, we only need to perform the following two calculations:

    - a_group_id == b_group_id: If so, they belong to the same group, i.e., there exists
a path between them.
    - a_weight / b_weight: If the above condition holds, by dividing over the relative
weights that are assigned to the variables, we then can obtain the result of a / b at
the end.

Now it all boils down to how we can build the above table with the help of Union-Find
algorithm.

    - Initially, the entries for each variable would look like the following, where the
group_id of each variable is the variable itself and the weight of each variable is 1.
Each variable forms a group on its own, since there is no relationship among them at the
moment.

    - Now if we process the equation a / b = 2, by joining (Union operation) the two
groups that the variables a and b belong to, we would obtain the results as shown in the
following graph. More precisely, we attach the group of dividend a to the one of the
divisor b. Meanwhile, we would also update the relative weight of the group a to reflect
the ratio between the two variables.

    - As one might notice, there is some inconsistency in the above graph, i.e., the
group_id of the variable of a should then be c and the weight of the variable a should
be 6 rather than 2. Indeed, these inconsistencies are expected. The magic happens when
we invoke the Find operation on the variable a, where a chain reaction would be
triggered to update the group_id and weight along the chain. Once the lazy evaluation of
find() is triggered, the states of the nodes along the chain would then be updated, and
eventually they become consistent.

We will implement two functions: find(variable) and union(dividend, divisor, quotient).

    - find(variable): the function will return the group_id that the variable belongs
to. Moreover, the function will update the states of variables along the chain, if there
is any discrepancy.

    - union(dividend, divisor, quotient): this function will attach the group of
dividend to that of the divisor, if they are not already the same group. In addition, it
needs to update the weight of the dividend variable accordingly, so that the ratio
between the dividend and divisor is respected.

Complexity
==========

Time
----

calcEquation_dfs(equations, values, queries): O(m * n), where m is the number of queries
and n is the number of input equations.
calcEquation_dset(equations, values, queries): O((m + n) * alpha(n)).

Space
-----

calcEquation_dfs(equations, values, queries): O(n).
calcEquation_dset(equations, values, queries): O(n).
"""


# Standard Library
from collections import defaultdict


def sol_dfs(equations, values, queries):
    graph, sol = defaultdict(defaultdict), []

    def backtrack(divid, divis, prod, seen):
        seen.add(divid)
        divisors, value = graph[divid], -1.0
        if divis in divisors:
            value = prod * divisors[divis]
        else:
            for d, v in divisors.items():
                if d not in seen:
                    value = backtrack(d, divis, prod * v, seen)
                    if value != -1.0:
                        break
        seen.remove(divid)
        return value

    for (divid, divis), value in zip(equations, values):
        graph[divid][divis] = value
        graph[divis][divid] = 1 / value
    for divid, divis in queries:
        if not (divid in graph and divis in graph):
            value = -1.0
        elif divid == divis:
            value = 1.0
        else:
            value = backtrack(divid, divis, 1, set())
        sol.append(value)
    return sol


def sol_dset(equations, values, queries):
    table, sol = {}, []

    def find(node_id):
        gid, weight = table.setdefault(node_id, (node_id, 1))
        if node_id != gid:
            new_gid, new_weight = find(gid)
            table[node_id] = (new_gid, weight * new_weight)
        return table[node_id]

    def union(divid, divis, value):
        divid_gid, divid_weight = find(divid)
        divis_gid, divis_weight = find(divis)
        if divid_gid != divis_gid:
            table[divid_gid] = (divis_gid, divis_weight * value / divid_weight)

    for (divid, divis), value in zip(equations, values):
        union(divid, divis, value)
    for divid, divis in queries:
        if not (divid in table and divis in table):
            value = -1.0
        else:
            divid_gid, divid_weight = find(divid)
            divis_gid, divis_weight = find(divis)
            value = -1.0 if divid_gid != divis_gid else divid_weight / divis_weight
        sol.append(value)
    return sol
