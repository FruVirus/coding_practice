"""
Performance and Capacity Considerations
=======================================

Our goal is generally to improve our metrics (engagement rate, etc.) while ensuring that
we meet the capacity and performance requirements.

Major performance and capacity discussions come in during the following two phases of
building a machine learning system:

    1. Training time: How much training data and capacity is needed to build our
predictor?

    2. Evaluation time: What are the Service Level Agreements (SLAs) that we have to
meet while serving the model and capacity needs?

We need to consider the performance and capacity along with optimization for the ML task
at hand, i.e., measure the complexity of the ML system at the training and evaluation
time and use it in the decision process of building our ML system architecture as well
as in the selection of the ML modeling technique.

Complexities consideration for an ML system
-------------------------------------------

Machine learning algorithms have three different types of complexities:

    - Training complexity. The training complexity of a machine learning algorithm is
the time taken by it to train the model for a given task.

    - Evaluation complexity. The evaluation complexity of a machine learning algorithm
is the time taken by it to evaluate the input at testing time.

    - Sample complexity. The sample complexity of a machine learning algorithm is the
total number of training samples required to learn a target function successfully.
Sample complexity changes if the model capacity changes. For example, for a deep neural
network, the number of training examples has to be considerably larger than decision
trees and linear regression.

Comparison of training and evaluation complexities
--------------------------------------------------

The evaluation complexity of the linear regression algorithm is equal to the complexity
of a single-layer neural network-based algorithm. Linear regression is the best choice
if we want to save time on training and evaluation.

Relatively deep neural network takes a lot more time in both training and evaluation.
Its need for training data is also high. However, it’s ability to learn complex tasks
such as image segmentation and language understanding, is much higher, and it gives more
accurate predictions in comparison to other models. Therefore a deep neural network is a
viable choice if it is well suited for the task at hand and capacity isn’t a problem.

MART is a tree-based algorithm that has a greater computation cost than linear models,
but it is much faster than a deep neural network. Tree-based algorithms are able to
generalize well using a moderately-sized training dataset. Therefore, if our training
data is limited to a few million examples and capacity/performance is critical, they
will be a good choice.

Performance and capacity considerations in large scale system
-------------------------------------------------------------

The ML-based system wants to respond with the most relevant web pages for the searcher
while meeting the system’s constraints. For our discussion of designing ML systems,
performance and capacity are the most important to think about when designing the
system. Performance based SLAs ensure that we return the results back within a given
time frame (e.g. 500ms) for 99% of queries. Capacity refers to the load that our system
can handle, e.g., the system can support 1000 QPS (queries per second). Since we cannot
have unlimited capacity, it’s important to have the system find the most optimal result
given a fixed capacity.

Layered/funnel based modeling approach
--------------------------------------

To manage both the performance and capacity of a system, one reasonable approach that’s
commonly used is to start with a relatively fast model when you have the most number of
documents e.g. 100 million documents in case of the query “computer science” for search.

In every later stage, we continue to increase the complexity (i.e. more optimized model
in prediction) and execution time but now the model needs to run on a reduced number of
documents e.g. our first stage could use a linear model and final stage can use a deep
neural network. If we apply deep neural network for only top 500 documents, with 1ms
evaluation time per document, we would need 500ms on a single machine. With five shards
we can do it in around 100ms.

In ML systems like search ranking, recommendation, and ad prediction, the layered/funnel
approach to modeling is the right way to solve for scale and relevance while keeping
performance high and capacity in check.
"""
