"""
16.1 An activity-selection problem
==================================

The activity-selection problem is the problem of scheduling several competing activities
that require exclusive use of a common resource, with a goal of selecting a maximum-size
set of mutually compatible activities. Suppose we have a set S = {a_1, a_2, ..., a_n} of
n proposed activities that wish to use a resource, which can serve only one activity at
a time. Each activity a_i has a start time s_i and a finish time f_i, where
0 <= s_i < f_i < float("inf"). If selected, activity a_i takes place during the
half-open time interval [s_i, f_i). Activities a_i and a_j are compatible if the
intervals [s_i, f_i) and [s_j, f_j) do not overlap. In the activity-selection problem,
we wish to select a maximum-size subset of mutually compatible activities. We assume
that the activities are sorted in increasing order of finish time.

Making the greedy choice
------------------------

What if we could choose an activity to add to our optimal solution without having to
first solve all the subproblems? That could save us from having to consider all the
choices inherent in a dynamic programming solution.

What do we mean by the greedy choice for the activity-selection problem? Intuition
suggests that we should choose an activity that leaves the resource available for as
many other activities as possible. Now, of the activities we end up choosing, one of
them must be the first one to finish. Our intuition tells us, therefore, to choose the
activity in S with the earliest finish time, since that would leave the resource
available for as many of the activities that follow as possible. If more than one
activity in S has the earliest finish time, then we can choose any such activity. In
other words, since the activities are sorted in increasing order by finish time, the
greedy choice is activity a_1.

If we make the greedy choice, we have only one remaining subproblem to solve: finding
activities that start after a_1 finishes since all activities that are compatible with
activity a_1 must start after a_1 finishes.

Thus, we can repeatedly choose the activity that finishes first, keep only the
activities compatible with this activity, and repeat until no activities remain.
Moreover, because we always choose the activity with the earliest finish time, the
finish times of the activities we choose must strictly increase. We can consider each
activity just once overall, in increasing order of finish times.

A recursive greedy algorithm
----------------------------

We assume that the n input activities are already ordered by increasing finish times. In
order to start, we add the fictitious activity a_0 with f_0 = 0, so that the subproblem
S_0 is the entire set of activities S.

Intuition
---------

Our intuition tells us to choose an activity with the earliest finish time, since that
would leave the resource available for as many of the activities that follow it as
possible (or break ties). If the activities are sorted in monotonically increasing order
by finish time, the greedy choice always selects the first activity (since it finishes
first in the sorted list).

If we make the greedy choice of adding the first activity, we have only one remaining
subproblem to solve: finding activities that start after the first activity finishes. We
don't have to consider activities that finish before the first activity starts since no
activity can have a finish time earlier than or equal to the first activity (since the
list is sorted by finishing times). Thus, all activities that are compatible with the
first activity must start after the first activity finishes.

Complexity
==========

Assuming that the activities have already been sorted by finish times, the running time
of the top-down approach is Theta(n) since each activity is examined exactly once in
the while loop.

Like the top-down version, the bottom-up version schedules a set of n activities in
Theta(n) time, going through each activity exactly once.

Time
----

as_bu() and as_td(): Theta(n).
"""


def as_bu(s, f, k, n, sol):
    for i in range(1, n):
        if s[i] >= f[k]:
            sol.append(i)
            k = i


def as_td(s, f, k, n, sol):
    i = k + 1
    while i < n and s[i] < f[k]:
        i += 1
    if i < n:
        sol.append(i)
        as_td(s, f, i, n, sol)


def activity_selector(s, f, td=False):
    n, k, sol = len(s), 0, [0]
    as_ = as_td if td else as_bu
    as_(s, f, k, n, sol)
    return sol
