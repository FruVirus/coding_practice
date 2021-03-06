"""
29 Linear Programming
=====================

An overview of linear programming
---------------------------------

The simplex algorithm takes as input a linear program and returns an optimal solution.
It starts at some vertex of the simplex and performs a sequence of iterations. In each
iteration, it moves along an edge of the simplex from a current vertex to a neighboring
vertex whose objective value is no smaller than that of the current vertex (and usually
is larger). The simplex algorithm terminates when it reaches a local maximum, which is a
vertex from which all neighboring vertices have a smaller objective value. Because the
feasible region is convex and the objective function is linear, this local optimum is
actually a global optimum.

We first write the given linear program in slack form, which is a set of linear
equalities. These linear equalities express some of the variables, called "basic
variables", in terms of other variables, called "nonbasic variables". We move from one
vertex to another by making a basic variable become nonbasic and making a nonbasic
variable become basic. We call this operation a "pivot" and, viewed algebraically, it is
nothing more than rewriting the linear program in an equivalent slack form.

29.1 Standard and slack forms
=============================

Standard form
-------------

In standard form, all the constraints are inequalities (i.e., <=) and the objective
function is to maximize.

An arbitrary linear program need not have non-negativity constraints on its variables,
but standard form requires them (i.e., x_j >= 0 for j = 1, 2, ..., n).

Converting linear programs into standard form
---------------------------------------------

A linear program might not be in standard form for any of four possible reasons:

1. The objective function might be a minimization rather than a maximization.

2. There might be variables without non-negativity constraints.

3. There might be equality constraints, which have an equal sign rather than a
less-than-or-equal-to sign.

4. There might be inequality constraints, but instead of having a less-than-or-equal-to
sign, they have a greater-than-or-equal-to sign.

Converting linear programs into slack form
------------------------------------------

In slack form, all the constraints are equalities (except for the non-negativity
constraints on the variables).

To efficiently solve a linear program with the simplex algorithm, we prefer to express
it in a form in which some of the constraints are equality constraints. More precisely,
we shall convert it into a form in which the non-negativity constraints are the only
inequality constraints, and the remaining constraints are equalities.

In slack form, each equation has the same set of variables on the RHS, and each of these
variables are also the only ones that appear in the objective function. We call the
variables on the LHS of the equalities basic variables and those on the RHS nonbasic
variables.

29.3 The simplex algorithm
==========================

The simplex algorithm is the classical method for solving linear programs. In contrast
to most of the other algorithms in this book, its running time is not polynomial in the
worst case.

The simplex algorithm can be viewed as Gaussian elimination for inequalities.

Associated with each iteration will be a "basic solution" that we can easily obtain from
the slack form of the linear program: set each nonbasic variable to 0 and compute the
values of the basic variables from the equality constraints. An iteration converts one
slack form into an equivalent slack form. The objective value of the associated basic
feasible solution will be no less than that at the previous iteration, and usually
greater. To achieve this increase in the objective value, we choose a nonbasic variable
such that if we were to increase that variable's value from 0, then the objective value
would increase, too. The amount by which we can increase the variable is limited by the
other equality constraints. In particular, we raise it until some basic variable becomes
0. We then rewrite the slack form, exchanging the roles of that basic variable and the
chosen nonbasic variable. Although we have used a particular setting of the variables to
guide the algorithm, the algorithm does not explicitly maintain this solution. It simply
rewrites the linear program until an optimal solution becomes "obvious" (i.e., the
objective function can no longer be increased).

In order to use the simplex algorithm, we must convert the linear program into slack
form. In addition to being an algebraic manipulation, slack is a useful algorithmic
concept. Recalling from Section 29.1 that each variable has a corresponding
non-negativity constraint, we say that an equality constraint is tight for a particular
setting of its nonbasic variables if they cause the constraint's basic variable to
become 0. Similarly, a setting of the nonbasic variables that would make a basic
variable become negative violates that constraint. Thus, the slack variables explicitly
maintain how far each constraint is from being tight, and so they help to determine how
much we can increase values of nonbasic variables without violating any of the
equality constraints.

We focus on the basic solution: set all the (nonbasic) variables on the right-hand side
to 0 and then compute the values of the (basic) variables on the left-hand side. An
iteration of the simplex algorithm rewrites the set of equations and the objective
function so as to put a different set of variables on the right-hand side. Thus, a
different basic solution is associated with the rewritten problem. We emphasize that the
rewrite does not in any way change the underlying linear-programming problem; the
problem at one iteration has the identical set of feasible solutions as the problem at
the previous iteration. The problem does, however, have a different basic solution than
that of the previous iteration.

If a basic solution is also feasible, we call it a basic feasible solution. As we run
the simplex algorithm, the basic solution is almost always a basic feasible solution.
However, for the first few iterations of the simplex algorithm, the basic solution might
not be feasible.

Our goal, in each iteration, is to reformulate the linear program so that the basic
solution has a greater objective value. We select a nonbasic variable x_e whose
coefficient in the objective function is positive, and we increase the value of x_e as
much as possible without violating any of the constraints. The variable x_e becomes
basic, and some other variable x_l becomes nonbasic. The values of other basic variables
and of the objective function may also change.

We pick the equation with the tightest constraint for a given nonbasic variable and
solve for that nonbasic variable in terms of the basic variable and the other nonbasic
variables in that equation. Then, we rewrite the other constraint equations and the
objective function in terms of the chosen nonbasic variable. When picking the nonbasic
variable, we must pick one that does not decrease the objective function.

We call this operation a pivot. A pivot chooses a nonbasic variable x_e, called the
entering variable, and a basic variable x_l, called the leaving variable, and exchanges
their roles in all the equality constraints and the objective function.

The linear program before and after the pivot is equivalent. We perform two operations
in the simplex algorithm: rewrite equations so that variables move between the left-hand
side and the right-hand side, and substitute one equation into another. The first
operation trivially creates an equivalent problem, and the second, by elementary linear
algebra, also creates an equivalent problem.

We continue pivoting until all coefficients in the objective function are negative. This
situation occurs only when we have rewritten the linear program so that the basic
solution is an optimal solution. The values of the slack variables in the final solution
measure how much slack remains in the original inequalities. Even though the
coefficients in the original slack form are integral, the coefficients in the other
linear programs are not necessarily integral, and the intermediate solutions are not
necessarily integral. Furthermore, the final solution to a linear program need not be
integral.

Pivoting
--------

The procedure pivot() takes as input a slack form, given by the tuple
(N, B, A, b, c, v), the index l of the leaving variable x_l, and the index e of the
entering variable x_e. It returns the tuple (N_hat, Bhat, Ahat, bhat, chat, vhat)
describing the new slack form.

The entries of A and Ahat in pivot() are actually the negatives of the coefficients that
appear in the slack form (or the same as the coefficients that appear in the standard
form).

The procedure pivot() works in three steps:

1. It computes the coefficients of the equation for the new basic variable x_e.
2. It updates the coefficients of the remaining equality constraints.
3. It updates the coefficients of the objective function.

pivot() is only ever called when A[l][e] is not 0.

The formal simplex algorithm
----------------------------

We assume that we have a procedure initialize_simplex(A, b, c) that takes as input a
linear program in standard form, that is an m x n matrix A, an m-vector b, and an
n-vector c. If the problem is infeasible, the procedure returns a message that the
problem is infeasible and then terminates. Otherwise, the procedures returns a slack
form for which the initial basic solution is feasible.

The procedure simplex() takes as input a linear program in standard form, as just
described. It returns an n-vector x_bar that is an optimal solution to the linear
program.

The procedure simplex() works as follows:

1. It calls the procedure initialize_simplex(A, b, c), described above, which either
determines that the linear program is infeasible or returns a slack form for which the
basic solution is feasible.
2. The while-loop forms the main part of the algorithm. If all coefficients in the
objective function are negative, then the while-loop terminates. Otherwise, we select a
variable x_e, whose coefficient in the objective function is positive, as the entering
variable.
3. Next, we check each constraint and pick the one that most severely limits the amount
by which we can increase x_e without violating any of the non-negativity constraints;
the basic variable associated with this constraint is x_l. If none of the constraints
limits the amount by which the entering variable can increase, the algorithm returns
"Unbounded!". Otherwise, we exchange the roles of the entering and leaving variables
by calling the procedure pivot().
4. Finally, we compute a solution, x_bar, for the original linear-programming variables
by setting all the nonbasic variables to 0 and each basic variable to b.

Termination
-----------

No iteration of the procedure simplex() can decrease the objective value associated with
the basic solution. Unfortunately, it is possible that an iteration leaves the objective
value unchanged. This phenomenon is called degeneracy.

Degeneracy can prevent the simplex algorithm from terminating, because it can lead to a
phenomenon known as cycling: the slack forms at two different iterations of the
procedure simplex() are identical. Because of degeneracy, simplex() could choose a
sequence of pivot operations that leave the objective value unchanged but repeat a slack
form within the sequence. Since simplex() is a deterministic algorithm, if it cycles,
then it will cycle through the same series of slack forms forever, never terminating.

Cycling is the only reason that simplex() might not terminate.

Cycling is theoretically possible, but extremely rare. We can prevent it by choosing the
entering and leaving variables somewhat more carefully. One option is to perturb the
input slightly so that it is impossible to have two solutions with the same objective
value. Another option is to break ties by always choosing the variable with the smallest
index, a strategy known as Bland's rule.

29.4 Duality
============

Linear-programming duality enables us to prove that a solution is indeed optimal. Given
a linear program in which the objective is to maximize, we can formulate a dual linear
program in which the objective is to minimize and whose optimal value is identical to
that of the original (primal) linear program.

To form the dual, we change the maximization to a minimization, exchange the roles of
coefficients on the RHS and the objective function, and replace each <= by a >=. Each of
the m constraints in the primal has an associated variable y_i in the dual, and each of
the n constraints in the dual has an associated variable x_j in the primal.

The optimal value of the dual linear program is always equal to the optimal value of the
primal linear program. Furthermore, the simplex algorithm actually implicitly solves
both the primal and dual programs simultaneously, thereby providing a proof of
optimality.

The negatives of the coefficients of the primal objective function are the values of the
dual variables.

29.5 The initial basic feasible solution
========================================

Finding an initial solution
---------------------------

A linear program can be feasible, yet the initial basic solution might not be feasible.
Thus, the procedure initialize_simplex() cannot just return any slack form. In order to
determine whether a linear program has any feasible solutions, we will formulate an
auxiliary linear program. For this auxiliary linear program we can find (with a little
work) a slack form for which the basic solution is feasible. Furthermore, the solution
of this auxiliary linear program determines whether the initial linear program is
feasible and if so, it provides a feasible solution with which we can initialize
simplex().

In order to determine whether a linear program has any feasible solutions, we formulate
an auxiliary linear program, L', using the procedure initialize_aux(). For L', we can
find a slack form for which the basic solution is feasible. Furthermore, the solution of
L' determines whether the original linear program, L, is feasible and if so, it provides
a feasible solution with which we can initialize simplex().

L is feasible iff the optimal objective value of L' is 0. If the optimal objective value
of L' is negative, then L does not have a feasible solution.

The input to initialize_simplex() is a linear program L in standard form.

The procedure initialize_aux() forms the auxiliary linear program by adding -x_0 to the
left-hand side of each constraint and setting the objective function to -x_0
(i.e., c[0] = -1).

The procedure return_aux() removes x_0 from the constrains and restores the original
objective function of L from L', but replaces each basic variable in this objective
function by the right-hand side of its associated constraint using the final slack form
of L'.

Fundamental theorem of linear programming
-----------------------------------------

Any linear program, L, given in standard form, either:

1. has an optimal solution with a finite object value,
2. is infeasible, or
3. is unbounded

If L is infeasible, the simplex algorithm returns "Infeasible!". If L is unbounded, the
simplex algorithm returns "Unbounded!". Otherwise, the simplex algorithm returns an
optimal solution with a finite objective value.

Intuition
---------

1. We start with a system of inequalities in standard form. Objective function is to
maximize, all inequalities are <= inequalities and the non-negativity constraints and
all >= constraints.

2. We transform the standard form to the slack form. All inequalities become equalities
with appropriate basic variable designations on the LHS.

3. Our goal in each iteration of the simplex algorithm is to reformulate the linear
program so that the basic solution has a greater objective value.

4. At each iteration, we select a nonbasic variable x_e whose coefficient in the
objective function is positive, and we increase the value of x_e as much as possible
without violating any of the equality constraints.

5. The variable x_e becomes basic, and some other variable x_l becomes nonbasic.

6. The values of other basic variables and of the objective function may also change.

7. If the simplex algorithm returns "Unbounded!", it means that increasing the objective
value via any of the nonbasic variables results in all of the basic variables
increasing without bound.

8. In order to determine if a linear program has any feasible solutions to begin with,
the initialize_simplex() procedure formulates an auxiliary linear program with a new
variable x_0. The objective of the auxiliary linear program is to maximize -x_0. The
original linear program has a feasible solution iff the optimal objective value of
the auxiliary linear program is 0. If the simplex algorithm returns "Infeasible!", it
means that the original linear program does not have a feasible solution at all.

9. Otherwise, the initialize_simplex() procedure will return a slack form for which the
basic solution is feasible and the simplex() procedure can use that slack form to start
and the simplex() procedure will return an optimal solution.

Complexity
==========

Time
----

simplex(): Exponential in the worst case, polynomial in practice.
"""


