"""
Overview
========

The simplex algorithm takes as input a linear program and returns an optimal solution.
It starts at some vertex of the simplex and performs a sequence of iterations. In each
iteration, it moves along an edge of the simplex from a current vertex to a neighboring
vertex whose objective value is no smaller than that of the current vertex (and usually
is larger).

The simplex algorithm terminates when it reaches a local maximum, which is a vertex from
which all neighboring vertices have a smaller objective value. Because the feasible
region is convex and the objective function is linear, this local optimum is actually a
global optimum.

We first write the given linear program in slack form, which is a set of linear
equalities. These linear equalities express some of the variables, called "basic
variables", in terms of other variables, called "non-basic variables". We move from one
vertex to another by making a basic variable become non-basic and making a non-basic
variable become basic. We call this operation a "pivot" and, viewed algebraically, it is
nothing more than rewriting the linear program in an equivalent slack form.

To efficiently solve a linear program with the simplex algorithm, we prefer to express
it in a form in which some of the constraints are equality constraints. More precisely,
we shall convert it into a form in which the non-negativity constraints are the only
inequality constraints, and the remaining constraints are equalities.

Fundamental Theorem of Linear Programming
-----------------------------------------

Any linear program, L, given in standard form, either:

1. has an optimal solution with a finite object value,
2. is infeasible, or
3. is unbounded

If L is infeasible, the simplex algorithm returns "Infeasible!". If L is unbounded, the
simplex algorithm returns "Unbounded!". Otherwise, the simplex algorithm returns an
optimal solution with a finite objective value.

initialize_simplex()
--------------------

A linear program can be feasible, yet the initial basic solution might not be feasible
(e.g., the initial basic solution might set the solution to be negative and violate the
non-negativity constraints). In order to determine whether a linear program has any
feasible solutions, we formulate an auxility linear program, L'. For L', we can find a
slack form for which the basic solution is feasible. Furthermore, the solution of L'
determines whether L is feasible and if so, it provides a feasible solution with which
we can initialize simplex().

L is feasible iff the optimal objective value of L' is 0. If the optimal objective value
of L' is negative, then L does not have a feasible solution.

The input to initialize_simple() is a linear program L in standard form.

pivot()
-------

A pivot operation chooses a non-basic variable x_e, called the entering variable, and a
basic variable x_l, called the leaving variable, and exchanges their roles in the linear
program.

The entries of A and Ahat in pivot() are actually the negatives of the coefficients that
appear in the slack form (or the same as the coefficients that appear in the standard
form).

pivot() is only ever called when A[l][e] is not 0.

simplex()
---------

simplex() takes as input a linear program in standard form and return an n-vector,
x_bar, that is an optimal solution to the linear program. Each iteration of the
while-loop in simplex() exchanges the role of a basic and non-basic variable by calling
pivot(). The slack form is equivalent to the one from the previous iteration which, by
the loop invariant, is equivalent to the initial slack form.

Degeneracy and Cycling
----------------------

No iteration of simplex() can decrease the objective value associated with the basic
solution. However, it is possible that an iteration leaves the objective value
unchanged. This phenomenon is called degeneracy.

Degeneracy can prevent the simplex algorithm from terminating, because it can lead to a
phenomenon known as cycling: the slack forms at two different iterations of simplex()
are identical. Because of degeneracy, the simplex algorithm could choose a sequence of
pivot operations that leave the objective value unchanged but repeat a slack form within
the sequence. Since simplex() is a deterministic algorithm, if it cycles, then it will
cycle through the same series of slack forms forever, never terminating.

Cycling is the only reason that simplex() might not terminate. if simplex() fails to
terminate in at most (n + m) choose m iterations, then it cycles. There are n + m
variables and |B| = m; therefore, there are at most (n + m) choose m ways to choose B.

We can prevent cycling by perturbing the input slightly so that it is impossible to have
two solutions with the same object value. Another option is to break ties by always
choosing the variable with the smallest index, a strategy known as Bland's rule.

Duality
-------

Linear-programming duality enables us to prove that a solution is indeed optimal. Given
a linear program in which the objective is to maximize, we can formulate a dual linear
program in which the objective is to minimize and whose optimal vlaue is identical to
that of the original (primal) linear program.

To form the dual, we change the maximization to a minimization, exhcnage the roles of
coefficients on the RHS and the objective function, and replace each <= by a >=. Each of
the m constraints in the primal has an associated variable y_i in the dual, and each of
the n constraints in the dual has an associated variable x_j in the primal.

The optimal value of the dual linear program is always equal to the optimal value of the
primal linear program. Furthermore, the simplex algorithm actually implicitly solves
both the primal and dual programs simultaneously, thereby providing a proof of
optimality.

The negatives of the coefficients of the primal objective function are the values of the
dual variables.
"""

# pylint: disable=C0200


def exclude(list_, item):
    return [x for x in list_ if x != item]


