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


def pivot(N, B, A, b, c, e, l, v=0):
    n, m, o = len(N), len(B), len(c)
    Ahat = [[0 for _ in range(n)] for _ in range(m)]
    bhat, chat = [0 for _ in range(n)], [0 for _ in range(o)]
    Bhat, Nhat = list(B), list(N)
    Bhat[l] = N[e]
    Nhat[e] = B[l]
    Bhat, Nhat = sorted(Bhat), sorted(Nhat)
    bhat[e] = b[l] / A[l][e]
    no_e = [x for i, x in enumerate(N) if i != e]
    no_l = [x for i, x in enumerate(B) if i != l]
    for j in no_e:
        x, y = Bhat.index(0), Nhat.index(j)
        Ahat[x][y] = A[l][j] / A[l][e]
    Ahat[e][l] = 1 / A[l][e]
    for i in no_l:
        x, x_ = Bhat.index(i), B.index(i)
        bhat[x] = b[x_] - A[x_][e] * bhat[e]
        for j in no_e:
            y, y_ = Nhat.index(j), N.index(j)
            Ahat[x][y] = A[x_][y_] - A[x_][e] * Ahat[e][y_]
        Ahat[x][l] = -A[x_][e] * Ahat[e][l]
    vhat = v + c[e] * bhat[e]
    for j in no_e:
        x, x_ = Nhat.index(j), N.index(j)
        chat[x] = c[x_] - c[e] * Ahat[e][x]
    chat[l] = -c[e] * Ahat[e][l]
    return Nhat, Bhat, Ahat, bhat, chat, vhat


N = [0, 1, 2]
B = [3, 4, 5]
A = [[1, 1, 3], [2, 2, 5], [4, 1, 2]]
b = [30, 24, 36]
c = [3, 1, 2]
e = N.index(0)
l = B.index(5)
Nhat, Bhat, Ahat, bhat, chat, vhat = pivot(N, B, A, b, c, e, l)
assert Nhat == [1, 2, 5]
assert Bhat == [0, 3, 4]
assert Ahat == [[0.25, 0.5, 0.25], [0.5, 2.75, -0.25], [1.0, 4.5, -0.5]]
assert bhat == [9.0, 21.0, 6.0]
assert chat == [0.25, 0.5, -0.75]
assert vhat == 27.0
