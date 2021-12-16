"""
16.5 A task-scheduling problem as a matroid
===========================================

An interesting problem taht we can solve using matroids is the problem of optimally
scheduling unit-time tasks on a single processor, where each task has a deadline, along
with a penalty paid if the task misses its deadline.

A unit-time task is a job, such as a program to be run on a computer, that requires
exactly one unit of time to complete. Given a finite set S of unit-time tasks, a
schedule for S is a permutation of S specifying the order in which to perform these
tasks. The first task in the schedule begins at time 0 and finishes at time 1, the
second task begins at time 1 and finishes at time 2, and so on.

The problem of scheduling unit-time tasks with deadlines and penalities for a single
processor has the following inputs:

1. a set S = {a_1, a_2, ..., a_n} of unit-time tasks;

2. a set of n integer deadlines d_1, d_2, ..., d_n, such that each d_i satisfies
1 <= d_i <= n and task a_i is supposed to finish by time d_i; and

3. a set of n non-negative weights or penalties w_1, w_2, ..., w_n, such that we incur a
penalty of w_i if task a_i is not finished by time d_i, and we incur no penalty if a
task finishes by its deadline (or earlier).

We wish to find a schedule for S that minimizes the total penalty incurred for missed
deadlines.

Consider a given schedule. We say that a task is late in this schedule if it finishes
after its deadline. Otherwise, the task is early in the schedule. We can always
transform an arbitrary schedule into early-first form, in which the early tasks precede
the late tasks. To see why, note that if some early task a_i follows some late task a_j,
then we can switch the positions of a_i and a_j, and a_i will still be early and a_j
will still be late.

Furthermore, we claim that we can always transform an arbitrary schedule into canonical
form, in which the early tasks precede the late tasks and we schedule the early tasks in
order of monotonically increasing deadlines.

The search for an optimal schedule thus reduces to finding a st A of tasks that we
assign to be early in the optimal schedule. Having determined A, we can create the
actual schedule by listing the elements of A in order of monotonically increasing
deadlines, then listing the late tasks in any order, producing a canonical ordering of
the optimal schedule.

The problem of minimizing the sum of the penalties of the late tasks is the same as the
problem of maximizing the sum of the penalties of the early tasks.

Complexity
==========

Each of the O(n) independence checks made in the for-loop takes O(n) time.

Time
----

js_bottom_up(): O(n^2).
"""


def js_bottom_up(d, w, num_jobs=None):
    n = len(d)
    num_jobs = num_jobs or n
    a = [[str(i), x, y] for i, x, y in zip(range(n), d, w)]
    a = sorted(a, key=lambda x: x[2], reverse=True)
    added, sol = [False] * num_jobs, ["-1"] * num_jobs
    for i in range(n):
        for j in reversed(range(min(num_jobs, a[i][1]))):
            if not added[j]:
                added[j], sol[j] = True, a[i][0]
                break
    return sol
