"""
32.2 The Rabin-Karp algorithm
=============================

Rabin-Karp is a string-matching algorithm that performs well in practice and also
generalizes to other algorithms for related problems, such as two-dimensional pattern
matching.

In the general case, we can assume that each character is a digit in radix-d notation,
where d = |sigma|. We can then view a string of k consecutive characters as representing
a length-k decimal number. The character string "31415" thus corresponds to the decimal
number 31,415.

Given a pattern P[1...m], let p denote its corresponding decimal value. In a similar
manner, given a text T[1...n], let t_s denote the decimal value of the length-m
substring T[s + 1...s + m], for s = 0, 1, ..., n - m. Certainly, t_s = p iff
T[s + 1...s + m] = P[1...m]; thus, s is a valid shift iff t_s = p. If we could compute p
in time Theta(m) and all the t_s values in a total of Theta(n - m + 1) time, then we
could determine all valid shifts s in time Theta(m) + Theta(n - m + 1) = Theta(n) by
comparing p with each of the t_s values. In other words, instead of comparing each
individual character in the pattern with each individual character in T[s + 1...s + m],
we compute a decimal (i.e., hashed) representation of P with a decimal (i.e., hashed)
representation of T[s + 1...s + m]. This comparison is faster since we're just comparing
numbers instead of comparing strings where each character has to be compared against
individually.

p and t_s may be too large to work with conveniently. If P contains m characters, then
we cannot reasonably assume that each arithmetic operation on p (which is m digits long)
takes "constant time." Fortunately, we can solve this problem easily: compute p and the
t_s values modulo a suitable modulus q. If we choose the modulus q as a prime such that
10 * q just fits within one computer word, then we can perform all the necessary
computations with single-precision arithmetic. In general, with a d-ary alphabet
{0, 1, ..., d - 1}, we choose q so that d * q fits within a computer word and adjust the
hash equations to work modulo q.

The solution of working modulo q is not perfect, however: t_s = p mod q does not imply
that t_s = p. On the other hand, if t_s != p mod q, then we definitely have that
t_s != p, so that shift s is invalid. We can thus use the test t_s = p mod q as a fast
heuristic test to rule out invalid shifts s. Any shift s for which t_s = p mod q must
be tested further to see whether s is really valid or we just have a spurious hit. This
additional test explicitly checks the condition P[1...m] = T[s + 1...s + m] (i.e., it
checks each character individually). If q is large enough, then we hope that spurious
hits occur infrequently enough that the cost of the extra checking is low.

If q is small, then we will get lots of hits that need to be explicitly checked---this
can waste time if the majority of hits are spurious hits (i.e., we don't expect a lot of
matches of P in T). If the expected number of valid shifts is small (i.e., we expect few
valid matches) and we choose the prime q to be larger than the length of the pattern,
then we can expect the Rabin-Karp algorithm to use only O(n + m) = O(n) matching time
since m <= n.

Intuition
---------

Rabin Karp avoids checking pattern the against the string for every shift by checking
the hash values of the pattern and text first. If the hash value of the pattern matches
the hash pattern of the text, then we check the pattern characters against the text
characters.

pattern: dba

4 * 10^2 + 2 * 10^1 + 1 * 10^0 = 421

p[1] * 10^(m - 1) + p[2] * 10^(m - 2) + p[3] * 10^(m - 3) --> improved hash

The base 10 comes from the example alphabet a - j <--> 1 - 10. If we use full (English)
alphabet, then we should use base 26. If we have lower case, upper case, digits, etc.,
then we should use the full ASCII base of 127.

cca = 3 * 10^2 + 3 * 10^1 + 1 * 10^0 = 331 != 421

To calculate the rolling hash for the next three characters, cac, we do the following:

[[3 * 10^2 + 3 * 10^1 +1 * 10^0] - 3 * 10^2] * 10 + 3 * 10^0 = 313

Complexity
==========

Time
----

rabin_karp(): Theta(m) preprocessing, Theta((n - m + 1) * m)/Theta(n) worst/average case
matching.
"""

# Repository Library
from src.clrs.selected_topics.number_theoretic_algorithms.numerical_methods.next_prime import (  # noqa: E501
    is_prime,
    next_prime,
)


def check_equal(t, p, t_, p_, row, col, pcols, prows, indices):
    if p_ == t_ and p == [t[i][col : col + pcols] for i in range(row, row + prows)]:
        indices.append([row, col])


def col_hash(list_, npcols, radix, q):
    return sum((radix ** (npcols - i - 1) * list_[i]) % q for i in range(npcols)) % q


def col_rolling_hash(t_list, t_, col, npcols, radix, q):
    t_ = (t_ * radix + t_list[col]) % q
    t_ -= (radix ** npcols * t_list[col - npcols]) % q
    return t_ % q


def init(t, p, radix, q, is2d=True):
    q = q if is_prime(q) else next_prime(q)
    assert radix * q < 2 ** radix - 1
    t, p = (t, p) if is2d else ([t], [p])
    trows, prows, tcols, pcols = len(t), len(p), len(t[0]), len(p[0])
    tlist, plist, ntcols, npcols = row_hash(t, p, tcols, pcols, prows, radix, q)
    indices, p_ = [], col_hash(plist, npcols, radix, q)
    return t, p, tlist, ntcols, npcols, trows, prows, pcols, p_, indices


def row_hash(t, p, tcols, pcols, prows, radix, q):
    tlist, plist = [], []
    for list_, a, cols in zip((tlist, plist), (t, p), (tcols, pcols)):
        for i in range(cols):
            h = 0
            for j in reversed(range(prows)):
                h += (radix ** (prows - j - 1) * ord(a[j][i])) % q
            list_.append(h % q)
    return tlist, plist, len(tlist), len(plist)


def rabin_karp(t, p, radix=256, q=101):
    t, p, tlist, ntcols, npcols, _, prows, pcols, p_, indices = init(
        t, p, radix, q, False
    )
    col, t_ = 0, col_hash(tlist, npcols, radix, q)
    for i in range(npcols, ntcols):
        check_equal(t, p, t_, p_, 0, col, pcols, prows, indices)
        col, t_ = col + 1, col_rolling_hash(tlist, t_, i, npcols, radix, q)
    return indices
