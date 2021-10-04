"""
Overview
========

We can formulate a linear system as a matrix equation in which each matrix or vector
element belongs to a field, typically the real numbers (e.g., Ax = b). lup() solves
such a system of linear equations using a method called LUP decomposition. LUP
decomposition is numerically stable and has the advantage of being faster in practice
then the approach of computing the inverse of A and then multiplying by b.

We only treat the case where there are exactly n equations in n unknowns; i.e., the rank
of A is equal to the number n of unknowns and A is non-singular so that x = A^-1 * b

If the rank of A is less than n, then the system is under-determined and the system will
typically have infinitely many solutions, although no solutions at all if the equations
are inconsistent.

If the rank of A exceeds the number n of unknowns, then the system is overdetermined and
there may not exist any solutions.

The idea of LUP decomposition is to find three n x n matrices L, U, and P such that:

    PA = LU

where:
    L is a unit lower-triangular matrix
    U is an upper-triangular matrix
    P is a permutation matrix

Every non-singular matrix posses such a decomposition.

Once we have found an LUP decomposition for A, we can solve the system of equations,
Ax = b, by solving only the triangular linear systems by multiplying both sides of
Ax = b by, which yields PAx = Pb. This amounts to permuting the system of equations.

    PAx = Pb
    LUx = Pb --> y = Ux
        Ly = Pb --> solve for y using forward substitution
        Ux = y --> solve for x using back substitution

    since P is invertible, P^(-1)PA = P^(-1)LU --> A = P^(-1)LU

    Ax = P^(-1)LUx
       = P^(-1)Ly
       = P^(-1)Pb
       = b

Complexity
==========


"""
