"""
Deep Q-Learning Tutorial: minDQN
===============================

Reinforcement Learning Background
---------------------------------

Reinforcement Learning can broadly be separated into two groups: model free and model
based RL algorithms. Model free RL algorithms don’t learn a model of their environment’s
transition function to make predictions of future states and rewards. Q-Learning, Deep
Q-Networks, and Policy Gradient methods are model-free algorithms because they don’t
create a model of the environment’s transition function.

Vanilla Q-Learning
------------------

Vanilla Q-Learning: A table maps each state-action pair to its corresponding Q-value.

1. Initialize your Q-table

The Q-table is a simple data structure that we use to keep track of the states, actions,
and their expected rewards. More specifically, the Q-table maps a state-action pair to a
Q-value (the estimated optimal future value) which the agent will learn. At the start of
the Q-Learning algorithm, the Q-table is initialized to all zeros indicating that the
agent doesn’t know anything about the world. As the agent tries out different actions at
different states through trial and error, the agent learns each state-action pair’s
expected reward and updates the Q-table with the new Q-value. Using trial and error to
learn about the world is called Exploration.

One of the goals of the Q-Learning algorithm is to learn the Q-Value for a new
environment. The Q-Value is the maximum expected reward an agent can reach by taking a
given action A from the state S. After an agent has learned the Q-value of each
state-action pair, the agent at state S maximizes its expected reward by choosing the
action A with the highest expected reward. Explicitly choosing the best known action at
a state is called Exploitation.

2. Choose an action using the Epsilon-Greedy Exploration Strategy

A common strategy for tackling the exploration-exploitation tradeoff is the Epsilon
Greedy Exploration Strategy.

1. At every time step when it’s time to choose an action, roll a dice.

2. If the dice has a probability less than epsilon, choose a random action.

3. Otherwise take the best known action at the agent’s current state.

Note that at the beginning of the algorithm, every step the agent takes will be random
which is useful to help the agent learn about the environment it’s in. As the agent
takes more and more steps, the value of epsilon decreases and the agent starts to try
existing known good actions more and more. Note that epsilon is initialized to 1 meaning
every step is random at the start. Near the end of the training process, the agent will
be exploring much less and exploiting much more.

3. Update the Q-table using the Bellman Equation

The Bellman Equation tells us how to update our Q-table after each step we take. To
summarize this equation, the agent updates the current perceived value with the
estimated optimal future reward which assumes that the agent takes the best current
known action. In an implementation, the agent will search through all the actions for a
particular state and choose the state-action pair with the highest corresponding
Q-value.

Deep Q-Network
--------------

Deep Q-Learning: A Neural Network maps input states to (action, Q-value) pairs.

1. Initialize your Main and Target neural networks

A core difference between Deep Q-Learning and Vanilla Q-Learning is the implementation
of the Q-table. Critically, Deep Q-Learning replaces the regular Q-table with a neural
network. Rather than mapping a state-action pair to a q-value, a neural network maps
input states to (action, Q-value) pairs.

One of the interesting things about Deep Q-Learning is that the learning process uses 2
neural networks. These networks have the same architecture but different weights. Every
N steps, the weights from the main network are copied to the target network. Using both
of these networks leads to more stability in the learning process and helps the
algorithm to learn more effectively.

The main and target neural networks map input states to an (action, q-value) pair. In
this case, each output node (representing an action) contains the action’s q-value as a
floating point number. Note that the output nodes do not represent a probability
distribution so they will not add up to 1.

In our implementation, the main and target networks are quite simple consisting of 3
densely connected layers with Relu activation functions. The most notable features are
that we use He uniform initialization as well as the Huber loss function to achieve
better performance.

2. Choose an action using the Epsilon-Greedy Exploration Strategy

In the Epsilon-Greedy Exploration strategy, the agent chooses a random action with
probability epsilon and exploits the best known action with probability 1 — epsilon.

How do you find the best known action from your network?

Both the Main model and the Target model map input states to output actions. These
output actions actually represent the model’s predicted Q-value. In this case, the
action that has the largest predicted Q-value is the best known action at that state.

3. Update your network weights using the Bellman Equation

After choosing an action, it’s time for the agent to perform the action and update the
Main and Target networks according to the Bellman equation. Deep Q-Learning agents use
Experience Replay to learn about their environment and update the Main and Target
networks.

To summarize, the main network samples and trains on a batch of past experiences every 4
steps. The main network weights are then copied to the target network weights every 100
steps.

Experience Replay
-----------------

One thing that can lead to our agent misunderstanding the environment is consecutive
interdependent states that are very similar.

For example, if we're teaching a self-driving car how to drive, and the first part of
the road is just a straight line, the agent might not learn how to deal with any curves
in the road.

This is where experience replay comes in.

From our self-driving car example, what happens with experience replay is that the
initial experiences of driving in a straight line don't get put through the neural
network right away. Instead, these experiences are saved into memory by the agent. Once
the agent reaches a certain threshold then we tell the agent to learn from it.

So the agent is now learning from a batch of experiences. From these experiences, the
agent randomly selects a uniformly distributed sample from this batch and learns from
that. Each experience is characterized by that state it was in, the action it took, the
state it ended up in, and the reward it received. By randomly sampling from the
experiences, this breaks the bias that may have come from the sequential nature of a
particular environment, for example driving in a straight line.

Experience Replay can be used in Off-Policy algorithms to learn in an offline fashion.
Off-policy methods are able to update the algorithm’s parameters using saved and stored
information from previously taken actions. Deep Q-Learning uses Experience Replay to
learn in small batches in order to avoid skewing the dataset distribution of different
states, actions, rewards, and next_states that the neural network will see. Importantly,
the agent doesn’t need to train after each step.
"""
