"""
Introduction
============

Many problems take the form of maximizing or minimizing an objective, given limited
resources and competing constraints. If we can specify the objective as a linear
function of certain variables, and if we can specify the constraints on resources as
equalities or inequalities on those variables, then we have a linear-programming
problem.

Formally, a linear-programming problem is the problem of either minimizing or maximizing
a linear function subject to a finite set of linear constraints. If we are to minimize,
then we call the linear program a minimization linear program and if we are to maximize,
then we call the linear program a maximization linear program. In linear programming, we
do not allow strict inequalities.

If we add to a linear program the additional requirement that all variables take on
integer values, we have an integer linear program. Since no polynomial-time algorithms
are known for any NP-hard problems, there is no known polynomial-time algorithm for
integer linear programming. In contrast, we can solve a general linear-programming
problem in polynomial time.

Canonical Forms
===============

In order to describe properties of and algorithms for linear programs, we find it
convenient to express them in canonical forms. We shall use two forms, standard and
slack.

Informally, a linear program in standard form is the maximization of a linear function
subject to linear inequalities, whereas a linear program in slack form is the
maximization of a linear function subject to linear equalities.

Convex Region
=============

A convex region is a region that fulfills the requirement that for any two points in the
region, all points on a line segment between them are also in the region.

Hyperplane
==========

In geometry, a hyperplane is a subspace whose dimension is one less than that of its
ambient space. If a space is 3-dimensional then its hyperplanes are the 2-dimensional
planes, while if the space is 2-dimensional, its hyperplanes are the 1-dimensional
lines. This notion can be used in any general space in which the concept of the
dimension of a subspace is defined.

Simplex
=======

In geometry, a simplex is a generalization of the notion of a triangle or tetrahedron to
arbitrary dimensions. The simplex is so-named because it represents the simplest
possible polytope in any given space.

For example,

    1. A 0-simplex is a point,
    2. A 1-simplex is a line segment,
    3. A 2-simplex is a triangle,
    4. A 3-simplex is a tetrahedron,
    6. A 4-simplex is a 5-cell.

Solutions
=========

We call any setting of the variables that satisfy all the constraints a feasible
solution to the linear program. The set of feasible solutions forms a convex region. We
call this convex region the feasible region and the function we wish to maximize the
objective function. Conceptually, we could evaluate the objective function at each point
in the feasible region; we call the value of the objective function at a particular
point the objective value. We could then identify a point that has the maximum objective
value as an optimal solution.

For most linear programs however, the feasible region contains an infinite number of
points, and so we need to determine an efficient way to find a point that achieves the
maximum objective value without explicitly evaluating the objective function at every
point in the feasible region.

In 2D, an optimal solution to the linear program occurs at a vertex of the feasible
region. The maximum value must be on the boundary of the feasible region, and thus the
intersection of the constraint line with the boundary of the feasible region is either a
single vertex or a line segment. If the intersection is a single vertex, then there is
just one optimal solution, and it is that vertex. If the intersection is a line segment,
every point on that line segment must have the same objective value; in particular, both
endpoints of the line segment are optimal solutions. Since each endpoint of a line
segment is a vertex, there is an optimal solution at a vertex in this case as well.

The same intuition holds in n dimensions. If we have n variables, each constraint
defines a half-space in n-dimensional space. We call the feasible region formed by the
intersection of these half-spaces a simplex. The objective function is now a hyperplane
and, because of convexity, an optimal solution still occurs at a vertex of the simplex.

Linear programs can have no solutions, no finite optimal solution, or a situation where
the origin is not a feasible solution.
"""
