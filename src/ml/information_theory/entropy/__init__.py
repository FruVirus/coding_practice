"""Entropy

Introduction
------------

Entropy is used for a lot of things in Data Science.

For example, Entropy can be used to build Classification Trees.

Entropy is also the basis of something called Mutual Information, which quantifies the
relationship between two things.

And Entropy is the basis of Relative Entropy (i.e., the KL Distance) and Cross Entropy,
which show up all over the place, including dimension reduction algorithms like t-SNE
and UMAP.

What these three things have in common is that they all use Entropy, or something
derived from it, to quantify similarities and differences.

Introduction to Surprise
------------------------

In order to talk about Entropy, first we have to understand Surprise.

Surprise is, in some way, inversely related to probability.

When the probability is high, the Surprise is low and vice versa.

We can't just use the inverse of probability to calculate Surprise. For example, if a
coin always gave Heads (i.e., P(Heads) = 1), then we want the Surprise to be 0. However,
1 / P(Heads) = 1 / 1 = 1.

Equation for Surprise
---------------------

Thus, we use the log of the inverse of the probability to calculate Surprise.

Surprise = log(1 / probability)

If the probability of something is 0 (i.e., it will never happen), then the log is
undefined since the Surprise of something that will never happen doesn't make any sense.

Note: When calculating Surprise for 2 outputs (e.g., Heads and Tails), then it is
customary to use the log base 2.

Calculating surprise for a series of events
-------------------------------------------

Let's imagine that our coin gets heads 90% of the time and tails 10% of the time. The
Surprise for getting heads and tails is 0.15 and 3.32, respectively.

Because getting tails is much rarer than getting heads, the Surprise for tails is much
larger.

If we flip the coin three times, the Surprise of getting 2 heads and 1 tail is
log(1 / (0.9 * 0.9 * 0.1)) = 3.62.

Thus, the total Surprise for a sequence of events is just the sum of Surprises for each
individual event.

For N events, we compute the expected number of heads (0.9 * N) and multiply the
expected number of heads by the Surprise for 1 head to get the total Surprise for N
heads.

(0.9 * 100) * 0.15 + (0.1 * 100) * 3.32 = 46.7 --> Total Surprise for 100 coin flips

Entropy defined for a coin
--------------------------

46.7 / 100 = 0.47 --> Average Surprise per coin toss

On average, we expect the Surprise to be 0.47 every time we flip a coin and that is the
Entropy of the coin: the expected Surprise every time we flip the coin.

We say that Entropy is the Expected Value of the Surprise:

Entropy = E[Surprise]

Note that the 100 cancels out in the numerator and denominator so that Entropy doesn't
depend on the number of trials.

Entropy is the expected value of surprise
-----------------------------------------

Entropy = E[Surprise] = Sum of Surprise_i * P_i

The entropy equation
--------------------

Thus, by definition:

Entropy = Sum log(1 / p(x)) * p(x) = Sum p(x) * log(1 / p(x)) = - Sum p(x) * log(p(x))

The equation for Entropy is made up of two terms: the Surprise and the probability of
the Surprise.

Entropy in action!!!
--------------------

Since Entropy is a product between Surprise and the probability of the Surprise, the
total entropy of a system can be closer to an event with low Surprise if the probability
of that event is relatively high compared with other events in the system.

We can use Entropy to quantify the similarity or difference between two
systems/distributions/etc.

Entropy is highest when a system is uniform. As we increase/decrease some aspect of that
system, then the entropy will decrease.
"""