def exclude(list_, item):
    return [x for x in list_ if x != item]


def include(l1, l2):
    return [x for x in l1 if x in l2]


def initialize_aux(A, k):
    n, m = len(A[0]), len(A)
    N = list(range(1, n + 1))
    Naux = [0] + N
    Baux = [Naux[-1] + i for i in range(1, m + 1)]
    Aaux = [[0] * len(Naux) for _ in range(len(Baux))]
    for row in range(len(Baux)):
        Aaux[row][0] = -1
        for col in range(1, len(Naux)):
            Aaux[row][col] = A[row][col - 1]
    caux = [0] * len(Naux)
    caux[0] = -1
    return N, Naux, Baux, Aaux, caux, len(Naux) + k


def initialize_simplex(A, b, c):
    n, m, k = len(A[0]), len(A), b.index(min(b))
    if b[k] >= 0:
        return list(range(n)), list(range(n, n + m)), A, b, c, 0
    N, Naux, Baux, Aaux, caux, l = initialize_aux(A, k)
    Naux, Baux, Aaux, baux, caux, vaux = pivot(Naux, Baux, Aaux, b, caux, 0, l, 0)
    x_bar, Naux, Baux, Aaux, baux, caux, vaux = simplex(
        Aaux, baux, caux, Naux, Baux, vaux
    )
    if x_bar[0] == 0:
        if Baux[0] == 0:
            i, e = 0, Naux[0]
            while Aaux[0][Naux.index(e)] == 0:
                i += 1
                e = Naux[i]
            Naux, Baux, Aaux, baux, caux, vaux = pivot(
                Naux, Baux, Aaux, baux, caux, e, l, vaux
            )
        return return_aux(N, c, Naux, Baux, Aaux, baux, vaux)
    return "Infeasible!"


