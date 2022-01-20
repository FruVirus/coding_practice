"""
31.6 Powers of an element
=========================

We consider the sequence of powers of a, modulo n, where a is in Z_n_star:

a^0, a^1, a^2, a^3, ...,

modulo n. Indexing from 0, the 0-th value in this sequence is a^0 mod n = 1, and the
i-th value is a^i mod n.

Theorem 31.31 (Fermat's theorem)

If p is prime, then a^(p - 1) = 1 mod p for all a in Z_star_p.

Equivalently, if p is prime, then a^p = a mod p.

Theorem 31.34

If p is an odd prime, and e >= 1, then the equation

x^2 = 1 mod p^e (31.34)

has only two solutions, namely x = 1 and x = -1.

Equation (31.34) is equivalent to p^e | (x - 1)(x + 1). Since p > 2, we can have
p | (x - 1) or p | (x + 1), but not both.

A number x is a nontrivial square root of 1, modulo n, if it satisfies the equation
x^2 = 1 mod n but x is equivalent to neither of the two "trivial" square roots: 1 or -1,
modulo n. For example, 6 is a nontrivial square root of 1, modulo 356 since 6^2 = 36 =
1 mod 35.

Corollary 31.35

If there exists a nontrivial square root of 1, modulo n, then n is composite.

For example:

5^2 = 1 mod 12

12 does not divide either (5 - 1) or (5 + 1); therefore, 12 is composite.

6^2 = 1 mod 7

7 does not divide (6 - 1) but it does divide (6 + 1); therefore, 7 is an odd prime.

6^2 = 1 mod 35

35 does not divide (6 - 1) or (6 + 1); there, 35 is composite

Raising to powers with repeated squaring
----------------------------------------

A frequently occurring operation in numerics is raising one number to a power modulo
another number, also known as modular exponentiation. More precisely, we would like an
efficient way of compute a^b mod n, where a and b are non-negative integers and n is a
positive integer. The method of repeated squares solves this problem efficiently using
the binary representation of b.

Let <b_k, b_k - 1, ..., b_1, b_0> be the binary representation of b. That is, the binary
representation is k + 1 bits long, b_k is the MSB and b_0 is the LSB. The procedure of
repeated squares essentially computes a^c mod n as c is increased by doublings and
incrementations from 0 to b.

Intuition
---------

The most direct method of calculating a modular exponent is to calculate it directly,
then to take the result modulo n. Consider trying to compute a^b mod n a = 4, b = 13,
and n = 497:

x = 4^13 mod 497

One could use a calculator to compute 4^13; this comes out to 67,108,864. Taking this
value modulo 497, the answer is 445.

Note that a is only one digit in length and that b is only two digits in length, but the
value a^b is 8 digits in length.

In strong cryptography, a is often at least 1024 bits. Consider a = 5 × 10^76 and
b = 17, both of which are perfectly reasonable values. In this example, a is 77 digits
in length and b is 2 digits in length, but the value a^b is 1,304 decimal digits in
length. Such calculations are possible on modern computers, but the sheer magnitude of
such numbers causes the speed of calculations to slow considerably. As a and b increase
even further to provide better security, the value be becomes unwieldy.

Keeping the numbers smaller requires additional modular reduction operations, but the
reduced size makes each operation faster, saving time (as well as memory) overall.

This algorithm makes use of the identity:

(a * b) mod n = [(a mod n) * (b mod n)] mod n

The procedure is:

1. Set c = 1, b′ = 0.
2. Increase b′ by 1.
3. Set c = (a * c) mod n.
4. If b′ < b, go to step 2. Otherwise, c contains the correct solution to c ≡ a^b mod n.

At each step of the for-loop (and before entering the for-loop), the condition
d = a^c mod n remains true (c = 0 before entering the for-loop). When the loop
terminates, step 3 has been executed b times and we have c = b and thus, d = a^c mod
n = a^b mod n.

Complexity
==========

Assuming a, b, and n are beta-bit numbers.

Time
----

mod_exp(): O(beta) arithmetic operations, O(beta^3) bit operations.
"""


def mod_exp(a, b, n):
    assert a >= 0 and b >= 0 and n > 0
    b, d = [int(i) for i in list(bin(b)[2:])], 1
    for i in b:
        d = (d * d) % n
        if i == 1:
            d = (d * a) % n
    return d
