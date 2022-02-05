"""
32.3 String matching with finite automata
=========================================

Many string-matching algorithms build a finite automaton---a simple machine for
processing information---that scans the text string T for all occurrences of the pattern
P. These string-matching automata are very efficient: they examine each text character
exactly once, taking constant time per text character. The matching time used---after
preprocessing the pattern to build the automaton---is therefore Theta(n). The time to
build the automaton, however, can be large if sigma is large.

Finite automata
---------------

A finite automaton M, is a 5-tuple (Q, q_0, A, sigma, delta), where

- Q is a finite set of states
- q_0 in Q is the start state
- A is a subset of Q is a distinguished set of accepting states
- sigma is a finite input alphabet
- delta is a function from Q x sigma into Q, called the transition function of M

The finite automaton begins in state q_0 and reads the characters of its input string
one at a time. If the automaton is in state q and reads input character a, it moves
("makes a transition") from state q to state delta(q, a). Whenever its current state q
is a member of A, the machine M has accepted the string read so far. An input that is
not accepted is rejected.

A finite automaton M induces a function phi, called the final-state function, from
sigma_star to Q such that phi(w) is the state M ends up in after scanning the string w.
Thus, M accepts a string w iff phi(w) is in A.

String-matching automata
------------------------

For a given pattern P, we construct a string-matching automaton in a preprocessing step
before using it to search the text string.

In order to specify the string-matching automaton corresponding to a given pattern
P[1...m], we first define an auxiliary function sigma, called the suffix function
corresponding to P. The function sigma maps sigma_star to {0, 1, ..., m} such that
sigma(x) is the length of the longest prefix of P that is also a suffix of x. For a
pattern P of length m, we have sigma(x) = m iff P is a suffix of x. In other words, if P
is a suffix of x, then sigma(x) equals the length of P, which is m.

We define the string-matching automaton that corresponds to a given pattern P[1...m] as
follows:

- The state set Q is {0, 1, ..., m}. The start state q_0 is state 0, and state m is the
only accepting state.
- The transition function delta is defined by the following equation, for any state q
and character a:

    delta(q, a) = sigma(P_q a).

We define delta(q, a) = sigma(P_q a) because we want to keep track of the longest prefix
of the pattern P that has matched the text string T so far. We consider the most
recently read characters of T. In order for a substring of T---let's say the substring
ending at T[i]---to match some prefix P_j of P, this prefix P_j must be a suffix of T_i.
Suppose q = phi(T_i), so that after reading T_i, the automaton is in state q. We design
the transition function delta so that this state number, q, tells us the length of the
longest prefix of P that matches a suffix of T_i. That is, in state q, P_q is a suffix
of T_i and q = sigma(T_i). Whenever q = m, all m characters of P match a suffix of T_i,
and so we have found a match. Thus, since phi(T_i) and sigma(T_i) both equal q, the
automaton maintains the following invariant:

    phi(T_i) = sigma(T_i).

If the automaton is in state q and reads the next character T[i + 1] = a, then we want
the transition to lead to the state corresponding to the longest prefix of P that is a
suffix of T_i a, and that state is sigma(T_i a). Because P_q is the longest prefix of P
that is a suffix of T_i, the longest prefix of P that is a suffix of T_i a is not only
sigma(T_i a) but also sigma(P_q a). Thus, when the automaton is in state q, we want the
transition function on character a to take the automaton to state sigma(P_q a).

There are two cases to consider. In the first case, a = P{q + 1], so that the character
a continues to match the pattern; in this case, because delta(q, a) = q + 1, the
transition continues to go along the "spine" of the automaton. In the second case,
a != P[q + 1], so that a does not continue to match the pattern. Here, we must find a
smaller prefix of P that is also a suffix of T_i. Because the preprocessing step matches
the pattern against itself when creating the string-matching automaton, the transition
function quickly identifies the longest such smaller prefix of P.

Intuition
---------

At each step, the finite automaton is merely keeping track of the longest prefix of the
pattern that is a suffix of what has been read so far in the text. If the longest prefix
of the pattern is the entire pattern itself and is a suffix of what has been read so far
in the text, then we have a match.

If a pattern has length m, then the finite automaton has m + 1 states (the 0 state is
the default initial state). As we read each character in the text, the finite automaton
will transition between states. If we match all m characters in the pattern at a given
position in the text, then the finite automaton will transition to its final (accepting)
state m. State m is the ONLY accepting state for a string-matching finite automaton. If
we have a mismatch between the pattern and the text, then the finite automaton will
transition to a previous state (which could be the initial state, q_0).

The automaton is in state sigma(T_i) after scanning character T[i]. Since sigma(T_i) = m
iff P is a suffix of T_i, the machine is in the accepting state m iff it has just
scanned the (entire) pattern P in T_i.

When the machine enters state q in the for-loop, then q is the largest value such that
P_q is a suffix of T_i. Thus, we have q == m iff the machine has just scanned an
occurrence of the (entire) pattern P in T_i.

Example:

P = ababaca, m = 7
T = abccbababacabbb, n = 15
Sigma = {a, b, c} = 3

First, we ignore the text and make a finite automaton for the pattern. The alphabet
consists of the characters a, b, and c only. The length of P + 1 is the number of states
of the finite automaton---7 + 1 = 8. Given the pattern P, the transition function
matrix, delta, is:

state   a       b       c       P   lps
0       "1"     0       0       a   0
1       1       "2"     0       b   0
2       "3"     0       0       a   1
3       1       "4"     0       b   2
4       "5"     0       0       a   3
5       1       4       "6"     c   0
6       "7"     0       0       a   1
7       1       2       0

The first "a" in T matches the first "a" in P --> the finite automaton transitions to
state 1.

The first "b" in T matches the first "b" in P --> the finite automaton transitions to
state 2.

The first "c" in T does NOT match the second "a" in P --> the finite automaton
transitions to state 0 since delta[3]["c"] = 0.

The second "c" in T does NOT match the first "a" in P --> the finite automaton
transitions tp state 0 since delta[0]["c"] = 0.

The second "b" in T does NOT match the first "a" in P --> the finite automaton
transitions to state 0 since delta[0]["b"] = 0.

The second "a" in T matches the first "a" in P --> the finite automaton transitions to
state 1.

The next "b" in T matches the next "b" in P --> the finite automaton transitions to
state 2.

The next "a" in T matches the next "a" in P --> the finite automaton transitions to
state 3.

The next "b" in T matches the next "b" in P --> the finite automaton transitions to
state 4.

The next "a" in T matches the next "a" in P --> the finite automaton transitions to
state 5.

The next "c" in T matches the next "c" in P --> the finite automaton transitions to
state 6.

The next "a" in T matches the next "a" in P --> the finite automaton transitions to
state 7. Since 7 == len(P), we have an exact pattern match.

The next "b" in T does NOT match the first "a" in P --> the finite automaton transitions
to state 2 since delta[7]["b"] = 2. In this state, we have still matched with "ab" so
far.

The next "b" in T does NOT match with the second "a" in P --> the finite automaton
transitions to state 0 since delta[2]["b"] = 0. Thus, we are back at the initial state
where no prefixes match. This is because if we have "abb" in T, then no prefix of P
matches this substring and thus, we must start the pattern matching from scratch again.

The last "b" in T does NOT match the first "a" in P --> the finite automaton transitions
to state 0 since delta[0]["b"] = 0.

The columns of the transition function matrix is filled in as follows:

delta(q, a) = sigma(P_q a)

delta(0, "a") = sigma(P_0 "a") = sigma(eps "a") = sigma("a") = 1 --> the length of the
longest prefix of P that is also a suffix of "a" is 1.

delta(1, "a") = sigma(P_1 "a") = sigma("aa") = 1 --> the length of the longest prefix of
P that is also a suffix of "aa" is 1.

delta(2, "a") = sigma(P_2 "a") = sigma("aba") = 3 --> the length of the longest prefix
of P that is also a suffix of "aba" is 3.

delta(3, "a") = sigma(P_3 "a") = sigma("abaa") = 1 --> the length of the longest prefix
of P that is also a suffix of "abaa" is 1.

delta(4, "a") = sigma(P_4 "a") = sigma("ababa") = 5 --> the length of the longest prefix
of P that is also a suffix of "ababa" is 5.

etc.

phi is the final state function. Since phi(T_i) = sigma(T_i), when we have phi(T_i) =
sigma(T_i) = m, then we have an entire pattern match. phi is calculated recursively as
follows:

phi(eps) = q_0
phi(wa) = delta(phi(w), a)

phi(T_0) = phi(eps) = q_0 = 0
phi(T_1) = delta(0, a) = 1 --> 1 matching character so far
phi(T_2) = delta(1, b) = 2 --> 2 matching characters so far
phi(T_3) = delta(2, a) = 3 --> 3 matching characters so far
phi(T_4) = delta(3, b) = 4 --> 4 matching characters so far
phi(T_5) = delta(4, a) = 5 --> 5 matching characters so far
phi(T_6) = delta(5, b) = 4 --> back to 4 matching characters so far
phi(T_7) = delta(4, a) = 5 --> 5 matching characters so far
phi(T_8) = delta(5, c) = 6 --> 6 matching characters so far
phi(T_9) = delta(6, a) = 7 --> 7 matching characters so far, we've matched the pattern P
phi(T_10) = delta(7, b) = 2 --> 7 back to 2 matching characters so far
phi(T_11) = delta(2, a) = 3 --> 3 matching characters so far

etc.

In compute_transition(), we are constructing the transition function matrix for the
entire pattern for all characters in the alphabet, sigma. The rows of tf correspond to
the possible states of the transition function (m + 1) and the columns of tf correspond
to the characters in the alphabet (sigma).

In compute_transition(), setting tf[i][ord(p[i])] = i + 1 moves the transition function
along the "spine" of the automaton (i.e., it corresponds to successful matches between
pattern and input characters)---this is denoted by the numbers in quotes in the example
transition function matrix above.

In compute_transition(), setting lps = tf[lps][ord(p[i])] updates the lps for the next
row to be filled in. The lps for the next row is the state that the automaton falls back
to when a mismatch occurs or we have a complete match. In other words,
delta(q, a) = delta(pi[q], a) if q = m or P{q + 1] != a, where pi[q] corresponds to the
longest prefix suffix of q. See the KMP algorithm for a more detailed explanation of how
lps is calculated here.

Complexity
==========

Time
----

compute_transition(): O(m * sigma) preprocessing.
fa(): O(n) matching.

Space
-----

compute_transition(): O(m * sigma) for tf table.
"""


def compute_transition(p, m, sigma):
    lps, tf = 0, [[0] * sigma for _ in range(m + 1)]
    tf[0][ord(p[0])] = 1
    for i in range(1, m + 1):
        for j in range(sigma):
            tf[i][j] = tf[lps][j]
        if i < m:
            lps, tf[i][ord(p[i])] = tf[lps][ord(p[i])], i + 1
    return tf


def fa(t, p, sigma=256):
    n, m, q, indices = len(t), len(p), 0, []
    tf = compute_transition(p, m, sigma)
    for i in range(n):
        q = tf[q][ord(t[i])]
        if q == m:
            indices.append(i - m + 1)
    return indices
