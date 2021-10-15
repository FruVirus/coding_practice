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
    n, m, o = len(N), len(B), len(c)
    Ahat = [[0 for _ in range(n)] for _ in range(m)]
    bhat, chat = [0 for _ in range(n)], [0 for _ in range(o)]
    Bhat, Nhat = list(B), list(N)
    Bhat[l] = N[e]
    Nhat[e] = B[l]
    Bhat, Nhat = sorted(Bhat), sorted(Nhat)
    bhat[N[e]] = b[l] / A[l][e]
    no_e = [x for i, x in enumerate(N) if i != e]
    no_l = [x for i, x in enumerate(B) if i != l]
    for j in no_e:
        x, x_ = Nhat.index(j), N.index(j)
        Ahat[N[e]][x] = A[l][x_] / A[l][e]
    Ahat[N[e]][N.index(l)] = 1 / A[l][e]
    for i in no_l:
        x, x_ = Bhat.index(i), B.index(i)
        bhat[x] = b[x_] - A[x_][e] * bhat[N[e]]
        for j in no_e:
            y, y_ = Nhat.index(j), N.index(j)
            Ahat[x][y] = A[x_][y_] - A[x_][e] * Ahat[N[e]][y]
        Ahat[x][N.index(l)] = -A[x_][e] * Ahat[N[e]][N.index(l)]
    vhat = v + c[e] * bhat[N[e]]
    for j in no_e:
        x, x_ = Nhat.index(j), N.index(j)
        chat[x] = c[x_] - c[e] * Ahat[N[e]][x]
    chat[N.index(l)] = -c[e] * Ahat[N[e]][N.index(l)]
    return Nhat, Bhat, Ahat, bhat, chat, vhat


def simplex(A, b, c):
    N, B, A, b, c, v = initialize_simplex(A, b, c)
    n, m = len(N), len(B)
    delta, x_bar = [0 for _ in range(m)], [0 for _ in range(n)]
    while any(c[N.index(x)] > 0 for x in N):
        e = min([N.index(x) for x in N if c[N.index(x)] > 0])
        for i in B:
            j = B.index(i)
            delta[j] = b[j] / A[j][e] if A[j][e] > 0 else float("inf")
        l = delta.index(min([delta[B.index(x)] for x in B]))
        if delta[l] == float("inf"):
            return "Unbounded!"
        print("N: ", N)
        print("B: ", B)
        print("A: ", A)
        print("b: ", b)
        print("c: ", c)
        print("e: ", e)
        print("l: ", l)
        print("v: ", v)
        print("delta: ", delta)
        print()
        N, B, A, b, c, v = pivot(N, B, A, b, c, e, l, v)
    for i in range(n):
        x_bar[i] = b[i] if i in B else 0
    return x_bar


# A = [[1, 1, 3], [2, 2, 5], [4, 1, 2]]
# b = [30, 24, 36]
# c = [3, 1, 2]
# print(simplex(A, b, c))

# N = [0, 1, 2]
# B = [3, 4, 5]
# A = [[1, 1, 3], [2, 2, 5], [4, 1, 2]]
# b = [30, 24, 36]
# c = [3, 1, 2]
# e = N.index(0)
# l = B.index(5)
# v = 0
# N = [1, 2, 5]
# B = [0, 3, 4]
# A = [[0.25, 0.5, 0.25], [0.75, 2.5, -0.25], [1.5, 4.0, -0.5]]
# b = [9.0, 21.0, 6.0]
# c = [0.25, 0.5, -0.75]
# e = N.index(2)
# l = B.index(4)
# v = 27.0
N = [1, 4, 5]
B = [0, 2, 3]
A = [[1 / 16, -1 / 8, 5 / 16], [3 / 8, 1 / 4, -1 / 8], [-3 / 16, -5 / 8, 1 / 16]]
b = [33 / 4, 3 / 2, 69 / 4]
c = [1 / 16, -1 / 8, -11 / 16]
e = N.index(1)
l = B.index(2)
v = 111 / 4
Nhat, Bhat, Ahat, bhat, chat, vhat = pivot(N, B, A, b, c, e, l, v)
print(Nhat)
print(Bhat)
print(Ahat)
print(bhat)
print(chat)
print(vhat)
# assert Nhat == [1, 2, 5]
# assert Bhat == [0, 3, 4]
# assert Ahat == [[0.25, 0.5, 0.25], [0.75, 2.5, -0.25], [1.5, 4, -0.5]]
# assert bhat == [9.0, 21.0, 6.0]
# assert chat == [0.25, 0.5, -0.75]
# assert vhat == 27.0