def pivot(N, B, A, b, c, e, l, v):
    assert e in N and l in B
    n, m, Ne, Bl = len(N), len(B), N.index(e), B.index(l)
    Ahat, bhat = [[0] * n for _ in range(m)], [0] * m
    Nhat, Bhat = list(N), list(B)
    Nhat[Ne], Bhat[Bl] = B[Bl], N[Ne]
    Nhat, Bhat = sorted(Nhat), sorted(Bhat)
    Nhatl, Bhate = Nhat.index(l), Bhat.index(e)
    pivot_var, no_e, no_l = A[Bl][Ne], exclude(N, e), exclude(B, l)
    for i in no_e:
        Ahat[Bhate][Nhat.index(i)] = A[Bl][N.index(i)] / pivot_var
    Ahat[Bhate][Nhatl], bhat[Bhate] = 1 / pivot_var, b[Bl] / pivot_var
    for i in no_l:
        Bhati, Bi = Bhat.index(i), B.index(i)
        pivot_var = A[Bi][Ne]
        bhat[Bhati] = b[Bi] - pivot_var * bhat[Bhate]
        for j in no_e:
            Nhatj = Nhat.index(j)
            Ahat[Bhati][Nhatj] = A[Bi][N.index(j)] - pivot_var * Ahat[Bhate][Nhatj]
        Ahat[Bhati][Nhatl] = -pivot_var * Ahat[Bhate][Nhatl]
    chat, vhat = [0] * len(Nhat), v + c[Ne] * bhat[Bhate]
    for i in no_e:
        Nhati = Nhat.index(i)
        chat[Nhati] = c[N.index(i)] - c[Ne] * Ahat[Bhate][Nhati]
    chat[Nhatl] = -c[Ne] * Ahat[Bhate][Nhatl]
    return Nhat, Bhat, Ahat, bhat, chat, vhat


