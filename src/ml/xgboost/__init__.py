"""XGBoost

Part 1: Regression
==================

The initial prediction
----------------------

The very first step in fitting XGBoost to the Training Data is to make an initial
prediction. This prediction can be anything, but by default it is 0.5, regardless of
whether you are using XGBoost for Regression or Classification.

The Residuals are the differences between the Observed and Predicted values.

Building an XGBoost Tree for regression
---------------------------------------

Just like Gradient Boost, XGBoost fits a Regression Tree to the residuals.

However, unlike Gradient Boost, which typically uses regular, off-the-shel, Regresssion
Trees, XGBoost uses a unique Regression Tree.

Note: There are many ways to build XGBoost Trees.

Each tree starts out as a single leaf and all of the Residuals go to the leaf.

Calculating Similarity Scores
-----------------------------

Now we calculate a Quality Score, or Similarity Score, for the Residuals.

Similarity Score = (Sum of Residuals) ^ 2 / (Number of Residuals + lambda)

lambda is a Regularization parameter.

Note: Because we do not square the Residuals before we add them together in the
numerator, negative and positive Residuals can cancel each other out.

Now the question is whether or not we can do a better job clustering similar Residuals
if we split them into two groups.

We continuously split observations into two groups based on their average values. And we
calculate new Similarity Scores for the split observations.

When we have calculated Similarity Scores for the root and the two leaf nodes, we see
that when the Residuals in a node are very different, they tend to cancel each other out
and the Similarity Score for the node is relatively small.

In contrast, when the Residuals are similar, or there is just one Residual in a node,
they do not cancel out and the Similarity Score is relatively large.

The minimum number of Residuals in each leaf is determined by calculating something
called Cover. Cover is defined as the denominator of the Similarity Score without the
lambda. For Regression, Cover is the Number of Residuals. By default, the minimum value
for Cover is 1. Thus, by default, when we use XGBoost for Regression, we can have as few
as 1 Residual per leaf. In other words, the default minimum value for Cover has no
effect on how we grow the tree for Regression.

Calculating Gain to evaluate different thresholds
-------------------------------------------------

Now we need to quantify how much better the leaves cluster similar Residuals than the
root.

We do this by calculating the Gain of splitting the Residuals into two groups.

Gain = Sum of Leaf Similarity Scores - Parent Similarity Score

Once we have calculated the Gain for a certain threshold, we can compare it to the Gains
calculate for other thresholds. To do this, we select another threshold (i.e., another
value of the variable we are using) and build a simple tree that divides the
observations using the new threshold.

Higher Gains implies that a given tree is better at splitting the Residuals into
clusters of similar values.

We use the threshold that gave us the largest Gain as the first branch in the XGBoost
tree. We then keep splitting the leaves of the tree and calculating the split that gives
us the highest Gain.

Pruning an XGBoost tree
-----------------------

Now we need to Prune the XGBoost tree. We Prune an XGBoost Tree based on its Gain
values.

We start by picking a number, gamma, referred to as the Tree Complexity Parameter. We
then calculate the difference between the Gain associated with the lowest branch in the
tree and the value for gamma. If the difference is negative, we will remove the branch;
otherwise, we keep the branch.

Note: We do not remove parent branches if the leaf branches are not removed.

Values for lambda > 0 reduce the sensitivity of the tree to individual observations by
pruning and combining them with other observations.

Building an XGBoost Tree with regularization
--------------------------------------------

Remember, lambda is a Regularization Parameter, which means that it is intended to
reduce the prediction's sensitivity to individual observations.

When lambda > 0, the Similarity Scores are smaller and the amount of decrease is
inversely proportional to the Number of Residuals in the node. In other words, leaves
with fewer number of Residuals experience the largest decrease in Similarity Scores.

When lambda > 0, the Gains for each node also decreases. This means that it is easier to
prune leaves when lambda > 0 since the values for Gain are smaller.

Note: setting gamma = 0 does not turn off pruning since Gain can be negative by itself.

Calculating output values for an XGBoost Tree
---------------------------------------------

The Output Value equation is:

Output Value = Sum of Residuals / (Number of Residuals + lambda)

When lambda > 0, it will reduce the amount that a single observation adds to the overall
prediction. Thus, lambda, the Regularization Parameter, will reduce the prediction's
sensitivity to an individual observation.

Making predictions with XGBoost
-------------------------------

After we build our first XGBoost tree, we can make new Predictions.

Just like Gradient Boost, XGBoost makes new predictions by starting with the initial
Prediction (e.g., 0.5) and adding the output of the XGBoost Tree scaled by a Learning
Rate, eta (e.g., 0.3).

Now we build another XGBoost tree based on the latest Residuals and make new predictions
that give us even smaller Residuals, and so on. We keep building trees until the
Residuals are super small, or we have reached the maximum number of trees.

Summary of concepts and main ideas
----------------------------------

In summary, when building XGBoost Trees for Regression:

1. We calculate Similarity Scores

2. We calculate Gain to determine how to split the data

3. And we prune the tree by calculating the differences between Gain values and
user-defined Tree Complexity Parameter, gamma. If gamma is negative, we prune the node;
otherwise, we do not prune.

4. Then we calculate the Output Values for the remaining leaves.

5. Lastly, lambda is a Regularization Parameter and when lambda > 0, it results in more
pruning, by shrinking the Similarity Scores, and it results in smaller Output Values for
the leaves.

Part 2: Classification
======================

The very first step in fitting XGBoost to the Training Data is to make an initial
prediction. This prediction can be anything, but by default it is 0.5 regardless of
whether you are using XGBoost for Regression or Classification.

The Residuals, the differences between the Observed and Predicted values, show us how
good the initial prediction is.

Just like we did for Regression, we fit an XGBoost Tree to the Residuals.

However, since we are using XGBoost for Classification, we have a different formula for
the Similarity Scores:

Similarity Score = (Sum of Residuals) ^ 2 /
                   (Sum of (Previous Probability * (1 - Previous Probability)) + lambda)

Just like for Regression, each tree starts out as a single leaf and all of the Residuals
go to the leaf.

Now we need to decide if we can do a better job clustering similar Residuals if we split
them into two groups.

We continuously split observations into two groups based on their average values. And we
calculate new Similarity Scores for the split observations.

If we are building the first tree, the previous probability refers to the prediction
from the initial leaf (i.e., 0.5).

After we have calculated the Similarity Scores for all the leaf nodes, we calculate the
Gain just like we did for Regression. And we pick the optimal threshold as the one that
maximizes the Gain.

For Classification, Cover is the
Sum of (Previous Probability * (1 - Previous Probability)). Thus, Cover depends on the
previously predicted probability of each Residual in a leaf.

We prune the tree by calculating the difference between the Gain associated with the
lowest branch and a number we pick for gamma.

For Classification, the Output Value for a leaf is:

Output Value = (Sum of Residuals) /
               (Sum of (Previous Probability * (1 - Previous Probability)) + lambda)

After building the first tree, we can make new Predictions. Just like other boosting
methods, XGBoost for Classification makes new predictions by starting with the initial
prediction. However, we need to convert this initial probability to a log(odds) value
using the formula:

log(p / (1 - p)) = log(odds)

In other words, Output = log(odds).

Now we add the log(odds) of the initial prediction to the output of the Tree, scaled by
a Learning Rate, eta. To convert a log(odds) into a probability, we plug the log(odds)
into the Logistic Function.

We keep building trees until the Residuals are super small, or we have reached the
maximum number of trees.

In summary, when building XGBoost Trees for Classification:

1. We calculate Similarity Scores

2. We calculate Gain to determine how to split the data

3. And we prune the tree by calculating the difference between Gain values and a
user-defined Tree Complexity Parameter, gamma. If gamma is negative, we prune the node;
otherwise, we do not prune.

4. Then we calculate the Output Values for the leaves.

5. Lastly, lambda is a Regularization Parameter and when lambda > 0, it results in more
pruning, by shrinking the Similarity Scores and smaller Output Values for the leaves.

Part 3: Mathematical Details
============================

See notes.

Part 4: Crazy Cool Optimizations
================================

The other parts of XGBoost are what makes XGBoost relatively efficient with relatively
large training datasets. These parts are:

1. Approximate Greedy Algorithm

2. Parallel Learning

3. Weighted Quantile Sketch

4. Sparsity-Aware Split Finding

5. Cache-Aware Access

6. Blocks for Out-of-Core Computation

Approximate Greedy Algorithm
----------------------------

The first thing XGBoost does is to make an initial prediction, which is 0.5 by default
but could be anything. Then we calculated Residuals and fit a tree to the Residuals.

We fit a tree to the Residuals by calculating the Similarity Scores and the Gain (using
the Similarity Scores) for different thresholds. And the threshold with the largest Gain
is the one XGBoost uses to split the data for the next level in the tree.

The decision to use the threshold that gives the largest Gain is made without worrying
about how the leaves will be split later on down the tree. And that means XGBoost uses
a Greedy Algorithm to build trees.

In other words, since XGBoost uses a Greedy Algorithm, it makes a decision without
looking ahead to see if it is the absolute best choice in the long term. By using a
Greedy Algorithm, XGBoost can build a tree relatively quickly.

That said, when we have a lot of data, the Greedy Algorithm becomes slow because it
still has to look at every possible threshold between data points. If our dataset
contained multiple features, then XGBoost would have to look at every single threshold
for every single feature---this would take forever.

This is where the approximate Greedy Algorithm comes in.

Instead of testing every single threshold, we could divide the data into Quantiles and
only use the Quantiles as candidate thresholds to split the observations. The more
Quantiles we have, the better our predictions but the more thresholds we will have to
test, and that means it will take longer to build the tree.

Thus, for XGBoost, the Approximate Greedy Algorithm means that instead of testing all
possible thresholds, we only test the Quantiles. By default, XGBoost uses about 33
quantiles.

Parallel Learning and Weighted Quantile Sketch
----------------------------------------------

With lots of data, finding quantiles become really slow. To get around this problem, a
class of algorithms, called Sketches, can quickly create approximate solutions.

Imagine splitting a dataset into small pieces and putting the pieces on different
computers on a network. The Quantile Sketch Algorithm combines the values from each
computer to make an approximate histogram. Then, the approximate histogram is used to
calculate approximate quantiles. And the Approximate Greedy Algorithm uses approximate
quantiles.

XGBoost uses a Weighted Quantile Sketch. Usually, quantiles are set up so that the same
number of observations are in each one. In contrast, with weighted quantiles, each
observation has a corresponding Weight and the sum of the Weights are the same in each
quantile.

The Weights are derived from the Cover metric. Specifically, the weight for each
observation is the second derivative of the Loss Function, the Hessian. Thus, for
Regression, the Weights are all equal to 1 and that means the weighted quantiles are
just like normal quantiles and contain an equal number of observations in each quantile.

In contrast, for Classification, the weights are the previous probability times 1 -
previous probability. In other words, the weights for the Weighted Quantile Sketch are
calculated from the previously predicted probabilities. When the previously predicted
probability is close to 0.5, meaning we don't have much confidence in the
classification, the weights are relatively large and vice versa.

By dividing the observations into quantiles where the sum of the weights are similar, we
split observations with low confidence predictions into separate quantiles instead of
grouping them into the same quantile (recall that if two observations end up in the same
leaf with roughly the same Residuals, they will cancel each other out).

In other words, the advantage of using the Weighted Quantile Sketch is that we get
smaller quantiles when we need them.

NB: XGBoost only uses the Approximate Greedy Algorithm, Parallel Learning, and the
Weighted Quantile Sketch when the Training Dataset is huge. When the Training Dataset is
small, XGBoost just uses a normal Greedy Algorithm.

Sparsity-Aware Split Finding
----------------------------

Sparsity-Aware Split Finding tells us how to build trees with missing data and how to
deal with new observations when there is missing data.

If we have missing values in our dataset, we can still calculate Residuals using the
initial prediction value of 0.5.

We put all of the initial Residuals into a single leaf and we need to determine if
splitting the Residuals into two leaves will do a better job clustering them. To
determine an optimal threshold, we need to sort the values. With missing values, we can
form two tables---one with missing values and one without.

We calculate two separate Gain values. The first Gain value is calculated by putting all
of the Residuals with missing values into the leaf on the left. The second Gain value is
calculated by putting all of the Residuals with missing values into the leaf on the
right. We repeat this process for every possible threshold (or weighted quantile). In
the end, we choose the threshold that gave us the largest value for Gain, overall, among
all left/right Gain splits among all possible thresholds.

The path we choose will be the default path for all future observations that are missing
values.

Cache-Aware Access
------------------

If you want your program to run really fast, the goal is to maximize what you can do
with the Cache Memory. So XGBoost puts the Gradients and Hessians in the Cache so that
it can rapidly calculate Similarity Scores and Output Values.

Blocks for Out-of-Core Computation
----------------------------------

When the dataset is too large for the Cache and Main Memory, then, at least some of it,
must be stored on the Hard Drive. Because reading and writing data to the Hard Drive is
super slow, XGBoost tries to minimize these actions by compressing the data. Even though
the CPU must spend some time decompressing the data that comes from the Hard Drive, it
can do this faster than the Hard Drive can read the data.

In other words, by spending a little bit of time uncompressing the data, we can avoid
spending a lot of time accessing the Hard Drive.

When there is more than one Hard Drive available for storage, XGBoost uses dataset
Sharding to speed up disk access.

Misc.
-----

XGBoost can also speed things up by allowing you to build each tree with only a random
subset of the data. And XGBoost can speed up building trees by only looking at a random
subset of features when deciding how to split the data.
"""
