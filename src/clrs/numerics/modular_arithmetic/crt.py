"""
Overview
========

The Chinese remainder theorem provides a correspondence between a system of equations
modulo a set of pairwise relatively prime moduli (e.g., 3, 5, and 7) and an equation
modulo their product (e.g., 105). All solutions are of the form 23 + 105 * k, for
arbitrary integers k.

Pairwise relatively prime means that every pair of items in a list are relatively prime
even though the individual items can be composite. For example, the list [121, 122, 123]
is pairwise relatively prime.

The theorem allows us to efficiently solve a system of modulo linear equations of the
form:

    x equiv 2 (mod 5) <--> x (mod 5) = 2 (mod 5)
    x equiv 3 (mod 7) <--> x (mod 7) = 3 (mod 7)

    or equivalently,

    x = 5 * a + 2
    x = 7 * a + 3

for x. If y is a solution then y + 35 is also solution. Note that 5 and 7 are pairwise
relatively prime and their product is 35. Thus, there is always a unique solution up to
a certain modulus for a system of equations like this.

In general, if:

    x = a (mod p)
    x = b (mod q)

then, there is a unique solution for x mod (p * q) if p and q are pairwise relatively
prime.

The theorem implies that we can represent an element of Z_pq by one element of Z_p and
one element of Z_q, and vice versa. In other words, we have a bijection between Z_pq and
Z_p x Z_q.

Some problems:

1. A box contains gold coins. If the coins are equally divided among six friends, four
coins are left over. If the coins are equally divided among five friends, three coins
are left over. If the box holds the smallest number of coins that meet these two
conditions, how many coins are left when equally divided among seven friends?

Solution: rems = [4, 3], coprimes = [6, 5]

2. Comets A, B, and C have orbital periods of 3, 8, and 13 years, respectively. The last
perihelions of each of these comets were in 2017, 2014, and 2008, respectively. What is
the next year in which all three of these comets will achieve perihelion in the same
year?

Solution: rems = [2017, 2014, 2008], coprimes = [3, 8, 13] --> crt() gives 214, answer
is 214 + (3 * 8 * 13) * k = next closest year after 2017 so that k = 6 and solution is
2086.

3. Find the smallest whole number that when divided by 5, 7, 9, and 11 gives remainders
of 1, 2, 3, and 4, respectively.

Solution: rems = [1, 2, 3, 4], coprimes = [5, 7, 9, 11]

Complexity
==========

O(n * lg(n))
"""

# Repository Library
from src.clrs.numerics.modular_arithmetic.gcd import gcd


def crt(rems, coprimes):
    prod = 1
    for i in coprimes:
        prod *= i
    prod_norm = [prod / i for i in coprimes]
    mod_inv = [gcd(i, j)[1] for i, j in zip(prod_norm, coprimes)]
    return sum((i * j * k) % prod for i, j, k in zip(mod_inv, prod_norm, rems)) % prod
