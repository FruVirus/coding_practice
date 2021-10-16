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
"""


def initialize_simplex(A, b, c):
    N = [0, 1, 2]
    B = [3, 4, 5]
    A = [[1, 1, 3], [2, 2, 5], [4, 1, 2]]
    b = [30, 24, 36]
    c = [3, 1, 2]
    v = 0
    return N, B, A, b, c, v


def pivot(N, B, A, b, c, e, l, v):
    assert e in N
    assert l in B
    n, m, o = len(N), len(B), len(c)
    Ahat = [[0 for _ in range(n)] for _ in range(m)]
    bhat, chat = [0 for _ in range(n)], [0 for _ in range(o)]
    Bhat, Nhat = list(B), list(N)
    Bhat[B.index(l)] = N[N.index(e)]
    Nhat[N.index(e)] = B[B.index(l)]
    Bhat, Nhat = sorted(Bhat), sorted(Nhat)
    assert e in Bhat
    assert l in Nhat
    bhat[Bhat.index(e)] = b[B.index(l)] / A[B.index(l)][N.index(e)]
    no_e, no_l = [x for x in N if x != e], [x for x in B if x != l]
    for j in no_e:
        Ahat[Bhat.index(e)][Nhat.index(j)] = (
            A[B.index(l)][N.index(j)] / A[B.index(l)][N.index(e)]
        )
    Ahat[Bhat.index(e)][Nhat.index(l)] = 1 / A[B.index(l)][N.index(e)]
    for i in no_l:
        bhat[Bhat.index(i)] = (
            b[B.index(i)] - A[B.index(i)][N.index(e)] * bhat[Bhat.index(e)]
        )
        for j in no_e:
            Ahat[Bhat.index(i)][Nhat.index(j)] = (
                A[B.index(i)][N.index(j)]
                - A[B.index(i)][N.index(e)] * Ahat[Bhat.index(e)][Nhat.index(j)]
            )
        Ahat[Bhat.index(i)][Nhat.index(l)] = (
            -A[B.index(i)][N.index(e)] * Ahat[Bhat.index(e)][Nhat.index(l)]
        )
    vhat = v + c[N.index(e)] * bhat[Bhat.index(e)]
    for j in no_e:
        chat[Nhat.index(j)] = (
            c[N.index(j)] - c[N.index(e)] * Ahat[Bhat.index(e)][Nhat.index(j)]
        )
    chat[Nhat.index(l)] = -c[N.index(e)] * Ahat[Bhat.index(e)][Nhat.index(l)]
    return Nhat, Bhat, Ahat, bhat, chat, vhat


def simplex(A, b, c):
    N, B, A, b, c, v = initialize_simplex(A, b, c)
    n, m = len(N), len(B)
    delta, x_bar = [0 for _ in range(m)], [0 for _ in range(n + m)]
    while any(c[N.index(x)] > 0 for x in N):
        e = min([x for x in N if c[N.index(x)] > 0])
        for i in B:
            delta[B.index(i)] = (
                b[B.index(i)] / A[B.index(i)][N.index(e)]
                if A[B.index(i)][N.index(e)] > 0
                else float("inf")
            )
        l = B[delta.index(min([delta[B.index(i)] for i in B]))]
        if delta[B.index(l)] == float("inf"):
            return "Unbounded!"
        N, B, A, b, c, v = pivot(N, B, A, b, c, e, l, v)
    for index, i in enumerate(B):
        x_bar[i] = b[index]
    return x_bar
