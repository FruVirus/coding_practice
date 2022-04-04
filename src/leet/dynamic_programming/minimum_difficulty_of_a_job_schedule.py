"""
Minimum Difficulty of a Job Schedule
------------------------------------

You want to schedule a list of jobs in d days. Jobs are dependent (i.e., to work on the
i-th job, you have to finish all the jobs j where 0 <= j < i).

You have to finish at least one task every day. The difficulty of a job schedule is the
sum of difficulties of each day of the d days. The difficulty of a day is the maximum
difficulty of a job done on that day.

You are given an integer array jobDifficulty and an integer d. The difficulty of the
i-th job is jobDifficulty[i].

Return the minimum difficulty of a job schedule. If you cannot find a schedule for the
jobs return -1.

Intuition
---------

1. A function that answers the problem for a given state

Let's first decide on state variables. What decisions are there to make, and what
information do we need to make these decisions? Reading the problem description
carefully, there are d total days, and on each day we need to complete some number of
jobs. By the end of the d days, we must have finished all jobs (in the given order).
Therefore, we can see that on each day, we need to decide how many jobs to take.

Let's use one state variable i, where i is the index of the first job that will be done
on the current day.

Let's use another state variable day, where day indicates what day it currently is.

The problem is asking for the minimum difficulty, so let's have a function dp(i, day)
that returns the minimum difficulty of a job schedule which starts on the i-th job and
day, day. To solve the original problem, we will just return dp(0, 1), since we start on
the first day with no jobs done yet.

2. A recurrence relation to transition between states

At each state, we are on day, day, and need to do job i. Then, we can choose to do a few
more jobs. How many more jobs are we allowed to do? The problem says that we need to do
at least one job per day. This means we must leave at least d - day jobs so that all the
future days have at least one job that can be scheduled on that day. If n is the total
number of jobs, jobDifficulty.length, that means from any given state (i, day), we are
allowed to do the jobs from index i up to but not including index n - (d - day).

We should try all the options for a given day - try doing only one job, then two jobs,
etc. until we can't do any more jobs. The best option is the one that results in the
easiest job schedule.

The difficulty of a given day is the most difficult job that we did that day. Since the
jobs have to be done in order, if we are trying all the jobs we are allowed to do on
that day (iterating through them), then we can use a variable hardest to keep track of
the difficulty of the hardest job done today. If we choose to do jobs up to the j-th job
(inclusive), where i <= j < n - (d - day) (as derived above), then that means on the
next day, we start with the (j + 1)-th job. Therefore, our total difficulty is
hardest + dp(j + 1, day + 1). This gives us our scariest recurrence relation so far:

dp(i, day) = min(hardest + dp(j + 1, day + 1)) for all i <= j < n - (d - day), where
hardest = max(jobDifficulty[k]) for all i <= k <= j.

The codified recurrence relation is a scary one to look at for sure. However, it is
easier to understand when we break it down bit by bit. On each day, we try all the
options - do only one job, then two jobs, etc. until we can't do any more (since we need
to leave some jobs for future days). hardest is the hardest job we do on the current
day, which means it is also the difficulty of the current day. We add hardest to the
next state which is the next day, starting with the next job. After trying all the jobs
we are allowed to do, choose the best result.

3. Base cases

Despite the recurrence relation being complicated, the base cases are much simpler. We
need to finish all jobs in d days. Therefore, if it is the last day (day == d), we need
to finish up all the remaining jobs on this day, and the total difficulty will just be
the largest number in jobDifficulty on or after index i.

    - If day == d then return the maximum job difficulty between job i and the end of
the array (inclusive).

We can precompute an array hardestJobRemaining where hardestJobRemaining[i] represents
the difficulty of the hardest job on or after day i, so that this base case is handled
in constant time.

Additionally, if there are more days than jobs (n < d), then it is impossible to do at
least one job each day, and per the problem description, we should return -1. We can
check for this case at the very start.

Complexity
==========

Time
----

minDifficulty(job_diff, d): O(d * (n - d)^2), where n is the length of job_diff.

Space
-----

minDifficulty_bu(job_diff, d): O(n * d).
minDifficulty_td(job_diff, d): O((n - d) * d).
"""


def sol_bu(job_diff, d):
    n = len(job_diff)
    if n < d:
        return -1
    dp = [float("inf")] * n + [0]
    for day in range(1, d + 1):
        new_dp = list(dp)
        for i in range(n - day + 1):
            curr_diff, new_dp[i] = 0, float("inf")
            for j in range(i, n - day + 1):
                curr_diff = max(curr_diff, job_diff[j])
                new_dp[i] = min(new_dp[i], curr_diff + dp[j + 1])
        dp = new_dp
    return dp[0]


def sol_td(job_diff, d):
    n = len(job_diff)
    if n < d:
        return -1
    memo, curr_diff, max_diff_remaining = {}, 0, [0] * n
    for i in reversed(range(n)):
        curr_diff = max(curr_diff, job_diff[i])
        max_diff_remaining[i] = curr_diff

    def dp(i, day):
        if day == d:
            return max_diff_remaining[i]
        if (i, day) not in memo:
            best_diff, curr_diff = float("inf"), 0
            for i in range(i, n - (d - day)):
                curr_diff = max(curr_diff, job_diff[i])
                best_diff = min(best_diff, curr_diff + dp(i + 1, day + 1))
            memo[(i, day)] = best_diff
        return memo[(i, day)]

    return dp(0, 1)
