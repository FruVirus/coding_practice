"""
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
too much time trying to optimize it. It’s generally a better idea to take model online
and then continue to iterate to improve the quality. The reason is primarily that model
improvement is an iterative process and we want validation from real traffic and data
along with offline validation.

Deploying and debugging v1 model
--------------------------------

In our first attempt to take the model online, i.e., enable live traffic, might not work
as expected and results don’t look as good as we anticipated offline. Let’s look at a
few failure scenarios that can happen at this stage and how to debug them.

Change in feature distribution

The change in the feature distribution of training and evaluation set can negatively
affect the model performance. Another scenario could be a significant change in incoming
traffic because of seasonality.

Feature logging issues
----------------------

When the model is trained offline, there is an assumption that features of the model
generated offline would exactly be the same when the model is taken online. However,
this might not be true as the way we generated features for our online system might not
exactly be the same. It’s a common practice to append features offline to our training
data for offline training and then add them later to the online model serving part. So,
if the model doesn’t perform as well as we anticipated online, it would be good to see
if feature generation logic is the same for offline training as well as online serving
part of model evaluation.

Overfitting
-----------

Overfitting happens when a model learns the intrinsic details in the training data to
the extent that it negatively impacts the performance of the model on new or unseen
data.

If our model performance is lower in the live system but it still performs well on our
training and validation set then there is a good chance that we have overfit our data by
trying to improve the performance a bit too much.

Another important part is to have a comprehensive and large test set to cover all
possible scenarios in a fairly similar distribution to how we anticipate them in live
traffic.

Under-fitting
-------------

One indication from training the model could be that the model is unable to learn
complex feature interactions especially if we are using a simplistic model. So, this
might indicate to us that using slightly higher-order features, introduce more feature
interactions, or use a more complex /expensive model such as a neural network.

Iterative model improvement
---------------------------

Few cases that we discussed above regarding overfitting and under-fitting are still the
questions that we should continue to ask during iterative model improvement but let’s
discuss a few more below. The best way to iterative improve model quality is to start
looking at failure cases of our model prediction and using that come up with the ideas
that will help in improving model performance in those cases.

Missing important feature

Digging deeper into failures examples can identify missing features that can help us
perform better in failures cases.

Insufficient training examples

We may also find that we are lacking training examples in cases where the model isn’t
performing well. We will cater to all possible scenarios where the model is not
performing well and update the training data accordingly.

Debugging large scale systems
-----------------------------

In the case of debugging large scale systems with multiple components (or models), we
need to see which part of the overall system is not working correctly. It could be done
for one failure example or over a set of examples to see where the opportunity lies to
improve the metrics.

The following are a few key steps to think about iterative model improvement for large
scale end to end ML systems:

    - Identify the component. This accounts for finding the architectural component
resulting in a high number of failures in our failure set. In order to see the cause of
failure, we will look at each layers’ performance to understand the opportunity to
significantly improve the quality of our search system.

    - Improve the quality of component. Some of the model improvement methods that we
have discussed above like adding more training data, features, modeling approach in case
of overfitting and underfitting will still be the same once we identify the component
that needs work.
"""
