"""
Multi-armed bandit
==================

What is the multi-armed bandit problem?
---------------------------------------

In marketing terms, a multi-armed bandit solution is a ‘smarter’ or more complex version
of A/B testing that uses machine learning algorithms to dynamically allocate traffic to
variations that are performing well, while allocating less traffic to variations that
are underperforming.

The term "multi-armed bandit" comes from a hypothetical experiment where a person must
choose between multiple actions (i.e., slot machines, the "one-armed bandits"), each
with an unknown payout. The goal is to determine the best or most profitable outcome
through a series of choices. At the beginning of the experiment, when odds and payouts
are unknown, the gambler must determine which machine to pull, in which order and how
many times. This is the “multi-armed bandit problem.”

Multi-armed bandit examples
---------------------------

One real-world example of a multi-armed bandit problem is when a news website has to
make a decision about which articles to display to a visitor. With no information about
the visitor, all click outcomes are unknown. The first question is, which articles will
get the most clicks? And in which order should they appear? The website’s goal is to
maximize engagement, but they have many pieces of content from which to choose, and they
lack data that would help them to pursue a specific strategy.

The news website has a similar problem in choosing which ads to display to its visitors.
In this case, they want to maximize advertising revenue, but they may be lacking enough
information about the visitor to pursue a specific advertising strategy. Similar to the
issue with news articles, they typically have a large number of ads from which to
choose. Which ads will drive maximum revenue for their news site?

The website needs to make a series of decisions, each with unknown outcome and payout.

Multi-armed bandit solutions
----------------------------

There are many different solutions that computer scientists have developed to tackle the
multi-armed bandit problem. Below is a list of some of the most commonly used
multi-armed bandit solutions:

Obviously the best approach would be to choose the best action every time and this is
what’s known as the optimal policy. It’s also obvious that this approach isn’t actually
practical, since you initially don’t know which action is the best. Some time has to be
spent exploring if you’re going to find the best one and therefore it’s not always
possible to choose the best action.

The optimal policy, although only theoretical, can however be used to evaluate other
policies, to see how close they come to being optimal. The difference between the return
that would be achieved by the optimal policy and the amount of return actually achieved
by the policy under consideration is known as the regret.

Epsilon-greedy

This is an algorithm for continuously balancing exploration with exploitation. In
greedy experiments, the lever with highest known payout is always pulled except when a
random action is taken. A randomly chosen arm is pulled a fraction ε of the time. The
other 1 - ε of the time, the arm with highest known payout is pulled.

- With an ε value of zero this is just the Greedy algorithm. Each socket is chosen with
an equal probability. No sockets are ever selected at random and there is no
exploration.

- As ε increases, so the random selection of actions increases and, consequently,
exploration increases. Initially this results in the optimal socket being located and
selected with increasing frequency. At the same time, the non-optimal sockets begin to
be selected less often.

Epsilon-greedy has linear regret. It continues to explore the set of all actions, long
after it has gained sufficient knowledge to know which of these actions are bad actions
to take.

Upper confidence bound

A better approach, in terms of maximising the total reward, would be to restrict the
sampling over time to the actions showing the best performance. This is the exact
approach taken by the Upper Confidence Bound (UCB) strategy.

UCB is based on the principle of “optimism in the fact of uncertainty”, which basically
means if you don’t know which action is best then choose the one that currently looks to
be the best.

Rather than performing exploration by simply selecting an arbitrary action, chosen with
a probability that remains constant, the UCB algorithm changes its
exploration-exploitation balance as it gathers more knowledge of the environment. It
moves from being primarily focused on exploration, when actions that have been tried the
least are preferred, to instead concentrate on exploitation, selecting the action with
the highest estimated reward.

Thompson Sampling (Bayesian)

With this randomized probability matching strategy, the number of pulls for a given
lever should match its actual probability of being the optimal lever.

In this sort of a policy, we model our uncertainty about the probability that each
bandit will dispense a reward using a Beta probability distribution. A Beta distribution
is not only flexible but also very easy to update as we get new information by observing
the result of each pull of a bandit’s arm.

In this context, we use our uncertainty about these parameters to enable a natural way
to balance exploration vs exploitation: we sample from the distribution describing our
uncertainty about the probability of a reward for each arm, and then pull the arm that
happened to have the largest sample. Since we start with a uniform prior distribution
for each arm (suggesting we have no idea whether its probability will be high or low),
we are initially equally likely to pick any given arm. After updating the distribution
for each arm with Bayes’ rule many times, we eventually become quite confident about
which arm is best and are thus very likely to always draw the largest sample from its
distribution, leading to very little exploration and almost complete exploitation.

In contrast to the Greedy algorithm, which at each time step selects the action with the
highest estimated reward, even if the confidence in that estimate is low, Thompson
sampling instead samples from the Beta distribution of each action and chooses the
action with the highest returned value. Since actions that have been tried infrequently
have wide distributions, they have a larger range of possible values. In this way, a
socket that currently has a low estimated mean reward, but has been tested fewer times
than a socket with a higher estimated mean, can return a larger sample value and
therefore become the selected socket at this time step.
"""
