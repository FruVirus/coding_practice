"""
31.5 The Chinese remainder theorem
==================================

The "Chinese remainder theorem" provides a correspondence between a system of equations
modulo a set of pairwise relatively prime moduli (e.g., 3, 5, and 7) and an equation
modulo their product (e.g., 105). For example, for 3, 5, and 7, all solutions are of the
form 23 + 105 * k, for arbitrary integers k.

The Chinese remainder theorem has two major applications. Let the integer n be factored
as n = n_1 * n_2 * ... * n_k, where the factors n_i are pairwise relatively prime.
First, the Chinese remainder theorem is a descriptive "structure theorem" that describes
the structure of Z_n as identical to that of the Cartesian product
Z_n_1 x Z_n_2 x ... x Z_n_k with component-wise addition and multiplication modulo n_i
in the i-th component. Second, this description helps us to design efficient algorithms,
since working in each of the systems Z_n_i can be more efficient (in terms of bit
operations) than working modulo n.

Theorem 31.27 (Chinese remainder theorem)

Let n = n_1 * n_2 * ... * n_k, where the n_i are pairwise relatively prime. Consider the
correspondence

a <--> (a_1, a_2, ..., a_k), (31.27)

where a is in Z_n, a_i is in Z_n_i, and

a_i = a mod n_i

for i = 1, 2, ..., k. Then, mapping (31.27) is a one-to-one correspondence (bijection)
between Z_n and the Cartesian product Z_n_1 x Z_n_2 x ... x Z_n_k. Operations performed
on the elements of Z_n can be equivalently performed on the corresponding k-tuples by
performing the operations independently in each coordinate position in the appropriate
system.

Transforming between the two representations if fairly straightforward. Going from a to
(a_1, a_2, ..., a_k) is quite easy and requires only k "mod" operations.

For example, consider 17 mod 35. Here a = 17 and n = 35 and we wish to decompose a into
its separate coordinate components. n can be decomposed as n_1 * n_2 = 5 * 7, where 5
and 7 are pairwise relatively prime. Thus, we can decompose a into its separate
components using 2 mod operations as follows:

a_1 = 17 mod 5 = 2
a_2 = 17 mod 7 = 3

so that a = 17 <--> (2, 3).

As a practical application, if we have many computations to perform a in Z_n (e.g., RSA
signing and decryption), we can convert a into (a_1, a_2, ..., a_k), where a_i in Z_n_i
and do all the computations on the individual components a_i instead before converting
back. This is often cheaper because for many algorithms, doubling the size of the input
more than doubles the running time.

For example, we can decompose 17 in Z_35 as (2, 3) in Z_5 x Z_7. Then, if we wished to
compute (17 x 17) mod 35, we can compute each coordinate position independently as
follows:

(ab) mod n          <--> (a_1 * b_1 mod n_1, a_2 * b_2 mod n_2)
(17 x 17) mod 35    <--> (2 * 2 mod 5, 3 * 3 mod 7) = (4 mod 5, 2 mod 7)

Thus, solving (17 x 17) mod 35 is equivalent to solving the system of equations:

4 = a mod 5
2 = a mod 7

To solve such a system of equations, we can use the Chinese remainder theorem to
reconstruct a from its components a_i.

Computing a from inputs (a_1, a_2, ..., a_k) is a bit more complicated. We begin by
defining m_i = n / n_i for i = 1, 2, ..., k; thus m_i is the product of all of the n_j's
other than n_i. We next define

c_i = m_i * (inv(m_i) mod n_i) = 1 mod n_i (31.31)

for i = 1, 2, ..., k. Finally, we can compute a as a function of a_1, a_2, ..., a_k as
follows:

a = (a_1 * c_1 + a_2 * c_2 + ... + a_k * c_k) mod n. (31.32)

Equation (31.32) ensures that a = a_i mod n_i for i = 1, 2, ..., k. Note that if j != i,
then m_j = 0 mod n_i, which implies that c_j = m_j = 0 mod n_i. Note also that
c_i = 1 mod n_i from equation (31.31). We thus have the appealing and useful
correspondence

c_i <--> (0, 0, ..., 0, 1, 0, ..., 0),

a vector that has 0's everywhere except in the i-th coordinate, where it has a 1; the
c_i thus form a "basis" for the representation, in a certain sense. For each i,
therefore, we have

a = a_i * c_i mod n_i
  = a_i * m_i * (inv(m_i) mod n_)
  = a_i mod n_i

For example, we have the system of equations:

4 = a mod 5
2 = a mod 7

a = (4 * c_1 + 2 * c_2) mod 35
c_1 = m_1 * (inv(m_1) mod 5) --> m_1 = 35 / 5 = 7
c_2 = m_2 * (inv(m_2) mod 7) --> m_2 = 35 / 7 = 5

To solve for inv(a) = mod n, we recall that if gcd(a, n)[0] = 1 (i.e., a and n are
relatively prime), then the unique solution to the equation ax = 1 mod n is the value
returned by gcd()[1]. In other words, solving the equation ax = 1 mod n gives us the
inverse of a mod n and that is what we want here. Thus, we can compute inv(a) mod n
using gcd().

inv(m_1) mod 5 = inv(7) mod 5 = gcd(7, 5)[1] = -2
inv(m_2) mod 7 = inv(5) mod 7 = gcd(5, 7)[1] = 3

c_1 = 7 * -2 = -14
c_2 = 5 * 3 = 15
a = (4 * -14 + 2 * 15) mod 35 = 9

Corollary 31.28

If n_1, n_2, ..., n_k are pairwise relatively prime and n = n_1 * n_2 * ... * n_k, then
for any integers a_1, a_2, ..., a_k, the set of simultaneous equations

x = a_i mod n_i

for i = 1, 2, ..., k, has a unique solution modulo n for the unknown x.

Corollary 31.29

If n_1, n_2, ..., n_k are pairwise relatively prime and n = n_1 * n_2 * ... * n_k, then
for all integers x and a,

x = a mod n_i

for i = 1, 2, ..., k iff

x = a mod n.

For example, if x = 4 mod 5 and x = 4 mod 11, then x = 4 since 4 = 4 mod 55 (5 * 11).

Intuition
---------

Some problems:

1. A box contains gold coins. If the coins are equally divided among six friends, four
coins are left over. If the coins are equally divided among five friends, three coins
are left over. If the box holds the smallest number of coins that meet these two
conditions, how many coins are left when equally divided among seven friends?

Solution: rems = [4, 3], coprimes = [6, 5] --> crt() gives 28 since 4 = 28 mod 6 and
3 = 28 mod 5. Thus, 0 coins are left when divided equally among seven friends since
0 = 28 mod 7.

2. Comets A, B, and C have orbital periods of 3, 8, and 13 years, respectively. The last
perihelions of each of these comets were in 2017, 2014, and 2008, respectively. What is
the next year in which all three of these comets will achieve perihelion in the same
year?

Solution: rems = [2017, 2014, 2008], coprimes = [3, 8, 13] --> crt() gives 214, answer
is 214 + (3 * 8 * 13) * k = next closest year after 2017 so that k = 6 and solution is
2086.

3. Find the smallest whole number that when divided by 5, 7, 9, and 11 gives remainders
of 1, 2, 3, and 4, respectively.

Solution: rems = [1, 2, 3, 4], coprimes = [5, 7, 9, 11] --> crt() gives 1731.

4. Find all integers x that leave remainders 1, 2, 3 when divided by 9, 8, 7
respectively.

Solution: rems = [1, 2, 3], coprimes = [9, 8, 7] --> crt() gives 10, answer is
10 + (9 * 8 * 7) * k = 10 + 504 * k, for all k in the set of integers.

Complexity
==========

We have to compute the inverse for each coprime. There are n coprimes and each inverse
computation calls gcd(), which takes O(lg n) per call.

Time
----

crt(): O(n * lg n).
"""

# Repository Library
from src.clrs.selected_topics.number_theoretic_algorithms.modular_arithmetic.gcd import (  # noqa: E501
    gcd,
)


def crt(rems, coprimes):
    n = 1
    for i in coprimes:
        n *= i
    m = [n / i for i in coprimes]
    m_inv = [gcd(i, j)[1] for i, j in zip(m, coprimes)]
    return sum((i * j * k) for i, j, k in zip(m, m_inv, rems)) % n
