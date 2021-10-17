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

# pylint: disable=C0200


def initialize_simplex(A, b, c):
    assert len(A) == len(b)
    assert len(A[0]) == len(c)
    k = b.index(min(b))
    if b[k] >= 0:
        n, m = len(A[0]), len(A)
        return list(range(n)), list(range(n, n + m)), A, b, c, 0
    Norig, corig = list(range(1, len(A[0]) + 1)), c
    N = list(range(len(A[0]) + 1))
    B = [N[-1] + i for i in range(1, len(b) + 1)]
    Ahat = [[0 for _ in range(len(N))] for _ in range(len(B))]
    for row in range(len(A)):
        for col in range(len(A[0]) + 1):
            Ahat[row][col] = -1 if col == 0 else A[row][col - 1]
    c = [0 for _ in range(len(c) + 1)]
    c[0] = -1
    l = len(N) + k
    N, B, A, b, c, v = pivot(N, B, Ahat, b, c, 0, l, 0)
    x_bar, N, B, A, b, c, v = simplex(A, b, c, N=N, B=B, v=v)
    if x_bar[0] == 0:
        if B[0] == 0:
            i, e = 0, N[0]
            while A[0][N.index(e)] == 0:
                i += 1
                e = N[i]
            N, B, A, b, corig, v = pivot(N, B, A, b, c, e, l, v)
        N.pop(N.index(0))
        n, m = len(N), len(B)
        Ahat = [[0 for _ in range(n)] for _ in range(m)]
        for row in range(len(A)):
            for col in range(1, len(A[0])):
                Ahat[row][col - 1] = A[row][col]
        e = [i for i in Norig if i in B]
        assert e
        Norige, Be = Norig.index(e[0]), B.index(e[0])
        vhat = v + corig[Norige] * b[Be]
        no_e = [x for x in Norig if x != e[0]]
        chat = [0 for _ in range(n)]
        for j in no_e:
            Nhatj, Nj = N.index(j), Norig.index(j)
            chat[Nhatj] = corig[Nj] - corig[Norige] * Ahat[Be][Nhatj]
        chat[Norige] = -corig[Norige] * Ahat[Be][Norige]
        return N, B, Ahat, b, chat, vhat
    return "Infeasible!"


def pivot(N, B, A, b, c, e, l, v):
    assert e in N and l in B
    n, m, o = len(N), len(B), len(c)
    Ahat = [[0 for _ in range(n)] for _ in range(m)]
    bhat, chat = [0 for _ in range(m)], [0 for _ in range(o)]
    Bhat, Nhat = list(B), list(N)
    Bl, Ne = B.index(l), N.index(e)
    Bhat[Bl] = N[Ne]
    Nhat[Ne] = B[Bl]
    Bhat, Nhat = sorted(Bhat), sorted(Nhat)
    Bhate, Nhatl = Bhat.index(e), Nhat.index(l)
    bhat[Bhate] = b[Bl] / A[Bl][Ne]
    no_e, no_l = [x for x in N if x != e], [x for x in B if x != l]
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
    vhat = v + c[Ne] * bhat[Bhate]
    for j in no_e:
        Nhatj, Nj = Nhat.index(j), N.index(j)
        chat[Nhatj] = c[Nj] - c[Ne] * Ahat[Bhate][Nhatj]
    chat[Nhatl] = -c[Ne] * Ahat[Bhate][Nhatl]
    return Nhat, Bhat, Ahat, bhat, chat, vhat


def simplex(A, b, c, N=None, B=None, v=None):
    if any(x is None for x in [N, B, v]):
        N, B, A, b, c, v = initialize_simplex(A, b, c)
    n, m = len(N), len(B)
    delta, x_bar = [0 for _ in range(m)], [0 for _ in range(n + m)]
    while any(c[N.index(x)] > 0 for x in N):
        e = min([x for x in N if c[N.index(x)] > 0])
        Ne = N.index(e)
        for i in B:
            Bi = B.index(i)
            delta[Bi] = b[Bi] / A[Bi][Ne] if A[Bi][Ne] > 0 else float("inf")
        l = B[delta.index(min([delta[B.index(i)] for i in B]))]
        if delta[B.index(l)] == float("inf"):
            return "Unbounded!"
        N, B, A, b, c, v = pivot(N, B, A, b, c, e, l, v)
    for index, i in enumerate(B):
        x_bar[i] = b[index]
    return x_bar, N, B, A, b, c, v
