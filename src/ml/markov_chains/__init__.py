"""
Part 1
------

A Markov Chain models a system that changes its state.

1. The Markov property states that the next state of the system depends only on its
current state, not on previous states.

Instead of:

P(X_(n + 1) = x | X_1 = x_1, X_2 = x_2, ..., X_n = x_n)

we have,

P(X_(n + 1) = x | X_n = x_n)

2. The sum of the weights of the outgoing edges from any state is equal to 1. This has
to be true since these weights represent probabilities.

3. We can transform the outgoing edges into a transition matrix, where the values in the
matrix denote the weights and a value of 0 means there is no edge between two nodes. To
start, we can assume pi = [0, 1, 0] which corresponds to an initial configuration where
all the probability is on the second state. If we multiply this row vector with the
matrix, we get the corresponding probabilities for that state.

If we then repeatedly multiply this row vector with the matrix and take the resultant
row vector as the new row vector for the next round of multiplication, we will
eventually get to a state where the output row vector does not change from the input row
vector---this is a stationary state that denotes a persistent state of the system in the
long run.

pi * A = 1 * pi

The pi vectors are the (left) eigenvectors of matrix A with eigenvalue of 1. In
addition, the elements of pi must add up to 1 since they represent probabilities.

Part 2
------

1. A transient state is a state where the probability of coming back to the state in a
random walk is less than one when we originally start from the state itself.

2. A recurrent state is a state where the probability of coming back to the state in a
random walk is one when we originally start from the state itself.

3. If there are states that are not reachable from other states, the Markov chain is
reducible.

4. If all states can be reachable from other states, the Markov chain is irreducible.

5. Communicating classes consists of states that can transition between one another.

Part 3
------

The probability of transitioning from state i to state j in n steps, P_ij(2), is equal
to the element (i, j) in the matrix A^n.

P_ij(n) = A_ij^(n).

If we take A to the power of infinity, we find the probability of being at j after an
infinite number of steps, regardless of the starting state. For this to hold, A must be
irreducible and aperiodic.

Part 5: Hidden Markov Model
---------------------------

A hidden Markov model consists of a hidden Markov chain and a set of observed variables.
The observed variables only depends on the current hidden state in the Markov chain.

Hidden Markov Model = Hidden Markov Chain + Observed Variables

In effect, we have to transition matrices. One denotes the transition matrix for the
hidden markov chain and the other denotes the transition matrix for the observed
variables.
"""