def initialize_simplex(A, b, c):
    assert len(A) == len(b) and len(A[0]) == len(c)
    k = b.index(min(b))
    if b[k] >= 0:
        n, m = len(A[0]), len(A)
        return list(range(n)), list(range(n, n + m)), A, b, c, 0
    N = list(range(1, len(A[0]) + 1))
    Naux = [0] + N
    Baux = [Naux[-1] + i for i in range(1, len(b) + 1)]
    Aaux = [[0 for _ in range(len(Naux))] for _ in range(len(Baux))]
    for row in range(len(A)):
        for col in range(len(A[0]) + 1):
            Aaux[row][col] = -1 if col == 0 else A[row][col - 1]
    baux = b
    caux = [0 for _ in range(len(c) + 1)]
    caux[0] = -1
    e = 0
    l = len(Naux) + k
    vaux = 0
    Naux, Baux, Aaux, baux, caux, vaux = pivot(Naux, Baux, Aaux, baux, caux, e, l, vaux)
    val = simplex(Aaux, baux, caux, Naux, Baux, vaux)
    if isinstance(val, str):
        return val
    x_bar, Naux, Baux, Aaux, baux, caux, vaux = val
    if x_bar[0] == 0:
        if Baux[0] == 0:
            i, e = 0, Naux[0]
            while A[0][Naux.index(e)] == 0:
                i += 1
                e = Naux[i]
            Naux, Baux, Aaux, baux, caux, vaux = pivot(
                Naux, Baux, Aaux, baux, caux, e, l, vaux
            )
        Naux.pop(Naux.index(0))
        n, m = len(Naux), len(Baux)
        Ahat = [[0 for _ in range(n)] for _ in range(m)]
        for row in range(len(Aaux)):
            for col in range(1, len(Aaux[0])):
                Ahat[row][col - 1] = Aaux[row][col]
        caux = update_caux(N, c, Naux, Baux, Ahat)
        vaux = update_vaux(N, c, Baux, baux, vaux)
        return Naux, Baux, Ahat, baux, caux, vaux
    return "Infeasible!"


def pivot(N, B, A, b, c, e, l, v):
    assert e in N and l in B
    n, m = len(N), len(B)
    Ahat, bhat = [[0 for _ in range(n)] for _ in range(m)], [0 for _ in range(m)]
    Bhat, Nhat = list(B), list(N)
    Bl, Ne = B.index(l), N.index(e)
    Bhat[Bl], Nhat[Ne] = N[Ne], B[Bl]
    Bhat, Nhat = sorted(Bhat), sorted(Nhat)
    Bhate, Nhatl = Bhat.index(e), Nhat.index(l)
    bhat[Bhate] = b[Bl] / A[Bl][Ne]
    no_e, no_l = exclude(N, e), exclude(B, l)
    for j in no_e:
        Nhatj, Nj = Nhat.index(j), N.index(j)
        Ahat[Bhate][Nhatj] = A[Bl][Nj] / A[Bl][Ne]
    Ahat[Bhate][Nhatl] = 1 / A[Bl][Ne]
    for i in no_l:
        Bhati, Bi = Bhat.index(i), B.index(i)
        bhat[Bhati] = b[Bi] - A[Bi][Ne] * bhat[Bhate]
        for j in no_e:
            Nhatj, Nj = Nhat.index(j), N.index(j)
            Ahat[Bhati][Nhatj] = A[Bi][Nj] - A[Bi][Ne] * Ahat[Bhate][Nhatj]
        Ahat[Bhati][Nhatl] = -A[Bi][Ne] * Ahat[Bhate][Nhatl]
    c, v = update_cv(N, c, v, Nhat, Ahat, bhat, Ne, Nhatl, Bhate, no_e)
    return Nhat, Bhat, Ahat, bhat, c, v


def update_caux(N, c, Naux, Baux, Ahat):
    caux = [0 for _ in range(len(Naux))]
    for i in N:
        if i in Naux:
            caux[Naux.index(i)] = c[N.index(i)]
    for i in N:
        if i in Baux:
            row = list(Ahat[Baux.index(i)])
            cval = -c[N.index(i)]
            for x in range(len(row)):
                row[x] = cval * row[x]
            for j, x in enumerate(row):
                caux[j] += x
    return caux


def update_cv(N, c, v, Nhat, Ahat, bhat, Ne, Nhatl, Bhate, no_e):
    v += c[Ne] * bhat[Bhate]
    chat = [0 for _ in range(len(c))]
    for j in no_e:
        Nhatj, Nj = Nhat.index(j), N.index(j)
        chat[Nhatj] = c[Nj] - c[Ne] * Ahat[Bhate][Nhatj]
    chat[Nhatl] = -c[Ne] * Ahat[Bhate][Nhatl]
    for chati, i in enumerate(chat):
        if abs(i) < 1e-12:
            chat[chati] = 0
    return chat, v


def update_vaux(N, c, Baux, baux, vaux):
    for i in N:
        if i in Baux:
            cval = c[N.index(i)]
            sgn = -1 if cval < 0 else 1
            vaux += sgn * baux[Baux.index(i)]
    return vaux


def simplex(A, b, c, N=None, B=None, v=None):
    if any(x is None for x in [N, B, v]):
        val = initialize_simplex(A, b, c)
        if isinstance(val, str):
            return val
        N, B, A, b, c, v = val
    delta = [0 for _ in range(len(B))]
    while any(c[i] > 0 for i in range(len(N))):
        e = min([x for i, x in enumerate(N) if c[i] > 0])
        Ne = N.index(e)
        for Bi, i in enumerate(B):
            delta[Bi] = b[Bi] / A[Bi][Ne] if A[Bi][Ne] > 0 else float("inf")
        l = B[delta.index(min(delta))]
        Bl = B.index(l)
        if delta[Bl] == float("inf"):
            return "Unbounded!"
        N, B, A, b, c, v = pivot(N, B, A, b, c, e, l, v)
    x_bar = [0 for _ in range(max(N[-1], B[-1]) + 1)]
    for index, i in enumerate(B):
        x_bar[i] = b[index]
    return x_bar, N, B, A, b, c, v


A = [[1, -1], [-1, -1], [-1, 4]]
b = [8, -3, 2]
c = [1, 3]
print(simplex(A, b, c))
