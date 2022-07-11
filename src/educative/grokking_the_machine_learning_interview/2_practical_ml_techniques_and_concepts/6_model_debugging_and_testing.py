"""
Main Takeaways
~~~~~~~~~~~~~~

There are two main phases in terms of the development of a model:

    - Building the first version of the model and the ML system.

    - Iterative improvements on top of the first version as well as debugging issues in
large scale ML systems.

The first goal is to build the 1st version of the model. Few important steps in this
stage are:

    - We begin by identifying a business problem in the first phase and mapping it to a
machine learning problem.

    - We then go onto explore the training data and machine learning techniques that
will work best on this problem.

    - Then we train the model given the available data and features, play around with
hyper-parameters.

    - Once the model has been set up and we have early offline metrics like accuracy,
precision/recall, AUC, etc., we continue to play around with the various features and
training data strategies to improve our offline metrics.

    - If there is already a heuristics or rule-based system in place, our objective from
the offline model would be to perform at least as good as the current system, e.g., for
ads prediction problem, we would want our ML model AUC to be better than the current
rule-based ads prediction based on only historical engagement rate.

It’s important to get version 1 launched to the real system quickly rather than spending
too much time trying to optimize it. The reason is primarily that model improvement is
an iterative process and we want validation from real traffic and data along with
offline validation.

In our first attempt to take the model online, i.e., enable live traffic, might not work
as expected and results don’t look as good as we anticipated offline. Let’s look at a
few failure scenarios that can happen at this stage and how to debug them.



Model Debugging and Testing
===========================

There are two main phases in terms of the development of a model that we will go over:

    - Building the first version of the model and the ML system.

    - Iterative improvements on top of the first version as well as debugging issues in
large scale ML systems.

Building model v1
-----------------

The goal in this phase is to build the 1st version of the model. Few important steps in
this stage are:

    - We begin by identifying a business problem in the first phase and mapping it to a
machine learning problem.

    - We then go onto explore the training data and machine learning techniques that
will work best on this problem.

    - Then we train the model given the available data and features, play around with
hyper-parameters.

    - Once the model has been set up and we have early offline metrics like accuracy,
precision/recall, AUC, etc., we continue to play around with the various features and
training data strategies to improve our offline metrics.

    - If there is already a heuristics or rule-based system in place, our objective from
the offline model would be to perform at least as good as the current system, e.g., for
ads prediction problem, we would want our ML model AUC to be better than the current
rule-based ads prediction based on only historical engagement rate.

It’s important to get version 1 launched to the real system quickly rather than spending
too much time trying to optimize it. For example, if our AUC is 0.7 and it’s better than
the current system with AUC 0.68, it’s generally a better idea to take model online and
then continue to iterate to improve the quality. The reason is primarily that model
improvement is an iterative process and we want validation from real traffic and data
along with offline validation.

Deploying and debugging v1 model
--------------------------------

Some ML-based systems only operate in an offline setting, for example, detect objects
from a large set of images. But, most systems have an online component as well, for
example, building a search ranking ML model will have to run online to service incoming
queries and ranking the documents that match the query.

In our first attempt to take the model online, i.e., enable live traffic, might not work
as expected and results don’t look as good as we anticipated offline. Let’s look at a
few failure scenarios that can happen at this stage and how to debug them.

Change in feature distribution


"""