def return_aux(N, c, Naux, Baux, Aaux, baux, vaux):
    n, m = len(Aaux[0]), len(Aaux)
    Naux.pop(0)
    Ahat = [[0] * len(Naux) for _ in range(len(Baux))]
    for row in range(m):
        for col in range(1, n):
            Ahat[row][col - 1] = Aaux[row][col]
    vaux += sum(-baux[Baux.index(i)] for i in include(N, Baux))
    caux = [0] * len(Naux)
    for i in include(N, Naux):
        caux[Naux.index(i)] = c[N.index(i)]
    for i in include(N, Baux):
        cval = -c[N.index(i)]
        for j, x in enumerate(Ahat[Baux.index(i)]):
            caux[j] += cval * x
    return Naux, Baux, Ahat, baux, caux, vaux


def simplex(A, b, c, N=None, B=None, v=None):
    if any(x is None for x in [N, B, v]):
        val = initialize_simplex(A, b, c)
        if isinstance(val, str):
            return val
        N, B, A, b, c, v = val
    delta = [0] * len(A)
    while any(c[N.index(i)] > 1e-12 for i in N):
        e = min([i for i in N if c[N.index(i)] > 0])
        Ne = N.index(e)
        for i in B:
            Bi = B.index(i)
            delta[Bi] = b[Bi] / A[Bi][Ne] if A[Bi][Ne] > 0 else float("inf")
        l = B[delta.index(min(delta))]
        if delta[B.index(l)] == float("inf"):
            return "Unbounded!"
        N, B, A, b, c, v = pivot(N, B, A, b, c, e, l, v)
    x_bar = [0] * (max(N[-1], B[-1]) + 1)
    for i in B:
        x_bar[i] = b[B.index(i)]
    return x_bar, N, B, A, b, c, v
